# Scientific Manuscript Writing Skill for Codex

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111827)](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex)
[![GitHub stars](https://img.shields.io/github/stars/yizheng-hub/scientific-manuscript-writing-skill)](https://github.com/yizheng-hub/scientific-manuscript-writing-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A reusable Codex skill for scientific manuscript writing, academic editing, narrative Supplementary Information (SI), publication figures, captions, verified references, reproducible plotting, and journal-ready Word deliverables.

It is designed for researchers who want one evidence-led workflow spanning manuscript structure, innovation and contribution framing, AI-defensive-writing removal, figure design, SI organization, reference verification, reader-role validation, and final DOCX formatting.

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

## Install in Codex

### Option 1 — ask Codex to install it

Send this prompt to Codex:

```text
Use $skill-installer to install the public skill from
https://github.com/yizheng-hub/scientific-manuscript-writing-skill.
The skill path is skills/scientific-manuscript-writing.
After installation, tell me when it will be available.
```

The installed skill is available on the next turn as `$scientific-manuscript-writing`.

### Option 2 — GitHub CLI

Install it for Codex at user scope:

```bash
gh skill install yizheng-hub/scientific-manuscript-writing-skill scientific-manuscript-writing --agent codex --scope user
```

To check for later updates:

```bash
gh skill update scientific-manuscript-writing
```

This repository follows the standard `skills/<skill-name>/SKILL.md` discovery layout. The installation paths above were tested against the public repository.

## Use it

Start a new Codex turn and explicitly invoke the skill:

```text
Use $scientific-manuscript-writing to revise this paper.

Target journal: [journal]
Task: [full manuscript / abstract / introduction / discussion / SI / figures / captions / Word formatting]
Main contribution: [your current best statement, if available]
Files: [draft, SI, figures, data, code, references, and journal template]

Preserve scientific accuracy, use simple English, remove defensive AI-style writing,
and return a journal-ready DOCX using the included manuscript template.
```

Codex can also invoke it automatically when the request clearly concerns high-level manuscript revision, SI, scientific figures, captions, evidence consistency, or publication Word formatting. Explicitly writing `$scientific-manuscript-writing` is the most reliable entry point.

## What to provide

For the best result, provide the target journal and article type; current manuscript and SI; figures and captions; source data or verified result tables; analysis/plotting code; reference library; and any required Word or journal template. Missing evidence is marked for verification rather than invented.

## Main files

- `skills/scientific-manuscript-writing/SKILL.md`: routing and non-negotiable standards.
- `skills/scientific-manuscript-writing/references/master-prompt.md`: comprehensive Chinese reusable prompt.
- `skills/scientific-manuscript-writing/references/`: writing, evidence, SI, caption, figure, Word, and validation contracts.
- `skills/scientific-manuscript-writing/assets/Manuscript Template.docx`: de-identified master Word template.

## 中文快速使用

可以直接把本仓库地址发给 Codex，并附上下面这句话：

```text
请使用 $skill-installer 安装这个公开仓库中的 Skill：
https://github.com/yizheng-hub/scientific-manuscript-writing-skill
Skill 路径是 skills/scientific-manuscript-writing。
```

安装完成后，在下一轮对话中写：

```text
请使用 $scientific-manuscript-writing，按照目标期刊要求完善这篇论文的正文、SI、图片、caption、参考文献和 Word 排版。
```

## Privacy and reference images

This public package contains only generic, de-identified instructions and placeholders. It contains no manuscript-specific title, authors, study topic, data, results, figures, review comments, file paths, or submission details.

Published reference images are not redistributed here because their licenses may not permit republication. Users may supply reference figures they are entitled to use; the skill will extract visual principles without copying scientific content.

## License

MIT. Third-party documents, figures, journal styles, and trademarks remain subject to their respective rights and terms.
