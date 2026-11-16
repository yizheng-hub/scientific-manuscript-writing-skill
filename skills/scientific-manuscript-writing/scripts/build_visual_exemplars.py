#!/usr/bin/env python3
"""Build original synthetic high-density figure exemplars."""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon


OUT = Path(__file__).resolve().parents[1] / "assets" / "visual-exemplars"
OUT.mkdir(parents=True, exist_ok=True)

BLUE = "#5B8DB8"
TEAL = "#4F9C91"
PURPLE = "#8C7AA9"
RED = "#D77A72"
OCHRE = "#D5A94E"
GRAY = "#A9B0B5"
DARK = "#2F3437"
PALETTE = [BLUE, TEAL, PURPLE, RED, OCHRE]

mpl.rcParams.update(
    {
        "font.family": "Times New Roman",
        "font.size": 11,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.labelsize": 11,
        "xtick.labelsize": 11,
        "ytick.labelsize": 11,
        "legend.fontsize": 11,
        "axes.linewidth": 0.8,
        "svg.fonttype": "none",
    }
)


def clean_axis(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(length=3, width=0.7, color="#555555")


def panel_title(ax, letter: str, title: str):
    ax.set_title(f"({letter}) {title}", loc="left", pad=8)


def fictional_grid(seed: int = 2):
    rng = np.random.default_rng(seed)
    xs = np.linspace(0, 5, 6)
    ys = np.linspace(0, 4, 5)
    points = np.stack(np.meshgrid(xs, ys), axis=-1)
    jitter = rng.normal(0, 0.12, size=points.shape)
    jitter[0, :, 1] = 0
    jitter[-1, :, 1] = 0
    jitter[:, 0, 0] = 0
    jitter[:, -1, 0] = 0
    points = points + jitter
    omit = {(0, 0), (0, 4), (3, 0), (3, 4), (0, 1), (3, 3)}
    cells = []
    for row in range(4):
        for col in range(5):
            if (row, col) in omit:
                continue
            cells.append(
                np.array(
                    [
                        points[row, col],
                        points[row, col + 1],
                        points[row + 1, col + 1],
                        points[row + 1, col],
                    ]
                )
            )
    return cells


def draw_fictional_map(ax, values, cmap, title, letter, change=False, network_seed=None, norm=None):
    cells = fictional_grid(5)
    if norm is None:
        norm = mpl.colors.Normalize(vmin=float(np.min(values)), vmax=float(np.max(values)))
    for cell, value in zip(cells, values):
        ax.add_patch(Polygon(cell, facecolor=cmap(norm(value)), edgecolor="white", linewidth=1.1))
    outline = np.vstack([np.min(np.vstack(cells), axis=0), np.max(np.vstack(cells), axis=0)])
    ax.set_xlim(outline[0, 0] - 0.18, outline[1, 0] + 0.18)
    ax.set_ylim(outline[0, 1] - 0.28, outline[1, 1] + 0.32)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    panel_title(ax, letter, title)

    centers = np.array([cell.mean(axis=0) for cell in cells])
    if network_seed is not None:
        rng = np.random.default_rng(network_seed)
        node_values = rng.uniform(12, 48, len(centers))
        for i in range(len(centers) - 1):
            choices = np.argsort(np.linalg.norm(centers - centers[i], axis=1))[1:4]
            for j in choices[: 1 + (i % 2)]:
                weight = 0.7 + 1.8 * rng.random()
                ax.plot(
                    [centers[i, 0], centers[j, 0]],
                    [centers[i, 1], centers[j, 1]],
                    color=BLUE if weight < 1.5 else TEAL,
                    lw=weight,
                    alpha=0.58,
                    zorder=4,
                )
        ax.scatter(
            centers[:, 0],
            centers[:, 1],
            s=node_values,
            c=np.where(node_values > 30, RED, OCHRE),
            edgecolors="white",
            linewidths=0.7,
            zorder=5,
        )
    else:
        for idx in np.argsort(np.abs(values - np.mean(values)))[-5:]:
            x, y = centers[idx]
            label = f"{values[idx]:+.1f}" if change else f"{values[idx]:.1f}"
            ax.text(x, y, label, ha="center", va="center", fontsize=11, color=DARK, zorder=5)

    ax.annotate("N", xy=(0.93, 0.92), xycoords="axes fraction", ha="center", va="bottom", fontsize=11)
    ax.annotate("", xy=(0.93, 0.90), xytext=(0.93, 0.78), xycoords="axes fraction", arrowprops=dict(arrowstyle="-|>", lw=0.9, color=DARK))
    ax.plot([0.05, 0.24], [0.10, 0.10], transform=ax.transAxes, color=DARK, lw=3, solid_capstyle="butt")
    ax.text(0.145, 0.018, "250 km", transform=ax.transAxes, ha="center", va="bottom", fontsize=11)
    return mpl.cm.ScalarMappable(norm=norm, cmap=cmap)


def save(fig, stem: str):
    fig.savefig(OUT / f"{stem}.svg", bbox_inches="tight", pad_inches=0.035)
    fig.savefig(OUT / f"{stem}.png", dpi=300, bbox_inches="tight", pad_inches=0.035)
    plt.close(fig)


def dense_spatiotemporal():
    rng = np.random.default_rng(42)
    fig = plt.figure(figsize=(14, 9), facecolor="white")
    gs = fig.add_gridspec(
        3,
        12,
        height_ratios=[1.03, 1.34, 1.34],
        left=0.045,
        right=0.985,
        bottom=0.075,
        top=0.955,
        wspace=0.52,
        hspace=0.52,
    )
    x = np.arange(0, 11)
    scenario_handles = []
    for i in range(5):
        ax = fig.add_subplot(gs[0, i * 2 : i * 2 + 2])
        clean_axis(ax)
        for scenario, color in enumerate(PALETTE[:4]):
            base = 0.18 + 0.055 * x + 0.008 * (i + 1) * x**2
            y = base * (0.82 + 0.11 * scenario) + 0.025 * np.sin(x / 2 + scenario)
            spread = 0.025 + 0.004 * x
            ax.fill_between(x, y - spread, y + spread, color=color, alpha=0.13, lw=0)
            line = ax.plot(x, y, color=color, lw=1.7, marker="o", ms=2.8, markevery=[0, 5, 10])[0]
            if i == 0:
                scenario_handles.append(line)
        panel_title(ax, chr(97 + i), f"Trajectory {i + 1}")
        ax.set_xlim(0, 10)
        ax.set_xticks([0, 5, 10], ["T0", "T5", "T10"])
        ax.set_ylim(0.05, 2.15 + 0.20 * i)
        if i == 0:
            ax.set_ylabel("Normalized response")
        else:
            ax.set_yticklabels([])
        if i in {1, 3}:
            inset = ax.inset_axes([0.11, 0.53, 0.49, 0.35])
            for scenario, color in enumerate(PALETTE[:4]):
                local_x = x[-4:]
                local_y = (0.18 + 0.055 * local_x + 0.008 * (i + 1) * local_x**2) * (0.82 + 0.11 * scenario)
                inset.plot(local_x, local_y, color=color, lw=1.0)
            inset.set_xticks([7, 10], ["T7", "T10"], fontsize=11)
            inset.set_yticks([])
            inset.tick_params(length=2)
            for spine in inset.spines.values():
                spine.set_color("#9CA3AA")
                spine.set_linewidth(0.6)

    legend_ax = fig.add_subplot(gs[0, 10:12])
    legend_ax.axis("off")
    legend_ax.legend(
        scenario_handles,
        ["Reference", "Adaptation", "Efficiency", "Transition"],
        loc="center left",
        frameon=False,
        handlelength=2.2,
        labelspacing=0.9,
        title="Shared scenario key",
        title_fontsize=11,
    )

    matrix_ax = fig.add_subplot(gs[1:, 0:8])
    matrix = rng.normal(0, 0.7, (18, 16))
    matrix += np.linspace(-0.8, 0.8, 18)[:, None]
    matrix[:, 5:9] += 0.65
    cmap = LinearSegmentedColormap.from_list("muted_div", [BLUE, "#F4F3EE", OCHRE])
    image = matrix_ax.imshow(matrix, cmap=cmap, vmin=-2.0, vmax=2.0, aspect="auto", interpolation="nearest")
    panel_title(matrix_ax, "f", "Region-by-scenario structure")
    matrix_ax.set_yticks(np.arange(18), [f"R{i:02d}" for i in range(1, 19)])
    matrix_ax.set_xticks(np.arange(16), [f"S{i:02d}" for i in range(1, 17)], rotation=70, ha="right")
    matrix_ax.set_xlabel("Scenario order shared across the manuscript")
    matrix_ax.set_ylabel("Fictional region")
    matrix_ax.tick_params(length=0)
    for spine in matrix_ax.spines.values():
        spine.set_color("#737A80")
        spine.set_linewidth(0.6)
    cax = matrix_ax.inset_axes([0.13, -0.13, 0.45, 0.025])
    cb = fig.colorbar(image, cax=cax, orientation="horizontal")
    cb.set_label("Standardized change", labelpad=3)
    cb.outline.set_visible(False)

    map_cmap = LinearSegmentedColormap.from_list("map_seq", ["#EEF3EA", "#A8CEC6", TEAL])
    values = np.linspace(0.3, 2.2, len(fictional_grid())) + rng.normal(0, 0.12, len(fictional_grid()))
    ax_g = fig.add_subplot(gs[1, 8:12])
    sm1 = draw_fictional_map(ax_g, values, map_cmap, "Spatial level", "g")
    cax_g = ax_g.inset_axes([0.83, 0.08, 0.03, 0.31])
    cb1 = fig.colorbar(sm1, cax=cax_g)
    cb1.set_ticks([])
    cb1.outline.set_visible(False)
    ax_g.text(0.88, 0.37, "High", transform=ax_g.transAxes, fontsize=11)
    ax_g.text(0.88, 0.06, "Low", transform=ax_g.transAxes, fontsize=11)

    ax_h = fig.add_subplot(gs[2, 8:12])
    change_cmap = LinearSegmentedColormap.from_list("map_div", [BLUE, "#F5F3ED", RED])
    changes = rng.normal(0, 1.0, len(fictional_grid()))
    sm2 = draw_fictional_map(ax_h, changes, change_cmap, "Spatial change", "h", change=True)
    cax_h = ax_h.inset_axes([0.83, 0.08, 0.03, 0.31])
    cb2 = fig.colorbar(sm2, cax=cax_h)
    cb2.set_ticks([])
    cb2.outline.set_visible(False)
    ax_h.text(0.88, 0.37, "Increase", transform=ax_h.transAxes, fontsize=11)
    ax_h.text(0.88, 0.06, "Decrease", transform=ax_h.transAxes, fontsize=11)
    save(fig, "dense-spatiotemporal-evidence")


def comparative_network():
    rng = np.random.default_rng(17)
    fig = plt.figure(figsize=(14, 7.2), facecolor="white")
    gs = fig.add_gridspec(
        2,
        12,
        height_ratios=[1.18, 1.0],
        left=0.045,
        right=0.985,
        bottom=0.085,
        top=0.955,
        wspace=0.48,
        hspace=0.34,
    )
    map_cmap = LinearSegmentedColormap.from_list("neutral_map", ["#F4F4F1", "#D6E5E1", "#A9CEC5"])
    shared_map_norm = mpl.colors.Normalize(vmin=0.1, vmax=1.0)
    shared_handles = [
        Line2D([0], [0], color=BLUE, lw=1.2, label="lower flow"),
        Line2D([0], [0], color=TEAL, lw=2.4, label="higher flow"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor=OCHRE, markeredgecolor="white", markersize=7, label="lower node"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor=RED, markeredgecolor="white", markersize=9, label="higher node"),
    ]
    for i, spec in enumerate((gs[0, 0:3], gs[0, 3:6], gs[0, 6:9], gs[0, 9:12])):
        ax = fig.add_subplot(spec)
        values = rng.uniform(0.1, 1.0, len(fictional_grid()))
        draw_fictional_map(
            ax,
            values,
            map_cmap,
            f"Network state {i + 1}",
            chr(97 + i),
            network_seed=50 + i,
            norm=shared_map_norm,
        )
    fig.legend(
        handles=shared_handles,
        loc="center",
        bbox_to_anchor=(0.5, 0.515),
        frameon=False,
        ncol=4,
        handlelength=2.0,
        columnspacing=1.5,
    )

    bubble_ax = fig.add_subplot(gs[1, 0:3])
    clean_axis(bubble_ax)
    years = np.arange(6)
    for row in range(8):
        y = row + 0.12 * np.sin(years + row)
        size = 18 + 70 * (years + 1) / 6 * (0.35 + row / 12)
        bubble_ax.scatter(years, y, s=size, c=np.linspace(0.2, 0.9, 6), cmap="Blues", vmin=0, vmax=1, edgecolor="white", linewidth=0.5)
    panel_title(bubble_ax, "e", "Marginal totals")
    bubble_ax.set_yticks(np.arange(8), [f"R{i:02d}" for i in range(1, 9)])
    bubble_ax.set_xticks(years, [f"T{i}" for i in years], rotation=45)
    bubble_ax.set_xlabel("Time")

    matrix_cmap = LinearSegmentedColormap.from_list("bivar", ["#F4F3EE", "#C9E1DB", TEAL])
    for offset, letter in enumerate(("f", "g", "h")):
        ax = fig.add_subplot(gs[1, 3 + offset * 3 : 6 + offset * 3])
        values = rng.uniform(0, 1, (8, 8))
        values[np.triu_indices(8, 2)] *= 0.25
        ax.imshow(values, cmap=matrix_cmap, vmin=0, vmax=1, aspect="equal", interpolation="nearest")
        yy, xx = np.mgrid[0:8, 0:8]
        sizes = 8 + 55 * rng.uniform(0, 1, values.size)
        ax.scatter(xx.ravel(), yy.ravel(), s=sizes, facecolors="none", edgecolors=PURPLE, linewidths=0.7, alpha=0.65)
        panel_title(ax, letter, f"Transition matrix {offset + 1}")
        ax.set_xticks(np.arange(8), [f"T{i}" for i in range(1, 9)], rotation=55, ha="right")
        if offset == 0:
            ax.set_yticks(np.arange(8), [f"R{i:02d}" for i in range(1, 9)])
        else:
            ax.set_yticks([])
        ax.tick_params(length=0)
        for spine in ax.spines.values():
            spine.set_visible(False)
    save(fig, "comparative-network-evidence")


if __name__ == "__main__":
    dense_spatiotemporal()
    comparative_network()
