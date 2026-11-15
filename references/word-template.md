# Word template and formatting contract

Use `../assets/Manuscript Template.docx` as the house-style source for main manuscripts, Supplementary Information, and cover letters. Target-journal requirements and an explicitly supplied journal template override this asset.

## Template structure

The DOCX contains three reusable parts:

1. main manuscript skeleton;
2. narrative SI skeleton with figures and tables interspersed;
3. one-page cover-letter skeleton.

When authoring a deliverable, copy the template and retain only the relevant part. Do not submit the master file with unused template sections. “Match the template” means reuse its section geometry, Word style definitions, paragraph rules, caption/table treatment, line-number settings, page-number fields, and cross-reference treatment; manually recreating a visually similar document is not sufficient.

## House formatting

- A4 portrait; 1.25 in left/right and 1.0 in top/bottom margins unless the journal template specifies otherwise.
- Times New Roman throughout.
- Main text and equations: 12 pt; justified; 1.5 line spacing; 0.33 in first-line indent; 7.8 pt before/after in the current house style.
- Main section headings: 14 pt bold; subsection headings: 12 pt bold.
- Figure captions, table text/notes, and references: 11 pt.
- Figure/table/section/panel cross-references use the bold treatment demonstrated by the template.
- Continuous line numbering and centered page numbers are enabled for review copies.
- Captions use `(a)`, `(b)`, ... and include independent abbreviation definitions.

The template was distilled from supplied manuscript-format references and then rewritten with generic placeholders. It deliberately omits project-specific text and Extended Data.

## DOCX workflow

1. Read the target-journal instructions and compare them with the template.
2. Copy the template; do not edit the retained asset.
3. Apply the template's real Word styles and section properties. Do not rebuild the document from a blank DOCX or approximate the styles with direct formatting unless a journal override requires it.
4. Preserve figure aspect ratios. Check that every figure and caption fits the page without overlap or clipping.
5. Use one journal-appropriate caption placement, never a duplicated caption list plus repeated full captions unless the journal explicitly requires both. Use dynamic numbering/cross-references where the workflow supports them; otherwise run an explicit numbering audit.
6. Update fields, page numbers, line numbers, bookmarks, cross-references, and numbering.
7. Run a programmatic DOCX preflight for unresolved placeholders; tracked changes, comments, hidden text, and metadata; broken fields, bookmarks, cross-references, hyperlinks, or numbering; style/template deviations; equation integrity; table overflow; image aspect ratio and effective resolution; and missing fonts.
8. Compare style names and key properties against the retained template, then render the final DOCX to page images, inspect every page at 100%, fix defects, and rerender until clean. A file does not pass merely because the font family and point size look similar.

