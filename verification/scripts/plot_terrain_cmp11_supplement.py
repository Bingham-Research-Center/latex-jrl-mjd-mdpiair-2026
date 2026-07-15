#!/usr/bin/env python3
"""Render the bounded CMP11 terrain diagnostic as one supplemental composite.

The calculation is X0 minus X4 (fine 3-arc-second minus coarse 5-arc-minute static
terrain) at one valid time.  Panels show d02 and d03 heat-deficit differences plus
lower-atmosphere d03 north--south and east--west potential-temperature sections.
This is a diagnostic with no retrospective evidence gate.
"""
from __future__ import annotations

import argparse
import csv
import json
import tomllib
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from brc_tools.nwp import wrf_output as wo
from plot_obs_feb0102 import save
from plot_wrf_transect_locator import (
    DEFAULT_CONTEXT,
    DEFAULT_PLACES,
    line_coordinates,
)

VERIFICATION = Path(__file__).resolve().parents[1]
DEFAULT_WAYPOINTS_CONFIG = VERIFICATION / "config" / "figures" / "pelican2013_terrain_d03.toml"
MAP_CMAP = "RdBu_r"
SELECTED_WAYPOINTS = {"Horsepool", "Pelican Lake", "Fort Duchesne", "Randlett", "Ouray"}


@dataclass
class MapProduct:
    domain: str
    lon: np.ndarray
    lat: np.ndarray
    terrain_m: np.ndarray
    difference_mj_m2: np.ndarray


@dataclass
class SectionProduct:
    orientation: str
    distance_km: np.ndarray
    lon_line: np.ndarray
    lat_line: np.ndarray
    terrain_m: np.ndarray
    heights_msl: np.ndarray
    difference_k: np.ndarray
    termini: tuple[str, str]


def _interp_columns(field2d: np.ndarray, height2d: np.ndarray,
                    target_heights: np.ndarray) -> np.ndarray:
    result = np.full((target_heights.size, field2d.shape[1]), np.nan)
    for index in range(field2d.shape[1]):
        result[:, index] = np.interp(
            target_heights,
            height2d[:, index],
            field2d[:, index],
            left=np.nan,
            right=np.nan,
        )
    return result


def _nan_gaussian(field: np.ndarray, sigma: float) -> np.ndarray:
    if sigma <= 0:
        return field
    from scipy.ndimage import gaussian_filter

    valid = np.isfinite(field)
    numerator = gaussian_filter(np.where(valid, field, 0.0), sigma=sigma)
    denominator = gaussian_filter(valid.astype(float), sigma=sigma)
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(denominator > 0, numerator / denominator, np.nan)


def load_waypoints(path: Path) -> dict[str, dict[str, float]]:
    with path.open("rb") as handle:
        raw = tomllib.load(handle).get("waypoints", {})
    return {
        name: {"lat": float(values["lat"]), "lon": float(values["lon"])}
        for name, values in raw.items()
        if name in SELECTED_WAYPOINTS
    }


def load_map(fine_run: Path, coarse_run: Path, domain: int, valid: datetime,
             crest_m: float) -> tuple[MapProduct, tuple[Path, Path]]:
    fine_path = wo.wrfout_path(fine_run, domain, valid)
    coarse_path = wo.wrfout_path(coarse_run, domain, valid)
    fine = wo.open_wrfout(fine_path)
    coarse = wo.open_wrfout(coarse_path)
    difference = (
        wo.heat_deficit_field(fine, crest_m) - wo.heat_deficit_field(coarse, crest_m)
    ) / 1e6
    return MapProduct(
        domain=f"d{domain:02d}",
        lon=np.asarray(wo.surface_field(fine, "XLONG")),
        lat=np.asarray(wo.surface_field(fine, "XLAT")),
        terrain_m=np.asarray(wo.surface_field(fine, "HGT")),
        difference_mj_m2=np.asarray(difference),
    ), (fine_path, coarse_path)


def load_section(fine_dataset, coarse_dataset, orientation: str, section_top_m: float,
                 smooth_sigma: float) -> SectionProduct:
    fine = wo.build_section(fine_dataset, orientation)
    coarse = wo.build_section(coarse_dataset, orientation)
    terrain = np.asarray(fine.terrain1d)
    bottom = float(np.floor(np.nanmin(terrain) / 100.0) * 100.0 - 50.0)
    if section_top_m <= bottom:
        raise ValueError(f"section top {section_top_m} m is below terrain floor {bottom} m")
    target = np.arange(bottom, section_top_m + 1.0, 25.0)
    fine_theta = _interp_columns(np.asarray(fine.theta2d), np.asarray(fine.height2d), target)
    coarse_theta = _interp_columns(np.asarray(coarse.theta2d), np.asarray(coarse.height2d), target)
    difference = _nan_gaussian(fine_theta - coarse_theta, smooth_sigma)
    return SectionProduct(
        orientation=orientation,
        distance_km=np.asarray(fine.distance_km),
        lon_line=np.asarray(fine.lon_line),
        lat_line=np.asarray(fine.lat_line),
        terrain_m=terrain,
        heights_msl=target,
        difference_k=difference,
        termini=tuple(fine.termini),
    )


def plot_context_lines(ax, path: Path) -> None:
    payload = json.loads(path.read_text())
    for feature in payload["features"]:
        feature_type = feature["properties"]["feature_type"]
        for coordinates in line_coordinates(feature["geometry"]):
            if len(coordinates) < 2:
                continue
            lon, lat = np.asarray(coordinates).T
            if feature_type == "road":
                ax.plot(lon, lat, color="white", lw=1.5, alpha=0.8, zorder=3)
                ax.plot(lon, lat, color="#6B4C3B", lw=0.55, alpha=0.9, zorder=3.1)
            elif feature_type == "river":
                ax.plot(lon, lat, color="white", lw=1.7, alpha=0.8, zorder=3)
                ax.plot(lon, lat, color="#2B83BA", lw=0.7, alpha=0.9, zorder=3.1)


def plot_places(ax, path: Path, extent: tuple[float, float, float, float]) -> None:
    import pandas as pd

    places = pd.read_csv(path)
    west, east, south, north = extent
    places = places[
        (places["label_priority"] <= 1)
        & places["longitude"].between(west, east)
        & places["latitude"].between(south, north)
    ]
    ax.scatter(places["longitude"], places["latitude"], s=8, marker="s", c="#F2C14E",
               edgecolor="0.15", linewidth=0.4, zorder=4)
    for row in places.itertuples(index=False):
        ax.annotate(row.name, (row.longitude, row.latitude), xytext=(2, 2),
                    textcoords="offset points", fontsize=5.5, color="0.12", zorder=4)


def plot_waypoints(ax, waypoints: dict[str, dict[str, float]],
                   extent: tuple[float, float, float, float]) -> None:
    west, east, south, north = extent
    for name, point in waypoints.items():
        lon, lat = point["lon"], point["lat"]
        if not (west <= lon <= east and south <= lat <= north):
            continue
        ax.scatter(lon, lat, marker="^", s=11, c="0.15", zorder=4)
        ax.annotate(name, (lon, lat), xytext=(2, 1), textcoords="offset points",
                    fontsize=5.2, color="0.12", zorder=4)


def draw_map(ax, product: MapProduct, limit: float, context: Path, places: Path,
             waypoints: dict[str, dict[str, float]], crest_m: float,
             panel: str, subtitle: str):
    mesh = ax.pcolormesh(
        product.lon,
        product.lat,
        product.difference_mj_m2,
        cmap=MAP_CMAP,
        vmin=-limit,
        vmax=limit,
        shading="auto",
        rasterized=True,
    )
    ax.contour(product.lon, product.lat, product.terrain_m, levels=[crest_m],
               colors="0.25", linewidths=0.45, alpha=0.8)
    extent = (
        float(product.lon.min()), float(product.lon.max()),
        float(product.lat.min()), float(product.lat.max()),
    )
    plot_context_lines(ax, context)
    plot_places(ax, places, extent)
    plot_waypoints(ax, waypoints, extent)
    ax.set_xlim(extent[0], extent[1])
    ax.set_ylim(extent[2], extent[3])
    ax.set_aspect(1.0 / np.cos(np.deg2rad(float(product.lat.mean()))))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.text(0.02, 0.98, f"({panel})", transform=ax.transAxes, va="top", ha="left",
            fontsize=8.5, fontweight="bold")
    ax.set_title(subtitle, fontsize=8, pad=3)
    return mesh


def section_waypoints(section: SectionProduct, waypoints: dict[str, dict[str, float]],
                      max_offset_km: float = 6.0):
    kx = 111.320 * np.cos(np.deg2rad(float(np.mean(section.lat_line))))
    ky = 110.574
    found = []
    for name, point in waypoints.items():
        dx = (section.lon_line - point["lon"]) * kx
        dy = (section.lat_line - point["lat"]) * ky
        index = int(np.argmin(dx * dx + dy * dy))
        offset = float(np.hypot(dx[index], dy[index]))
        if offset <= max_offset_km and 0 < index < section.distance_km.size - 1:
            found.append((float(section.distance_km[index]), name, float(section.terrain_m[index])))
    return sorted(found)


def draw_section(ax, section: SectionProduct, limit: float,
                 waypoints: dict[str, dict[str, float]], crest_m: float,
                 panel: str, subtitle: str):
    mesh = ax.pcolormesh(
        section.distance_km,
        section.heights_msl,
        section.difference_k,
        cmap=MAP_CMAP,
        vmin=-limit,
        vmax=limit,
        shading="gouraud",
        rasterized=True,
    )
    ax.contour(section.distance_km, section.heights_msl, section.difference_k,
               levels=[0.0], colors="0.2", linewidths=0.4)
    bottom = float(section.heights_msl.min())
    ax.fill_between(section.distance_km, bottom, section.terrain_m, color="0.55", zorder=5)
    ax.plot(section.distance_km, section.terrain_m, color="0.15", lw=0.6, zorder=6)
    ax.axhline(crest_m, color="0.35", lw=0.5, ls=(0, (4, 3)), zorder=4)
    for distance, name, terrain in section_waypoints(section, waypoints):
        ax.axvline(distance, color="0.25", lw=0.45, ls=(0, (3, 3)), alpha=0.65)
        ax.text(distance, ax.get_ylim()[1], f"{name} ", rotation=90, va="top", ha="right",
                fontsize=5.2, color="0.15")
        ax.plot(distance, terrain, marker="v", ms=3, color="0.15", zorder=7)
    ax.set_xlim(float(section.distance_km.min()), float(section.distance_km.max()))
    ax.set_ylim(bottom, float(section.heights_msl.max()))
    ax.set_xlabel("distance (km)")
    ax.set_ylabel("height (m MSL)")
    ax.text(0.02, 0.98, f"({panel})", transform=ax.transAxes, va="top", ha="left",
            fontsize=8.5, fontweight="bold")
    ax.text(0.0, -0.13, section.termini[0], transform=ax.transAxes, ha="left", va="top",
            fontsize=7, fontweight="bold")
    ax.text(1.0, -0.13, section.termini[1], transform=ax.transAxes, ha="right", va="top",
            fontsize=7, fontweight="bold")
    ax.set_title(subtitle, fontsize=8, pad=3)
    return mesh


def descriptive_row(product: str, domain: str, orientation: str, units: str,
                    values: np.ndarray, valid: datetime, crest_m: float,
                    weighting: str) -> dict[str, str | int | float]:
    finite = np.asarray(values)[np.isfinite(values)]
    if not finite.size:
        raise ValueError(f"no finite values for {product} {domain} {orientation}")
    return {
        "product": product,
        "domain": domain,
        "orientation": orientation,
        "valid_time_utc": valid.isoformat(),
        "pair": "X0-X4",
        "operation": "fine_3arcsec_minus_coarse_5arcmin",
        "units": units,
        "crest_reference_msl_m": crest_m,
        "n_values": int(finite.size),
        "minimum": float(np.min(finite)),
        "q10": float(np.quantile(finite, 0.10)),
        "median": float(np.median(finite)),
        "mean": float(np.mean(finite)),
        "q90": float(np.quantile(finite, 0.90)),
        "maximum": float(np.max(finite)),
        "fraction_negative": float(np.mean(finite < 0.0)),
        "fraction_positive": float(np.mean(finite > 0.0)),
        "weighting": weighting,
    }


def write_summary(path: Path, maps: list[MapProduct], sections: list[SectionProduct],
                  valid: datetime, crest_m: float) -> None:
    rows = []
    for product in maps:
        mask = (product.terrain_m < crest_m) & np.isfinite(product.difference_mj_m2)
        rows.append(descriptive_row(
            "heat_deficit_difference", product.domain, "", "MJ m-2",
            product.difference_mj_m2[mask], valid, crest_m,
            "unweighted model-grid cells below crest",
        ))
    for section in sections:
        mask = section.heights_msl[:, None] <= crest_m
        values = np.where(mask, section.difference_k, np.nan)
        rows.append(descriptive_row(
            "potential_temperature_section_difference", "d03", section.orientation, "K",
            values, valid, crest_m,
            "unweighted plotted section cells at or below crest",
        ))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {path}")


def plot_composite(maps: list[MapProduct], sections: list[SectionProduct], out_dir: Path,
                   stem: str, map_limit: float, section_limit: float, context: Path,
                   places: Path, waypoints: dict[str, dict[str, float]], crest_m: float) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(7.2, 7.5), layout="constrained")
    map_mesh = draw_map(axes[0, 0], maps[0], map_limit, context, places, {}, crest_m,
                        "a", "d02 basin-wide heat-deficit response")
    draw_map(axes[0, 1], maps[1], map_limit, context, places, waypoints, crest_m,
             "b", "d03 inner-basin heat-deficit response")
    section_mesh = draw_section(axes[1, 0], sections[0], section_limit, waypoints, crest_m,
                                "c", "d03 north--south potential-temperature response")
    draw_section(axes[1, 1], sections[1], section_limit, waypoints, crest_m,
                 "d", "d03 west--east potential-temperature response")
    map_bar = fig.colorbar(map_mesh, ax=axes[0, :], location="right", shrink=0.86,
                           extend="both", pad=0.02)
    map_bar.set_label(r"$\Delta$ heat deficit (MJ m$^{-2}$)")
    section_bar = fig.colorbar(section_mesh, ax=axes[1, :], location="right", shrink=0.86,
                               extend="both", pad=0.02)
    section_bar.set_label(r"$\Delta\theta$ (K)")
    save(fig, stem, out_dir=out_dir)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fine-run", type=Path, required=True)
    ap.add_argument("--coarse-run", type=Path, required=True)
    ap.add_argument("--valid", default="2013-02-02T16:00:00")
    ap.add_argument("--crest-m", type=float, default=2200.0)
    ap.add_argument("--map-limit", type=float, default=1.6)
    ap.add_argument("--section-limit", type=float, default=4.0)
    ap.add_argument("--section-top-m", type=float, default=2400.0)
    ap.add_argument("--smooth-sigma", type=float, default=1.5)
    ap.add_argument("--context-geojson", type=Path, default=DEFAULT_CONTEXT)
    ap.add_argument("--places", type=Path, default=DEFAULT_PLACES)
    ap.add_argument("--waypoints-config", type=Path, default=DEFAULT_WAYPOINTS_CONFIG)
    ap.add_argument("--out-dir", type=Path, required=True)
    ap.add_argument("--data-out-dir", type=Path, required=True)
    args = ap.parse_args()

    valid = datetime.fromisoformat(args.valid)
    maps = []
    sources = []
    for domain in (2, 3):
        product, paths = load_map(args.fine_run, args.coarse_run, domain, valid, args.crest_m)
        maps.append(product)
        sources.extend(paths)

    fine_d03_path = wo.wrfout_path(args.fine_run, 3, valid)
    coarse_d03_path = wo.wrfout_path(args.coarse_run, 3, valid)
    fine_d03 = wo.open_wrfout(fine_d03_path)
    coarse_d03 = wo.open_wrfout(coarse_d03_path)
    sections = [
        load_section(fine_d03, coarse_d03, orientation, args.section_top_m, args.smooth_sigma)
        for orientation in ("NS", "EW")
    ]
    waypoints = load_waypoints(args.waypoints_config)
    stem = f"wrf_terrain_cmp11_d02_d03_{valid:%H}z"
    plot_composite(
        maps, sections, args.out_dir, stem, args.map_limit, args.section_limit,
        args.context_geojson, args.places, waypoints, args.crest_m,
    )
    write_summary(
        args.data_out_dir / f"terrain_cmp11_d02_d03_{valid:%H}z_summary.csv",
        maps, sections, valid, args.crest_m,
    )
    for path in dict.fromkeys([*sources, fine_d03_path, coarse_d03_path]):
        print(f"source={path}")


if __name__ == "__main__":
    main()
