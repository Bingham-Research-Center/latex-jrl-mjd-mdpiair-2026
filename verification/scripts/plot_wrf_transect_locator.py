#!/usr/bin/env python3
"""Plot the d02/d03 terrain context for current and proposed WRF transects.

The current diagonal is USU07 (Pariette Draw) to USU03 (Mountain Home).
Two hypothesis-led alternatives are shown without selecting them from model results:
USU07 to USU04 samples the southern bench, and UUT01 to USU08 follows the
west-to-east basin floor with nearly matched endpoint elevations.

Run on a CHPC compute node because the script opens WRF output. It reads only the
static latitude, longitude, and terrain fields from one d02 and one d03 file.
"""
from __future__ import annotations

import argparse
import glob
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import pandas as pd
import xarray as xr

from reduce_wrf_to_stations import DEFAULT_STATIONS_CSV, nearest_cell


TRANSECTS = (
    ("Current: floor to northwest bench", "USU07", "USU03", "#D55E00", "-"),
    ("Proposed: floor to southern bench", "USU07", "USU04", "#0072B2", "--"),
    ("Proposed: west-east basin floor", "UUT01", "USU08", "#009E73", "-."),
)


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


def distance_km(lats: np.ndarray, lons: np.ndarray) -> np.ndarray:
    km = np.zeros(len(lats))
    km[1:] = np.cumsum(
        np.hypot(
            np.diff(lats) * 111.32,
            np.diff(lons) * 111.32 * np.cos(np.deg2rad(lats[:-1])),
        )
    )
    return km


def terrain_profile(
    lat: np.ndarray,
    lon: np.ndarray,
    hgt: np.ndarray,
    p0: tuple[float, float],
    p1: tuple[float, float],
    n: int = 240,
) -> tuple[np.ndarray, np.ndarray]:
    lats = np.linspace(p0[0], p1[0], n)
    lons = np.linspace(p0[1], p1[1], n)
    terrain = np.empty(n)
    for k, (sample_lat, sample_lon) in enumerate(zip(lats, lons)):
        j, i = nearest_cell(lat, lon, sample_lat, sample_lon)
        terrain[k] = hgt[j, i]
    return distance_km(lats, lons), terrain


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

    fig, ax = plt.subplots(figsize=(8.2, 6.8), layout="constrained")
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

    for label, start, end, color, linestyle in TRANSECTS:
        p0 = stations.loc[start]
        p1 = stations.loc[end]
        ax.plot([p0.longitude, p1.longitude], [p0.latitude, p1.latitude],
                color=color, ls=linestyle, lw=2.2, label=label, zorder=5)
        km, terrain = terrain_profile(
            lat2,
            lon2,
            hgt2,
            (p0.latitude, p0.longitude),
            (p1.latitude, p1.longitude),
        )
        print(
            f"{start}->{end}: "
            f"start={p0.latitude:.4f},{p0.longitude:.4f},{p0.elev_m:.0f}m; "
            f"end={p1.latitude:.4f},{p1.longitude:.4f},{p1.elev_m:.0f}m; "
            f"length_km={km[-1]:.1f}; d02_terrain_min_max_m={terrain.min():.0f},{terrain.max():.0f}"
        )

    mean_lat = float(np.mean(lat2))
    ax.set_aspect(1.0 / np.cos(np.deg2rad(mean_lat)))
    ax.set_xlim(float(lon2.min()), float(lon2.max()))
    ax.set_ylim(float(lat2.min()), float(lat2.max()))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{abs(x):.1f}°W"))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:.1f}°N"))
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

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

    args.out_dir.mkdir(parents=True, exist_ok=True)
    stem = args.out_dir / "wrf_transect_locator_d02_d03"
    fig.savefig(stem.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(stem.with_suffix(".pdf"), bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {stem}.png + .pdf")
    print(f"d02_source={d02_file}")
    print(f"d03_source={d03_file}")


if __name__ == "__main__":
    main()
