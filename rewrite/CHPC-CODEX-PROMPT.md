# CHPC Codex handoff

This is the stable bridge from the writing checkout to a fresh Codex session on
CHPC. It replaces the former one-shot July task list and its hard-coded source
branch. Current scientific priorities live in
`rewrite/HYBRID-ARCHITECTURE-HANDOFF.md`; this file owns only CHPC bootstrap,
execution, and return conventions.

The active multi-product v3 figure dispatch is factored into
`rewrite/CHPC-V3-FIGURE-RECOMPUTE-HANDOFF.md`.
Use its immutable source commit and exact boundary after reading this bootstrap.
The ANA-16 packet retained at the end of this file is a completed historical
record and must not be copied or rerun.

Use one bounded request per dispatch:

- `FIGURE`: regenerate or audit a named figure from existing data;
- `LOOKUP`: answer a named archive, run, configuration, or provenance question;
- `GATE`: close one named Architecture C evidence gate from existing outputs.

No mode authorizes a new WRF integration, manuscript edits, or figure promotion.
Those require a separate writing-host decision.

An executable dispatch must contain one completed task packet.  The templates alone
are not a plan and authorize no archive scan, analysis, rendering, or write.  When
John asks for critique plus execution in an already clean CHPC checkout, the critique
may add the packet on a new topic branch and use the pre-edit `HEAD` as `SOURCE_REF`.
That planning-only edit does not make the scientific inputs mutable: record both the
starting commit and the final evidence commit, and stop if any pre-existing dirty file
overlaps the packet's allowed writes.

## Before dispatching from the writing host

1. Commit and push every file the CHPC task needs. Give the CHPC session an
   immutable commit when possible; never tell it to use an unspecified “latest”
   branch. If the needed state exists only in a dirty checkout, it has not been
   handed off.
2. Copy the bootstrap prompt below into the CHPC session.
3. Append one completed task packet from the templates at the end of this file.
   `SOURCE_REF` is required. Delete irrelevant fields rather than adding a broad
   reading list.

The writing branch and the CHPC work branch are request data, not permanent
facts in this document.

## Copy-ready bootstrap prompt

```text
You are the CHPC-side evidence and figure worker for the private MDPI Air
manuscript repository about WRF meteorology during the 2 February 2013 Uinta
Basin winter-ozone episode.

The task packet appended to this prompt is your complete assignment. Execute one
bounded FIGURE, LOOKUP, or GATE request. Do not revive an older task list from
repository history and do not expand into adjacent experiments merely because
their files are available.

Bootstrap safely:

1. Run hostname -f, date -u, pwd, and git status --short --branch if already in a
   checkout.
2. Locate latex-jrl-mjd-mdpiair-2026 with explicit path tests or a bounded search
   under likely checkout roots. Do not search the WRF archive, scratch, or bulk
   image trees merely to find the Git repository.
3. Treat SOURCE_REF in the task packet as mandatory. Fetch only enough to resolve
   it and record the exact commit. Never switch to main or to a branch named in
   this document by default. If SOURCE_REF is absent, unavailable, or does not
   contain the referenced handoff files, stop and report that handoff failure.
4. Preserve every dirty checkout. If it overlaps the request, use a clean Git
   worktree at SOURCE_REF or stop; never reset, clean, stash, or overwrite someone
   else's work.
5. Record branch, commit, remotes, and dirty state for this repository. Locate and
   record brc-tools only for a renderer/analysis task, and brc-wrf only for a
   run/control-packet lookup. Do not pull or switch those repositories blindly.
6. In the selected manuscript checkout, read AGENTS.md completely, then README.md
   and ROADMAP.md. Take the CHPC route by reading this file, then open only the
   mode-specific sources named below and the rows needed by the task.

Repository roles and authority:

- This repository owns manuscript-specific run/comparison identity, evidence
  records, figure configurations, admission state, and small derived products.
- brc-tools owns reusable plotting and analysis code. Record its exact commit and
  dirty state whenever it generates an artifact.
- brc-wrf owns runnable cases and control packets. Large WRF, NWP, observation,
  and bulk figure data remain outside Git.
- Run and comparison inventories govern identity and design. The archive
  inventory proves only existence. Figure manifests govern tracking/admission.
  The claim ledger plus exact artifacts governs scientific claims.
- Architecture C is frozen. C1/C2 are anchors; C3--C6 and supplement C2 remain
  gated. X6/X10/X5/X3 are the confirmed floor, not the full scope.
- Never infer a run from a filename. Never identify trang_ref as the literal Tran
  et al. (2018) production run. Keep controlled comparisons, heterogeneous
  context, and literature context separate.
- Do not edit main.tex or _manuscript_test.tex, promote into figures/, or change
  figures/MANIFEST.md unless a later, explicit writing-host request authorizes
  that exact action.

CHPC operating boundary:

- Login node: Git work, explicit path tests, small-file metadata, bounded rclone
  listings, job submission, and scheduler monitoring.
- Allocation or batch job: recursive shared-filesystem scans, NetCDF header/data
  reads, heavy hashing, analysis, and rendering.
- Keep generated bulk output in archive or task-scoped scratch. Do not commit raw
  WRF output, private archive listings, caches, logs, or bulk figure trees.
- Validate tool and path availability instead of assuming the host matches an old
  job record. In particular, inspect the committed Slurm wrapper before using its
  Python, checkout, archive, account, or partition paths.

MODE=FIGURE

1. Resolve the named figure ID or comparison through only the relevant rows of:
   verification/figures/manifest.csv,
   verification/provenance/run-inventory.csv,
   verification/provenance/comparison-inventory.csv, and
   verification/figures/archive-inventory.md.
2. For a brc-tools full-figure family, read
   verification/config/figures/README.md, the selected TOML, and
   verification/slurm/pelican_figures.slurm. For a manuscript-specific figure,
   use its registered generator and exact command/provenance record instead.
3. Verify exact inputs, domains, stations, window, configuration hash, generator
   commit, environment, and output destination before submitting anything.
   Reproduction means those fields match; --skip-existing proves only reuse, not
   regeneration with current code.
4. Submit the narrowest existing-data job that answers the request. Supported
   entry-point patterns include:

       sbatch verification/slurm/pelican_figures.slurm \
         --case <config-key> --figure <family> --time <UTC-list>

       PELICAN_FIGURE_CONFIG=/absolute/path/to/config.toml \
         sbatch verification/slurm/pelican_figures.slurm <narrow selectors>

       sbatch verification/slurm/run_retention_analysis.slurm

   Use the retention wrapper only for its registered four-run product. Do not
   substitute it for a different comparison. If a wrapper path or environment is
   stale, report it and make only a task-authorized narrow repair.
5. Do not overwrite an accepted or promoted artifact unless the task packet names
   that replacement. Prefer task-scoped scratch/candidate output while validating
   a changed generator.
6. Monitor every submitted job through a terminal scheduler state, inspect stdout
   and stderr, verify expected artifacts, compute SHA-256 values, and visually
   inspect every requested raster/PDF at useful resolution. A successful exit
   code alone is not figure review.
7. Record the artifact as external, diagnostic, reserve, candidate, or regenerated
   as requested. Rendering does not create a claim or authorize promotion.

MODE=LOOKUP

1. Turn the question into explicit candidate relationships: run identity, storage
   location, configuration equivalence, output production, figure production,
   publication use, direct descent, design heritage, exclusion, or unknown. Do
   not collapse those into a vague “same dataset” statement.
2. Start with exact inventory rows and explicit paths. Use bounded login-node
   metadata first. Move find, ncdump -h, representative header fingerprints, or
   large local archive reads into an allocation.
3. Use verification/provenance/chpc_wrf_publication_inventory.sh and
   verification/provenance/CHPC-WRF-INVENTORY-HANDOFF.md only for a task that
   actually concerns the legacy Trang/OSIP/publication lineage. Do not rerun that
   broad inventory to answer a current X0--X10 path question.
4. Prefer small evidence: namelists, WPS records, control packets, file
   size/mtime manifests, TITLE, P_TOP, ZNW, exact dates, FDDA/OBS_DOMAIN fields,
   domain fingerprints, and hashes. Do not download or copy raw WRF output unless
   a later task explicitly proves that it is the smallest necessary step.
5. Return a structured evidence table with question/relationship, observed value,
   exact source path, exact command, hash or header fingerprint, status, and
   caveat. Conflicts remain unresolved and both sources stay visible.

MODE=GATE

1. Read rewrite/HYBRID-ARCHITECTURE-HANDOFF.md and only the selected Architecture C
   row plus fallback rules in
   rewrite/RESULTS-ARCHITECTURE-DECISION-PACKET.md.
2. Close exactly the gate named in the task packet. If the packet says “next
   gate,” follow the current order in the hybrid handoff; do not copy a priority
   order from this bootstrap.
3. Before reading bulk data, predeclare the primary metric, masks, units, retained
   window, sensitivity set, pass test, falsifier, and failed-gate disposition.  A
   falsified hypothesis is a completed gate result, not a reason to stop before
   recording it.  Stop only when identity, inputs, or metric validity cannot be
   established.
4. Use existing immutable output first. Record exact runs, comparison sign,
   domain, sample, window, inputs, command, numerical result, visual finding,
   falsifier, and small/null result.
5. Write facts first to the authoritative run/data/claim/figure record. Update
   rewrite/HYBRID-GATE-REVIEW.md only if ALLOWED_WRITES authorizes it. Do not fill
   a failed slot with a visually suggestive substitute.

Completion and return:

- Do not call a submitted job complete. Monitor it, inspect logs and artifacts,
  and report its terminal state. If an external limit truly prevents monitoring,
  give the exact job ID, log paths, current state, and resume commands.
- Read-only or scratch-only tasks make no Git commit. If ALLOWED_WRITES requests a
  durable repo record, use a branch jrl/chpc-<request-id> from SOURCE_REF, touch
  only named files, run git diff --check and relevant smoke/Make checks, commit one
  verified concern at a time with John's Git identity and
  Co-Authored-By: Codex <noreply@openai.com>, push, and report the remote branch
  and full commit.
- End with: request ID and mode; source ref and all repo commits/dirty states;
  commands and jobs with terminal states/logs; input and output paths plus hashes;
  visual review; evidence/findings with uncertainty; files changed; pushed branch
  and commits or “none”; unresolved items; and the smallest safe next action.
```

## Task packet templates

Fill one template and append it to the bootstrap prompt. A free-form question is
fine inside `QUESTION`, but the execution boundary must remain explicit.

### Regenerate or audit one figure

```text
REQUEST_ID: <YYYYMMDD-short-slug>
MODE: FIGURE
SOURCE_REF: <pushed branch plus full commit, or immutable full commit>
QUESTION: <what must be regenerated, compared, or visually checked?>
TARGETS: <figure_id, comparison ID, run IDs, family, times, and/or exact paths>
EXPECTED_OUTPUT: <scratch/archive paths and required PNG/PDF/table/report>
ALLOWED_WRITES: <scratch/archive only, or exact repository files>
COMPUTE: existing-data analysis/render jobs allowed; no WRF integration
RETURN: <paste report only, or commit and push jrl/chpc-REQUEST_ID>
STOP_IF: <identity, input, config, environment, or overwrite conditions>
```

### Look up one evidence question

```text
REQUEST_ID: <YYYYMMDD-short-slug>
MODE: LOOKUP
SOURCE_REF: <pushed branch plus full commit, or immutable full commit>
QUESTION: <one run/archive/configuration/publication/provenance question>
TARGETS: <known run IDs, candidate paths, archive prefixes, or files>
EXPECTED_OUTPUT: structured evidence table plus small fingerprints/manifests
ALLOWED_WRITES: read-only; task-scoped evidence bundle outside Git
COMPUTE: bounded allocation allowed for find/ncdump/header work; no model run
RETURN: paste findings, evidence-bundle path, and bundle SHA-256; no Git commit
STOP_IF: a broad scan, large transfer, credential disclosure, or destructive step
  would be required
```

### Close one selected hybrid gate

```text
REQUEST_ID: <YYYYMMDD-gate-id>
MODE: GATE
SOURCE_REF: <pushed branch plus full commit, or immutable full commit>
QUESTION: <one C3, C4, C5, C6, or supplement-C2 gate>
TARGETS: <ANA/CMP IDs, exact run IDs, domain, sample, window, and known artifacts>
PREDECLARED_TEST: <primary metric, masks, units, retained window, sensitivities,
  pass rule, and falsifier>
EXPECTED_OUTPUT: <analysis artifacts and a pass/fail/unresolved evidence record>
ALLOWED_WRITES: <exact authoritative records and HYBRID-GATE-REVIEW.md, or scratch only>
COMPUTE: existing-output analysis/render jobs allowed; no WRF integration
RETURN: <paste report, or commit and push jrl/chpc-REQUEST_ID>
FAIL_DISPOSITION: <main, supplement, reserve, or dropped result if the test fails>
STOP_IF: <unresolved identity, missing immutable input, invalid metric, unsafe write,
  or other condition that prevents a valid pass/fail result>
```

## Completed dispatch record: 20260713-c4-ana16 (do not rerun)

This packet was executed and is retained only as provenance for the completed gate.
Its result is recorded in `rewrite/HYBRID-GATE-REVIEW.md`.
It authorizes no current computation or repository write.

```text
REQUEST_ID: 20260713-c4-ana16
MODE: GATE
SOURCE_REF: bf79b507739afeb04499592d8b437e9e028683a1
QUESTION: Does a registered-footprint, definition-tested heat-deficit trajectory show that
  both GFS-driven members remain weaker than their feedback-matched NAM members after
  spin-up, and does it support the stronger claim that GFS loses more cold-pool heat
  deficit from 14 to 18 UTC?
TARGETS: ANA-16; CMP01 X6-X5 and CMP02 X10-X3; run IDs
  pelican_gfs_2way_default_ysu_20130202,
  pelican_nam_2way_default_ysu_20130202,
  pelican_gfs_1way_default_ysu_20130202, and
  pelican_nam_1way_default_ysu_20130202; d02; trajectory 13-18 UTC; retained
  decision window 14-18 UTC; exact archive paths from run-inventory.csv.
PREDECLARED_TEST: For each column compute the productized Whiteman-style heat deficit
  H=(cp/g) integral max(theta_crest-theta,0) dp below an ASL reference surface, in
  J m-2. Freeze X3 (NAM one-way) as the mask terrain. The primary horizontal
  footprint is the convex hull of the 11 in-window reporting stations in
  verification/data/stations_2013_selection.csv plus the configured basin waypoints
  in verification/config/figures/pelican2013.toml, intersected with X3 HGT below
  2200 m. Weight it by physical cell area DX*DY/MAPFAC_M^2. The footprint must close
  within d02 rather than intersect a domain edge. Report area-weighted mean H in MJ m-2, horizontal integral in
  TJ, and area fractions above 0.5, 1.0, and 2.0 MJ m-2. Verify coordinates within
  1e-5 degree, map factors within 5e-7, and equal spacing across all four runs,
  plus HGT equality within 0.001 m for each
  feedback-matched GFS-NAM pair; record but do not require HGT equality across the
  one-way/two-way feedback boundary. The seven definitions are the combined
  footprint at 2100, 2200, and 2300 m; station-only and waypoint-only hulls at
  2200 m; and one-cell erosion and constrained dilation of the combined 2200 m
  mask. The bounded weaker-state test
  passes only if GFS-minus-NAM mean H is negative at every 14-18 UTC hour for both
  feedback modes under every definition. The stronger maintenance test passes only
  if GFS18-GFS14 is negative and (GFS18-GFS14)-(NAM18-NAM14) is also negative
  for both pairs under every definition. The 13 UTC value is trajectory context,
  not retained evidence.
EXPECTED_OUTPUT: A manuscript-specific tested analysis script and Slurm wrapper;
  small CSV trajectory, pair-summary, and sensitivity tables; provenance JSON with
  exact inputs, commands, commits, environment, job, definitions, and hashes; a
  candidate PNG/PDF trajectory inspected at useful resolution; a claim-ledger fact;
  a figure-manifest diagnostic row; and a pass/fail row in HYBRID-GATE-REVIEW.md.
ALLOWED_WRITES: rewrite/CHPC-CODEX-PROMPT.md;
  verification/scripts/analyze_heat_deficit.py;
  verification/scripts/smoke_test_heat_deficit.py;
  verification/slurm/run_heat_deficit_analysis.slurm;
  verification/data/heat_deficit_trajectory.csv;
  verification/data/heat_deficit_pair_summary.csv;
  verification/data/heat_deficit_sensitivity.csv;
  verification/data/manifest.csv;
  verification/figures/candidates/wrf_heat_deficit_d02_13to18.png;
  verification/figures/candidates/wrf_heat_deficit_d02_13to18.pdf;
  verification/figures/manifest.csv;
  verification/provenance/heat-deficit-analysis.json;
  notes/claim-evidence-ledger.md; rewrite/HYBRID-GATE-REVIEW.md. Scratch job logs
  and task-scoped working output are also allowed; no other repository file is.
COMPUTE: Existing X6/X5/X10/X3 d02 output analysis on one batch node is allowed;
  no WRF integration and no complete figure-family rerender.
RETURN: Commit and push jrl/chpc-20260713-c4-ana16 after terminal job, artifact,
  visual, provenance, smoke, diff, and repository checks pass.
FAIL_DISPOSITION: Record any reproducible weaker-state result separately, mark Main C4
  failed or dropped if the maintenance test fails, and do not promote a maintenance
  claim or substitute a point-scale figure.
STOP_IF: Stop before a scientific decision if a run identity is unresolved; an exact
  13-18 UTC d02 input is absent; grids/terrain are not pairable; MAPFAC_M or required
  pressure, potential-temperature, or geopotential fields are invalid; the maintained
  brc-tools heat-deficit implementation is unavailable; a registered footprint is
  malformed or intersects the d02 boundary; or an unlisted write, broad
  scan, destructive action, new integration, or overwrite of an accepted artifact
  would be required.
```
