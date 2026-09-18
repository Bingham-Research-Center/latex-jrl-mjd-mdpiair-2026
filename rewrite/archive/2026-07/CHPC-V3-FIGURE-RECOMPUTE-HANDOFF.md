> Completed historical dispatch, archived 18 September 2026. Do not execute.
> Original request text follows unchanged; see [archive context](README.md).

# CHPC v3 figure recomputation handoff

Status: active existing-output dispatch, 14 July 2026.

This is the single execution record for the unfinished CHPC figure work in the
Codex v3 review.  It consolidates the older line-free overlay baton with John's
14 July terrain, domain, profile, and restyle requests.  Scientific rationale
remains in `notes/manuscript-v3-structure-and-domain-review.md`; commands in that
note are not a second dispatch.

## Dispatch boundary

```text
REQUEST_ID: 20260714-v3-figure-review
MODE: FIGURE
SOURCE_REF: the immutable full pushed manuscript commit supplied with this handoff
BRC_TOOLS_REF: 69ddbe07af2e38e5e2d4f12f681bb360ff506a1a
RETURN_BRANCH: jrl/chpc-20260714-v3-figure-review
COMPUTE: existing WRF output and frozen observation-cache analysis/rendering only
```

Do not use a branch name alone as `SOURCE_REF`.
The writing-host publication message supplies the full commit containing this file.
If that commit or the pinned `brc-tools` commit cannot be resolved, stop.

This packet authorizes six bounded product groups:

1. regenerate the withheld X6/X5 and reserve X3/X5 two-site bulk-theta overlays
   without the invalid 8 K reference line;
2. rerender the d02 CMP11 fine-minus-coarse top-down heat-deficit field;
3. render the matched d03 CMP11 heat-deficit field and north--south/east--west
   potential-temperature sections;
4. render only X6 and X5 Horsepool profiles at 12 and 13 UTC;
5. rerender the clean d02/d03 geographic locator used as Figure 1(a); and
6. restyle the already failed, measurement-limited ANA-18 slope-radiation
   diagnostic without map-coordinate ticks.

No item promotes a new scientific claim or reopens a failed gate.
Only item 1 may restore an already registered promoted figure, and only after its
real-data, hash, line-removal, and visual checks pass.

## Explicit exclusions

Do not run or infer any of the following:

- a new WRF integration, restart, or multi-day fine/coarse-terrain experiment;
- cumulative multi-day cold-air storage, drainage, erosion, or export;
- a vertical-velocity, turbulence, gravity-wave, moist-convection, or chemistry
  diagnostic;
- the fine-terrain two-way-feedback comparison X9 minus X0;
- MODIS or ozone acquisition, which are separate lookup/data tasks;
- a new CMP11 gate, d02--d03 resolution claim, terrain-source ranking, or figure
  promotion beyond the conditional line-free overlay below; or
- reruns of completed ANA-16, ANA-17, ANA-18, or ANA-19 decisions.

The current archives cover only the six-hour 12--18 UTC event window for X0/X4.
A multi-day cumulative-impact figure therefore requires a separately authorized,
matched longer integration and is not a recomputation from the present files.

## Read order on CHPC

After the bootstrap in `rewrite/CHPC-CODEX-PROMPT.md`, read only:

1. this file;
2. the CMP01, CMP03, CMP07, and CMP11 rows in
   `verification/provenance/comparison-inventory.csv` and the X0, X1, X3, X4,
   X5, and X6 rows in `verification/provenance/run-inventory.csv`;
3. the relevant rows in `verification/figures/manifest.csv`,
   `figures/MANIFEST.md`, and `verification/figures/archive-inventory.md`;
4. `figures-draft/HARVEST.md`;
5. `verification/config/figures/README.md`, `pelican2013.toml`, and
   `pelican2013_terrain_d03.toml`; and
6. only the scripts and Slurm wrappers named below.

Do not traverse the archive or bulk figure trees.
Resolve the exact run directories through the inventory and then test only the
named paths and expected hourly files.

## Clean-checkout and preflight contract

Use clean worktrees at `SOURCE_REF` and `BRC_TOOLS_REF` if either existing checkout
is dirty or at a different commit.
Never reset, clean, stash, switch, or pull over an occupied checkout.
The committed Slurm wrappers accept `MANUSCRIPT_DIR`, `AIR_REPO`, and
`BRC_TOOLS_DIR` so jobs can use those clean worktrees.

Record `hostname -f`, UTC time, both full commits, remotes, worktree paths, and dirty
states before submission.
Verify the renderer CLI advertises `--output-dir`, `difference`, and
`heatdeficit_map`, and verify that the shared-axis profile script imports against
the pinned `brc-tools` checkout.
Use the CHPC Python environment only after checking it exists.

The source commit must contain these exact hashes:

| File | Required SHA-256 |
|---|---|
| `verification/config/figures/pelican2013.toml` | `ad9d933854fc7067260f1bb398e25aff2e7c286b9df8135a64c9dfa1cf8d2fd7` |
| `verification/config/figures/pelican2013_terrain_d03.toml` | `d723f6061edbf28ad9b2ee85281e85f0f3806a67471863a4b3894543479f3262` |
| `verification/slurm/pelican_figures.slurm` | `667379f82535c2acea98df244907f210c8f8bb894ab43cc71e0bf4e131cdc5e0` |
| `verification/scripts/plot_wrf_vs_obs_feb0102.py` | `931b944e10d1130ebdfae76a9791b78765dcea65917a4452ddddb838200ee9ec` |
| `verification/scripts/plot_wrf_transect_locator.py` | `3687eb9f034266e7846c89eaa5fa87ddbb73e10e3b60f647c2c8882eae3a768c` |
| `verification/scripts/plot_wrf_profile_spinup.py` | `345aa72d3835ff48c860efaf97272187b43f5b8a6dff60ebbe7a8e9859403c87` |
| `verification/scripts/analyze_radiation_response.py` | `e5c349d6232972362c47d92646fd91cb2d7fb761a9dd846592297fbdfe3efe39` |
| `verification/slurm/run_radiation_response.slurm` | `75972327b5dda695c6a5a0bfdc6a683d7a09751d34b728ba6c35080228b0d834` |

The line-free overlay also requires these immutable inputs:

| Input | Required SHA-256 |
|---|---|
| frozen observation cache `obs_basin_2013_feb0102.parquet` | `733181afd09db704aafe2c148cf19b41bca83e8b020b9839768d7618217eeb64` |
| `verification/data/wrf_gfs_2way_d02_per_station.csv` | `fefff6a5b55ee8ef64265920d1f783d1fa1e469a2b79fd3ff9c8cc473142dfe7` |
| `verification/data/wrf_nam_2way_d02_per_station.csv` | `2d5ae81963e8d0b17f5b4ec464af5cd3db8af30a34625d529d529f214201fb53` |
| `verification/data/wrf_nam_1way_d02_per_station.csv` | `3327de6a6b81a5fa5141190def2cadf05f97b7922cb1c5b4eaadb9753941a235` |

The registered frozen cache path is
`/scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/obs_basin_2013_feb0102.parquet`.
If it is absent or its hash differs, stop that product group; do not substitute a
network download, current observation pull, or synthetic cache.

Define task-scoped paths from the clean checkouts before submitting jobs:

```bash
export AIR_REPO=/absolute/path/to/clean/latex-jrl-mjd-mdpiair-2026
export BRC_TOOLS_DIR=/absolute/path/to/clean/brc-tools
export AIR_PYTHON=/uufs/chpc.utah.edu/common/home/u0737349/software/pkg/miniforge3/envs/brc-tools-2026/bin/python
export PELICAN_PYTHON="$AIR_PYTHON"
export REVIEW_ROOT="/scratch/general/vast/$USER/latex_jrl_20260714_v3_figure_review"
mkdir -p "$REVIEW_ROOT"/{overlay,d02,d03,profiles,locator,radiation}
cd "$AIR_REPO"
```

All Python analysis and rendering runs on an allocation or batch node.
Login-node work is limited to Git, hashes of small repository files, explicit path
tests, job submission, and scheduler monitoring.

## Product 1: line-free bulk-theta overlays

Run both commands on a compute node, writing to `$REVIEW_ROOT/overlay` first:

```bash
env PYTHONPATH="$BRC_TOOLS_DIR" \
  "$AIR_PYTHON" verification/scripts/plot_wrf_vs_obs_feb0102.py \
  --wrf verification/data/wrf_gfs_2way_d02_per_station.csv \
        verification/data/wrf_nam_2way_d02_per_station.csv \
  --labels 'GFS two-way' 'NAM two-way' \
  --obs /scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/obs_basin_2013_feb0102.parquet \
  --min-time 2013-02-02T14:00 --max-time 2013-02-02T18:00 \
  --out-suffix _gfs2way_vs_nam2way_d02_14to18 \
  --out-dir "$REVIEW_ROOT/overlay"

env PYTHONPATH="$BRC_TOOLS_DIR" \
  "$AIR_PYTHON" verification/scripts/plot_wrf_vs_obs_feb0102.py \
  --wrf verification/data/wrf_nam_1way_d02_per_station.csv \
        verification/data/wrf_nam_2way_d02_per_station.csv \
  --labels 'NAM one-way' 'NAM two-way' \
  --obs /scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/obs_basin_2013_feb0102.parquet \
  --min-time 2013-02-02T14:00 --max-time 2013-02-02T18:00 \
  --out-suffix _nam1way_vs_nam2way_d02_14to18 \
  --out-dir "$REVIEW_ROOT/overlay"
```

The script also writes temperature-series companions.
Hash and inspect them in scratch, but do not copy them into Git in this dispatch.
For both bulk-theta plots, confirm visually that there is no horizontal 8 K reference
line or 8 K classification annotation, that the two-site quantity is labelled as
bench minus floor, and that all curves and legends are legible.

After those checks, replace only these candidate files:

| Scratch source under `overlay/` | Repository destination |
|---|---|
| `wrf_inversion_index_feb0102_gfs2way_vs_nam2way_d02_14to18.png` | `verification/figures/candidates/wrf_inversion_index_feb0102_gfs2way_vs_nam2way_d02_14to18.png` |
| same stem, `.pdf` | `verification/figures/candidates/wrf_inversion_index_feb0102_gfs2way_vs_nam2way_d02_14to18.pdf` |
| `wrf_inversion_index_feb0102_nam1way_vs_nam2way_d02_14to18.png` | `verification/figures/candidates/wrf_inversion_index_feb0102_nam1way_vs_nam2way_d02_14to18.png` |
| same stem, `.pdf` | `verification/figures/candidates/wrf_inversion_index_feb0102_nam1way_vs_nam2way_d02_14to18.pdf` |

Only if the X6/X5 PDF passes every check, copy that exact PDF to
`figures/wrf_inversion_index_feb0102_gfs2way_vs_nam2way_d02_14to18.pdf`, change its
row in `figures/MANIFEST.md` from `withheld` to `promoted`, and update the matching
row in `verification/figures/manifest.csv` with the new generator commit, host/job,
hashes, and visual-review date.
The X3/X5 feedback plot stays a candidate even if it passes.

## Products 2--4: terrain maps, sections, and 12/13 UTC profiles

Submit two separate renderer jobs so d02 and d03 failures and provenance remain
separable:

```bash
MANUSCRIPT_DIR="$AIR_REPO" \
BRC_TOOLS_DIR="$BRC_TOOLS_DIR" \
PELICAN_PYTHON="$PELICAN_PYTHON" \
PELICAN_FIGURE_CONFIG="$AIR_REPO/verification/config/figures/pelican2013.toml" \
sbatch verification/slurm/pelican_figures.slurm \
  --case nam_terrain3s,nam_terrain5m \
  --figure heatdeficit_map \
  --time 16 \
  --output-dir "$REVIEW_ROOT/d02"

MANUSCRIPT_DIR="$AIR_REPO" \
BRC_TOOLS_DIR="$BRC_TOOLS_DIR" \
PELICAN_PYTHON="$PELICAN_PYTHON" \
PELICAN_FIGURE_CONFIG="$AIR_REPO/verification/config/figures/pelican2013_terrain_d03.toml" \
sbatch verification/slurm/pelican_figures.slurm \
  --case fine,coarse \
  --figure difference,heatdeficit_map \
  --time 16 \
  --output-dir "$REVIEW_ROOT/d03"

```

Run the two-time profile renderer on a compute node or allocation.
It pools both members and both hours before fixing the axes, which the generic
one-hour-at-a-time profile family cannot guarantee:

```bash
env PYTHONPATH="$BRC_TOOLS_DIR" \
  "$AIR_PYTHON" verification/scripts/plot_wrf_profile_spinup.py \
  --config verification/config/figures/pelican2013.toml \
  --run gfs=/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive/pelican2013_gfs_3_1_333m_75lev/full6h/run_20260630T181555Z \
  --run nam=/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive/pelican2013_nam_3_1_333m_75lev/full6h/run_20260626T163737Z \
  --valid 2013-02-02T12:00:00 2013-02-02T13:00:00 \
  --out-dir "$REVIEW_ROOT/profiles"
```

Monitor both Slurm jobs to terminal states and inspect both stdout and stderr.
Record the allocation/job used for the profile command.
The d02 and d03 maps must use X0 minus X4, 16 UTC, a 2200 m crest reference, and the
same fixed +/-1.6 MJ m-2 display scale.
The sections must be d03 X0 minus X4 potential-temperature differences on a common
+/-4 K scale.
The profiles must contain only X6 and X5, use identical axes, and show 12 and 13 UTC
as separate files.

After inspection, copy and rename only:

| Scratch source | Repository destination |
|---|---|
| `d02/heatdeficit_map/heatdeficit_terrain-3arcsec-5arcmin_16z.png` | `figures-draft/heatdeficit_terrain-3arcsec-5arcmin_16z.png` |
| `d03/heatdeficit_map/heatdeficit_terrain-3arcsec-5arcmin_16z.png` | `figures-draft/heatdeficit_terrain-3arcsec-5arcmin_d03_16z.png` |
| `d03/diff_terrain_res/section_ns_terrain-3arcsec-5arcmin_16z.png` | `figures-draft/section_ns_terrain-3arcsec-5arcmin_d03_16z.png` |
| `d03/diff_terrain_res/section_ew_terrain-3arcsec-5arcmin_16z.png` | `figures-draft/section_ew_terrain-3arcsec-5arcmin_d03_16z.png` |
| `profiles/theta_profiles_horsepool_gfs_nam_12z.png` | `figures-draft/theta_profiles_horsepool_gfs_nam_12z.png` |
| `profiles/theta_profiles_horsepool_gfs_nam_13z.png` | `figures-draft/theta_profiles_horsepool_gfs_nam_13z.png` |

The d03 job also produces
`d03/diff_terrain_res/theta2m_terrain-3arcsec-5arcmin_16z.png` and per-run
heat-deficit maps.
Hash and inspect those as reserve/scratch products, but do not copy, register, or
promote them in this dispatch.
The shared-axis profile script also writes two PDF companions; hash and inspect them
in scratch, but copy only the PNGs wired into `_manuscript_v3.tex`.

## Product 5: Figure 1(a) locator rerender

Run on a compute node from `SOURCE_REF`:

```bash
env PYTHONPATH="$BRC_TOOLS_DIR" \
  "$AIR_PYTHON" verification/scripts/plot_wrf_transect_locator.py \
  --wrf-dir /uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive/pelican2013_nam_3_1_333m_75lev_oneway_terrain3s/full6h/run_20260708T021809Z \
  --d02-glob 'wrfout_d02_2013-02-02_12:00:00' \
  --d03-glob 'wrfout_d03_2013-02-02_12:00:00' \
  --out-dir "$REVIEW_ROOT/locator"
```

Inspect the PNG and PDF at useful resolution.
Panel (a) must have no latitude/longitude ticks, no obsolete transect lines, legible
station labels, a north arrow, a 40 km scale, and clear d02/d03 context.
The archived `figures-draft/nested_domains.png` is already Figure 1(b) and is not
regenerated here.
Replace only
`verification/figures/candidates/wrf_transect_locator_d02_d03.{png,pdf}` and update
its manifest row and archive record.

If the staged road/river basemap cache is unavailable, record that fact; do not
download from a compute node or improvise unverified geographic features.

## Product 6: slope-radiation restyle only

Submit the existing ANA-18 analysis through its override-safe wrapper:

```bash
AIR_REPO="$AIR_REPO" \
BRC_TOOLS_DIR="$BRC_TOOLS_DIR" \
AIR_PYTHON="$AIR_PYTHON" \
ANA18R_OUT_DIR="$REVIEW_ROOT/radiation" \
sbatch verification/slurm/run_radiation_response.slurm
```

Monitor the job to a terminal state and compare the new summary and criteria CSVs
against the committed versions.
Numerical differences are a stop condition; this is a style rerender, not a gate
rerun.
Confirm visually that the two maps have no coordinate ticks and that all four panels,
color bars, labels, and the measurement-limited interpretation remain legible.
Then replace only
`verification/figures/candidates/wrf_radiation_response_cmp07_d02.{png,pdf}`.
Do not change the ANA-18 failed-gate disposition, its claim, or its criteria.

## Durable record and allowed writes

Before copying any artifact, hash every scratch output and keep the scratch manifest.
Create `verification/provenance/v3-figure-review-20260714.json` containing:

- `SOURCE_REF`, `BRC_TOOLS_REF`, hosts, worktree paths, and dirty states;
- exact commands, environment paths, Slurm job IDs, terminal states, stdout/stderr;
- exact WRF inputs or registered run IDs and the frozen observation-cache hash;
- script, wrapper, and configuration hashes;
- every scratch-output hash, the selected-copy mapping, and destination hash; and
- a per-file visual-review result and any rejected/reserve output.

Repository writes are limited to:

- the four line-free candidate overlay files named above;
- the conditionally restored X6/X5 PDF under `figures/`;
- the six selected `figures-draft/` PNG files named above;
- `verification/figures/candidates/wrf_transect_locator_d02_d03.{png,pdf}`;
- `verification/figures/candidates/wrf_radiation_response_cmp07_d02.{png,pdf}`;
- `figures-draft/HARVEST.md`;
- `verification/figures/manifest.csv`;
- `verification/figures/archive-inventory.md`;
- `figures/MANIFEST.md` only for the conditional X6/X5 re-promotion;
- `verification/provenance/v3-figure-review-20260714.json`; and
- this handoff's final return-record section.

Do not edit a manuscript, `paperpile.bib`, a run/comparison inventory, a claim/gate
record, or any other figure.
Do not commit logs, caches, task-scoped scratch scripts, or unselected outputs.

## Validation and return

After selected files and records are updated:

1. run `git diff --check`;
2. run `make check`, `make rewrite-check`, `make v3-check`, and `make smoke` in the
   documented environment;
3. rebuild `_manuscript_v3.pdf` with `make v3-pdf` and inspect every page
   containing a changed figure at useful resolution;
4. confirm `main.tex` remains unchanged unless the conditional promoted PDF is
   restored by its existing filename (the TeX source still stays unchanged);
5. confirm no build product or scratch artifact is staged; and
6. commit with John's identity and
   `Co-Authored-By: Codex <noreply@openai.com>`, then push
   `jrl/chpc-20260714-v3-figure-review`.

End the CHPC report with all job states and log paths, copied/rejected output hashes,
visual findings, validation results, files changed, full pushed commit, unresolved
items, and the smallest safe next action.

## Return record

Completed on CHPC for `REQUEST_ID=20260714-v3-figure-review` from
`SOURCE_REF=29854aac5fe4a2acbcecb705591c064197b3a8c3` with
`BRC_TOOLS_REF=69ddbe07af2e38e5e2d4f12f681bb360ff506a1a`.
The return branch is `jrl/chpc-20260714-v3-figure-review`.

All four jobs completed with `ExitCode=0:0` on `notch392`:

- `13952692`, d03 CMP11 maps and sections:
  `/scratch/general/vast/u0737349/pelican_figures_13952692.{out,err}`;
- `13952693`, ANA-18 radiation style rerender:
  `/scratch/general/vast/u0737349/latex_jrl_ana18r_13952693.{out,err}`;
- `13952694`, d02 CMP11 heat-deficit maps:
  `/scratch/general/vast/u0737349/pelican_figures_13952694.{out,err}`; and
- `13952705`, overlays, profiles, and locator:
  `/scratch/general/vast/u0737349/latex_jrl_v3_aux_13952705.{out,err}`.

All stderr files are empty.
The 30-output scratch manifest is
`/scratch/general/vast/u0737349/latex_jrl_20260714_v3_figure_review/scratch_output_sha256.txt`
with SHA-256
`5bfd3175e1e73ee2624b4567f8f2e2a2d5e10fc460030575fedbf194e29a3543`.
Exact selected-copy and reserve-output hashes, job-log hashes, commands, run inputs,
and per-file visual findings are recorded in
`verification/provenance/v3-figure-review-20260714.json`.

The line-free X6/X5 bulk-theta overlay passed conditional re-promotion; its PDF hash
is `1a8d5c45953ed08d0db5b9d9c024cf46035a4db09252f0ef888f0809d2ce5c31`.
The X3/X5 overlay remains a candidate.
Temperature companions, per-run maps, and profile PDF companions passed visual
review but remain scratch reserves; no numerical product was rejected.
The ANA-18 summary and criteria CSVs were byte-identical to the committed records,
so its failed-gate disposition remains unchanged.

`git diff --check`, `make check`, `make rewrite-check`, `make v3-check`, `make smoke`,
and `make v3-pdf` passed in the documented CHPC environment.
Pages 3, 12, 13, 16, 17, and 22 of the rebuilt 23-page `_manuscript_v3.pdf` passed
150-dpi inspection.
No manuscript source, bibliography, run/comparison inventory, claim/gate record,
build product, task script, or log is included in the return batch.
There are no unresolved items within this bounded packet.
The smallest safe next action is writing-host review of the pushed return branch
before merge or manuscript promotion.
