# Scientific figure design and review

## Figure-led narrative

Plan the paper as a sequence of visual evidence. Before plotting, create a portfolio storyboard with one row per figure: scientific question, take-home finding, data relation, candidate chart families, geographic opportunity, chosen panel roles, and why the chosen visual form is superior to simpler alternatives. Assign each figure one scientific question and each panel one non-duplicative role, such as context, central result, distribution, mechanism, validation, comparison, uncertainty, or boundary. Results panels must display real data, model output, or a verifiable analysis. Use a conceptual framework or flow diagram only in Methods or a study-design overview when it materially helps the reader.

Panel count is evidence-driven. Build substantial multi-panel figures when complementary views are needed, but never add a panel merely to reach a count or split one weak chart into several cosmetic variants.

## Methods framework and conceptual figures

A Methods framework is allowed only when it explains a scientific or computational relation that prose cannot show as clearly. It must be designed as a publication figure, not as a generic slide diagram.

- Do not use a row of rounded colored cards, repeated text boxes, decorative gradients, or template-style arrows as a substitute for scientific structure.
- Show the minimum necessary entities, transformations, inputs, outputs, and dependencies. Prefer short labels, mathematical symbols, data-shaped glyphs, or compact schematics over sentences copied from Methods.
- Show the study-specific logic needed to judge validity: independent units, controls or comparators, train/validation/test or other data splits, leakage barriers, estimand, calibration/validation, uncertainty propagation, and which outputs are observed, estimated, inferred, or predicted, as applicable. A visually clean framework that hides these relations fails.
- Stage letters inside boxes are not panel labels. A single schematic may use unlettered stages; a genuinely multi-panel framework must place the exact `(a) Title`, `(b) Title`, ... headers outside the panel content.
- Use restrained semantic color, consistent line weight, direct connectors, and a clear reading path. Arrows may not cross text, boxes, or each other without a routing reason.
- Apply the same Times New Roman typography, final-size legibility, compactness, caption, and zero-overlap gates as data figures. Reject a framework that looks like presentation software even when its content is technically correct.

## Choose the graphic from the scientific relation

Prefer displays that reveal the structure the reader must evaluate:

- distributions, dot-and-interval or raincloud plots for variation;
- effect sizes and confidence intervals for comparisons;
- paired slopes or connected points for within-unit changes;
- frontiers, contours, or joint distributions for trade-offs;
- maps with physically meaningful encodings for spatial coverage or patterns;
- small-multiple or bivariate maps for comparable geographic scenarios, provided they share extent, normalization, and legend semantics;
- trajectories and event windows for temporal dynamics;
- ranked or decomposed displays for contributions;
- flow, transition, or alluvial displays when movement between states is the scientific result;
- ridgeline, half-violin, beeswarm, hexbin, contour, or density displays when they reveal distributional or joint structure that summary marks hide;
- local enlargement only when it resolves genuine crowding or detail.

Do not default an entire figure set to simple line, point-line, lollipop, heatmap, bar, or column plots because they are easy to code. Use them when they are the clearest representation, not as the repeated grammar of the paper. A heatmap is appropriate for a genuinely dense matrix whose two-dimensional pattern matters; it is not the default container for a small table of values. A dot-line plot is appropriate for ordered, paired, or interval information; it is not a generic replacement for every result. Visual sophistication comes from an appropriate evidence structure, layered but interpretable encodings, and disciplined hierarchy—not ornament.

For a central result, reject an isolated default line, point, bar, or column chart when complementary uncertainty, distribution, composition, spatial heterogeneity, scenario structure, mechanism, or validation evidence is necessary to judge the claim or materially changes its interpretation. The elementary mark may remain simple; the finished figure should coordinate only the layers needed to support the claim. A single simple chart is acceptable when it is genuinely sufficient for one decisive comparison.

When local reference figures are available, use them as a visual grammar rather than as content to copy: emulate their dense but readable multi-panel composition, restrained palette, layered encodings, map or distribution emphasis where scientifically appropriate, and compact use of horizontal space. Preserve the new study's actual data relationships and never force an unsuitable chart merely to resemble a reference.

## Composition grammar from high-level published figures

Translate reference quality into structure, not decoration.

- When the evidence is asymmetric, establish one visual anchor: a dominant map, response surface, trajectory, distribution, or mechanism panel carries the main claim while supporting panels explain scale, uncertainty, comparison, or local detail. Matched experiments, scenario panels, or coequal maps may instead use equal visual weight when direct comparison is the reading task.
- Build a cross-scale reading path: overview to regional detail, global pattern to mechanism, temporal trend to spatial consequence, or distribution to effect estimate. Use insets, connectors, aligned axes, and shared legends only when they make that path explicit.
- Mix complementary chart families inside a figure instead of cloning one panel type. Heterogeneous panels should answer one question, share typography and color semantics, and remain visually comparable.
- Encode data through position first, then restrained color, size, shape, line, texture, or transparency. Every encoding must be defined and interpretable; decorative layers fail.
- Use asymmetric layouts when evidence importance is asymmetric. Equal-sized 2-by-2 panels are not a default. A principal panel may occupy half or more of the figure while compact diagnostic panels use the remaining space.
- Maintain high information density without crowding: reserve whitespace for reading and legends, not as a consequence of undersized plots. Integrate legends, scale bars, color bars, and regional summaries into genuine negative space.
- Make maps analytical rather than illustrative. Boundaries provide context; fills, symbols, flows, contours, uncertainty, or linked regional summaries carry the result.

Before coding, sketch at least two substantially different layouts and reject the weaker one against the scientific reading path. Do not accept a figure merely because each panel is individually correct.

## Dense composition and edge utilization

High information density means that most of the canvas carries readable evidence, not that every space is filled with marks.

- Build figures in evidence bands: for example, aligned small multiples across the top; a dense comparison matrix below; and one or two map, mechanism, or local-detail panels at the side. Each band must advance the same claim at a different scale.
- Use shared axes, shared legends, shared color bars, aligned category orders, and repeated geographic extents to reduce duplicated furniture. A shared legend belongs beside the panels it governs, not in a remote empty corner.
- Use nested insets only for a real change of scale, a threshold, or a locally crowded pattern. Give the inset a clear source region, connector, or visual reason; a miniature duplicate with no added inference fails.
- Design the final physical composition with `GridSpec`, `subplot_mosaic`, inset axes, or deliberate axes positions. Automatic `tight_layout` alone is not a design method.
- Treat edge use as a preflight. After labels and legends are included, unnecessary outer margins should normally be only a few percent of the canvas, panel gaps should be visually consistent, and no large quadrant should remain blank because plots were undersized. These are diagnostic targets, not permission to clip labels.
- Export with a tight bounding box only after checking that panel headers, map insets, color bars, scale bars, north arrows, and legend glyphs remain complete. A cropped character or symbol is a failure even when whitespace is reduced.
- Preserve a clear hierarchy at thumbnail size and readable labels at final size. If density is achieved only by shrinking text, the layout has failed.

## Panel occupancy, figure height, and spacing

Audit the data envelope and the allocated panel rectangle separately. Sparse evidence must not be stretched across a large panel merely because the default subplot grid assigned that space.

- After transformations, uncertainty, thresholds, and annotations are included, compare the finite data envelope with the allocated panel rectangle. Treat visually dominant unused space as a redesign trigger when it does not serve a reading task. Do not use an occupancy percentage as a quota and never tighten an axis merely to make marks fill the panel.
- Tighten limits, change orientation, use a compact strip or inset, combine aligned summaries, or reduce the panel/figure height before accepting large internal blank regions. Never crop meaningful uncertainty, hide an outlier, or change a common scale merely to improve occupancy.
- Panels with only a few points or categories should normally receive less area when their evidentiary role is also secondary. A sparse decisive estimate may remain the visual anchor. For a secondary sparse row, use deliberate `height_ratios`, shorter axes, or a shorter total figure height rather than leaving most of each panel empty.
- Measure horizontal and vertical gaps after tick labels, axis labels, and legends are present. A large blank band is a failure when it results from automatic padding or undersized plots; it is valid when fixed aspect, deliberate group separation, a shared comparison scale, or another reading task requires it.
- Do not place the first column far from the second merely because an automatic layout reserved excessive label space. Adjust axes rectangles and label padding explicitly while preserving alignment.

Scientific comparison, honest baselines, uncertainty, and shared scales take priority over compactness. When a deliberately sparse range is retained, state its reading purpose in the panel manifest.

## Axis and grid scaffold

Choose one figure-level scaffold before styling individual panels.

- Comparable Cartesian panels must use the same spine policy, tick direction, tick length, grid direction, grid color, line width, and alpha. Default to visible left and bottom axes for quantitative Cartesian panels unless another convention is justified.
- Do not show pale dashed or solid gridlines in some comparable panels while leaving others blank by accident. Use either no grid or one restrained major-grid treatment consistently; reference thresholds are not gridlines and must remain visually distinct.
- Axis omission is acceptable for maps, matrices, pictograms, diagrams, or intentionally axis-free distributions. It must be consistent within the same chart family and must not remove a quantitative scale the reader needs.
- When panels use different chart families, consistency means a coherent visual grammar rather than identical furniture. Record intentional exceptions in the panel manifest and verify that they do not look like missing axes.
- Preserve axis integrity before styling. Use zero when magnitude-from-zero is part of the task; otherwise show the scientifically relevant range without implying a false baseline. Label log, reciprocal, normalized, indexed, or other transformed axes explicitly. Avoid broken axes; if unavoidable, mark the break unambiguously and never use it to exaggerate a difference. Avoid dual axes unless the relation cannot be read more honestly as aligned panels, and map each series to its axis unmistakably.
- Comparable panels should share limits, transformations, tick locations, and color normalization when readers must compare absolute values. If different limits are scientifically necessary, make the difference conspicuous. Diverging scales require a meaningful stated midpoint; clipped color scales and saturated values must be disclosed in the legend or caption.

## Conditional advanced encodings

Use complex forms when their geometry matches the question.

- Small multiples are preferred when readers must compare the same relation across regions, scenarios, materials, times, or outcomes. Keep axes, scales, annotation rules, and category order consistent; consolidate legends.
- A matrix may be paired with marginal bubbles, distributions, maps, or ranked summaries when both the dense two-dimensional pattern and its totals matter.
- Radial bars may summarize many categories when the task is to compare overall profiles or spatial/category cycles. They are poor for precise rank comparisons; provide reference rings, readable labels, a fixed category order, and a conventional supporting panel when exact differences matter.
- Radar or polar profiles are acceptable for normalized multivariate shape comparisons with common directionality and scale. Do not use them for raw variables with incompatible units or as the only evidence for a quantitative claim.
- Stacked bars or decomposition bands are appropriate when parts sum to a meaningful whole. Label only decision-relevant shares and provide a direct total or baseline so composition is not mistaken for magnitude.
- Network maps must encode node and edge quantities with interpretable size, color, width, direction, or uncertainty. Pair them with a non-map summary when the reader must compare totals or time trends precisely.
- Map insets, north arrows, scale bars, administrative boundaries, and locator boxes are functional only when they help interpret extent, scale, or local detail. Do not add cartographic decoration without a reading task.

## Portfolio diversity gate

Review all main and supplementary figures together before accepting any one figure.

- Do not let one chart family dominate the manuscript unless the repeated form is required for direct comparison.
- Adjacent main figures should not repeat the same panel grammar, layout, and palette with only different variables.
- A heatmap-dominant figure should normally be followed by a different evidence form, such as a map, distribution, effect-size display, joint relationship, decomposition, trajectory, or flow.
- Combine complementary evidence within a figure: for example, a dominant map with distribution and uncertainty panels, or a joint-density panel with effect estimates and a decomposition.
- Judge complexity at the level of the evidence composition, not the individual mark. Lines, points, bars, cells, contours, and polygons become publication-level when their coordinated roles reveal trajectory, distribution, scale, mechanism, or uncertainty without redundancy.
- Reject a portfolio made mainly of diagnostic matrices, sparse scatters, simple bars, or point-line panels when the data support richer distributional, spatial, relational, or multiscale views.
- Use visual complexity only when every encoding answers a scientific question. “Advanced” never means decorative complexity or more colors.
- Review main-figure variety separately from SI. Repetition is justified for direct comparison, especially across SI sensitivity analyses or matched cohorts; change chart families only when the data relation or reading task changes. Reject monotony that comes from default plotting, not a repeated grammar that improves valid comparison.
- Do not make every figure equally dense. Use the richest multi-panel compositions for central evidence and simpler figures for single decisive comparisons, while maintaining the same typography, palette semantics, and finish.

## Geographic evidence

When valid coordinates, boundaries, networks, regions, or spatial exposure variables exist, actively test whether geographic displays clarify heterogeneity, transferability, coverage, clustering, scale, or decision relevance. Prefer using multiple spatial views across the paper when different geographic questions are genuinely present. Do not add a map merely because a place name exists.

- A map that carries a principal result should be visually dominant, not a tiny silhouette surrounded by unused canvas.
- Show meaningful geographic context with restrained boundaries, appropriate projection, consistent extent, and data-driven fill, symbol, flow, contour, or uncertainty layers.
- Use insets, source boxes, connectors, small multiples, or linked statistical panels when they explain scale or local detail.
- Avoid pale basemaps with only a few highlighted polygons when the same information would be clearer as a focused extent or a data-rich spatial layer.
- Comparable maps must share normalization and legend semantics. State when values are counts, rates, modeled surfaces, uncertainty, or residuals.

## House style

These are hard defaults for this retained house style. An explicit target-journal rule or user-supplied figure template may override typography or panel-header syntax; record the override and apply it consistently across the complete figure set.

- Times New Roman throughout every visible text element, including panel labels, titles, axes, ticks, annotations, legends, color bars, map labels, and inset labels. Default body labels: 11 pt; panel titles: 12 pt bold. If final-size constraints require 9/10 pt, change the entire figure set consistently rather than shrinking isolated figures.
- Panel labels and titles must appear as one header in the exact form `(a) Title`, with lowercase sequential letters, parentheses, and one space. A bare `a`, a separated panel letter, or a title without its marker fails preflight. Align headers within rows/columns when their roles are parallel.
- Use black regular text and coordinated low-saturation, color-blind-aware palettes. A useful starting family is muted blue `#5B8DB8`, teal-green `#4F9C91`, purple `#8C7AA9`, muted red `#D77A72`, ochre `#D5A94E`, and neutral gray `#A9B0B5`. Select only colors with defined semantics; do not use the full palette merely for variety. Pair red/green distinctions with shape, line, or texture cues.
- Legends have no border. Prefer a transparent legend in genuine empty space or a reserved legend region; on a dense map, contour, or field, a compact neutral opaque or haloed background is allowed when it improves contrast without hiding evidence. Never cover data, labels, error bars, axes, or another panel.
- A bubble-size legend must use the same area scaling as the plotted bubbles. Separate size and color legends when they encode different quantities.
- Maps should be large enough to carry the spatial argument. A dominant map may occupy at least twice the area of one supporting panel. Use shared extent, normalization, and legend semantics for comparable maps. Inset maps need source boxes and connectors.
- Keep axis lines, units, tick conventions, and comparable panel sizes consistent. Align same-row x labels and same-column y labels.
- Reduce empty outer margins and panel gaps after preserving internal room for data and text. Tight layout means compact panel-to-panel spacing, not cramped content. Reject large unused regions caused by undersized panels, remote legends, or poorly chosen aspect ratios.
- Derive related colors from a small set of semantic base hues: one hue family per metric, material, mechanism, or direction; use lightness, saturation, alpha, texture, or outline for scenarios and uncertainty. Do not assign a new unrelated color to every series.

## Zero-overlap gate

At final publication size, inspect every panel for legend/data, legend/text, label/error-bar, title/panel, and adjacent-panel overlap; clipped labels, symbols, color bars, or annotations; inconsistent axes; excessive blank space; unreadable fonts after Word placement; distorted aspect ratio; inconsistent color meaning or duplicate legends; missing parentheses in panel headers; non-Times New Roman text; and internal audit terms, code names, failure labels, or process status.

Fix layout, text length, axis range, legend placement, or panel allocation before reducing font size. Treat any unintended text–text, text–graphic, legend–data, or cross-panel occlusion that hides evidence or changes interpretation as a failed figure. Intentional graphic layering—such as markers on lines, confidence bands, error bars, contours, networks, or map overlays—is valid when every layer remains interpretable.

Annotation text may not touch or cross tick labels, tick marks, axis spines, threshold lines, markers, error bars, or another annotation. It may sit over a background grid only when an opaque or haloed text treatment keeps both the label and data unambiguous. After `fig.canvas.draw()`, inspect rendered bounding boxes for every title, tick label, axis label, annotation, legend, and color-bar label; use explicit offsets or reserved space to eliminate unintended intersections. Automated geometry is a preflight, not a substitute for final visual inspection.

Inspect the exported asset at its final physical size. Verify raster DPI or vector output, font embedding, stroke widths, clipping, transparency and color mode, contrast and color-blind legibility, grayscale readability, preserved aspect ratio, and agreement between plotted values and verified source tables. The export—not only the notebook canvas—must pass.

## Figure-to-text gate

- Cite every panel in the main manuscript or corresponding SI section. Analyze distinct evidentiary roles individually; a systematic small-multiple, matched cohort, or repeated sensitivity series may be addressed as an explicit panel range or logically defined group when the caption enumerates its members and the prose explains the group-level pattern rather than reciting panels mechanically.
- Explain the relationship among panels, not only what each panel contains.
- Confirm that the caption independently defines the visual encoding and abbreviations.
- Confirm that the plotted numbers match the verified result tables and that the plotting notebook recreates the delivered asset.
- Run a portfolio-level review after individual figures pass: confirm chart-family diversity, map opportunities, palette consistency, panel-header syntax, balanced information density, and the absence of repeated visual grammar without scientific justification.

