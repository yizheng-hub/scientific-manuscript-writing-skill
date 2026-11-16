# Role-based self-validation

Use independent cold reads after the evidence, prose, figures, captions, and SI are assembled. Give each role the manuscript as a new reader would see it. Do not tell the evaluator the intended answer, suspected weakness, another reviewer's comments, or the planned revision.

## Independent-agent orchestration

For a full manuscript, SI, or journal-ready package, do not ask one agent to impersonate every reader in one shared response. Invoking this skill for a full package authorizes the independent review passes below unless the user explicitly forbids agent orchestration. When the host supports orchestration, assign each required role below to a separate agent or isolated context. Reviewers work in parallel when possible and cannot read one another's reports before submitting their own.

If separate agents are unavailable, run isolated sequential passes with fresh context and withhold prior reviews. Record this limitation in the internal validation report. A single blended “review from several perspectives” does not satisfy the full-manuscript gate.

Use one final integration agent only after the independent reports are frozen. The integrator groups findings as: scientific error or missing evidence; contribution/story problem; field-context problem; technical/method problem; broad-reader comprehension problem; figure/layout problem; publication-file defect; optional preference; or reviewer conflict. Verified evidence and explicit journal rules take precedence. Readability cannot overrule technical or field accuracy. If field and technical reviewers still disagree on a meaning-changing issue, acceptance is blocked until new evidence resolves it, the claim is narrowed to common ground, or the user makes an explicit adjudicating decision; merely escalating the issue does not pass the gate. Optional preferences may remain documented as non-blocking.

## Roles

### Professional academic editor

Judge whether the problem is consequential, the innovation is distinct from prior work, the contribution is supported, the story has broad relevance, and the title/abstract/figures earn further review. Identify the first place interest or comprehension drops.

### Broad-journal reviewer

Test the logic from question to claim, the adequacy of evidence and controls, the match between conclusions and data, the literature context, and whether alternative explanations are addressed by evidence rather than rhetoric.

### Field-expert reviewer

Review from inside the manuscript's research field. Test whether the stated gap is real, the closest prior art is represented fairly, the terminology and assumptions match field practice, the innovation is more than a renamed known method, and the contribution would change what specialists understand or do. Flag omitted field-standard baselines, controls, citations, or interpretations without duplicating the technical audit.

### Technical specialist reviewer

Audit the methods, estimand, data structure, baselines, statistics, uncertainty, reproducibility, parameter choices, figure values, and claim boundaries. This role protects accuracy when language is simplified.

### Cross-disciplinary scientific reader

Read outside the narrow specialty. State the background, gap, main finding, innovation, contribution, and impact in plain language. Mark every unexplained term, dense sentence, missing transition, or panel whose purpose is unclear.

### In-field novice reader

Assume foundational knowledge of the broad field but no familiarity with the paper's exact method, dataset, or subtopic. Use only the manuscript and captions. Separately state the background, precise gap, main finding, innovation, contribution, and impact. Explain the baseline, denominator, central construct, and what every main panel contributes. Distinguish direct observation, proxy or model output, inference, association, and causal claim. Flag places that require hidden project knowledge or insider shorthand.

### High-school or news reader

Read the title, abstract, introduction opening and final paragraph, main figure titles/captions, and discussion opening. State the background, precise gap, main discovery, innovation, contribution, and why society or practice should care. Identify who could act differently, what decision changes, and under what conditions. Write a one-sentence headline and two-sentence explainer, then have the technical reviewer check them for causal inflation, universality, certainty, and unsupported benefit. This role does not judge technical sufficiency; it tests whether the core story survives specialist language.

### Stand-alone visual reader

View each exported main or supplementary figure at final publication size with only its caption. Recover the figure question, factual takeaway, role of every panel, comparison and baseline, direction and decision-relevant magnitude, uncertainty, and the claim directly supported. Flag any answer that depends on surrounding prose, hidden disciplinary knowledge, color alone, or unreadable layout.

### Visual portfolio reviewer

View all main and supplementary figures as one set. Reject repeated heatmap, sparse point-line, bar, or layout grammar without a direct-comparison reason; a central result reduced to an isolated default chart when complementary uncertainty, distributional, compositional, spatial, mechanistic, or validation evidence exists; missed opportunities for valid geographic evidence; undersized maps surrounded by blank canvas; bare panel letters instead of `(a) Title`; non-Times New Roman text; uncontrolled palette drift; and any overlap or clipping. Confirm that each figure has a distinct scientific role while the full set retains consistent semantic colors and typography. At final size, also reject large unused outer margins, gaps comparable to a neighboring panel, sparse marks stretched through a full-height panel, a figure whose height could be reduced without losing evidence, inconsistent spines/ticks/gridlines among comparable Cartesian panels, duplicate legends, annotations crossing ticks/grids/spines/data, and any figure that appears dense only because text was reduced.

### Publication-file auditor

Inspect the final DOCX structure and rendered pages, not only the source prose. Reject ordinary tables unless they use exactly three rules (1.5 pt top, 0.5 pt below the header, 1.5 pt bottom), no vertical or extra internal rules, and Times New Roman 11 pt. Treat borderless equation-layout tables as a separate exception. Reject any equation stored as an image, any display equation outside a borderless one-row two-column container, or missing/nonsequential `Eq. (n)` numbering. Reject supplementary naming other than `Fig. S1`, `Table S1`, and top-level heading `S1. [Topic]` cited as `Section S1`. Audit the first-citation sequence independently for supplementary figures, supplementary tables, and numbered SI sections; each sequence must introduce S1, S2, S3, ... without gaps or reversals. Audit Figure/Table/Section/panel cross-references for grammar and run-level bold boundaries, including regular-weight conjunctions. Reject pagination formatting that produces the prohibited black square markers in the Word left margin, while preserving clean rendered pagination. Compare paragraph spacing, line spacing, indentation, headings, captions, figures, and table geometry against the retained Word template and inspect every rendered page.

## Common questions

Ask every role, at its appropriate level:

1. What problem does the study address, and why does it matter?
2. What was unknown before this work?
3. What is the main finding?
4. What is genuinely innovative?
5. What is the principal scientific contribution?
6. Which evidence most directly supports it?
7. What broader impact follows, without going beyond the data?
8. Where did the story become unclear or overly technical?

## Revision loop

1. Before testing, create a private evidence-anchored answer sheet for background, consequential problem, precise gap, main finding, innovation, contribution, impact, direct evidence, causal status, and material boundary. Keep it hidden from readers.
2. Collect each reader's independent paraphrase and confusion points. Compare meaning, not wording, against the answer sheet.
3. Separate accuracy problems, missing evidence, structural problems, and wording problems.
4. Resolve evidence problems before prose. Use the technical reviewer to approve any simplification that changes a scientific statement or its causal status, observed-versus-inferred status, population, comparator, direction, magnitude, uncertainty, or scope.
5. Use the field-expert reviewer to approve changes to novelty, prior-art comparison, field terminology, field-standard baselines, and specialist interpretation.
6. Revise only the passages and figures responsible for observed confusion; do not rewrite stable sections merely for stylistic variety.
7. Repeat every affected reader test plus the technical and field-expert reviews. Stop only when every mandatory role passes or every material objection has been resolved, narrowed to the evidence, or explicitly adjudicated by the user. In particular, no unresolved contribution/story, broad-interest, alternative-explanation, literature-context, evidence, novelty, method, or reviewer-conflict issue may remain; every stand-alone figure passes its recovery test; the visual portfolio has zero hard rejects; the DOCX validator passes or every remaining report is a documented journal-template override whose substituted rule passes inspection; and every rendered page passes publication-file inspection.

Record an internal matrix with: canonical answer; reader paraphrase for each required element; accuracy finding; confusion location; issue class; exact revision; field-expert result; technical-review result; stand-alone visual result; portfolio result; publication-file result; conflict disposition; retest result; and final gate status. Never expose this answer sheet or review history in the paper.

Save the validation report as an internal artifact. Do not insert role labels, scores, AI commentary, or review history into the manuscript.

