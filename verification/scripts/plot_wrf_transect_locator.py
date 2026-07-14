#!/usr/bin/env python3
"""Plot the d02/d03 terrain and reporting-station context.

Run on a CHPC compute node because the script opens WRF output. It reads only the
static latitude, longitude, and terrain fields from one d02 and one d03 file.

Transects were removed from the manuscript locator on 14 July 2026 because no
retained result uses or explains them.  A later two-panel orientation figure will
add geographic context and the full d01--d03 nesting without restoring those lines.
"""
from __future__ import annotations

import argparse
import glob
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr

from plot_obs_feb0102 import FULL_W, save
from reduce_wrf_to_stations import DEFAULT_STATIONS_CSV


def first_file(run_dir: Path, pattern: str) -> Path:
    files = sorted(Path(p) for p in glob.glob(str(run_dir / pattern)))
    if not files:
        raise SystemExit(f"no WRF files matched {run_dir / pattern}")
    return files[0]


def static_fields(path: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    with xr.open_dataset(path, decode_times=False) as ds:
        return (
            np.asarray(ds["XLAT"].isel(Time=0)),
            np.asarray(ds["XLONG"].isel(Time=0)),
            np.asarray(ds["HGT"].isel(Time=0)),
        )


def perimeter(lat: np.ndarray, lon: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    plat = np.concatenate((lat[0], lat[1:, -1], lat[-1, -2::-1], lat[-2:0:-1, 0]))
    plon = np.concatenate((lon[0], lon[1:, -1], lon[-1, -2::-1], lon[-2:0:-1, 0]))
    return plat, plon


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--wrf-dir", required=True, type=Path)
    ap.add_argument("--d02-glob", default="wrfout_d02_*")
    ap.add_argument("--d03-glob", default="wrfout_d03_*")
    ap.add_argument("--stations", type=Path, default=DEFAULT_STATIONS_CSV)
    ap.add_argument("--out-dir", required=True, type=Path)
    args = ap.parse_args()

    d02_file = first_file(args.wrf_dir, args.d02_glob)
    d03_file = first_file(args.wrf_dir, args.d03_glob)
    lat2, lon2, hgt2 = static_fields(d02_file)
    lat3, lon3, _ = static_fields(d03_file)
    stations = pd.read_csv(args.stations)
    stations = stations[stations["in_case_window"]].set_index("stid")

    fig, ax = plt.subplots(figsize=(FULL_W, 5.1), layout="constrained")
    mesh = ax.pcolormesh(
        lon2,
        lat2,
        hgt2,
        shading="auto",
        cmap="terrain",
        vmin=1300.0,
        vmax=3200.0,
        rasterized=True,
    )
    ax.contour(lon2, lat2, hgt2, levels=[1500, 1800, 2200], colors="0.35",
               linewidths=0.45, alpha=0.7)

    for domain, lat, lon, color, width in (
        ("d02 (1 km)", lat2, lon2, "black", 1.6),
        ("d03 (333 m)", lat3, lon3, "#6A3D9A", 1.8),
    ):
        plat, plon = perimeter(lat, lon)
        ax.plot(plon, plat, color=color, lw=width, label=domain, zorder=4)

    ax.scatter(stations["longitude"], stations["latitude"], s=20, c="white",
               edgecolor="black", linewidth=0.7, zorder=6)
    for stid, row in stations.iterrows():
        ax.annotate(stid, (row.longitude, row.latitude), xytext=(3, 3),
                    textcoords="offset points", fontsize=6.5, color="0.1", zorder=7)

    mean_lat = float(np.mean(lat2))
    ax.set_aspect(1.0 / np.cos(np.deg2rad(mean_lat)))
    ax.set_xlim(float(lon2.min()), float(lon2.max()))
    ax.set_ylim(float(lat2.min()), float(lat2.max()))
    ax.set_xticks([])
    ax.set_yticks([])

    scale_lat = float(lat2.min() + 0.06 * (lat2.max() - lat2.min()))
    scale_lon = float(lon2.min() + 0.06 * (lon2.max() - lon2.min()))
    scale_km = 40.0
    scale_dlon = scale_km / (111.32 * np.cos(np.deg2rad(scale_lat)))
    ax.plot([scale_lon, scale_lon + scale_dlon], [scale_lat, scale_lat], color="black", lw=3)
    ax.text(scale_lon + scale_dlon / 2, scale_lat + 0.015, "40 km", ha="center", va="bottom",
            fontsize=8)
    ax.annotate("N", xy=(0.96, 0.94), xytext=(0.96, 0.84), xycoords="axes fraction",
                ha="center", va="center", fontsize=9,
                arrowprops={"arrowstyle": "-|>", "lw": 1.2, "color": "black"})

    ax.legend(loc="upper left", fontsize=7.5, framealpha=0.92)
    cbar = fig.colorbar(mesh, ax=ax, pad=0.02, shrink=0.86)
    cbar.set_label("WRF terrain elevation (m MSL)")

    save(fig, "wrf_transect_locator_d02_d03", out_dir=args.out_dir)
    print(f"d02_source={d02_file}")
    print(f"d03_source={d03_file}")


if __name__ == "__main__":
    main()
