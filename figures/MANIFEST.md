# Promoted manuscript figures

`main.tex` may include only files recorded here with status `promoted`.
Candidate and diagnostic outputs belong under `verification/figures/candidates/`.

| Figure file | Status | Script and commit | Run/data IDs | Valid window | Style check | Notes |
|---|---|---|---|---|---|---|
| `obs_temp_timeseries_feb0102.pdf` | promoted | `verification/scripts/plot_obs_feb0102.py`, `041183f` | observations; cache SHA-256 `733181afd09db704aafe2c148cf19b41bca83e8b020b9839768d7618217eeb64` | 31 January 00 UTC--4 February 00 UTC | visually inspected 10 July 2026; manuscript-native vector style | Observed floor-to-bench temperature evolution; four sites do not define basin volume. |
| `wrf_inversion_index_feb0102_gfs2way_vs_nam2way_d02_14to18.pdf` | promoted | `verification/scripts/plot_wrf_vs_obs_feb0102.py`, `29854aac` | X6; X5; real observations | 2 February 14--18 UTC | visually inspected 14 July 2026; line-free manuscript-native vector style | The bench-minus-floor bulk-theta contrast is not inversion depth. The real-data rerender contains no 8 K reference line or classification annotation; PDF SHA-256 `1a8d5c45953ed08d0db5b9d9c024cf46035a4db09252f0ef888f0809d2ce5c31`; provenance `verification/provenance/v3-figure-review-20260714.json`. |
| `wrf_retention_ventilation_d02_14to18.pdf` | promoted | `verification/scripts/analyze_wrf_retention.py`, `10e5d34` | X6; X10; X5; X3; Slurm 13896641 | 2 February 14--18 UTC | visually inspected 14 July 2026; compact two-panel manuscript-native vector style | Solid lines are two-way and dashed lines are one-way; lines are station medians and shading is station IQR; stability and transport wind are plotted; PBLH remains in the tables but is omitted from the figure; transport wind is a fixed-layer proxy, not basin export. |

Promotion requires a real-data check, matched evaluation window, complete provenance, visual inspection, and canonical WRF styling review.
Synthetic or smoke-test output is never eligible.
