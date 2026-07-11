# Hosts, run inventory, and figure workflow

## Detect the host first

Run `hostname -f` and test the needed path before reading or generating data.

### Akamai/Linode writing host

- Manuscript, Git, lightweight Python, and local LaTeX.
- Selective extracted literature and critiques under `~/reviews`.
- `brc-tools` is normally available at `~/brc-tools` but must be checked.

### CHPC compute host

- WRF execution, large outputs, and publication-figure generation.
- Durable archive root: `/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive/`.
- Do not assume that `~/reviews` exists.
- Check for the `wrf-full-figures` skill before claiming canonical figure styling.

Bulk WRF output, raw archive manifests, and observation caches remain off Git.

## CHPC inventory contract

The default-terrain manuscript factorial is reconciled in
`verification/provenance/run-inventory.csv`: X6/X10 GFS and X5/X3 NAM under
two-way/one-way feedback.
Add one row per independently runnable configuration; do not infer a new row
from a folder name or candidate namelist.

Required fields:

| Field | Meaning |
|---|---|
| `run_id` | Stable manuscript-facing identifier. |
| `owner` | Person or group responsible for the run. |
| `host` | Host on which the evidence was inspected. |
| `archive_path` | Absolute durable path; never infer ownership from a parent folder. |
| `wrf_version` | From the WRF output header where possible. |
| `init_time_utc`, `valid_start_utc`, `valid_end_utc` | Exact forecast and coverage times. |
| `forcing` | GFS, NAM, RAP, or other initial/boundary dataset and cycle. |
| `domains`, `dx_m` | Domain count and grid spacing by domain. |
| `e_vert`, `p_top_pa` | Vertical interfaces and model top. |
| `feedback` | One-way or two-way nesting. |
| `physics` | PBL, surface layer, land surface, microphysics, radiation, and cumulus choices. |
| `fdda` | Grid/observation nudging master switches, variables, coefficients, and domains. |
| `surface_inputs` | Snow, albedo, land-use, and terrain sources or modifications. |
| `outputs` | Available domains, variables, and cadence. |
| `namelist_sha256`, `rsl_sha256` | Evidence fingerprints where available. |
| `confidence`, `notes` | `high`, `medium`, or `low`, plus unresolved caveats. |

Do not place secret locations, credentials, or bulk archive listings in the public-facing manuscript package.

The X10 WRF record is `verification/provenance/gfs-oneway-wrf-13894282.json`,
and its four-run analysis record is
`verification/provenance/retention-analysis-13896641.json`. Full figure counts,
renderer state, and the representative visual audit are recorded in
`verification/figures/gfs-feedback-factorial-2026-07-10.md`.

## Figure candidate contract

Record every diagnostic or proposed panel in `verification/figures/manifest.csv`.
The row must name its run IDs, input tables or WRF output, evaluation window, generator and commit, output file, whether the data are synthetic, provenance status, style status, and intended narrative role.

Candidate states are `synthetic`, `diagnostic`, `provisional`, `rejected`, and `promoted`.
Only `promoted` files are copied into `figures/` and entered in `figures/MANIFEST.md`.

## Promotion checklist

1. Confirm all input run IDs against the inventory.
2. Use an identical valid-time window and station/domain sample for compared runs.
3. Run the generating command with an explicit output directory.
4. Inspect units, time zone, terrain, color scale, labels, missing data, and panel ordering.
5. Apply `wrf-full-figures` when available; otherwise record the `brc-tools` style source and mark canonical review pending.
6. Export a vector PDF for review and a high-resolution RGB PNG or TIFF for submission.
7. Copy only the accepted final into `figures/` and update both manifests.

Synthetic smoke tests must write under a temporary directory and must leave `git status --short` unchanged.
