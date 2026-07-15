#!/usr/bin/env python3
"""Build the manuscript-owned X8 deficit-transport evidence packet.

This script is intentionally specific to the archived 111 m X8 context run and the
review-only supplementary figures in ``_manuscript_v3.tex``. Reusable WRF diagnostics,
transect integration, and renderers remain in ``brc-tools``.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timedelta
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

from brc_tools.nwp import wrf_output as wo
from brc_tools.nwp.wrf_figures import CaseConfig
from brc_tools.visualize.deficitflux import (
    plot_deficit_budget,
    plot_deficit_bulk_diagnostics,
    plot_deficitflux_divergence,
    plot_deficitflux_map,
)
from brc_tools.visualize.style import resolve_style, use_publication_style


REPO = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = REPO / "verification/config/figures/pelican2013_d04.toml"
DEFAULT_RUN = Path(
    "/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive/"
    "pelican2013_nam_d04_111m_50lev_oneway_terrain3s/full6h/"
    "run_20260709T041225Z_d04only3s_ts12"
)


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.rstrip("Z"))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--run-dir", type=Path, default=DEFAULT_RUN)
    parser.add_argument("--domain", type=int, default=4)
    parser.add_argument("--start", type=parse_time, default=parse_time("2013-02-02T12:00:00"))
    parser.add_argument("--end", type=parse_time, default=parse_time("2013-02-02T18:00:00"))
    parser.add_argument(
        "--retained-start", type=parse_time, default=parse_time("2013-02-02T14:00:00")
    )
    parser.add_argument("--map-valid", type=parse_time, default=parse_time("2013-02-02T15:00:00"))
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--data-out-dir", type=Path, required=True)
    parser.add_argument("--dpi", type=int, default=300)
    return parser


def interior(field: np.ndarray, margin: int) -> np.ndarray:
    field = np.asarray(field)
    if margin <= 0:
        return field
    if 2 * margin >= field.shape[-2] or 2 * margin >= field.shape[-1]:
        raise ValueError(f"{margin}-cell crop removes full field with shape {field.shape}")
    return field[..., margin:-margin, margin:-margin]


def area_mean(field: np.ndarray, area: np.ndarray, margin: int) -> float:
    values = interior(np.asarray(field, dtype=float), margin)
    weights = interior(np.asarray(area, dtype=float), margin)
    valid = np.isfinite(values) & np.isfinite(weights) & (weights > 0.0)
    return float(np.average(values[valid], weights=weights[valid]))


def finite_percentile(field: np.ndarray, percentile: float, margin: int) -> float:
    values = interior(np.asarray(field, dtype=float), margin)
    values = values[np.isfinite(values)]
    return float(np.percentile(values, percentile)) if values.size else float("nan")


def save_gate_figure(
    times: list[datetime],
    gate_series: dict[str, np.ndarray],
    retained_start: datetime,
    out_base: Path,
    dpi: int,
) -> None:
    for suffix in (".png", ".pdf"):
        fig, ax = plt.subplots(figsize=(9.2, 4.8), constrained_layout=True)
        for label, values in gate_series.items():
            ax.plot(times, values, marker="o", ms=2.5, lw=1.25, label=label)
        ax.axhline(0.0, color="0.3", lw=0.8)
        ax.axvspan(times[0], retained_start, color="0.75", alpha=0.35, lw=0)
        ax.text(
            0.015,
            0.96,
            "spin-up context",
            transform=ax.transAxes,
            ha="left",
            va="top",
            fontsize=8,
            color="0.35",
        )
        ax.set_ylabel(r"signed deficit transport $\Phi$ (GW)")
        ax.set_xlabel("valid time (UTC)")
        ax.set_title("X8 d04 signed heat-deficit transport across model-terrain transects")
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
        ax.grid(True, alpha=0.25)
        ax.legend(fontsize=7, ncol=2)
        fig.text(
            0.01,
            0.005,
            "All transects run west to east; positive is southward. "
            "The d04 footprint is not a basin boundary.",
            fontsize=6.5,
            color="0.35",
        )
        fig.savefig(out_base.with_suffix(suffix), dpi=dpi)
        plt.close(fig)


def write_rows(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    args = build_parser().parse_args()
    cfg = CaseConfig.from_toml(args.config)
    if not cfg.transects:
        raise SystemExit("configuration contains no deficit-transport transects")
    all_times = wo.list_valid_times(args.run_dir, args.domain)
    times = [valid for valid in all_times if args.start <= valid <= args.end]
    if len(times) < 2:
        raise SystemExit("fewer than two X8 d04 valid times in the requested window")
    if args.map_valid not in times:
        raise SystemExit(f"map valid time {args.map_valid.isoformat()} is unavailable")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    args.data_out_dir.mkdir(parents=True, exist_ok=True)
    use_publication_style()

    margin = cfg.deficit_budget_margin_cells
    heat_means: list[float] = []
    convergence_means: list[float] = []
    state_rows: list[dict] = []
    gate_values = {transect.name: [] for transect in cfg.transects}
    map_payload: dict | None = None
    dx_m = float("nan")

    for valid in times:
        source = wo.wrfout_path(args.run_dir, args.domain, valid)
        dataset = wo.open_wrfout(source)
        try:
            bulk = wo.deficit_bulk_fields(
                dataset,
                cfg.crest_m,
                min_deficit_k=cfg.deficit_active_min_k,
                min_heat_deficit_j_m2=cfg.deficit_min_heat_mj_m2 * 1e6,
            )
            convergence = -wo.horizontal_flux_divergence(
                dataset,
                bulk.flux_x_w_m,
                bulk.flux_y_w_m,
                earth_relative=True,
            ) * 3600.0 / 1e6
            area = wo.grid_cell_area_m2(dataset)
            dx_m, _ = wo.dx_dy(dataset)
            speed = np.hypot(bulk.velocity_x_m_s, bulk.velocity_y_m_s)
            heat_mean = area_mean(bulk.heat_deficit_j_m2 / 1e6, area, margin)
            convergence_mean = area_mean(convergence, area, margin)
            heat_means.append(heat_mean)
            convergence_means.append(convergence_mean)

            row = {
                "valid_utc": valid.isoformat(),
                "lead_hours": f"{(valid - times[0]).total_seconds() / 3600.0:.6g}",
                "retained_window": str(valid >= args.retained_start).lower(),
                "area_mean_heat_mj_m2": f"{heat_mean:.9g}",
                "area_mean_horizontal_convergence_mj_m2_h": f"{convergence_mean:.9g}",
                "median_depth_m_agl": f"{finite_percentile(bulk.depth_m, 50, margin):.9g}",
                "p90_depth_m_agl": f"{finite_percentile(bulk.depth_m, 90, margin):.9g}",
                "median_deficit_speed_m_s": f"{finite_percentile(speed, 50, margin):.9g}",
                "p90_deficit_speed_m_s": f"{finite_percentile(speed, 90, margin):.9g}",
                "median_bulk_froude": f"{finite_percentile(bulk.froude, 50, margin):.9g}",
                "p90_bulk_froude": f"{finite_percentile(bulk.froude, 90, margin):.9g}",
            }
            for transect in cfg.transects:
                result = wo.integrate_flux_transect(
                    dataset,
                    bulk.flux_x_w_m,
                    bulk.flux_y_w_m,
                    transect.lat_a,
                    transect.lon_a,
                    transect.lat_b,
                    transect.lon_b,
                    label=transect.name,
                )
                value_gw = result.total_w / 1e9
                gate_values[transect.name].append(value_gw)
                row[f"{transect.name}_gw"] = f"{value_gw:.9g}"
            state_rows.append(row)

            if valid == args.map_valid:
                map_payload = {
                    "lon": np.asarray(wo.surface_field(dataset, "XLONG")),
                    "lat": np.asarray(wo.surface_field(dataset, "XLAT")),
                    "terrain": np.asarray(wo.surface_field(dataset, "HGT")),
                    "heat_mj_m2": np.asarray(bulk.heat_deficit_j_m2 / 1e6),
                    "flux_x": np.asarray(bulk.flux_x_w_m),
                    "flux_y": np.asarray(bulk.flux_y_w_m),
                    "convergence": np.asarray(convergence),
                    "depth": np.asarray(bulk.depth_m),
                    "speed": np.asarray(speed),
                    "froude": np.asarray(bulk.froude),
                }
        finally:
            dataset.close()

    if map_payload is None:
        raise RuntimeError("map payload was not captured")

    heat = np.asarray(heat_means)
    convergence = np.asarray(convergence_means)
    dt_hours = np.asarray(
        [(end - start).total_seconds() / 3600.0 for start, end in zip(times[:-1], times[1:])]
    )
    interval_times = [start + (end - start) / 2 for start, end in zip(times[:-1], times[1:])]
    storage = np.diff(heat) / dt_hours
    interval_convergence = 0.5 * (convergence[:-1] + convergence[1:])
    unresolved = storage - interval_convergence

    state_fields = list(state_rows[0])
    write_rows(
        args.data_out_dir / "x8_deficit_transport_timeseries.csv",
        state_fields,
        state_rows,
    )
    interval_rows = []
    for index, midpoint in enumerate(interval_times):
        interval_rows.append(
            {
                "interval_start_utc": times[index].isoformat(),
                "interval_end_utc": times[index + 1].isoformat(),
                "interval_midpoint_utc": midpoint.isoformat(),
                "retained_window": str(midpoint >= args.retained_start).lower(),
                "storage_mj_m2_h": f"{storage[index]:.9g}",
                "horizontal_convergence_mj_m2_h": f"{interval_convergence[index]:.9g}",
                "unresolved_mj_m2_h": f"{unresolved[index]:.9g}",
            }
        )
    write_rows(
        args.data_out_dir / "x8_deficit_budget_intervals.csv",
        list(interval_rows[0]),
        interval_rows,
    )

    retained = np.asarray([midpoint >= args.retained_start for midpoint in interval_times])
    correlation = float(np.corrcoef(storage[retained], interval_convergence[retained])[0, 1])
    residual_rmse = float(np.sqrt(np.mean(np.square(unresolved[retained]))))

    def hour_metrics(start_hour: int) -> tuple[float, float, float]:
        start = datetime(2013, 2, 2, start_hour)
        end = start + timedelta(hours=1)
        i0, i1 = times.index(start), times.index(end)
        elapsed = np.asarray([(valid - start).total_seconds() / 3600.0 for valid in times[i0:i1 + 1]])
        storage_hour = float(heat[i1] - heat[i0])
        convergence_hour = float(np.trapezoid(convergence[i0:i1 + 1], x=elapsed))
        return storage_hour, convergence_hour, storage_hour - convergence_hour

    summary_rows: list[dict] = []

    def add_summary(metric: str, value, units: str, window: str, interpretation: str) -> None:
        summary_rows.append(
            {
                "metric": metric,
                "value": value if isinstance(value, str) else f"{float(value):.9g}",
                "units": units,
                "window": window,
                "interpretation": interpretation,
            }
        )

    add_summary("domain_nominal_dx", dx_m, "m", "X8 d04", "nominal grid spacing")
    add_summary("edge_margin", margin, "grid cells", "all spatial means", "symmetric crop")
    add_summary(
        "edge_margin_distance", margin * dx_m, "m", "all spatial means", "nominal one-sided crop"
    )
    add_summary("active_deficit_threshold", cfg.deficit_active_min_k, "K", "bulk fields", "diagnostic definition")
    add_summary("minimum_heat_threshold", cfg.deficit_min_heat_mj_m2, "MJ m-2", "F/H fields", "diagnostic mask")
    add_summary("retained_storage_convergence_correlation", correlation, "1", "14:00-18:00 UTC", "temporal interval association")
    add_summary("retained_unresolved_rmse", residual_rmse, "MJ m-2 h-1", "14:00-18:00 UTC", "not uniquely diabatic")
    for start_hour in (15, 16):
        storage_hour, convergence_hour, unresolved_hour = hour_metrics(start_hour)
        window = f"{start_hour:02d}:00-{start_hour + 1:02d}:00 UTC"
        add_summary(f"storage_{start_hour:02d}to{start_hour + 1:02d}", storage_hour, "MJ m-2 h-1", window, "one-hour H change")
        add_summary(f"horizontal_convergence_{start_hour:02d}to{start_hour + 1:02d}", convergence_hour, "MJ m-2 h-1", window, "10-min trapezoidal mean")
        add_summary(f"unresolved_{start_hour:02d}to{start_hour + 1:02d}", unresolved_hour, "MJ m-2 h-1", window, "storage minus horizontal convergence")
    map_row = state_rows[times.index(args.map_valid)]
    for key, units in (
        ("median_depth_m_agl", "m AGL"),
        ("p90_depth_m_agl", "m AGL"),
        ("median_deficit_speed_m_s", "m s-1"),
        ("p90_deficit_speed_m_s", "m s-1"),
        ("median_bulk_froude", "1"),
        ("p90_bulk_froude", "1"),
    ):
        add_summary(key + "_15z", map_row[key], units, "2013-02-02 15:00 UTC", "interior spatial percentile")
    north_name = "northern_reference"
    if north_name in gate_values:
        north = np.asarray(gate_values[north_name])
        retained_points = np.asarray([valid >= args.retained_start for valid in times])
        retained_indices = np.flatnonzero(retained_points)
        min_index = retained_indices[int(np.argmin(north[retained_points]))]
        max_index = retained_indices[int(np.argmax(north[retained_points]))]
        add_summary("northern_reference_min", north[min_index], "GW", "14:00-18:00 UTC", "negative is northward")
        add_summary("northern_reference_min_time", times[min_index].isoformat(), "UTC", "14:00-18:00 UTC", "valid time")
        add_summary("northern_reference_max", north[max_index], "GW", "14:00-18:00 UTC", "positive is southward")
        add_summary("northern_reference_max_time", times[max_index].isoformat(), "UTC", "14:00-18:00 UTC", "valid time")
    write_rows(
        args.data_out_dir / "x8_deficit_transport_summary.csv",
        ["metric", "value", "units", "window", "interpretation"],
        summary_rows,
    )

    annotation = (
        f"X8 | d04 | nominal {dx_m:.1f} m | crest {cfg.crest_m:.0f} m MSL | "
        f"active deficit >= {cfg.deficit_active_min_k:g} K"
    )
    heat_style = resolve_style("heat_deficit", overrides=cfg.style.overrides)
    for suffix in (".png", ".pdf"):
        plot_deficitflux_map(
            map_payload["lon"],
            map_payload["lat"],
            map_payload["heat_mj_m2"],
            map_payload["flux_x"],
            map_payload["flux_y"],
            args.out_dir / f"x8_deficit_transport_map_15z{suffix}",
            style=heat_style,
            crest_terrain=map_payload["terrain"],
            crest_m=cfg.crest_m,
            title="X8 d04 crest-referenced heat deficit and horizontal transport | 15:00 UTC",
            annotation=annotation,
            waypoints=cfg.waypoints,
            overlays=cfg.map_overlays,
            transects=cfg.transects,
            dpi=args.dpi,
        )

    gate_series = {
        transect.label: np.asarray(gate_values[transect.name]) for transect in cfg.transects
    }
    save_gate_figure(
        times,
        gate_series,
        args.retained_start,
        args.out_dir / "x8_deficit_transport_gates_12to18",
        args.dpi,
    )

    convergence_style = resolve_style("deficit_advection", overrides=cfg.style.overrides)
    smooth_sigma = cfg.deficitflux_smooth_km * 1000.0 / dx_m
    for suffix in (".png", ".pdf"):
        plot_deficitflux_divergence(
            map_payload["lon"],
            map_payload["lat"],
            map_payload["convergence"],
            args.out_dir / f"x8_deficit_convergence_15z{suffix}",
            style=convergence_style,
            smooth_sigma=smooth_sigma,
            crest_terrain=map_payload["terrain"],
            crest_m=cfg.crest_m,
            title="X8 d04 horizontal heat-deficit flux convergence | 15:00 UTC",
            annotation=annotation + f" | display smoothing {cfg.deficitflux_smooth_km:g} km",
            waypoints=cfg.waypoints,
            overlays=cfg.map_overlays,
            dpi=args.dpi,
        )

    bulk_styles = tuple(
        resolve_style(name, overrides=cfg.style.overrides)
        for name in ("deficit_depth", "deficit_speed", "deficit_froude")
    )
    for suffix in (".png", ".pdf"):
        plot_deficit_bulk_diagnostics(
            map_payload["lon"],
            map_payload["lat"],
            map_payload["depth"],
            map_payload["speed"],
            map_payload["froude"],
            args.out_dir / f"x8_deficit_bulk_15z{suffix}",
            styles=bulk_styles,
            crest_terrain=map_payload["terrain"],
            crest_m=cfg.crest_m,
            title="X8 d04 exploratory crest-referenced bulk diagnostics | 15:00 UTC",
            annotation=annotation + f" | F/H masked below H={cfg.deficit_min_heat_mj_m2:g} MJ m-2",
            waypoints=cfg.waypoints,
            overlays=cfg.map_overlays,
            dpi=args.dpi,
        )

    for suffix in (".png", ".pdf"):
        plot_deficit_budget(
            times,
            heat,
            interval_times,
            storage,
            interval_convergence,
            unresolved,
            args.out_dir / f"x8_deficit_budget_12to18{suffix}",
            title="X8 d04 interior heat-deficit tendency diagnostic",
            spinup_end=args.retained_start,
            annotation=(
                f"{annotation} | {margin}-cell ({margin * dx_m / 1000.0:.2f} km) edge crop; "
                "unresolved = storage - horizontal convergence"
            ),
            dpi=args.dpi,
        )

    print(f"wrote {len(list(args.out_dir.glob('x8_deficit_*')))} figure files to {args.out_dir}")
    print(f"wrote 3 CSV files to {args.data_out_dir}")


if __name__ == "__main__":
    main()
