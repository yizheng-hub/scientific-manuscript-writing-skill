# Scientific Manuscript Writing Skill

A reusable Codex skill for evidence-led scientific manuscripts, narrative Supplementary Information (SI), publication figures, captions, references, and Word deliverables.

The skill emphasizes:

- a single, explicit innovation and contribution across the title, abstract, introduction, results, discussion, and cover letter;
- simple English, funnel-shaped abstracts and introductions, and removal of defensive AI-style prose;
- figure-led results in which every results panel is data-backed, cited, and interpreted in order;
- independently readable SI sections with figures and tables interspersed in the narrative;
- self-contained captions, independent abbreviation definitions, and verified citation support;
- reproducible `plot.ipynb` figure generation and a strict zero-overlap visual gate;
- role-based cold reads by an editor, broad reviewer, technical reviewer, general reader, novice reader, and high-school/news reader;
- a generic `Manuscript Template.docx` retaining the house Word styles for main text, SI, and a cover letter.

Extended Data is intentionally not part of the default structure because it is journal-specific. Add it only when the target journal requires it.

## Install

Clone this repository into your Codex skills directory, or install it from the GitHub repository path with the Codex skill installer. Invoke it as `$scientific-manuscript-writing`.

## Main files

- `SKILL.md`: routing and non-negotiable standards.
- `references/master-prompt.md`: comprehensive Chinese reusable prompt.
- `references/`: writing, evidence, SI, caption, figure, Word, and validation contracts.
- `assets/Manuscript Template.docx`: de-identified master Word template.

## Privacy and reference images

This public package contains only generic, de-identified instructions and placeholders. It contains no manuscript-specific title, authors, study topic, data, results, figures, review comments, file paths, or submission details.

Published reference images are not redistributed here because their licenses may not permit republication. Users may supply reference figures they are entitled to use; the skill will extract visual principles without copying scientific content.

## License

MIT. Third-party documents, figures, journal styles, and trademarks remain subject to their respective rights and terms.
