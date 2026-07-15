#!/usr/bin/env python3
"""Synthetic smoke test for the CMP11 supplemental composite."""
from __future__ import annotations

import csv
import tempfile
from datetime import datetime
from pathlib import Path

import numpy as np

from plot_terrain_cmp11_supplement import (
    DEFAULT_CONTEXT,
    DEFAULT_PLACES,
    DEFAULT_WAYPOINTS_CONFIG,
    MapProduct,
    SectionProduct,
    load_waypoints,
    plot_composite,
    write_summary,
)


def synthetic_map(domain: str, west: float, east: float, south: float, north: float,
                  ny: int, nx: int) -> MapProduct:
    lon_1d = np.linspace(west, east, nx)
    lat_1d = np.linspace(south, north, ny)
    lon, lat = np.meshgrid(lon_1d, lat_1d)
    terrain = 1450.0 + 950.0 * ((lat - south) / (north - south)) ** 2
    difference = 0.8 * np.sin(4 * np.pi * (lon - west) / (east - west))
    difference -= 0.9 * np.exp(-((lat - 40.15) / 0.18) ** 2)
    return MapProduct(domain, lon, lat, terrain, difference)


def synthetic_section(orientation: str) -> SectionProduct:
    distance = np.linspace(0.0, 50.0, 70)
    heights = np.arange(1350.0, 2401.0, 25.0)
    terrain = 1475.0 + 90.0 * np.sin(distance / 8.0) ** 2
    z, x = np.meshgrid(heights, distance, indexing="ij")
    difference = 1.2 * np.exp(-((z - 1780.0) / 180.0) ** 2) * np.cos(x / 9.0)
    difference[z < terrain[None, :]] = np.nan
    if orientation == "NS":
        lon_line = np.full(distance.size, -109.65)
        lat_line = np.linspace(40.05, 40.45, distance.size)
        termini = ("C", "D")
    else:
        lon_line = np.linspace(-109.9, -109.35, distance.size)
        lat_line = np.full(distance.size, 40.25)
        termini = ("A", "B")
    return SectionProduct(
        orientation, distance, lon_line, lat_line, terrain, heights, difference, termini
    )


def main() -> None:
    tmp = Path(tempfile.mkdtemp(prefix="terrain_cmp11_smoke_"))
    maps = [
        synthetic_map("d02", -110.6, -108.8, 39.55, 40.95, 45, 60),
        synthetic_map("d03", -109.95, -109.35, 40.02, 40.48, 50, 62),
    ]
    sections = [synthetic_section("NS"), synthetic_section("EW")]
    waypoints = load_waypoints(DEFAULT_WAYPOINTS_CONFIG)
    plot_composite(
        maps, sections, tmp, "wrf_terrain_cmp11_d02_d03_16z", 1.6, 4.0,
        DEFAULT_CONTEXT, DEFAULT_PLACES, waypoints, 2200.0,
    )
    summary = tmp / "terrain_cmp11_d02_d03_16z_summary.csv"
    write_summary(summary, maps, sections, datetime(2013, 2, 2, 16), 2200.0)
    for extension in ("png", "pdf"):
        path = tmp / f"wrf_terrain_cmp11_d02_d03_16z.{extension}"
        assert path.exists() and path.stat().st_size > 10_000, f"missing/empty {path}"
    with summary.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 4, f"expected four summary rows, got {len(rows)}"
    assert {row["domain"] for row in rows} == {"d02", "d03"}
    print(f"OK: CMP11 composite and four-row summary -> {tmp}")


if __name__ == "__main__":
    main()
