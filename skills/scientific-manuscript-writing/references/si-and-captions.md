# Supplementary Information, captions, notes, and abbreviations

## SI is a second scientific narrative

SI must be independently readable. Do not create warehouse sections for all figures, all tables, or miscellaneous notes. Order top-level SI sections by first citation in the main manuscript. Each section should develop one scientific topic:

1. state the purpose or question;
2. give only the method context needed to understand the analysis;
3. present the supplementary result;
4. place the relevant figure or table near its first discussion;
5. explain what the result establishes and how it supports the main evidence chain.

Define important concepts, denominators, comparisons, units, and abbreviations again when they first appear in SI. Keep detailed parameters, derivations, expanded controls, sensitivity analyses, validation, and reproducibility information here without turning SI into a limitation list or development log.

Narrative organization does not excuse incomplete methods. Each SI analysis must still state enough data, software or model identifiers, parameters, statistical specification, and code or availability information to be reproduced. Use a brief contents map or consistent topic-level subheads when it helps readers locate methods, validation, sensitivity, and reproducibility material, but never separate all figures or all tables into warehouse sections.

Every supplementary panel must be cited and explained in sequence. Do not insert an image or table without scientific prose that gives it a role.

## Caption contract

A reader should understand the figure by viewing the image and caption without reading the surrounding body text. Each caption should provide, as applicable:

- a concise, finding-oriented figure title;
- an ordered description of every panel using `(a)`, `(b)`, ...;
- the object, population, condition, and comparison shown;
- definitions of colors, symbols, lines, shading, size encodings, and facets;
- axes and units when the graphic alone is insufficient;
- sample size for each relevant panel/group and what `n` counts; independent unit; biological, technical, or model replication; and aggregation rule;
- definitions of points, boxes, whiskers, distributions, error bars, interval type and level, test or model, sidedness, and multiplicity correction;
- normalization or reference value, exclusions, missing observations, and denominators that materially change interpretation;
- whether a displayed construct is directly observed, estimated, inferred, proxied, or model-derived;
- definitions of every abbreviation needed to read the figure.

Captions describe the evidence objectively. The body text or SI narrative explains the result, mechanism, scientific contribution, and broader meaning. Do not extend the Discussion inside a caption.

Use a factual takeaway as the figure title: state the empirical relationship the panels establish without adding an unsupported mechanism. Provide redundant non-color encodings where practical, confirm grayscale legibility, and prepare alt text or an equivalent concise textual description when the publication workflow supports it.

Use a short note below a figure or table when a dense definition, naming convention, formula, or repeated qualification would make the caption difficult to follow. Notes clarify reading; they do not become a second discussion.

## Independent abbreviation scopes

Treat the main manuscript, SI, each figure caption, and each stand-alone table note as separate reading entrances. At the first occurrence within each scope, write the full term followed by the abbreviation in parentheses. Thereafter use the abbreviation consistently. When there is room, prefer the full term inside the figure itself; otherwise define it in the caption.

## Cross-references and order

- Cite every panel in the order needed by the argument, normally left-to-right and top-to-bottom unless the figure has a deliberate alternative flow.
- Use the exact numbering, grammar, and run-level bold cross-reference style defined by the Word template. Bold the reference token, not surrounding parentheses, commas, semicolons, or conjunctions.
- Use `Fig. S1` and `Table S1` in captions, prose, main-text callouts, and bookmarks. In the house style, number every top-level SI heading as `S1. [Topic]`, `S2. [Topic]`, ... and refer to it in prose as `Section S1`, `Section S2`, .... Do not write `Supplementary Fig. 1`, `Supplementary Figure 1`, `Supplementary Table 1`, `Supplementary Section 1`, or omit the `S` prefix. Caption punctuation follows the retained template or target journal, for example `Fig. S1 | [Title]` in the house template; safe asset filenames may use `Fig_S1.png`.
- Number figures and tables strictly by first appearance, then update all main-text, SI, caption, and note references together. Audit the three sequences independently: Fig. S1, S2, ...; Table S1, S2, ...; and Section S1, S2, ....
- Run a first-citation sequence audit on the final assembled files. The first new supplementary item cited must be S1, the next previously unseen item S2, and so on, with no gaps or reversals. If the prose first cites an item currently called S2, either move the S1 citation earlier when scientifically logical or rename that item S1 and update every cross-reference, caption, file name, and callout. Never accept S2-before-S1 merely because the assets were created in that order.
- Keep panel markers as `(a) Title` with one space between marker and title, both in the image and caption.
- Verify that a reader can find every referenced SI section without encountering an undefined prerequisite.

For panel callouts, use the following grammar:

- one panel: `Fig. 2a`;
- two panels: `Figs. 2a` + regular-weight ` and ` + bold `b`;
- a continuous range: `Figs. 2a–c`;
- non-contiguous panels: bold each reference token while commas and `and` remain regular.

Literal Word run maps for ambiguous cases:

- regular `(` + bold `Fig. S1a` + regular `)`;
- bold `Figs. 2a` + regular `, ` + bold `c` + regular ` and ` + bold `e`;
- bold `Figs. 2` + regular ` and ` + bold `3`.

The automated validator is a structural preflight; a human or agent must still inspect the run boundaries of later bare panel identifiers in compound references.

In the actual DOCX, apply bold to the Word runs or cross-reference fields. Markdown asterisks are examples only and must never appear in the delivered file.

