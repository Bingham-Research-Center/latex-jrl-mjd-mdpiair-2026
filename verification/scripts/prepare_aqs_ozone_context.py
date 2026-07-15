#!/usr/bin/env python3
"""Reduce an EPA AQS AirData parquet to the tracked episode-context table."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import date
from pathlib import Path

import polars as pl


SITES = {
    "49-013-0002": ("Roosevelt", "Utah DEQ"),
    "49-047-0014": ("Little Mountain", "USFS"),
    "49-047-1003": ("Vernal", "Utah DEQ"),
    "49-047-2002": ("Redwash", "Ute Indian Tribe"),
    "49-047-2003": ("Ouray", "Ute Indian Tribe"),
}
START = date(2013, 1, 1)
END = date(2013, 2, 28)
STANDARD = "Ozone 8-hour 2015"
UNITS = "Parts per million"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def site_id_expr() -> pl.Expr:
    return pl.concat_str(
        [
            pl.col("State Code").cast(pl.String).str.zfill(2),
            pl.col("County Code").cast(pl.String).str.zfill(3),
            pl.col("Site Num").cast(pl.String).str.zfill(4),
        ],
        separator="-",
    )


def reduce_table(source: Path) -> pl.DataFrame:
    frame = pl.read_parquet(source).with_columns(site_id_expr().alias("aqs_id"))
    observed_sites = set(frame["aqs_id"].unique().to_list())
    if observed_sites != set(SITES):
        raise ValueError(f"unexpected AQS site set: {sorted(observed_sites)}")
    if set(frame["Pollutant Standard"].unique().to_list()) != {STANDARD}:
        raise ValueError("input is not exclusively the AQS 2015 eight-hour ozone row")
    if set(frame["Units of Measure"].unique().to_list()) != {UNITS}:
        raise ValueError("input ozone units are not parts per million")
    if frame["date_local"].min() != START or frame["date_local"].max() != END:
        raise ValueError("input does not cover the frozen January-February window")
    if frame.select(pl.struct(["aqs_id", "date_local"]).is_duplicated().any()).item():
        raise ValueError("duplicate site/date rows in AQS reduction")

    expected_days = (END - START).days + 1
    coverage = frame.group_by("aqs_id").len()
    if coverage["len"].to_list() != [expected_days] * len(SITES):
        raise ValueError("one or more selected sites lacks a daily AQS row")

    names = pl.DataFrame(
        {
            "aqs_id": list(SITES),
            "site_name": [SITES[key][0] for key in SITES],
            "operator": [SITES[key][1] for key in SITES],
        }
    )
    return (
        frame.join(names, on="aqs_id", how="left")
        .select(
            "aqs_id",
            "site_name",
            "operator",
            pl.col("Latitude").alias("latitude"),
            pl.col("Longitude").alias("longitude"),
            "date_local",
            (pl.col("1st Max Value") * 1000.0).alias("mda8_ozone_ppb"),
            pl.col("Observation Percent").alias("observation_percent"),
            pl.col("Observation Count").alias("observation_count"),
            pl.col("1st Max Hour").alias("first_max_hour_local"),
            pl.col("AQI").alias("aqi"),
            pl.col("Event Type").alias("event_type"),
            pl.col("Pollutant Standard").alias("source_pollutant_standard"),
            pl.col("Units of Measure").alias("source_units"),
        )
        .sort("aqs_id", "date_local")
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--provenance", type=Path, required=True)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--source-url", required=True)
    parser.add_argument("--last-modified", required=True)
    parser.add_argument("--retrieved-at", required=True)
    parser.add_argument("--brc-tools-commit", required=True)
    parser.add_argument("--fetch-command", required=True)
    args = parser.parse_args()

    reduced = reduce_table(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    reduced.write_csv(args.output, float_precision=6)

    completeness = (
        reduced.group_by("aqs_id", "site_name", "operator")
        .agg(
            pl.len().alias("daily_rows"),
            pl.col("observation_percent").min().alias("minimum_observation_percent"),
            pl.col("observation_percent").max().alias("maximum_observation_percent"),
            (pl.col("observation_percent") < 75).sum().alias("days_below_75_percent"),
            pl.col("mda8_ozone_ppb").max().alias("maximum_reported_ppb"),
        )
        .sort("aqs_id")
        .to_dicts()
    )
    record = {
        "schema_version": 1,
        "dataset": "EPA AQS reported daily maximum 8-hour ozone context",
        "source_url": args.source_url,
        "source_http_last_modified": args.last_modified,
        "retrieved_at_utc": args.retrieved_at,
        "source_archive_sha256": sha256(args.archive),
        "filtered_parquet_sha256": sha256(args.input),
        "tracked_csv": str(args.output),
        "tracked_csv_sha256": sha256(args.output),
        "date_window_local_inclusive": [START.isoformat(), END.isoformat()],
        "daily_record_count": reduced.height,
        "pollutant_standard_row": STANDARD,
        "source_units": UNITS,
        "plotted_units": "parts per billion",
        "time_convention": "AQS Date Local; daily rows, not UTC timestamps",
        "missingness": {
            "missing_site_dates": 0,
            "note": "All five sites have 59 daily rows; within-day observation coverage varies and is retained explicitly.",
        },
        "site_completeness": completeness,
        "selection": {
            "site_ids": sorted(SITES),
            "reason": "four basin-floor, bench, or population-center monitors plus one north-rim context monitor",
        },
        "generator": "verification/scripts/prepare_aqs_ozone_context.py",
        "brc_tools_commit": args.brc_tools_commit,
        "fetch_command": args.fetch_command,
        "interpretation_limits": [
            "Values are EPA AQS daily summaries as reported; MDA8 was not recomputed.",
            "The figure shows no regulatory threshold and makes no attainment determination.",
            "The ozone record supplies episode context, not WRF chemistry validation or causal attribution.",
        ],
    }
    args.provenance.parent.mkdir(parents=True, exist_ok=True)
    args.provenance.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {reduced.height} rows -> {args.output}")
    print(f"wrote provenance -> {args.provenance}")


if __name__ == "__main__":
    main()
