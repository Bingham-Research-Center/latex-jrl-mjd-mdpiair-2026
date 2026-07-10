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
| C02 | The three short touchstones vary driving analysis and NAM nest feedback. | provisional | GFS two-way, NAM two-way, and NAM one-way reduced CSVs | Confirm the as-run namelists are otherwise identical. |
| C03 | The 1 km d02 is the current common station-evaluation domain because d03 excludes most bench stations. | provisional | `verification/docs/chpc-feb-touchstones.md`; station/grid mapping | Confirm against the archived domain geometry in the CHPC inventory. |
| C04 | The current score tables suggest warmer GFS than NAM surface errors during 14--18 UTC. | provisional | `verification/data/wrf_runs_scores_feb0102_postspinup.csv` | Recompute from provenance-checked runs and matched observations; add uncertainty before prose. |
| C05 | `trang_ref` is the literal simulation evaluated by Tran et al. (2018). | contradicted | `verification/provenance/WRF-RUN-TO-REPORT-MAP.md`; review contradictions | Identify the exact staged WRF file; describe only as SIP-era lineage after Tran et al. |
| C06 | `trang_ref` provides a controlled fourth member of the touchstone experiment. | contradicted | Different WRF version, resolution, levels, run length, and likely surface/configuration choices | Use only as heterogeneous same-case context after matching the time window. |
| C07 | A January nudged run is the baseline that the February touchstones must beat. | contradicted | Different sub-period and configuration; see `verification/docs/baseline-eval-2013.md` | Retain its analysis as historical context only. |
| C08 | The heterogeneous February simulations span roughly 6.8 degrees C in station-mean 2 m-temperature bias. | provisional/context only | `verification/data/wrf_runs_scores_feb0102_postspinup_withtrang.csv` | Match `trang_ref` to the five-hour window and label the range as heterogeneous, not an isolated sensitivity. |
| C09 | Tran et al.'s four nudging configurations span 5.5 degrees C in published episode-mean bias. | context only | Tran critique and extracted Table 1 | Do not present as an apples-to-apples statistic with this study. |
| C10 | The committed WRF overlay figures were real-data publication candidates. | contradicted | Removed files contained `fake_cool` and `fake_warm`; the repaired smoke test now writes only to a temporary directory | Regenerate from provenance-checked real inputs into `verification/figures/candidates/` and inspect before promotion. |
| C11 | Emissions inventories and chemical mechanisms are relatively settled. | contradicted | Ahmadov and Matichuk critiques; UBAQR-2020 mechanism critique | State that meteorological fidelity is necessary, not uniquely dominant. |
| C12 | Five defensible configuration hypotheses exist in the current archive. | open | `notes/narrative-and-hypotheses.md` | Await John's CHPC inventory and construct controlled run pairs. |

## Manuscript admission rule

Rendered numerical claims require a confirmed run identity, exact common window, common station sample, reproducible command, and figure/table provenance.
Provisional values may remain in this ledger but not in `main.tex`.
