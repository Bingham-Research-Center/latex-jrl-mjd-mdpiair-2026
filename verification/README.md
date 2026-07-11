# Verification and provenance

This directory retains Michael's useful 2013 evaluation work, small derived tables, candidate diagnostics, and CHPC provenance tools.
It is supporting evidence, not a second manuscript and not part of the MDPI submission package.

## Layout

- `data/` — `manifest.csv` plus small station selections, reduced WRF tables, scores, block-sensitivity summaries, and common-AGL retention tables.
- `figures/candidates/` — inherited diagnostic longlist; none is automatically manuscript-ready.
- `figures/manifest.csv` — candidate status and provenance.
- `scripts/` — reduction, scoring, plotting, and smoke tests.
- `docs/` — reproduction notes and historical evaluations.
- `provenance/` — CHPC inventory tools, the canonical run inventory, and the run-to-claim comparison inventory.

## Evidence tiers

1. X6/X10 GFS and X5/X3 NAM form the frozen default-terrain forcing-by-feedback factorial; their as-run identities, grids, physics, window, and source-specific metgrid levels are reconciled.
2. X6 versus X10 and X5 versus X3 change only nest feedback within each forcing family, allowing the GFS-minus-NAM response to be checked under both feedback modes.
3. The SIP-era `trang_ref` and January nudged run are heterogeneous context, not controlled members of the February matrix.
4. Terrain, PBL, slope/shading, and resolution candidates remain outside the first-draft result core.

See `notes/claim-evidence-ledger.md` before moving any result into `main.tex`.

## Local observations

Bulk Synoptic observations remain local, with the frozen cache recorded in the figure report and retention provenance JSON, and are ignored by Git.
The tracked CSVs are derived products and must remain traceable to their source window and reduction command.
`data/manifest.csv` is the compact authority for that lineage and clearly marks superseded, context-only, and partially reproducible tables.

## Commands

Use the maintained `brc-tools-2026` environment and keep synthetic outputs under temporary directories:

```bash
make smoke

PYTHONPATH=../brc-tools conda run -n brc-tools-2026 \
  python verification/scripts/plot_wrf_vs_obs_feb0102.py \
  --obs /scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/obs_basin_2013_feb0102.parquet \
  --wrf verification/data/wrf_gfs_2way_d02_per_station.csv \
        verification/data/wrf_nam_2way_d02_per_station.csv \
        verification/data/wrf_nam_1way_d02_per_station.csv \
  --out-dir verification/figures/candidates
```

The real common-AGL analysis is intentionally off-login and reproducible through:

```bash
sbatch verification/slurm/run_retention_analysis.slurm
```

The accepted four-run execution was Slurm job `13896641`; its exact archive paths, matched WRF files, station cells, interaction definition, software versions, diagnostics, and hashes are in `provenance/retention-analysis-13896641.json`.
The earlier three-run execution `13893307` remains as historical provenance and is superseded for the promoted figure and tables.

Before accepting regenerated results, verify the host, run identities, exact 2013 window, common stations/domain, and unchanged Git state outside intended outputs.
