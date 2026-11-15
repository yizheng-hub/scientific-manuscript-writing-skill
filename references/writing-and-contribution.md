# Writing, contribution, and defensive-language review

## Contribution before prose

Before drafting, write five short statements supported by the actual evidence:

1. **Problem:** What consequential scientific or practical problem does the study address?
2. **Gap:** What decision, relationship, or mechanism could prior work not resolve?
3. **Finding:** What changed, differed, or became identifiable in this study?
4. **Advance:** What new understanding follows beyond the reported numbers?
5. **Use:** Who can act differently because of this advance, and under what conditions?

Do not call scale, technical complexity, simulation volume, or a new metric a contribution by itself. The contribution is the new scientific understanding enabled by those elements.

Create a contribution matrix before substantial rewriting:

| Contribution claim | Direct evidence | Figure panels | Boundary | Where emphasized |
|---|---|---|---|---|
| [One sentence] | [Analysis/result] | [Fig. X(a-c)] | [Condition that changes meaning] | Title / Abstract / Introduction / Results / Discussion / Cover letter |

Also create a novelty-delta table for the closest precedent in every relevant field: what that work already established; what relationship, decision, or mechanism remained unresolved; what this study newly reveals; and which evidence supports that delta. A combination of known methods, larger scale, or first use in a domain is not automatically a conceptual advance.

If a claim lacks direct evidence, narrow the claim or perform the necessary analysis. Do not repair an evidence gap with more confident wording.

## Keep one story across the manuscript

- **Title:** Name the research object and the most transferable finding. Lead with the method only when the method is the principal scientific advance.
- **Abstract:** Use a funnel: broad importance -> established knowledge -> specific gap -> study question and design -> principal finding -> supporting findings -> integrated contribution. Each sentence should narrow or advance the preceding one. Do not compress every result into a list.
- **Introduction:** Use a paragraph-level funnel: practical motivation and the decision at stake; the scientific challenge; established knowledge and the precise gap; study design, contribution, and principal questions; then a brief preview of what the findings change. Explain early why the assessment problem matters to relevant researchers, practitioners, or decision-makers. Support the gap with the closest verified literature and synthesize rather than catalogue prior work. The sequence is functional, not a mandatory paragraph count.
- **Results:** Use finding-led subheadings. Start each section with the question or result, then show panel-level evidence and its meaning.
- **Discussion:** Keep it distinct from Results. For each major insight, move through synthesis -> relation or tension with cited literature -> evidence-supported explanation -> plausible alternative tested by available evidence -> transfer boundary -> implication. Omit a step when it is not scientifically relevant; never fill it with speculation. Do not repeat Results as a list.
- **Cover letter:** Explain the problem, contradiction or decision consequence, the principal findings, why the target journal's broad readers should care, and what is distinct from prior work.

## Simple English and selective numbers

Prefer concrete subjects and verbs. Introduce a technical term only after the reader understands the scientific problem it helps solve. Replace internal labels, code names, and compressed compounds with established scientific terms. In the line-edit pass, keep one main idea per sentence, unpack noun stacks, define before abbreviating, maintain given-to-new information flow, and make the opening sentence of each paragraph recoverable by a non-specialist.

Use numbers when they establish the magnitude or direction of a principal result, show uncertainty or robustness, define the population or comparison, or distinguish scientifically different cases. Move exhaustive counts, parameter grids, and secondary values to Methods, SI, or tables. A paragraph should not become a sequence of numerals with no hierarchy.

Make every quantitative comparison interpretable. Pair a change with its meaningful baseline; add a percentage or standardized effect when an absolute value alone is scale-dependent. For a mean, proportion, or pooled result, state the population, denominator, weighting, treatment of zeros, exclusions, and missing values. Do not call an all-case mean a typical positive-case value. Match significant digits to measurement or model precision, and reserve words such as “identical”, “unchanged”, and “no difference” for cases supported at the stated precision or by an appropriate test.

Define a central construct at first use and distinguish it from nearby concepts. If the construct is estimated, inferred, proxied, or model-derived, say so consistently instead of presenting it as directly observed.

Classify every central claim as descriptive, associational, predictive, attributive, mechanistic, or causal. Audit verbs against the study design and evidence level. Do not turn temporal order, model attribution, prediction, or association into causation through wording.

## Detect and remove defensive writing

Defensive writing is language whose main function is to anticipate criticism rather than advance the question, evidence, interpretation, or necessary boundary. Common forms include:

- adding "this does not mean..." immediately after a supported finding;
- repeatedly stressing that a metric is not a different construct that nobody claimed it was;
- inserting a limitation after each result;
- listing failed runs, skipped tests, internal stopping reasons, or audit status;
- using vague hedges in layers: "may potentially perhaps suggest";
- pre-emptively rebutting imagined reviewers;
- describing the paper as safe, validated, passed, failed, qualified, or reviewed when those are internal workflow labels.

For every sentence, ask whether it performs one of these functions: scientific claim, evidence, interpretation, necessary method, logical transition, literature context, reproducibility detail, or material boundary. Delete or rewrite sentences that perform none.

Instead of a broad disclaimer, state the condition that actually governs the claim:

> Under [tested population/conditions], Y changed by [effect and uncertainty].

This preserves scientific scope without turning the paragraph into a rebuttal.

## Scientific honesty with non-positive results

Do not hide a result because it is null, adverse, or contrary to the expected direction. Decide whether it changes the scientific conclusion.

- If it does, state the insight it reveals, such as a trade-off, boundary condition, or separation between mechanisms.
- If it is a technical failure that does not affect valid results, keep it in internal records.
- If it invalidates a claim, repair the analysis or narrow the claim before writing.

Keep local scope conditions beside the claim they govern: population, setting, comparator, measured versus inferred status, and tested range. These are not defensive limitations. Reserve the final Discussion paragraph for two or three confident, factual sentences on genuine study-level limitations and the most specific next research direction. Ordinary implementation diagnostics belong in code documentation or internal records.

For the house style, keep the genuine study-level limitations to two or three confident, factual sentences in the final Discussion paragraph. Do not distribute them through the manuscript.

## Reference discipline

Use no more than three references at one citation position and per atomic claim. Split compound claims when different sources support different parts. Each source must directly support the adjacent factual, methodological, theoretical, or comparative claim. Maintain an internal claim-level audit with the supporting passage, table, or figure; primary/secondary status; DOI or stable identifier; full-text verification date; and correction, retraction, or version check.

For a full-length high-level research article, aim for at least 45 verified references as a house-style coverage target, unless the target journal, article type, or field convention clearly calls for fewer. The number is never a pass criterion: never add an irrelevant source to reach it, and do not stop when relevant literature remains uncovered. Synthesize literature into an argument; do not turn the Introduction or Discussion into a catalogue of papers.

## Cold-read questions

- Can a broad scientific reader state the background, precise gap, main finding, innovation, contribution, and significance after the Abstract and main figures?
- Does each Results paragraph advance one idea rather than accumulate terms and numbers?
- Does every major claim point to evidence?
- Are contribution statements stronger than method descriptions but no stronger than the evidence?
- Are limitations concentrated and proportionate rather than scattered?
- Would removing a sentence make the scientific argument weaker? If not, remove it.

