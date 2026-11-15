# Scientific figure design and review

## Figure-led narrative

Plan the paper as a sequence of visual evidence. Assign each figure one scientific question and each panel one non-duplicative role, such as context, central result, distribution, mechanism, validation, comparison, uncertainty, or boundary. Results panels must display real data, model output, or a verifiable analysis. Use a conceptual framework or flow diagram only in Methods or a study-design overview when it materially helps the reader.

Aim for substantial multi-panel figures when the evidence supports them, often four or more panels in this house style. Never add a panel merely to reach a count.

## Choose the graphic from the scientific relation

Prefer displays that reveal the structure the reader must evaluate:

- distributions, dot-and-interval or raincloud plots for variation;
- effect sizes and confidence intervals for comparisons;
- paired slopes or connected points for within-unit changes;
- frontiers, contours, or joint distributions for trade-offs;
- maps with physically meaningful encodings for spatial coverage or patterns;
- trajectories and event windows for temporal dynamics;
- ranked or decomposed displays for contributions;
- local enlargement only when it resolves genuine crowding or detail.

Do not default an entire figure set to simple line, heatmap, bar, or column plots because they are easy to code. Use them when they are the clearest representation. Visual sophistication comes from an appropriate evidence structure and disciplined hierarchy, not ornament.

When local reference figures are available, use them as a visual grammar rather than as content to copy: emulate their dense but readable multi-panel composition, restrained palette, layered encodings, map or distribution emphasis where scientifically appropriate, and compact use of horizontal space. Preserve the new study's actual data relationships and never force an unsuitable chart merely to resemble a reference.

## House style

- Times New Roman throughout. Default body labels: 11 pt; panel titles: 12 pt bold. If final-size constraints require 9/10 pt, change the entire figure set consistently rather than shrinking isolated figures.
- Panel labels and titles use `(a) Title` with one space. Align titles within rows/columns when their roles are parallel.
- Use black regular text and low-saturation, color-blind-aware palettes. Keep the same object, condition, or direction in the same color across the manuscript and SI.
- Legends have no border or background. Place them in genuine empty space or reserve a legend region; never cover data, labels, error bars, axes, or another panel.
- A bubble-size legend must use the same area scaling as the plotted bubbles. Separate size and color legends when they encode different quantities.
- Maps should be large enough to carry the spatial argument. A dominant map may occupy at least twice the area of one supporting panel. Use shared extent, normalization, and legend semantics for comparable maps. Inset maps need source boxes and connectors.
- Keep axis lines, units, tick conventions, and comparable panel sizes consistent. Align same-row x labels and same-column y labels.
- Reduce empty outer margins and panel gaps only after preserving internal room for data and text. Tight layout means compact panel-to-panel spacing, not cramped content.

## Zero-overlap gate

At final publication size, inspect every panel for legend/data, legend/text, label/error-bar, title/panel, and adjacent-panel overlap; clipped labels, symbols, color bars, or annotations; inconsistent axes; excessive blank space; unreadable fonts after Word placement; distorted aspect ratio; inconsistent color meaning or duplicate legends; and internal audit terms, code names, failure labels, or process status.

Fix layout, text length, axis range, legend placement, or panel allocation before reducing font size. Treat any text–text, text–graphic, graphic–graphic, legend–data, or cross-panel collision as a failed figure, even if the overlapping elements remain partly readable.

Inspect the exported asset at its final physical size. Verify raster DPI or vector output, font embedding, stroke widths, clipping, transparency and color mode, contrast and color-blind legibility, grayscale readability, preserved aspect ratio, and agreement between plotted values and verified source tables. The export—not only the notebook canvas—must pass.

## Figure-to-text gate

- Cite and analyze every panel in the main manuscript or corresponding SI section.
- Explain the relationship among panels, not only what each panel contains.
- Confirm that the caption independently defines the visual encoding and abbreviations.
- Confirm that the plotted numbers match the verified result tables and that the plotting notebook recreates the delivered asset.

