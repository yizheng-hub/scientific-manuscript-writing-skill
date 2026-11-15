# Scientific Manuscript Writing Skill

[![Reusable Skill](https://img.shields.io/badge/Reusable-Skill-111827)](https://agentskills.io/specification)
[![GitHub stars](https://img.shields.io/github/stars/yizheng-hub/scientific-manuscript-writing-skill)](https://github.com/yizheng-hub/scientific-manuscript-writing-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A reusable skill for scientific manuscript writing, academic editing, narrative Supplementary Information (SI), publication figures, captions, verified references, reproducible plotting, and journal-ready Word deliverables.

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

## Compatible agents

The core package follows the portable Agent Skills layout and does not depend on one model provider. It can be installed for Codex, Claude Code, Kimi CLI, and other agents supported by `gh skill install`.

| Agent | GitHub CLI installation |
|---|---|
| Codex | `gh skill install yizheng-hub/scientific-manuscript-writing-skill scientific-manuscript-writing --agent codex --scope user` |
| Claude Code | `gh skill install yizheng-hub/scientific-manuscript-writing-skill scientific-manuscript-writing --agent claude-code --scope user` |
| Kimi CLI | `gh skill install yizheng-hub/scientific-manuscript-writing-skill scientific-manuscript-writing --agent kimi-cli --scope user` |

The optional `agents/openai.yaml` file supplies UI metadata for OpenAI hosts. Other agents ignore it and use the same `SKILL.md`, references, and assets.

## Install

### Option 1 — GitHub CLI

Choose the agent identifier from the table above and install at user scope. For example:

```bash
gh skill install yizheng-hub/scientific-manuscript-writing-skill scientific-manuscript-writing --agent claude-code --scope user
```

To check for later updates:

```bash
gh skill update scientific-manuscript-writing
```

### Option 2 — ask an agent to install it

If the agent can run shell commands or has a skill installer, send:

```text
Install the public Agent Skill from
https://github.com/yizheng-hub/scientific-manuscript-writing-skill.
The skill path is skills/scientific-manuscript-writing.
Install it for this agent at user scope, review the files before enabling it,
and tell me when a new session can use it.
```

In Codex, the equivalent explicit prompt is: `Use $skill-installer to install the skill at skills/scientific-manuscript-writing from this repository.` Installer names and explicit-invocation syntax can differ in other agents.

This repository follows the standard `skills/<skill-name>/SKILL.md` discovery layout.

## Use it

Start a new agent session and ask it to use the `scientific-manuscript-writing` skill. In Codex, the explicit form is:

```text
Use $scientific-manuscript-writing to revise this paper.

Target journal: [journal]
Task: [full manuscript / abstract / introduction / discussion / SI / figures / captions / Word formatting]
Main contribution: [your current best statement, if available]
Files: [draft, SI, figures, data, code, references, and journal template]

Preserve scientific accuracy, use simple English, remove defensive AI-style writing,
and return a journal-ready DOCX using the included manuscript template.
```

Agents that support automatic skill discovery may load it when a request clearly concerns high-level manuscript revision, SI, scientific figures, captions, evidence consistency, or publication Word formatting. Explicitly naming the skill is the most reliable cross-agent entry point.

## What to provide

For the best result, provide the target journal and article type; current manuscript and SI; figures and captions; source data or verified result tables; analysis/plotting code; reference library; and any required Word or journal template. Missing evidence is marked for verification rather than invented.

## Main files

- `skills/scientific-manuscript-writing/SKILL.md`: routing and non-negotiable standards.
- `skills/scientific-manuscript-writing/references/master-prompt.md`: comprehensive Chinese reusable prompt.
- `skills/scientific-manuscript-writing/references/`: writing, evidence, SI, caption, figure, Word, and validation contracts.
- `skills/scientific-manuscript-writing/assets/Manuscript Template.docx`: de-identified master Word template.

## 中文快速使用

这是一个通用 Agent Skill，不限于 Codex。可以将仓库地址发给 Codex、Claude Code、Kimi CLI 或其他支持 Agent Skills 的智能体，并附上：

```text
请安装这个公开仓库中的 Agent Skill：
https://github.com/yizheng-hub/scientific-manuscript-writing-skill
Skill 路径是 skills/scientific-manuscript-writing。
请按当前智能体的用户级 Skill 目录安装，并在启用前检查文件。
```

安装完成后，新建一轮对话并写：

```text
请使用 scientific-manuscript-writing Skill，按照目标期刊要求完善这篇论文的正文、SI、图片、caption、参考文献和 Word 排版。
```

## Privacy and reference images

This public package contains only generic, de-identified instructions and placeholders. It contains no manuscript-specific title, authors, study topic, data, results, figures, review comments, file paths, or submission details.

Published reference images are not redistributed here because their licenses may not permit republication. Users may supply reference figures they are entitled to use; the skill will extract visual principles without copying scientific content.

## License

MIT. Third-party documents, figures, journal styles, and trademarks remain subject to their respective rights and terms.
