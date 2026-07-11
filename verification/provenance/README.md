# Provenance — recovering the WRF run config for the Methods section

Read-only CHPC probes used to recover the exact configuration of the 2013 WRF runs
(forcing dataset, PBL / land-surface / microphysics schemes, vertical levels, d03 `dx`,
analysis-nudging settings, run window) so the manuscript Methods can disclose them
accurately. No model runs here — just digging the group archive for the namelist and
config that produced the runs.

## Files
- `chpc_pathcheck.sh` — first-pass probe: locate Trang's `WRF_TRANG_frozone` / `WRF_anlnudge`
  baseline run dir and its namelist on the group archive / scratch (read-only: `ls`/`stat`/`find`/
  `grep`, `rclone ls`, `ncdump -h`).
- `chpc_wrf_provenance.sh` — targeted dig of the archive subtrees that hold the run config,
  extracting the Methods-relevant settings. Read-only except an optional, size-capped,
  auto-deleted single-`wrfout` fallback download used only when no `namelist.input` is found.
- `chpc_wrf_publication_inventory.sh` — read-only manifests for the Trang/OSIP archive trees,
  exact paths for John's touchstones, candidate-config hashes, and optional local wrfout-header
  fingerprints. Run it via `CHPC-WRF-INVENTORY-HANDOFF.md`.
- `namelist_candidates.txt` — the `namelist.input` candidates surfaced from the archive
  (raw config to reconcile against the runs before it enters Methods).
- `CHPC-WRF-INVENTORY-RESULTS.md` — summary of running the inventory (checksum, per-tree
  counts, config labels, header coverage) to reconcile against the run lookup table. The
  full report tarball is transferred out-of-band, not committed (raw archive listings /
  namelist contents kept out of this public repo).

## Running (on CHPC)
```sh
module load rclone netcdf-c          # or: module load nco
bash chpc_pathcheck.sh      2>&1 | tee chpc_pathcheck_$(date +%F).log
bash chpc_wrf_provenance.sh 2>&1 | tee chpc_wrf_provenance_$(date +%F).log
```
Run logs (`*.log`, `*.log.txt`) are gitignored — large raw dumps, not tracked. The original
2026-07-01 dumps are preserved on the `jrl/first-edits` branch if ever needed.

## Status
The four default-terrain runs used by the manuscript factorial are reconciled
against as-run namelists and output headers in `run-inventory.csv`: X6/X10 GFS
and X5/X3 NAM.
Other recovered candidate namelists remain unverified until they are matched to
their actual outputs; do not extend the Methods matrix from filenames or
candidate configurations alone.
