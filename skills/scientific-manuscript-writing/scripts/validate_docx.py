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
WP = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
NS = {"w": W, "m": M, "wp": WP}


def q(namespace: str, name: str) -> str:
    return f"{{{NS[namespace]}}}{name}"


def attr(element, name: str, namespace: str = "w"):
    return None if element is None else element.get(q(namespace, name))


def paragraph_text(element) -> str:
    return "".join(node.text or "" for node in element.findall(".//w:t", NS))


def is_si_title(paragraph) -> bool:
    text = paragraph_text(paragraph).strip()
    style_id = (attr(paragraph.find("./w:pPr/w:pStyle", NS), "val") or "").lower()
    return bool(
        re.fullmatch(r"Supplementary Information(?:\s+for(?:\s+.+)?)?", text, flags=re.IGNORECASE)
        and any(label in style_id for label in ("title", "heading"))
    )


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


def toggle_is_on(element) -> bool:
    if element is None:
        return False
    value = attr(element, "val")
    return value is None or value.lower() not in {"0", "false", "off", "no"}


def style_is_bold(style_id, styles_by_id, seen=None):
    if not style_id or style_id not in styles_by_id:
        return None
    seen = set() if seen is None else seen
    if style_id in seen:
        return None
    seen.add(style_id)
    style = styles_by_id[style_id]
    direct = style.find("./w:rPr/w:b", NS)
    if direct is not None:
        return toggle_is_on(direct)
    return style_is_bold(attr(style.find("./w:basedOn", NS), "val"), styles_by_id, seen)


def style_has_shading(style_id, styles_by_id, seen=None) -> bool:
    if not style_id or style_id not in styles_by_id:
        return False
    seen = set() if seen is None else seen
    if style_id in seen:
        return False
    seen.add(style_id)
    style = styles_by_id[style_id]
    for shading in style.findall(".//w:shd", NS):
        if attr(shading, "fill") not in {None, "auto"} or attr(shading, "val") not in {None, "clear", "nil"}:
            return True
    return style_has_shading(attr(style.find("./w:basedOn", NS), "val"), styles_by_id, seen)


def run_is_bold(run, styles_by_id, paragraph_style_id=None) -> bool:
    direct = run.find("./w:rPr/w:b", NS)
    if direct is not None:
        return toggle_is_on(direct)
    style_ref = attr(run.find("./w:rPr/w:rStyle", NS), "val")
    character_value = style_is_bold(style_ref, styles_by_id)
    if character_value is not None:
        return character_value
    paragraph_value = style_is_bold(paragraph_style_id, styles_by_id)
    return bool(paragraph_value)


def paragraph_text_and_bold(paragraph, styles_by_id):
    text_parts: list[str] = []
    bold_mask: list[bool] = []
    paragraph_style_id = attr(paragraph.find("./w:pPr/w:pStyle", NS), "val")
    for run in paragraph.findall(".//w:r", NS):
        bold = run_is_bold(run, styles_by_id, paragraph_style_id)
        for node in run.findall(".//w:t", NS):
            value = node.text or ""
            text_parts.append(value)
            bold_mask.extend([bold] * len(value))
    return "".join(text_parts), bold_mask


def segment_is_bold(text: str, mask: list[bool], start: int, end: int) -> bool:
    positions = [index for index in range(start, end) if not text[index].isspace()]
    return bool(positions) and all(mask[index] for index in positions)


def segment_is_regular(text: str, mask: list[bool], start: int, end: int) -> bool:
    positions = [index for index in range(start, end) if not text[index].isspace()]
    return bool(positions) and all(not mask[index] for index in positions)


def validate_cross_references(paragraph, index: int, styles_by_id, errors: list[str]) -> None:
    text, bold = paragraph_text_and_bold(paragraph, styles_by_id)
    if not text:
        return

    if re.search(r"\bSupplementary\s+(?:Figure|Fig\.)\s*S?\d+", text, flags=re.IGNORECASE):
        errors.append(f"paragraph {index}: use 'Fig. S#', not 'Supplementary Figure/Fig. #'")
    if re.search(r"\bSupplementary\s+Table\s*S?\d+", text, flags=re.IGNORECASE):
        errors.append(f"paragraph {index}: use 'Table S#', not 'Supplementary Table #'")
    if re.search(r"\bSupplementary\s+Section\s*S?\d+", text, flags=re.IGNORECASE):
        errors.append(f"paragraph {index}: use 'Section S#', not 'Supplementary Section #'")
    if re.search(r"\bFigure\s+S\d+", text, flags=re.IGNORECASE):
        errors.append(f"paragraph {index}: use abbreviated 'Fig. S#', not 'Figure S#'")

    style_id = attr(paragraph.find("./w:pPr/w:pStyle", NS), "val") or ""
    stripped = text.lstrip()
    if (
        any(label in style_id.lower() for label in ("caption", "heading", "figure"))
        or re.match(r"^(?:Fig\.|Table)\s+S?\d+\s*[|.]", stripped, flags=re.IGNORECASE)
    ):
        return

    invalid_patterns = (
        (r"\bFig\.\s*S?\d+[a-z](?:\s*,\s*[a-z])+", "use plural 'Figs.' and grammatical panel separators"),
        (r"\bFig\.\s*S?\d+[a-z]\s+and\s+[a-z]\b", "use plural 'Figs.' for two panels"),
        (r"\bFig\.\s*S?\d+[a-z]\s*[-–]\s*[a-z]\b", "use plural 'Figs.' for a panel range"),
    )
    for pattern, guidance in invalid_patterns:
        if re.search(pattern, text, flags=re.IGNORECASE):
            errors.append(f"paragraph {index}: invalid panel-reference grammar; {guidance}")

    item_pattern = r"(?:S?\d+[a-z]?(?:\s*[–-]\s*(?:S?\d+[a-z]?|[a-z]))?|[a-z])"
    connector_pattern_text = r"(?:\s*,\s*(?:and\s+)?|\s+and\s+)"
    expression_pattern = re.compile(
        rf"\b(?P<label>Figs?\.|Tables?|Sections?)\s+"
        rf"(?P<items>S?\d+[a-z]?(?:\s*[–-]\s*(?:S?\d+[a-z]?|[a-z]))?"
        rf"(?:{connector_pattern_text}{item_pattern})*)",
        flags=re.IGNORECASE,
    )
    for match in expression_pattern.finditer(text):
        label_end = match.start("items")
        if not segment_is_bold(text, bold, match.start("label"), label_end):
            errors.append(f"paragraph {index}: cross-reference label must be bold")
        items = match.group("items")
        item_start = match.start("items")
        identifier_pattern = re.compile(
            r"S?\d+[a-z]?(?:\s*[–-]\s*(?:S?\d+[a-z]?|[a-z]))?|(?<![A-Za-z])[a-z](?![A-Za-z])",
            re.I,
        )
        for identifier in identifier_pattern.finditer(items):
            start = item_start + identifier.start()
            end = item_start + identifier.end()
            if not segment_is_bold(text, bold, start, end):
                errors.append(
                    f"paragraph {index}: cross-reference identifier {text[start:end]!r} must be bold"
                )
        connector_pattern = re.compile(connector_pattern_text, re.I)
        for connector in connector_pattern.finditer(items):
            start = item_start + connector.start()
            end = item_start + connector.end()
            if not segment_is_regular(text, bold, start, end):
                errors.append(
                    f"paragraph {index}: cross-reference punctuation/conjunction {text[start:end]!r} must be regular weight"
                )
        if match.start() > 0 and text[match.start() - 1] == "(" and bold[match.start() - 1]:
            errors.append(f"paragraph {index}: opening parenthesis around a cross-reference must be regular weight")
        if match.end() < len(text) and text[match.end()] == ")" and bold[match.end()]:
            errors.append(f"paragraph {index}: closing parenthesis around a cross-reference must be regular weight")
        cursor = match.end()
        while cursor < len(text) and text[cursor].isspace():
            cursor += 1
        if cursor < len(text) and text[cursor] in ",;" and bold[cursor]:
            errors.append(
                f"paragraph {index}: punctuation after a cross-reference must be regular weight"
            )


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    with zipfile.ZipFile(path) as archive:
        document = ET.fromstring(archive.read("word/document.xml"))
        styles = ET.fromstring(archive.read("word/styles.xml"))
    parent_map = {child: parent for parent in document.iter() for child in parent}

    def has_ancestor(element, tag) -> bool:
        current = element
        while current in parent_map:
            current = parent_map[current]
            if current.tag == tag:
                return True
        return False

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
    styles_by_id = {}
    for style in styles.findall(".//w:style", NS):
        style_id = attr(style, "styleId")
        if style_id:
            styles_by_id[style_id] = style
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
    normal_style = styles_by_name.get("normal")
    normal_indent = None if normal_style is None else normal_style.find("./w:pPr/w:ind", NS)
    if normal_style is not None and attr(normal_indent, "firstLine") not in {"475", "480"}:
        errors.append(
            f"style Normal: expected two-character first-line indent (475–480 twips), found {attr(normal_indent, 'firstLine')}"
        )

    paragraphs = document.findall(".//w:p", NS)
    prose_texts = []
    for paragraph in paragraphs:
        text = paragraph_text(paragraph).strip()
        style_id = (attr(paragraph.find("./w:pPr/w:pStyle", NS), "val") or "").lower()
        if not text or any(label in style_id for label in ("caption", "heading", "figure", "toc")):
            continue
        if re.match(r"^(?:Fig\.|Table)\s+S?\d+\s*[|.]", text, flags=re.IGNORECASE):
            continue
        if re.match(r"^S\d+\.\s+", text, flags=re.IGNORECASE):
            continue
        prose_texts.append(text)
    prose_text = "\n".join(prose_texts)
    validate_sequence(prose_text, "Fig. S prose callout", r"\bFigs?\.\s*S(\d+)", errors)
    validate_sequence(prose_text, "Table S prose callout", r"\bTables?\s+S(\d+)", errors)
    validate_sequence(prose_text, "Section S prose callout", r"\bSections?\s+S(\d+)", errors)

    if any(is_si_title(p) for p in paragraphs):
        si_headings = []
        for paragraph in paragraphs:
            text = paragraph_text(paragraph).strip()
            style_id = (attr(paragraph.find("./w:pPr/w:pStyle", NS), "val") or "").lower()
            match = re.match(r"^S(\d+)\.\s+\S", text, flags=re.IGNORECASE)
            if match and "heading" in style_id:
                si_headings.append(int(match.group(1)))
        if si_headings and si_headings != list(range(1, len(si_headings) + 1)):
            errors.append(
                f"top-level SI heading order is {si_headings}; expected {list(range(1, len(si_headings) + 1))}"
            )

    for index, paragraph in enumerate(paragraphs, 1):
        validate_cross_references(paragraph, index, styles_by_id, errors)
        drawings = paragraph.findall(".//w:drawing", NS) + paragraph.findall(".//w:pict", NS)
        if not drawings or paragraph.find(".//m:oMath", NS) is not None:
            continue
        metadata = " ".join(
            value
            for node in paragraph.findall(".//wp:docPr", NS)
            for value in (node.get("name"), node.get("title"), node.get("descr"))
            if value
        ).lower()
        style_id = (attr(paragraph.find("./w:pPr/w:pStyle", NS), "val") or "").lower()
        if "equation" in metadata:
            errors.append(f"paragraph {index}: equation is stored as an image; use native Word OMML")
        elif not paragraph_text(paragraph).strip() and "figure" not in style_id and "caption" not in style_id:
            errors.append(
                f"paragraph {index}: unclassified drawing-only paragraph outside the figure style; "
                "use a figure paragraph or replace a rasterized equation with native OMML"
            )
        if "figure" in style_id:
            if not re.search(r"\bfig(?:ure)?\b", metadata):
                errors.append(
                    f"paragraph {index}: figure drawing lacks explicit figure-role alt text; "
                    "label it as a figure so a raster equation cannot pass as a generic picture"
                )
            following = next((candidate for candidate in paragraphs[index:] if paragraph_text(candidate).strip()), None)
            following_style = "" if following is None else (
                attr(following.find("./w:pPr/w:pStyle", NS), "val") or ""
            ).lower()
            following_text = "" if following is None else paragraph_text(following).lstrip()
            caption_shape = re.match(
                r"^(?:Supplementary\s+)?(?:Fig\.|Figure|Table)\s+S?\d+\s*[|.]",
                following_text,
                flags=re.IGNORECASE,
            )
            if "caption" not in following_style and not caption_shape:
                errors.append(f"paragraph {index}: figure drawing is not followed by a caption paragraph")

    for math_para in document.findall(".//m:oMathPara", NS):
        if not has_ancestor(math_para, q("w", "tbl")):
            errors.append("display equation appears outside the required one-row two-column layout table")
    for paragraph in document.findall(".//w:p", NS):
        if (
            paragraph.find(".//m:oMath", NS) is not None
            and not has_ancestor(paragraph, q("w", "tbl"))
            and (
                not paragraph_text(paragraph).strip()
                or re.fullmatch(r"\s*Eq\.\s*\(\d+\)\s*", paragraph_text(paragraph), flags=re.IGNORECASE)
            )
        ):
            errors.append("stand-alone native equation appears outside the required two-column layout table")

    table_parts: dict[int, str] = {}
    current_part = "main"
    for element in document.iter():
        if element.tag == q("w", "p") and is_si_title(element):
            current_part = "si"
        elif element.tag == q("w", "tbl"):
            table_parts[id(element)] = current_part

    equation_numbers: dict[str, list[int]] = {}
    for index, table in enumerate(document.findall(".//w:tbl", NS), 1):
        rows = table.findall("./w:tr", NS)
        first_cells = [] if not rows else rows[0].findall("./w:tc", NS)
        has_display_math = table.find(".//m:oMathPara", NS) is not None
        right_text = "" if len(first_cells) != 2 else paragraph_text(first_cells[1]).strip()
        left_has_math = len(first_cells) == 2 and first_cells[0].find(".//m:oMath", NS) is not None
        is_equation = has_display_math or (
            len(rows) == 1
            and len(first_cells) == 2
            and left_has_math
            and re.fullmatch(r"Eq\.\s*\(\d+\)", right_text, flags=re.IGNORECASE)
        )
        if is_equation:
            if len(rows) != 1 or len(first_cells) != 2:
                errors.append(f"table {index}: equation layout must be one row and two columns")
            for edge in ("top", "insideH", "bottom", "left", "right", "insideV"):
                rule = border(table, edge)
                if rule is None or attr(rule, "val") not in {"nil", "none"}:
                    errors.append(f"table {index}: equation layout has visible {edge} border")
            table_style_id = attr(table.find("./w:tblPr/w:tblStyle", NS), "val")
            shading_nodes = table.findall("./w:tblPr/w:shd", NS) + table.findall("./w:tr/w:trPr/w:shd", NS)
            if style_has_shading(table_style_id, styles_by_id) or any(
                attr(shading, "fill") not in {None, "auto"}
                or attr(shading, "val") not in {None, "clear", "nil"}
                for shading in shading_nodes
            ):
                errors.append(f"table {index}: equation layout must not use table-, row-, or style-level shading")
            widths = [int(attr(cell.find("./w:tcPr/w:tcW", NS), "w") or 0) for cell in first_cells]
            if len(widths) == 2 and not widths[0] > widths[1] > 0:
                errors.append(f"table {index}: equation left column must be wider than the number column")
            if len(first_cells) == 2:
                left, right = first_cells
                if left.find(".//m:oMath", NS) is None or right.find(".//m:oMath", NS) is not None:
                    errors.append(f"table {index}: native equation must be in the wide left cell only")
                for cell_number, cell in enumerate(first_cells, 1):
                    if attr(cell.find("./w:tcPr/w:vAlign", NS), "val") != "center":
                        errors.append(f"table {index}, cell {cell_number}: equation cells must be vertically centered")
                    shading = cell.find("./w:tcPr/w:shd", NS)
                    if shading is not None and (
                        attr(shading, "fill") not in {None, "auto"}
                        or attr(shading, "val") not in {None, "clear", "nil"}
                    ):
                        errors.append(f"table {index}, cell {cell_number}: equation layout must be unshaded")
                left_paragraph = left.find("./w:p", NS)
                right_paragraph = right.find("./w:p", NS)
                if attr(None if left_paragraph is None else left_paragraph.find("./w:pPr/w:jc", NS), "val") != "center":
                    errors.append(f"table {index}: equation paragraph in the left cell must be centered")
                if attr(None if right_paragraph is None else right_paragraph.find("./w:pPr/w:jc", NS), "val") not in {"right", "end"}:
                    errors.append(f"table {index}: equation number in the right cell must be right-aligned")
                number_matches = re.findall(r"Eq\.\s*\((\d+)\)", right_text, flags=re.IGNORECASE)
                if len(number_matches) != 1 or not re.fullmatch(
                    r"Eq\.\s*\(\d+\)", right_text, flags=re.IGNORECASE
                ):
                    errors.append(f"table {index}: right cell must contain exactly one number in the form Eq. (n)")
                else:
                    part = table_parts.get(id(table), "main")
                    equation_numbers.setdefault(part, []).append(int(number_matches[0]))
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

    for part, numbers in equation_numbers.items():
        expected = list(range(1, len(numbers) + 1))
        if numbers != expected:
            errors.append(
                f"{part} equation numbering is {numbers}; expected continuous sequence {expected}"
            )

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
