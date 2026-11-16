# Plot notebook contract

Use this contract when figures are generated from `plot.ipynb` or an equivalent notebook.

## One editable source of truth

- Each delivered manuscript or SI figure must be created by one clearly identified code cell. The cell should load or receive the verified data, construct every panel, apply layout and visual styling, add legends and annotations, and export the final assets.
- Keep all figure-specific layout and style parameters visible in the notebook cell: figure size, grid geometry, axes positions, palette, line and marker rules, typography, legend placement, annotation offsets, output size, and file names.
- Do not make the notebook a thin wrapper around a hidden `plot.py`, imported house-style module, or pre-rendered image. Shared imports and small generic helpers may live in the same notebook, but a reader must be able to modify the final appearance without editing external plotting code.
- Record the verified input path or object, the output file names, and the manuscript figure number near the cell. Never hard-code unverified result values merely to reproduce an appearance.

## Layout engineering

- Plan panel rectangles before plotting. Use `GridSpec`, `subplot_mosaic`, inset axes, or deliberate axes positions when they improve hierarchy, small multiples, shared legends, maps, or marginal summaries.
- Use automatic layout only as a starting point. Inspect and adjust outer margins, inter-panel gaps, legend regions, color-bar widths, inset positions, label rotations, and map aspect ratios explicitly.
- Consolidate repeated legends and axes. Prefer one shared legend or color bar for panels with identical semantics, while keeping separate keys when color, size, shape, or line width encode different quantities.
- Use semantic palette families rather than a long flat list of unrelated colors. Define base hues and derive lighter/darker variants or alpha levels for related scenarios.
- Define the spine, tick, and grid policy once per figure. Comparable Cartesian panels must not mix missing axes, full boxes, left/bottom spines, or different grid treatments without an explicit scientific reason.
- Size panels from their information density. Use `width_ratios`, `height_ratios`, explicit axes positions, or a shorter figure height when a panel contains only a few marks or categories; do not leave a full-size panel mostly empty.

## Geometry and collision preflight

- After plotting, call `fig.canvas.draw()` and inspect the final renderer, not the pre-layout artist positions. Check titles, tick labels, axis labels, annotations, legends, color-bar labels, and inset labels against axes and neighboring text.
- Treat unintended intersections between annotation text and tick labels, tick marks, spines, thresholds, markers, or error bars as failures. Background grids may pass behind opaque or haloed labels only when both data and text remain unambiguous. Move the label, reserve space, shorten the text, or adjust limits before reducing font size.
- Compare the finite data envelope with the allocated panel rectangle. When unused space dominates without serving a zero baseline, common comparison scale, threshold, forecast horizon, uncertainty range, or other stated reading task, redesign the panel or allocate it less area. Never tighten limits merely to meet an occupancy percentage.
- Inspect panel-to-panel gaps after all labels are drawn. Blank bands caused by automatic padding must be reduced; reserved legend regions must contain the legend they were created for.
- Recheck the entire exported figure after any limit, annotation, legend, or figure-size change. A clean notebook canvas does not override a collision or blank-space defect in the saved SVG/PNG.

## Cell output and reproducibility

- One execution of the figure cell must regenerate every delivered form of that figure from verified data. Save a vector form when the workflow supports it and a high-resolution raster form for Word or review; use at least 300 dpi for raster output unless the target requires more.
- Use tight export bounds only after confirming that no header, tick, legend, color bar, scale bar, north arrow, connector, inset, or annotation is clipped. Keep padding small but nonzero when necessary.
- Preserve exact aspect ratios when placing the exported asset in Word. Never resize width and height independently.
- Re-run the notebook from a clean kernel or environment, compare plotted values with the result ledger or source tables, and hash or version the delivered outputs when reproducibility matters.

## Notebook figure preflight

For each cell, inspect the exported file at final physical size and fail it for any of the following:

- a default chart or equal grid was accepted without comparing alternative layouts;
- panel labels do not use exact `(a) Title` syntax;
- visible text is not Times New Roman or becomes unreadable after placement;
- a legend, annotation, inset, or label overlaps evidence or another panel;
- large blank borders or gaps remain while evidence panels are undersized;
- sparse panels occupy a full row or column when the same evidence could use a compact panel or shorter figure height;
- comparable Cartesian panels use inconsistent spines, ticks, or gridlines without an explicit reason;
- an annotation unintentionally crosses a tick label, tick mark, spine, threshold, marker, or error bar, or a grid crossing makes the label ambiguous;
- shared scales or legends are duplicated inconsistently;
- semantic colors change across figures or too many unrelated hues are used;
- a map lacks interpretable data layers, projection/extent logic, or required cartographic context;
- raster-only output is low resolution, or vector/raster exports disagree;
- the cell depends on hidden styling code outside the notebook.
