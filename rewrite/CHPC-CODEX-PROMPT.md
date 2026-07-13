# Copy-ready prompt for CHPC Codex

Give the fenced prompt below to a fresh Codex session on CHPC.
It is intentionally independent of the starting directory and keeps manuscript prose on the writing host.

```text
You are the CHPC-side evidence and figure worker for the private MDPI Air manuscript repository about WRF meteorology during the 2 February 2013 Uinta Basin winter-ozone episode.

Goal: close the CHPC-only methods, observation-provenance, and figure gaps identified by the blank-slate rewrite, without rewriting manuscript prose or broadening the scientific claims.

Start safely from any directory:

1. Run `hostname -f`, `pwd`, and path tests before reading data.
2. Locate the manuscript checkout by testing likely paths under `$HOME` and the Lawson group project space for a directory named `latex-jrl-mjd-mdpiair-2026`.
   Use bounded metadata searches; do not recursively scan the full WRF archive or bulk image trees.
   Also locate readable `brc-wrf` and `brc-tools` checkouts, and record their branches, commits, and dirty state before using their cases, docs, or renderers.
3. In the checkout, run `git status --short --branch`, `git remote -v`, and `git log -3 --oneline`.
4. Fetch `origin` if available.
   Base the work on `origin/jrl/evidence-gated-human-draft` and use a new branch named `jrl/chpc-rewrite-evidence`.
   If the checkout is dirty, preserve all existing work, report the overlap, and use a clean worktree or stop before modifying overlapping files.
5. Read, in order:
   - `AGENTS.md`
   - `README.md`
   - `ROADMAP.md`
   - `rewrite/README.md`
   - `rewrite/blueprint.md`
   - `notes/manuscript-audit-2026-07-13.md`
   - the relevant rows only in `notes/claim-evidence-ledger.md`
   - `verification/provenance/run-inventory.csv`
   - `verification/provenance/comparison-inventory.csv`
   - `verification/figures/chpc-figure-inventory-2026-07-10.md`
   - `verification/figures/manifest.csv`
   - `figures/MANIFEST.md`
6. Do not assume `~/reviews` exists on CHPC.
   Do not open raw PDFs, candidate image trees, or unrelated WRF runs unless a task below names the need.

The frozen core is X6 (GFS two-way), X10 (GFS one-way), X5 (NAM two-way), and X3 (NAM one-way), evaluated on d02 from 14--18 UTC.
Resolve every path through the run inventory.
Never infer identity from filenames, and never identify `trang_ref` as the literal Tran et al. (2018) run.

Work in this priority order.

TASK A — close exact WRF Methods metadata

- Locate the immutable as-run namelists, WRF headers, WPS/geogrid records, metgrid manifests, and control packets for X3/X5/X6/X10.
- Verify, rather than infer:
  - map projection and true/standard longitudes and latitudes;
  - domain dimensions, centers, parent ratios, and parent starts;
  - time step, history cadence, boundary-update interval, and run start/end;
  - WRF/WPS versions and any source commit recorded by the run;
  - static-geography dataset names/resolutions and land-use source;
  - snow/SWE/albedo initialization source and whether any fields were overwritten;
  - exact GFS and NAM product identifiers, cycles, files, metgrid levels, and hashes;
  - feedback and FDDA state for each domain.
- Record each fact with exact source path, command, and SHA-256 or header fingerprint.
- Add confirmed facts to the canonical run inventory or a narrowly named provenance record before touching any prose-facing note.
- If evidence conflicts, record both sources and leave the field unresolved.

TASK B — close observation provenance

- Locate the exact observation cache with SHA-256 `733181afd09db704aafe2c148cf19b41bca83e8b020b9839768d7618217eeb64`, plus its pull script, job log, request record, or sidecars.
- Recover the exact API request window, station list, variables, units, token-free endpoint form, QC flags/parameters, and any completeness filters.
- Record station ownership/network, sensor identity and heights where present, provider QC, missing-data handling, access date, public-access route, and license/terms source.
- Do not guess metadata that are absent from the archive.
  Create a compact unresolved list that names the provider or human question needed.
- Update `verification/data/manifest.csv`, the claim ledger, or a focused provenance note before proposing manuscript wording.

TASK C — regenerate the held bulk-theta figure correctly

- Use the exact real observation cache and exact X6/X5 reduced inputs already named in `verification/figures/manifest.csv`.
- Use the current `verification/scripts/plot_wrf_vs_obs_feb0102.py`.
- Reproduce the registered command and environment, changing only what the current committed generator already changes.
- Regenerate PNG and vector PDF for `wrf_inversion_index_feb0102_gfs2way_vs_nam2way_d02_14to18`.
- Confirm visually and with text extraction if available that the guide reads `8 K literature reference`, not `8 K CAP threshold`.
- Keep the caption/manifest interpretation explicit: USU03 minus USU07 is a horizontally separated bulk potential-temperature contrast, not a measured inversion depth or physical classification threshold.
- Compute hashes, record the exact environment, source commit, command, host, and Slurm job if used, replace the promoted PDF only after the real-data and visual checks pass, and update both figure manifests atomically.
- Never promote synthetic output.

TASK D — produce decision-grade diagnostics, not a figure dump

1. Common-AGL cross-sections:
   - Using exact X6/X5 and X10/X3 paths, render matched GFS-minus-NAM potential-temperature difference sections at 14, 16, and 18 UTC on the same common-AGL grid and symmetric scale.
   - Prefer a compact multipanel output or a manifest-registered small set.
   - Register it as diagnostic or reviewer reserve, not promoted.
   - State whether the product response is shallow/basin-confined only if the panels and interpolation checks support that description.

2. Domain/station locator:
   - Reproduce or audit the current d02/d03 locator with all evaluation stations, domain boundaries, terrain, and the reason d02 is the common sample.
   - Record whether it materially improves Methods comprehension.
   - Do not promote it automatically.

3. Heat-deficit maintenance hypothesis:
   - Audit the productized `heatdeficit_map` family and the existing time series using exact X6/X5/X10/X3 inputs.
   - Define the crest/reference surface, integration domain, units, masks, and post-spin-up window in a reproducible record.
   - Quantify the 13--18 UTC trajectories and test sensitivity to reasonable basin-boundary or threshold choices.
   - Check the exploratory statement “GFS fails to maintain a cold pool” against the productized outputs; do not copy it into the ledger unless the definition, trajectory, and sensitivity checks survive.
   - Keep the single-point phase portrait and threshold-dependent reservoir prototype out of manuscript evidence unless separately productized and validated.

4. Initial versus boundary diagnosis:
   - Inventory available `met_em`, `wrfinput`, `wrfbdy`, and early wrfout fields for the four core runs.
   - Produce a compact comparison of lower-tropospheric temperature, moisture, and wind at initialization and through the retained hours.
   - The purpose is to expose what can and cannot separate inherited initial state from boundary evolution.
   - Do not claim causal separation from a visual difference alone.

Do not submit a new WRF integration for this handoff.
Use existing immutable outputs and plotting/metadata jobs only.
If a new model run is genuinely required, write the exact proposed experiment, storage estimate, Slurm command, and decision it would resolve, then stop before submission.

Validation and handoff requirements:

- Facts enter the run inventory, data manifest, figure manifest, or claim ledger before prose-facing summaries.
- Preserve the five-hour, fixed-column, deterministic scope.
- Keep controlled comparisons, heterogeneous context, and literature context separate.
- Record exact commands, source commits, hashes, hostnames, job IDs, input paths, and output paths.
- Run the relevant synthetic smoke tests in an environment with the required packages.
- Run `git diff --check`.
- Inspect every regenerated figure; do not rely on successful rendering alone.
- Write a concise `verification/provenance/chpc-rewrite-evidence-2026-07.md` handoff containing:
  - confirmed Methods facts and their sources;
  - observation metadata confirmed and still missing;
  - each regenerated/diagnostic figure and its status;
  - whether the heat-deficit maintenance hypothesis survived;
  - what remains impossible with current files;
  - exact next commands, if any.
- Commit one verified concern at a time with John Lawson's Git identity and
  `Co-Authored-By: Codex <noreply@openai.com>`.
- Push `jrl/chpc-rewrite-evidence`.

At the end, report:

1. branch and commit hashes pushed;
2. files changed;
3. methods facts newly confirmed;
4. figures regenerated or kept diagnostic, with hashes and job IDs;
5. unresolved questions requiring John, Michael, the provider, or a new run;
6. the smallest safe writing-host integration sequence.
```
