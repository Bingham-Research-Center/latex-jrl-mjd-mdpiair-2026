# Verification and provenance

This directory retains Michael's useful 2013 evaluation work, small derived tables, candidate diagnostics, and CHPC provenance tools.
It is supporting evidence, not a second manuscript and not part of the MDPI submission package.

## Layout

- `data/` — small station selections, reduced WRF tables, scores, and spread tables.
- `figures/candidates/` — inherited diagnostic longlist; none is automatically manuscript-ready.
- `figures/manifest.csv` — candidate status and provenance.
- `scripts/` — reduction, scoring, plotting, and smoke tests.
- `docs/` — reproduction notes and historical evaluations.
- `provenance/` — CHPC inventory tools, run mappings, and the TBC canonical run inventory.

## Evidence tiers

1. The GFS two-way, NAM two-way, and NAM one-way touchstones are candidate controlled comparisons pending as-run namelist reconciliation.
2. The SIP-era `trang_ref` is heterogeneous same-case context, not the literal Tran et al. (2018) run or a controlled fourth member.
3. The January nudged-run analysis in `docs/baseline-eval-2013.md` is cross-period historical context, not a baseline that February runs must beat.

See `notes/claim-evidence-ledger.md` before moving any result into `main.tex`.

## Local observations

Bulk Synoptic observations remain local, normally under `~/brc-tools/data/`, and are ignored by Git.
The tracked CSVs are derived products and must remain traceable to their source window and reduction command.

## Commands

Use the `brc-tools` conda environment and make synthetic outputs explicit:

```bash
make smoke

PYTHONPATH=~/brc-tools conda run -n brc-tools \
  python verification/scripts/plot_wrf_vs_obs_feb0102.py \
  --obs ~/brc-tools/data/obs_basin_2013_feb0102.parquet \
  --wrf verification/data/wrf_gfs_2way_d02_per_station.csv \
        verification/data/wrf_nam_2way_d02_per_station.csv \
        verification/data/wrf_nam_1way_d02_per_station.csv \
  --out-dir verification/figures/candidates
```

Before accepting regenerated results, verify the host, run identities, exact 2013 window, common stations/domain, and unchanged Git state outside intended outputs.
