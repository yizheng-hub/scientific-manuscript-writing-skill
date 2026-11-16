#!/usr/bin/env python3
"""Preflight publication DOCX structure before visual page inspection."""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
M = "http://schemas.openxmlformats.org/officeDocument/2006/math"
NS = {"w": W, "m": M}


def q(namespace: str, name: str) -> str:
    return f"{{{NS[namespace]}}}{name}"


def attr(element, name: str, namespace: str = "w"):
    return None if element is None else element.get(q(namespace, name))


def paragraph_text(element) -> str:
    return "".join(node.text or "" for node in element.findall(".//w:t", NS))


def border(table, edge: str):
    return table.find(f"./w:tblPr/w:tblBorders/w:{edge}", NS)


def validate_sequence(text: str, label: str, pattern: str, errors: list[str]) -> None:
    seen = []
    for match in re.finditer(pattern, text, flags=re.IGNORECASE):
        value = int(match.group(1))
        if value not in seen:
            seen.append(value)
    if seen and seen != list(range(1, len(seen) + 1)):
        errors.append(f"{label} first-citation order is {seen}, expected {list(range(1, len(seen) + 1))}")


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    with zipfile.ZipFile(path) as archive:
        document = ET.fromstring(archive.read("word/document.xml"))
        styles = ET.fromstring(archive.read("word/styles.xml"))

    for scope_name, root in (("styles", styles), ("document", document)):
        for flag in ("keepNext", "keepLines", "pageBreakBefore"):
            if root.findall(f".//w:{flag}", NS):
                errors.append(f"{scope_name} contains w:{flag}, which can create a left-margin black square")

    for root_name, root in (("styles", styles), ("document", document)):
        for fonts in root.findall(".//w:rFonts", NS):
            for key in ("ascii", "hAnsi", "eastAsia"):
                value = attr(fonts, key)
                if value and value != "Times New Roman":
                    errors.append(f"{root_name} uses non-Times New Roman font {value!r}")

    styles_by_name = {}
    for style in styles.findall(".//w:style", NS):
        name = attr(style.find("./w:name", NS), "val")
        if name:
            styles_by_name[name.lower()] = style

    def check_style(name: str, size: str, before: str | None, after: str | None, line: str | None = None) -> None:
        style = styles_by_name.get(name.lower())
        if style is None:
            errors.append(f"missing required Word style {name!r}")
            return
        actual_size = attr(style.find("./w:rPr/w:sz", NS), "val")
        if actual_size != size:
            errors.append(f"style {name}: expected size {size} half-points, found {actual_size}")
        spacing = style.find("./w:pPr/w:spacing", NS)
        for field, expected in (("before", before), ("after", after), ("line", line)):
            if expected is not None and attr(spacing, field) != expected:
                errors.append(f"style {name}: expected {field}={expected}, found {attr(spacing, field)}")

    check_style("Normal", "24", "120", "120", "360")
    check_style("heading 1", "28", "120", "120", "360")
    check_style("heading 2", "24", "120", "120", "360")
    check_style("caption", "22", "0", "240")
    check_style("figure placeholder", "22", "240", "0")
    check_style("reference", "22", "0", "0")

    all_text = "\n".join(paragraph_text(p) for p in document.findall(".//w:p", NS))
    validate_sequence(all_text, "Supplementary Figure", r"Supplementary\s+(?:Figure|Fig\.)\s*S(\d+)", errors)
    validate_sequence(all_text, "Supplementary Table", r"Supplementary\s+Table\s*S(\d+)", errors)
    validate_sequence(all_text, "Supplementary Section", r"Supplementary\s+Section\s+(\d+)", errors)

    for index, table in enumerate(document.findall(".//w:tbl", NS), 1):
        is_equation = table.find(".//m:oMath", NS) is not None
        rows = table.findall("./w:tr", NS)
        first_cells = [] if not rows else rows[0].findall("./w:tc", NS)
        if is_equation:
            if len(rows) != 1 or len(first_cells) != 2:
                errors.append(f"table {index}: equation layout must be one row and two columns")
            for edge in ("top", "insideH", "bottom", "left", "right", "insideV"):
                rule = border(table, edge)
                if rule is None or attr(rule, "val") not in {"nil", "none"}:
                    errors.append(f"table {index}: equation layout has visible {edge} border")
            widths = [int(attr(cell.find("./w:tcPr/w:tcW", NS), "w") or 0) for cell in first_cells]
            if len(widths) == 2 and not widths[0] > widths[1] > 0:
                errors.append(f"table {index}: equation left column must be wider than the number column")
            if not re.search(r"Eq\.\s*\(\d+\)", paragraph_text(table)):
                errors.append(f"table {index}: equation number must use Eq. (n)")
            continue

        expected = {"top": ("single", "12"), "bottom": ("single", "12")}
        for edge, (value, size) in expected.items():
            rule = border(table, edge)
            if rule is None or attr(rule, "val") != value or attr(rule, "sz") != size:
                errors.append(f"table {index}: {edge} border must be 1.5 pt (w:sz=12)")
        for edge in ("insideH", "left", "right", "insideV"):
            rule = border(table, edge)
            if rule is None or attr(rule, "val") not in {"nil", "none"}:
                errors.append(f"table {index}: {edge} border must be absent")
        for cell_index, cell in enumerate(first_cells, 1):
            rule = cell.find("./w:tcPr/w:tcBorders/w:bottom", NS)
            if rule is None or attr(rule, "val") != "single" or attr(rule, "sz") != "4":
                errors.append(f"table {index}, header cell {cell_index}: bottom rule must be 0.5 pt (w:sz=4)")
        for size in table.findall(".//w:sz", NS):
            if attr(size, "val") != "22":
                errors.append(f"table {index}: ordinary table text must be 11 pt (w:sz=22)")

    return sorted(set(errors))


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: validate_docx.py FILE.docx [FILE.docx ...]", file=sys.stderr)
        return 2
    failed = False
    for raw_path in sys.argv[1:]:
        path = Path(raw_path)
        errors = validate(path)
        if errors:
            failed = True
            print(f"FAIL {path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
