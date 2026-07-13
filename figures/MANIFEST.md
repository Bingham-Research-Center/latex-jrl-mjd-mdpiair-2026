# Promoted manuscript figures

`main.tex` may include only files recorded here with status `promoted`.
Candidate and diagnostic outputs belong under `verification/figures/candidates/`.

| Figure file | Status | Script and commit | Run/data IDs | Valid window | Style check | Notes |
|---|---|---|---|---|---|---|
| `obs_temp_timeseries_feb0102.pdf` | promoted | `verification/scripts/plot_obs_feb0102.py`, `041183f` | observations; cache SHA-256 `733181afd09db704aafe2c148cf19b41bca83e8b020b9839768d7618217eeb64` | 31 January 00 UTC--4 February 00 UTC | visually inspected 10 July 2026; manuscript-native vector style | Observed floor-to-bench temperature evolution; four sites do not define basin volume. |
| `wrf_inversion_index_feb0102_gfs2way_vs_nam2way_d02_14to18.pdf` | promoted | `verification/scripts/plot_wrf_vs_obs_feb0102.py`, `b3bd6ea` | X6; X5; real observations | 2 February 14--18 UTC | visually inspected 13 July 2026; manuscript-native vector style | USU03 minus USU07 is a horizontal bulk theta contrast, not measured inversion depth; 8 K is a literature yardstick; plotted annotation corrected to ``8 K literature reference'' from identical hashed inputs (FIG-11). |
| `wrf_retention_ventilation_d02_14to18.pdf` | promoted | `verification/scripts/analyze_wrf_retention.py`, `07d01e2` | X6; X10; X5; X3; Slurm 13896641 | 2 February 14--18 UTC | visually inspected 10 July 2026; manuscript-native vector style | Solid lines are two-way and dashed lines are one-way; lines are station medians and shading is station IQR; PBLH is scheme dependent; transport wind is a fixed-layer proxy, not basin export. |

Promotion requires a real-data check, matched evaluation window, complete provenance, visual inspection, and canonical WRF styling review.
Synthetic or smoke-test output is never eligible.
