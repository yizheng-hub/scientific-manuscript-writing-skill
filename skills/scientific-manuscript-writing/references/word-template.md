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
- Main text and equations: 12 pt; justified; 1.5 line spacing; first-line indent of two characters (24 pt, implemented as approximately 0.33 in for 12 pt text); 6 pt before/after in the current house style.
- Main section headings: 14 pt bold; subsection headings: 12 pt bold.
- Figure captions, table text/notes, and references: 11 pt.
- Place each figure in a centered figure paragraph with 12 pt space before and 0 pt after. Preserve its aspect ratio and final publication width.
- Set each figure caption to 0 pt before and 12 pt after. Do not insert blank paragraphs to simulate figure or caption spacing.
- Every Figure, Table, Section, and panel cross-reference in the main manuscript and SI uses the bold treatment demonstrated by the template, including references from the main text into SI and references within SI. Parentheses, commas, semicolons, and conjunctions remain regular weight.
- Continuous line numbering and centered page numbers are enabled for review copies.
- Captions use `(a)`, `(b)`, ... and include independent abbreviation definitions.

## Data tables

- Format every ordinary data or text table as a three-line table. Use only a 1.5 pt top rule, a 0.5 pt rule below the header row, and a 1.5 pt bottom rule. Remove left, right, vertical, and all other internal rules. Do not approximate this with gray gridlines or a generic table style.
- Use Times New Roman 11 pt for all table headings, body cells, and notes unless an explicit journal template overrides it. Preserve the template's cell margins, paragraph spacing, line spacing, alignment, and table-caption style; do not shrink text to make an overwide table fit.
- Keep a table within the text width by revising labels, column widths, orientation, or table structure. Never solve overflow with unreadably small type.
- The borderless two-cell display-equation container is a layout table, not a data table, and is exempt from the three-line rule.

## Paragraph pagination markers

- Delivered files must not show black square markers in the left margin when Word's formatting marks are enabled. These usually indicate `keep with next`, `keep lines together`, or `page break before` paragraph properties.
- Do not apply those pagination properties globally to Title, Heading, Caption, Table title, Reference, or body styles, and do not add them as direct formatting merely to force layout. Use the retained template's safe spacing and explicit section/page breaks where a break is genuinely required.
- Run an OOXML preflight for `w:keepNext`, `w:keepLines`, and `w:pageBreakBefore`. Any occurrence that produces a visible left-margin square must be removed unless an explicitly supplied journal template requires that exact property.

## Equations

- Use native editable Word equations (OMML/Word Equation), not plain-text approximations, screenshots, SVG/EMF pictures, or raster images. An equation stored as any image object is a structural failure, even when it looks sharp in the rendered page.
- Place each display equation in a borderless, unshaded one-row, two-column table. Use a wide left cell for the centered equation and a narrow right cell for the number in the form `Eq. (1)`.
- Vertically center both cells. Keep the number aligned consistently and update it sequentially according to the target journal. Do not simulate the layout with spaces or tab stops.
- Keep inline equations as native Word equation objects within the sentence.
- Every display equation receives a sequential number unless the target journal explicitly exempts a specific equation class. A native equation placed as a stand-alone paragraph outside the two-cell container fails the house style.

## Cross-reference grammar and bold runs

- One panel: bold `Fig. 2a`.
- Two panels: bold `Figs. 2a`, regular ` and `, and bold `b`. Implement these as separate Word runs. Do not write `Fig. 2a,b`, `Fig. 2a and b`, or bold the conjunction.
- A continuous panel range may be written as bold `Figs. 2a–c`. For non-contiguous panels, bold each reference token while keeping commas and `and` regular.
- Apply the same run-level rule to multiple Figures, Tables, and Sections. The object label and identifier are bold; connecting prose and punctuation are not.
- Compound examples: regular `(` + bold `Fig. S1a` + regular `)`; bold `Figs. 2a` + regular `, ` + bold `c` + regular ` and ` + bold `e`; bold `Figs. 2` + regular ` and ` + bold `3`.
- Use `Fig. S1` and `Table S1` for supplementary objects. Number top-level SI headings `S1. [Topic]`, `S2. [Topic]`, ... and cite them as `Section S1`, `Section S2`, .... Do not use `Supplementary Fig. 1`, `Supplementary Figure 1`, `Supplementary Section 1`, or a supplementary number without the `S` prefix.
- Cross-reference formatting must be applied to the actual Word runs or fields, not simulated with Markdown asterisks. Recheck it after fields are updated or materialized.
- Give every inserted figure explicit figure-role alt text such as `Figure 2`. Generic `Picture 1` metadata is not sufficient for the structural preflight because it cannot distinguish a real figure from a rasterized equation.

The template was distilled from supplied manuscript-format references and then rewritten with generic placeholders. It deliberately omits project-specific text and Extended Data.

## DOCX workflow

1. Read the target-journal instructions and compare them with the template.
2. Copy the template; do not edit the retained asset.
3. Apply the template's real Word styles and section properties. Do not rebuild the document from a blank DOCX or approximate the styles with direct formatting unless a journal override requires it.
4. Preserve figure aspect ratios. Check that every figure and caption fits the page without overlap or clipping.
5. Use one journal-appropriate caption placement, never a duplicated caption list plus repeated full captions unless the journal explicitly requires both. Use dynamic numbering/cross-references where the workflow supports them; otherwise run an explicit numbering audit.
6. Update fields, page numbers, line numbers, bookmarks, cross-references, and numbering.
7. Run a programmatic DOCX preflight for unresolved placeholders; tracked changes, comments, hidden text, and metadata; broken fields, bookmarks, cross-references, hyperlinks, or numbering; style/template deviations; rasterized or unnumbered equations; native-equation integrity; borderless two-cell display-equation layout and sequential `Eq. (n)` numbering; exact supplementary naming; cross-reference grammar and run-level bold boundaries; exact three-line data-table borders and 11 pt Times New Roman table text; paragraph pagination properties that create left-margin black squares; table overflow; image aspect ratio and effective resolution; and missing fonts.
8. Compare style names and key properties against the retained template, then render the final DOCX to page images, inspect every page at 100%, fix defects, and rerender until clean. Manually inspect compound cross-reference run boundaries because automated checks cannot prove every later bare panel token is bold. A file does not pass merely because the font family and point size look similar.

Run `python scripts/validate_docx.py <deliverable.docx>` from the skill directory as part of step 7. The script enforces this retained house template. If an explicit journal template overrides a reported house rule, record that override and audit the substituted journal rule rather than silently ignoring the failure. Fix every remaining structural failure, then complete the render-and-inspect gate; the script does not replace visual page review.

