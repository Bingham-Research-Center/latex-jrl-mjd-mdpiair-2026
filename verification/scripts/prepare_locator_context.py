#!/usr/bin/env python3
"""Clip cached Natural Earth roads and rivers to a portable Uinta locator subset.

Run this on the writing host, where Cartopy may populate its Natural Earth cache.
The committed GeoJSON is then sufficient for an offline CHPC locator render.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from cartopy.io import shapereader
from shapely.geometry import box, mapping

DEFAULT_BBOX = (-111.0, 39.5, -108.9, 41.0)
ROAD_LABELS = {"40": "US 40", "191": "US 191"}
RIVER_LABELS = {"Green": "Green River"}
SOURCE_URLS = {
    "road": "https://naturalearth.s3.amazonaws.com/10m_cultural/ne_10m_roads.zip",
    "river": (
        "https://naturalearth.s3.amazonaws.com/10m_physical/"
        "ne_10m_rivers_lake_centerlines.zip"
    ),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def features(path: Path, feature_type: str, labels: dict[str, str], clip_box) -> list[dict]:
    selected = []
    for record in shapereader.Reader(path).records():
        name = str(record.attributes.get("name", ""))
        if name not in labels or record.geometry is None:
            continue
        geometry = record.geometry.intersection(clip_box)
        if geometry.is_empty:
            continue
        geometry = geometry.simplify(0.001, preserve_topology=True)
        selected.append({
            "type": "Feature",
            "properties": {
                "feature_type": feature_type,
                "name": name,
                "label": labels[name],
                "source": "Natural Earth 1:10m",
            },
            "geometry": mapping(geometry),
        })
    return selected


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--roads", type=Path, default=None,
                    help="Natural Earth ne_10m_roads.shp; Cartopy cache by default")
    ap.add_argument("--rivers", type=Path, default=None,
                    help="Natural Earth ne_10m_rivers_lake_centerlines.shp")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--bbox", type=float, nargs=4, default=DEFAULT_BBOX,
                    metavar=("WEST", "SOUTH", "EAST", "NORTH"))
    args = ap.parse_args()

    roads = args.roads or Path(shapereader.natural_earth("10m", "cultural", "roads"))
    rivers = args.rivers or Path(
        shapereader.natural_earth("10m", "physical", "rivers_lake_centerlines")
    )
    clip_box = box(*args.bbox)
    selected = features(roads, "road", ROAD_LABELS, clip_box)
    selected.extend(features(rivers, "river", RIVER_LABELS, clip_box))
    selected.sort(key=lambda item: (
        item["properties"]["feature_type"], item["properties"]["name"],
        json.dumps(item["geometry"], sort_keys=True),
    ))
    if not selected:
        raise SystemExit("no requested road or river features intersected the locator bbox")

    payload = {
        "type": "FeatureCollection",
        "bbox": list(args.bbox),
        "preparation_date": "2026-07-15",
        "source_urls": SOURCE_URLS,
        "source_sha256": {
            "roads_shp": sha256(roads),
            "roads_dbf": sha256(roads.with_suffix(".dbf")),
            "rivers_shp": sha256(rivers),
            "rivers_dbf": sha256(rivers.with_suffix(".dbf")),
        },
        "features": selected,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(f"wrote {args.out}: {len(selected)} clipped features")


if __name__ == "__main__":
    main()
