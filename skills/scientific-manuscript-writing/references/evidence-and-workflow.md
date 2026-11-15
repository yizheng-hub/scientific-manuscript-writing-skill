# Evidence, analysis, and reproducibility workflow

## Establish the evidence base

Before expensive experiments or simulations, define the scientific question and primary metric; whether each construct is directly observed, estimated, inferred, proxied, or model-derived; samples, groups, inclusion rules, controls, and baselines; denominators, weighting, treatment of zeros, exclusions, and missing values; replication and data-leakage controls; preprocessing rules; uncertainty and statistical tests; parameters, units, versions, seeds, and stopping rules; needed sensitivity, ablation, robustness, and validation analyses; ethics and data-use requirements; and expected figures and tables.

Maintain a construct dictionary with the conceptual and operational definition, observation unit, instrument or model, aggregation scale, target population and estimand, transformations, calibration or validation, and material proxy limitations. Carry the observed/estimated/inferred/proxied/model-derived status into prose, axes, tables, and captions.

Maintain a sample-flow record with counts after each exclusion or imputation step and the `n` for each reported group or panel. Distinguish true zeros, structural zeros, censored or below-detection values, and unobserved values. Record missingness assumptions, complete-case or imputation rules, weight construction and normalization, and sensitivity analyses when these choices could change the conclusion.

Acceptance criteria must concern data integrity, model validity, reproducibility, or prespecified statistical rules. Never require a preferred direction, strategy ranking, effect size, or significant result before continuing.

## Reproduce before extending

Lock the manuscript, SI, data, model, code, and environment versions. Maintain a claim/result ledger with the data path and checksum or version; cohort and filters; variables, units, transformations, and statistic; code commit plus file, function, notebook cell or command; environment and seed; output path and checksum; and verification status. Reproduce the central numbers before adding analyses. If reproduction fails, locate the discrepancy instead of covering it with a new analysis.

Separate validation already completed, genuinely missing validation, implementation diagnostics that do not belong in the manuscript, and study boundaries that change interpretation.

## Resolve risks in evidence, not rhetoric

When a credible concern can be answered with an available control, sensitivity analysis, independent validation, or direct comparison, resolve it before final prose. Do not use defensive wording as a substitute for an analysis. If the necessary evidence cannot be obtained, narrow the claim and describe the study-level boundary briefly and neutrally.

## Plotting notebooks

When the project uses code-backed figures, keep a direct, editable path from results to every publication figure:

- `plot.ipynb` should read retained data or verified analysis outputs and produce the final figure.
- One clearly labeled cell or contiguous cell group should create one manuscript or SI figure.
- The notebook should contain the actual panel assembly, fonts, colors, legends, labels, dimensions, and export settings. It should not be only a thin `plot.show()` or wrapper around a separate styling script.
- Shared style constants and small helper functions may live in the notebook to avoid duplication. Preserve established analysis modules for scientific calculations.
- Save the figure-to-data and panel-to-analysis mapping. Confirm that the notebook reproduces the delivered file from a clean kernel.
- Give every panel a manifest row containing immutable input and checksum, exact columns and row filters, aggregation and normalization, denominator and `n`, estimator and uncertainty, code cell or function, exported asset, caption clause, and manuscript/SI citations.
- Use pinned dependencies, portable relative paths, deterministic seeds, and immutable inputs. Prohibit manual post-processing and hidden external state. Clear outputs, run all cells, retain an execution log, and fail on stale or missing inputs.
- Validate exported files, not only the live canvas: expected filename, dimensions, final physical size, DPI or vector status, fonts, and agreement between plotted/caption values and the verified result table.

## Final consistency gate

Check that manuscript, SI, captions, tables, source data, plotting outputs, and any cover letter agree on population and denominator; weighting, zeros, exclusions, and missing values; comparison baseline; absolute and relative magnitude; statistic, uncertainty, units, and significant digits; observed versus inferred status; terminology and abbreviation; figure/table number, panel reference, and cross-reference style; and software/model version. Replace unsupported absolutes such as “identical” or “no difference” with the precise relationship the evidence establishes.

For inferential results, record effect size; uncertainty type, level, and computation; independent unit and replicate type; model or test; sidedness and assumptions; multiplicity adjustment; exact-`P` convention; and how uncertainty propagates through transformations or weighting. Apply a journal-aware rounding rule consistently across text, tables, captions, and figures.

