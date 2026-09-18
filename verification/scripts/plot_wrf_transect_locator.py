#!/usr/bin/env python3
"""Plot one coherent geographic locator with an inset of d01--d03 nesting.

Run on a CHPC compute node because the script opens WRF output. It reads only the
static latitude, longitude, and terrain fields from one d01, d02, and d03 file.

Transects were removed from the manuscript locator on 14 July 2026 because no
retained result uses or explains them. Roads, rivers, and towns come from small,
committed, provenance-recorded files prepared on Akamai so CHPC needs no network.
"""
from __future__ import annotations

import argparse
import glob
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd
import xarray as xr

from plot_obs_feb0102 import FULL_W, save
from reduce_wrf_to_stations import DEFAULT_STATIONS_CSV

VERIFICATION = Path(__file__).resolve().parents[1]
DEFAULT_CONTEXT = VERIFICATION / "data" / "locator_context.geojson"
DEFAULT_PLACES = VERIFICATION / "data" / "locator_places.csv"
REGION_LABELS = (
    ("Uinta Mountains", -109.78, 40.72),
    ("Uinta Basin floor", -109.72, 39.94),
    ("Tavaputs Plateau", -109.62, 39.74),
)
PLACE_OFFSETS = {
    "Vernal": (8, 8),
    "Roosevelt": (-45, 6),
    "Duchesne": (4, 4),
    "Myton": (4, -10),
    "Fort Duchesne": (4, 4),
}
STATION_OFFSETS = {
    "QRS": (3, 4),
    "QV4": (-23, 5),
    "KVEL": (4, -11),
    "UUT01": (4, -11),
    "USU02": (4, 4),
}
CONTEXT_LABEL_POSITIONS = {
    "US 40": (-110.16, 40.12),
    "US 191": (-109.33, 40.60),
    "Green River": (-109.50, 40.00),
}


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


def line_coordinates(geometry: dict):
    """Yield coordinate sequences from GeoJSON line and collection geometries."""
    kind = geometry.get("type")
    coordinates = geometry.get("coordinates", [])
    if kind == "LineString":
        yield coordinates
    elif kind == "MultiLineString":
        yield from coordinates
    elif kind == "GeometryCollection":
        for child in geometry.get("geometries", []):
            yield from line_coordinates(child)


def midpoint(coordinates) -> tuple[float, float]:
    point = coordinates[len(coordinates) // 2]
    return float(point[0]), float(point[1])


def plot_geographic_context(ax, path: Path) -> None:
    payload = json.loads(path.read_text())
    label_lines: dict[str, list] = {}
    for feature in payload["features"]:
        props = feature["properties"]
        feature_type = props["feature_type"]
        label = props["label"]
        for coordinates in line_coordinates(feature["geometry"]):
            if len(coordinates) < 2:
                continue
            lon, lat = np.asarray(coordinates).T
            if feature_type == "road":
                ax.plot(lon, lat, color="white", lw=2.0, alpha=0.9, zorder=2.2)
                ax.plot(lon, lat, color="#6B4C3B", lw=0.8, alpha=0.95, zorder=2.3)
            elif feature_type == "river":
                ax.plot(lon, lat, color="white", lw=2.2, alpha=0.85, zorder=2.2)
                ax.plot(lon, lat, color="#2B83BA", lw=1.0, alpha=0.95, zorder=2.3)
            if len(coordinates) > len(label_lines.get(label, [])):
                label_lines[label] = coordinates

    for label, coordinates in label_lines.items():
        lon, lat = CONTEXT_LABEL_POSITIONS.get(label, midpoint(coordinates))
        text = ax.text(lon, lat, label, fontsize=6.5, color="#2B83BA" if "River" in label
                       else "#4A332A", ha="center", va="center", zorder=5)
        text.set_path_effects([path_effects.withStroke(linewidth=2.0, foreground="white")])


def plot_places(ax, path: Path, max_priority: int, extent: tuple[float, float, float, float]) -> None:
    places = pd.read_csv(path)
    west, east, south, north = extent
    places = places[
        (places["label_priority"] <= max_priority)
        & places["longitude"].between(west, east)
        & places["latitude"].between(south, north)
    ]
    ax.scatter(places["longitude"], places["latitude"], s=12, marker="s", c="#F2C14E",
               edgecolor="0.15", linewidth=0.5, zorder=5)
    for row in places.itertuples(index=False):
        offset = PLACE_OFFSETS.get(row.name, (4, 4))
        annotation = ax.annotate(row.name, (row.longitude, row.latitude), xytext=offset,
                                 textcoords="offset points", fontsize=6.5, fontweight="bold",
                                 color="0.12", zorder=6)
        annotation.set_path_effects([
            path_effects.withStroke(linewidth=2.0, foreground="white")
        ])


def plot_region_labels(ax, extent: tuple[float, float, float, float]) -> None:
    west, east, south, north = extent
    for label, lon, lat in REGION_LABELS:
        if west <= lon <= east and south <= lat <= north:
            text = ax.text(lon, lat, label, fontsize=6.5, fontstyle="italic", color="0.18",
                           ha="center", va="center", alpha=0.9, zorder=5)
            text.set_path_effects([
                path_effects.withStroke(linewidth=1.8, foreground="white", alpha=0.85)
            ])


def add_nesting_inset(ax, domains) -> None:
    inset = ax.inset_axes([0.70, 0.67, 0.27, 0.27])
    inset.set_facecolor((1, 1, 1, 0.92))
    colors = {"d01": "0.35", "d02": "black", "d03": "#6A3D9A"}
    widths = {"d01": 1.0, "d02": 1.3, "d03": 1.5}
    for name, lat, lon in domains:
        plat, plon = perimeter(lat, lon)
        inset.plot(plon, plat, color=colors[name], lw=widths[name], label=name)
    lat1, lon1 = domains[0][1], domains[0][2]
    inset.set_xlim(float(lon1.min()), float(lon1.max()))
    inset.set_ylim(float(lat1.min()), float(lat1.max()))
    inset.set_aspect(1.0 / np.cos(np.deg2rad(float(np.mean(lat1)))))
    inset.set_xticks([])
    inset.set_yticks([])
    inset.set_title("WRF nesting", fontsize=7, pad=2)
    inset.legend(loc="lower left", fontsize=5.8, frameon=False, handlelength=1.4,
                 handletextpad=0.35, borderpad=0.1)
    for spine in inset.spines.values():
        spine.set_linewidth(0.7)
        spine.set_edgecolor("0.35")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--wrf-dir", required=True, type=Path)
    ap.add_argument("--d01-glob", default="wrfout_d01_*")
    ap.add_argument("--d02-glob", default="wrfout_d02_*")
    ap.add_argument("--d03-glob", default="wrfout_d03_*")
    ap.add_argument("--stations", type=Path, default=DEFAULT_STATIONS_CSV)
    ap.add_argument("--context-geojson", type=Path, default=DEFAULT_CONTEXT)
    ap.add_argument("--places", type=Path, default=DEFAULT_PLACES)
    ap.add_argument("--max-place-priority", type=int, default=1)
    ap.add_argument("--out-dir", required=True, type=Path)
    args = ap.parse_args()

    d01_file = first_file(args.wrf_dir, args.d01_glob)
    d02_file = first_file(args.wrf_dir, args.d02_glob)
    d03_file = first_file(args.wrf_dir, args.d03_glob)
    lat1, lon1, _ = static_fields(d01_file)
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

    extent = (float(lon2.min()), float(lon2.max()), float(lat2.min()), float(lat2.max()))
    plot_geographic_context(ax, args.context_geojson)
    plot_places(ax, args.places, args.max_place_priority, extent)
    plot_region_labels(ax, extent)

    for domain, lat, lon, color, width in (
        ("d02 (1 km)", lat2, lon2, "black", 1.6),
        ("d03 (333 m)", lat3, lon3, "#6A3D9A", 1.8),
    ):
        plat, plon = perimeter(lat, lon)
        ax.plot(plon, plat, color=color, lw=width, label=domain, zorder=4)

    ax.scatter(stations["longitude"], stations["latitude"], s=20, c="white",
               edgecolor="black", linewidth=0.7, zorder=6)
    for stid, row in stations.iterrows():
        annotation = ax.annotate(
            stid,
            (row.longitude, row.latitude),
            xytext=STATION_OFFSETS.get(stid, (3, 3)),
            textcoords="offset points",
            fontsize=6.5,
            color="0.1",
            zorder=7,
        )
        annotation.set_path_effects([
            path_effects.withStroke(linewidth=1.5, foreground="white", alpha=0.9)
        ])

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
    ax.annotate("N", xy=(0.61, 0.95), xytext=(0.61, 0.85), xycoords="axes fraction",
                ha="center", va="center", fontsize=9,
                arrowprops={"arrowstyle": "-|>", "lw": 1.2, "color": "black"})

    add_nesting_inset(ax, (("d01", lat1, lon1), ("d02", lat2, lon2), ("d03", lat3, lon3)))

    legend_handles = [
        Line2D([], [], color="black", lw=1.6, label="d02 (1 km)"),
        Line2D([], [], color="#6A3D9A", lw=1.8, label="d03 (333 m)"),
        Line2D([], [], marker="o", ls="", ms=4.2, markerfacecolor="white",
               markeredgecolor="black", label="reporting station"),
        Line2D([], [], marker="s", ls="", ms=4.0, markerfacecolor="#F2C14E",
               markeredgecolor="0.15", label="town or city"),
        Line2D([], [], color="#6B4C3B", lw=1.0, label="major road"),
        Line2D([], [], color="#2B83BA", lw=1.1, label="river"),
    ]
    ax.legend(handles=legend_handles, loc="upper left", fontsize=6.2, ncols=2,
              framealpha=0.92, columnspacing=0.8, handlelength=1.8,
              handletextpad=0.45, borderpad=0.35)
    cbar = fig.colorbar(mesh, ax=ax, pad=0.02, shrink=0.86)
    cbar.set_label("WRF terrain elevation (m MSL)")

    # Use a new stem so an older terrain-and-stations-only candidate cannot be
    # mistaken for this sourced geographic-context version.
    save(fig, "wrf_geographic_locator_d01_d03", out_dir=args.out_dir)
    print(f"d01_source={d01_file}")
    print(f"d02_source={d02_file}")
    print(f"d03_source={d03_file}")
    print(f"context_source={args.context_geojson}")
    print(f"places_source={args.places}")


if __name__ == "__main__":
    main()
