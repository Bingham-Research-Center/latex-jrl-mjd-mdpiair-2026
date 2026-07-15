#!/usr/bin/env python3
"""Synthetic contract test for the shared-axis profile data table."""
from __future__ import annotations

import csv
import tempfile
from datetime import datetime
from pathlib import Path

from plot_wrf_profile_spinup import write_profile_table


def main() -> None:
    tmp = Path(tempfile.mkdtemp(prefix="profile_table_smoke_"))
    rows = []
    for when in (datetime(2013, 2, 2, 12), datetime(2013, 2, 2, 13)):
        for case, label in (("gfs", "GFS two-way"), ("nam", "NAM two-way")):
            for level in range(3):
                rows.append({
                    "valid_time_utc": when.isoformat(),
                    "case_id": case,
                    "display_label": label,
                    "domain": "d03",
                    "source_path": f"/synthetic/{case}/{when:%H}",
                    "focus_name": "Horsepool",
                    "focus_latitude": 40.144,
                    "focus_longitude": -109.467,
                    "level_index": level,
                    "height_msl_m": 1600.0 + 100.0 * level,
                    "potential_temperature_k": 275.0 + level,
                    "terrain_msl_m": 1580.0,
                })
    path = write_profile_table(
        rows, tmp, "Horsepool", "gfs_nam",
        [datetime(2013, 2, 2, 12), datetime(2013, 2, 2, 13)],
    )
    with path.open(newline="") as handle:
        written = list(csv.DictReader(handle))
    assert len(written) == 12
    assert path.name == "theta_profiles_horsepool_gfs_nam_12z_13z.csv"
    assert written[0]["valid_time_utc"] == "2013-02-02T12:00:00"
    assert b"\r\n" not in path.read_bytes(), "profile table must be Git-clean LF text"
    print(f"OK: exact profile table contract -> {path}")


if __name__ == "__main__":
    main()
