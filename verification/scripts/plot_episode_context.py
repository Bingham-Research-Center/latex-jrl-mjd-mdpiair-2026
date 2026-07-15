#!/usr/bin/env python3
"""Combine registered MODIS snow context with selected EPA AQS ozone data."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


STYLE = {
    "Ouray": ("#7b3294", "o"),
    "Redwash": ("#d95f02", "s"),
    "Roosevelt": ("#1b9e77", "^"),
    "Vernal": ("#2166ac", "D"),
    "Little Mountain": ("#666666", "v"),
}


def load_ozone(path: Path):
    series = defaultdict(list)
    with path.open(newline="", encoding="utf-8") as stream:
        for row in csv.DictReader(stream):
            series[row["site_name"]].append(
                (
                    datetime.fromisoformat(row["date_local"]),
                    float(row["mda8_ozone_ppb"]),
                    float(row["observation_percent"]),
                )
            )
    if set(series) != set(STYLE):
        raise ValueError(f"unexpected site set: {sorted(series)}")
    return series


def render(ozone_csv: Path, modis_png: Path, output: Path) -> None:
    series = load_ozone(ozone_csv)
    modis = mpimg.imread(modis_png)
    # Crop the already registered source render to its map and coordinate frame.
    # Fractions, rather than fixed pixels, preserve the crop if the PNG is rescaled.
    height, width = modis.shape[:2]
    crop = modis[
        int(0.13 * height) : int(0.79 * height),
        int(0.14 * width) : int(0.90 * width),
    ]

    plt.rcParams.update(
        {
            "font.size": 13,
            "axes.titlesize": 14,
            "axes.labelsize": 13,
            "legend.fontsize": 9.5,
            "savefig.bbox": "tight",
        }
    )
    fig, (sat_ax, ozone_ax) = plt.subplots(
        1, 2, figsize=(13.2, 5.8), gridspec_kw={"width_ratios": [1.03, 1.0]}
    )

    sat_ax.imshow(crop)
    sat_ax.set_axis_off()
    sat_ax.set_title("(a) MODIS Terra daily browse context, 2 February 2013")

    low_coverage_seen = False
    for name, values in series.items():
        color, marker = STYLE[name]
        dates = [item[0] for item in values]
        ozone = [item[1] for item in values]
        coverage = [item[2] for item in values]
        ozone_ax.plot(dates, ozone, color=color, lw=1.6, label=name, zorder=2)
        full = [i for i, value in enumerate(coverage) if value >= 75.0]
        low = [i for i, value in enumerate(coverage) if value < 75.0]
        ozone_ax.scatter(
            [dates[i] for i in full],
            [ozone[i] for i in full],
            s=24,
            marker=marker,
            facecolor=color,
            edgecolor="white",
            linewidth=0.25,
            zorder=3,
        )
        if low:
            low_coverage_seen = True
            ozone_ax.scatter(
                [dates[i] for i in low],
                [ozone[i] for i in low],
                s=32,
                marker=marker,
                facecolor="white",
                edgecolor=color,
                linewidth=0.9,
                zorder=4,
            )

    case_date = datetime(2013, 2, 2)
    ozone_ax.axvline(case_date, color="black", ls="--", lw=1.0, zorder=1)
    ozone_ax.text(
        case_date,
        139,
        "WRF case date",
        ha="right",
        va="top",
        rotation=90,
        fontsize=10.5,
        transform=ozone_ax.transData,
    )
    ozone_ax.set_xlim(datetime(2013, 1, 1), datetime(2013, 2, 28))
    ozone_ax.set_ylim(0, 145)
    ozone_ax.set_ylabel(r"Reported daily maximum 8 h O$_3$ (ppb)")
    ozone_ax.set_title("(b) EPA AQS ozone context, January–February 2013")
    ozone_ax.grid(axis="y", color="0.88", lw=0.6)
    ozone_ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO, interval=2))
    ozone_ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
    ozone_ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    ozone_ax.tick_params(axis="x", rotation=30)
    handles, labels = ozone_ax.get_legend_handles_labels()
    if low_coverage_seen:
        handles.append(
            Line2D(
                [],
                [],
                marker="o",
                color="0.35",
                markerfacecolor="white",
                lw=0,
            )
        )
        labels.append("within-day coverage <75%")
    ozone_ax.legend(handles, labels, loc="upper left", ncol=3, frameon=True)
    ozone_ax.text(
        0.01,
        0.015,
        "AQS Date Local; values plotted as reported; no threshold shown.",
        transform=ozone_ax.transAxes,
        fontsize=10,
        va="bottom",
        bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.82},
    )

    fig.subplots_adjust(wspace=0.12)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output.with_suffix(".png"), dpi=220)
    fig.savefig(
        output.with_suffix(".pdf"),
        dpi=300,
        metadata={
            "Creator": "verification/scripts/plot_episode_context.py",
            "CreationDate": None,
            "ModDate": None,
        },
    )
    plt.close(fig)
    print(f"wrote {output.with_suffix('.png')} + .pdf")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ozone-csv", type=Path, required=True)
    parser.add_argument("--modis-png", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    render(args.ozone_csv, args.modis_png, args.output)


if __name__ == "__main__":
    main()
