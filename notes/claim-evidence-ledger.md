# Claim and evidence ledger

This file separates manuscript-ready evidence from inherited prose, contextual comparisons, and open questions.
Nothing becomes true because it appears in both a note and `main.tex`.

## Status vocabulary

- **confirmed** — provenance and analysis window are reconciled; suitable for scoped manuscript use.
- **provisional** — supported by a current artifact but awaiting a named check.
- **context only** — informative but not a controlled comparison.
- **contradicted** — known to be false or mislabeled.
- **open** — no defensible answer yet.

## Current ledger

| ID | Claim | Status | Evidence | Remaining gate |
|---|---|---|---|---|
| C01 | The case studied by the inherited touchstone pipeline is 2 February 2013. | confirmed | `verification/data/wrf_*_d02_per_station.csv`; provenance notes | Preserve 2013 in every case reference; 2026 is publication metadata only. |
| C02 | The three short touchstones vary driving analysis and NAM nest feedback. | confirmed | As-run namelist/header reconciliation in `verification/provenance/run-inventory.csv`; controlled-comparison matrix in `verification/figures/chpc-figure-inventory-2026-07-10.md` | X6/X5 differ by driving product plus its expected metgrid-level count; X3/X5 differ only by feedback. Outcome claims still require matched diagnostics. |
| C03 | The 1 km d02 is the current common station-evaluation domain because d03 excludes most bench stations. | confirmed | Archived d02/d03 geometry; `verification/figures/candidates/wrf_transect_locator_d02_d03.*`; station/grid mapping | Treat d03 only as an interior resolution diagnostic unless a narrower sample is explicitly defined. |
| C04 | Over 14--18 UTC, GFS has a larger warm 2 m-temperature bias and larger absolute temperature error than NAM on the frozen d02 station sample. | confirmed | `verification/data/surface_skill_pair_summary.csv`; real-data overlays; Slurm job 13893307 | The paired hourly-median bias difference is +1.79 degrees C with a +0.57 to +3.08 degrees C two-hour block sensitivity interval; the five-hour result does not establish persistence. |
| C05 | `trang_ref` is the literal simulation evaluated by Tran et al. (2018). | contradicted | `verification/provenance/WRF-RUN-TO-REPORT-MAP.md`; review contradictions | Identify the exact staged WRF file; describe only as SIP-era lineage after Tran et al. |
| C06 | `trang_ref` provides a controlled fourth member of the touchstone experiment. | contradicted | Different WRF version, resolution, levels, run length, and likely surface/configuration choices | Use only as heterogeneous same-case context after matching the time window. |
| C07 | A January nudged run is the baseline that the February touchstones must beat. | contradicted | Different sub-period and configuration; see `verification/docs/baseline-eval-2013.md` | Retain its analysis as historical context only. |
| C08 | The heterogeneous February simulations span roughly 6.8 degrees C in station-mean 2 m-temperature bias. | provisional/context only | `verification/data/wrf_runs_scores_feb0102_postspinup_withtrang.csv` | Match `trang_ref` to the five-hour window and label the range as heterogeneous, not an isolated sensitivity. |
| C09 | Tran et al.'s four nudging configurations span 5.5 degrees C in published episode-mean bias. | context only | Tran critique and extracted Table 1 | Do not present as an apples-to-apples statistic with this study. |
| C10 | The committed WRF overlay figures were real-data publication candidates. | contradicted | Removed files contained `fake_cool` and `fake_warm`; the repaired smoke test writes only to a temporary directory | Provenance-complete real-data replacements now exist under distinct names (C15), but the historical claim remains false. |
| C11 | Emissions inventories and chemical mechanisms are relatively settled. | contradicted | Ahmadov and Matichuk critiques; UBAQR-2020 mechanism critique | State that meteorological fidelity is necessary, not uniquely dominant. |
| C12 | Five defensible configuration hypotheses exist in the current archive. | confirmed | As-run pairs in `verification/provenance/run-inventory.csv`; controlled-comparison matrix in `verification/figures/chpc-figure-inventory-2026-07-10.md` | Driving state, feedback, slope/shading, PBL/surface layer, and terrain pairs exist. Do not count the confounded resolution ladder or heterogeneous nudging context as additional controlled tests. |
| C13 | Three BRC/USU-orbit report slices attribute missed modeled ozone accumulation to excessive meteorological dilution or loss from the inverted layer. | context only | Raw extracts: `~/reviews/wrf-ozone-studies/_extracts/ramboll-racm2-2023.md` sections 3.3/4.0; `~/reviews/wrf-ozone-studies/_extracts/topdown-inventory-s9_6-9_7.md` section 9.7; `~/reviews/wrf-ozone-studies/_extracts/rmp-2022-sIIIB.md` section III.B; registered in `notes/literature-synthesis-register.md` | Verify full report metadata and exact passages before citation; the reports are related, span 2013/2019, and do not provide three independent or run-reconciled tests. |
| C14 | Aggregate surface or episode scores alone can conceal failure to retain the cold pool and reproduce event evolution. | context only | Top-down inventory Figure 15; Ramboll 2023 ozone performance summary; Rocky Mountain Power 2022 Figures 19--21 in the extracts named by C13 | Pre-register a time-resolved retention diagnostic for the matched WRF comparisons; recompute rather than quote inherited statistics. |
| C15 | Provenance-complete real-data WRF-versus-observation overlays now exist for the primary driving-state pair and secondary feedback pair. | confirmed | Twelve verified rows in `verification/figures/manifest.csv`; generator commits `c5bbe1a`, `5deba95`, and `041183f`; visual audit in the CHPC figure report | Canonical WRF styling, uncertainty, and promotion review remain open; no file is promoted. |
| C16 | The available X7/X0/X8 1 km/333 m/111 m sequence is not a controlled resolution experiment. | confirmed | Run inventory: different initialization/forecast age, domains, feedback, terrain placement, vertical levels, slope/shading, geometry, and cadence | Design a matched resolution experiment before making a resolution claim. |
| C17 | Over 14--18 UTC, controlled X6 GFS has weaker 50--500 m AGL stability and stronger layer transport wind than X5 NAM at the fixed station columns. | confirmed | `verification/data/retention_pair_summary.csv`; `figures/wrf_retention_ventilation_d02_14to18.pdf`; Slurm job 13893307 | GFS minus NAM is -3.63 K for stability and +0.79 m s-1 for transport wind; both two-hour block sensitivity intervals exclude zero and all five hourly medians have the same sign. Initial versus lateral-boundary causation remains unresolved. |
| C18 | NAM one-way versus NAM two-way feedback is negligible relative to the driving-state response over the five-hour d02 sample. | confirmed | `verification/data/retention_pair_summary.csv`; `verification/data/surface_skill_pair_summary.csv`; X3/X5 overlays | One-way minus two-way is +0.002 K for 50--500 m stability and +0.006 m s-1 for transport wind, with both intervals spanning zero. This bounds only the present window/sample and is not a general equivalence claim. |
| C19 | The MYJ/Eta treatment cannot yet be summarized as having only a small sub-700-m response. | provisional | X2/X1 as-run control; X2 mean bulk theta contrast 18.49 K versus X1 17.18 K in the matched window | Reproduce the sibling profile metric on common AGL levels with scheme-aware PBLH/TKE diagnostics before accepting or rejecting that description. |
| C20 | Native PBLH alone does not explain the X6/X5 common-AGL stability and transport-wind separation. | confirmed | `verification/data/retention_pair_summary.csv`; promoted retention figure | GFS minus NAM PBLH changes sign across hours and has a -11.24 to +10.48 m block sensitivity interval; retain PBLH only as a scheme-dependent companion diagnostic. |

## Manuscript admission rule

Rendered numerical claims require a confirmed run identity, exact common window, common station sample, reproducible command, and figure/table provenance.
Provisional values may remain in this ledger but not in `main.tex`.
