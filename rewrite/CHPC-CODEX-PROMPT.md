# Copy-ready prompt for CHPC Codex

Give the fenced prompt below to a fresh Codex session on CHPC.
It is intentionally independent of the starting directory and keeps manuscript prose on the writing host.

```text
You are the CHPC-side evidence and figure worker for the private MDPI Air manuscript repository about WRF meteorology during the 2 February 2013 Uinta Basin winter-ozone episode.

Goal: close CHPC-only methods and observation-provenance gaps and evaluate the broader X0--X10 result/figure matrix identified by the writing-host expansion handoff. Do not rewrite manuscript prose, and do not promote a scientific claim merely because a figure exists.

Start safely from any directory:

1. Run `hostname -f`, `pwd`, and path tests before reading data.
2. Locate the manuscript checkout by testing likely paths under `$HOME` and the Lawson group project space for a directory named `latex-jrl-mjd-mdpiair-2026`.
   Use bounded metadata searches; do not recursively scan the full WRF archive or bulk image trees.
   Also locate readable `brc-wrf` and `brc-tools` checkouts, and record their branches, commits, and dirty state before using their cases, docs, or renderers.
3. In the checkout, run `git status --short --branch`, `git remote -v`, and `git log -3 --oneline`.
4. Fetch `origin` if available.
   Base the work on `origin/jrl/evidence-gated-human-draft` and use a new branch named `jrl/chpc-expanded-results`.
   If the checkout is dirty, preserve all existing work, report the overlap, and use a clean worktree or stop before modifying overlapping files.
5. Read, in order:
   - `AGENTS.md`
   - `README.md`
   - `ROADMAP.md`
   - `rewrite/README.md`
   - `rewrite/RESULTS-EXPANSION-HANDOFF.md`
   - `rewrite/blueprint.md`
   - `notes/manuscript-audit-2026-07-13.md`
   - the relevant rows only in `notes/claim-evidence-ledger.md`
   - `verification/provenance/run-inventory.csv`
   - `verification/provenance/comparison-inventory.csv`
   - `verification/figures/archive-inventory.md`
   - `verification/figures/MANUSCRIPT-EXPANSION-HANDOFF.md`
   - `verification/figures/chpc-figure-inventory-2026-07-10.md`
   - `verification/figures/manifest.csv`
   - `figures/MANIFEST.md`
6. Do not assume `~/reviews` exists on CHPC.
   Do not open raw PDFs, candidate image trees, or unrelated WRF runs unless a task below names the need.

The minimum confirmed core is X6 (GFS two-way), X10 (GFS one-way), X5 (NAM two-way), and X3 (NAM one-way), evaluated on d02 from 14--18 UTC.
It is not the scope of the paper.
The expansion candidates include X1-X0 slope/shading, X2-X1 PBL/surface layer, X3-X0/X3-X4/X0-X4 terrain, X9-X0 fine-terrain feedback, and the productized heat-deficit and spatial/vertical families.
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

TASK E — evaluate the controlled non-core matrix from existing outputs

Start from the current `verification/figures/archive-inventory.md` rather than the older
figure-strategy counts. Verify by bounded metadata checks that X9, X9-X0, the cleaned
terrain families, and `heatdeficit_map` products still exist; do not rerender complete
sets simply to prove their presence.

1. Slope/shading, X1-X0:
   - Sample matched `SWDOWN`, `GLW`, `TSK`, T2, common-AGL stability, and wind through time.
   - Stratify by a predeclared slope/aspect or shaded/exposed definition so a local response
     is not erased by a domain mean.
   - Test a physical radiation/energy question; do not treat close aggregate bias as a
     proven null.

2. PBL/surface layer, X2-X1:
   - Recompute common-AGL theta, temperature, and wind profiles plus surface fluxes.
   - Show native PBLH only with an explicit scheme caveat, and never treat absent YSU
     `TKE_PBL` as zero.
   - Reconcile the 18.49 versus 17.18 K exploratory bulk-theta contrast and the inherited
     "small below 700 m" description against an explicitly defined profile metric.

3. Terrain, X3-X0, X3-X4, and X0-X4:
   - Resolve or clearly retain the X4 archive-path lineage caveat before quantitative use.
   - Separate terrain/elevation displacement from pressure skill.
   - Test rim, slope/tributary, floor, and heat-deficit geometry with one common set of
     diagnostics and scales.
   - Do not call source-terrain spacing the WRF model-grid spacing.

4. Fine-terrain feedback, X9-X0:
   - Treat this as a robustness comparison, not the organizing thesis.
   - Recompute the same matched surface/common-AGL quantities used for the default-terrain
     feedback result and compare spatial heat-deficit response on an honest small-signal
     scale.

For each pair, write a compact result record containing the exact question, held-common
fields, residual caveats, source paths and hashes, command, numerical summary, visual
finding, falsifier, and recommended status: confirmed, provisional, diagnostic, or
rejected. Register candidate outputs but do not promote them without a writing-host
editorial decision.

Do not submit a new WRF integration for this handoff.
Use existing immutable outputs and plotting/metadata jobs only.
If a new model run is genuinely required, write the exact proposed experiment, storage estimate, Slurm command, and decision it would resolve, then stop before submission.

Validation and handoff requirements:

- Facts enter the run inventory, data manifest, figure manifest, or claim ledger before prose-facing summaries.
- Preserve the five-hour, fixed-column, deterministic scope for the confirmed factorial;
  define and record the matched domain, sample, and window separately for every added pair.
- Keep controlled comparisons, heterogeneous context, and literature context separate.
- Record exact commands, source commits, hashes, hostnames, job IDs, input paths, and output paths.
- Run the relevant synthetic smoke tests in an environment with the required packages.
- Run `git diff --check`.
- Inspect every regenerated figure; do not rely on successful rendering alone.
- Write a concise `verification/provenance/chpc-expanded-results-evidence-2026-07.md` handoff containing:
  - confirmed Methods facts and their sources;
  - observation metadata confirmed and still missing;
  - each regenerated/diagnostic figure and its status;
  - whether the heat-deficit maintenance hypothesis survived;
  - what CMP06--CMP11 support after matched analysis, including small or null findings;
  - what remains impossible with current files;
  - exact next commands, if any.
- Commit one verified concern at a time with John Lawson's Git identity and
  `Co-Authored-By: Codex <noreply@openai.com>`.
- Push `jrl/chpc-expanded-results`.

At the end, report:

1. branch and commit hashes pushed;
2. files changed;
3. methods facts newly confirmed;
4. figures regenerated or kept diagnostic, with hashes and job IDs;
5. unresolved questions requiring John, Michael, the provider, or a new run;
6. the smallest safe writing-host integration sequence.
```
