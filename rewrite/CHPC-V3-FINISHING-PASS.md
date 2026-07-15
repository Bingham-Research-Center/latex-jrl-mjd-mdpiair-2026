# CHPC v3 finishing pass

Date: 15 July 2026
Request ID: `20260715-v3-finishing-pass`
Authority: `notes/manuscript-v3-integration-plan.md` and this handoff
Source branch: `origin/jrl/codex-v3-integration`
Return branch: `jrl/chpc-20260715-v3-finishing-return`

## The simple version

Akamai decides what the paper needs and supplies tested plotting code.
CHPC runs one pinned compute job against the archived WRF files and returns candidates plus exact tables.
Akamai then inspects, registers, and either admits or rejects each candidate before any prose is strengthened.

This pass improves the figures rather than parking them:

1. the bulk-theta overlay gains the exact values used by the plotted lines;
2. the locator gains sourced towns, roads, rivers, regional labels, and a coherent nesting inset;
3. the two profile panels gain a long-form plotted-value table and an unambiguous 2200 m reference label; and
4. four raw terrain panels become one restrained supplemental composite with a four-row numerical summary.

No scientific gate is rerun or rescued.
No CHPC action promotes a figure or edits manuscript prose.

## Server baton

| Stage | Host | Owner action | Exit condition |
|---|---|---|---|
| A | Akamai | Test code, fix editorial role, push one exact source commit | Remote source hash is reported and the worktree is clean |
| B | CHPC | Run `verification/slurm/run_v3_finishing_pass.slurm` from clean detached worktrees | Slurm state is `COMPLETED`, exit is `0:0`, stderr is empty, the separate command trace is nonempty, and the return bundle verifies |
| C | CHPC | Copy only the repo-shaped return bundle to a new return branch and push it | One return commit, based directly on the source hash, is visible on origin |
| D | Akamai | Verify branch ancestry, inspect every image and CSV, then register or reject candidates | Manifests, prose wiring, PDF inspection, and all checks agree |

The active baton belongs to exactly one host at a time.
Do not edit the same branch on both servers.

## Why one job

The chosen one-job route has one queue wait, one environment, one source commit, and one provenance bundle.
Its main cost is that a late terrain failure prevents packaging even if earlier renders succeeded.
That is acceptable here because every component has passed a synthetic Akamai smoke test and the job preserves all raw scratch output for diagnosis.

Separate jobs would isolate failures and allow different memory limits, but would create more scheduler records, more copy steps, and more opportunities to mix source commits.
Use separate jobs only if this bundled job fails for a resource-specific reason.

Keeping all returns as candidates adds one deliberate Akamai review step.
The benefit is that compute success cannot silently become scientific or editorial admission.

## Corrective rerun record

Job `13968061` completed every plotting command, but the CHPC return audit rejected its
bundle before any commit.
The original wrapper sent its own `set -x` trace to stderr while simultaneously
requiring empty stderr, two Python CSV writers emitted CRLF files that failed
`git diff --check`, and the terrain display smoother did not reapply the original
shared-support mask.
The corrected source sends xtrace to `command_trace.log`, emits Git-clean LF tables,
keeps smoothed section colors on the original finite mask, and computes section
summaries from unsmoothed shared-support values.
Do not package or cite the scratch return from job `13968061`.

Corrective job `13968359` passed the numerical and rendering commands but was also
rejected before packaging because its fresh per-job Matplotlib cache emitted one
expected initialization notice to stderr.
The wrapper now warms that cache explicitly and records only the initialization
notice in `command_trace.log`; later plotting stderr remains a strict failure signal.
Do not package or cite the scratch return from job `13968359`.

## Fixed scope

The job produces only these scientific products:

| Product | Runs and window | Intended role | Required data return |
|---|---|---|---|
| Bulk-theta overlay | X6 and X5 on d02, 14:00--18:00 UTC, five hourly samples | Main-paper candidate for surface corroboration | Exact 15-row plotted-value CSV and three-row grouped summary |
| Geographic locator | X0 static d01, d02, and d03 fields at 12:00 UTC | Main-paper Methods candidate | Source-recorded context is already committed; return PNG and PDF |
| Horsepool profiles | X6 and X5 on d03 at 12:00 and 13:00 UTC | Appendix candidate cited from the supplied-state discussion | Exact long-form model-level CSV |
| CMP11 composite | X0 minus X4 on d02 and d03 at 16:00 UTC | Appendix diagnostic | Exact four-row map/section summary |

The radiation panel is not rerun because the CHPC return already preserved its failed, measurement-limited status and its numerical tables were unchanged.
The NAM feedback overlay is not rerun because it has no selected manuscript role.

Do not run generic all-case renderers, excluded experiments, new thresholds, chemistry, or long-window analyses.
Do not edit `main.tex`, `_manuscript_v3.tex`, `paperpile.bib`, the run/comparison inventories, or any claim/gate record on CHPC.

## Stop conditions

Stop before submission if any of the following is true:

- the host is not CHPC;
- `origin/jrl/codex-v3-integration` is absent or differs from the Akamai transition hash;
- either detached worktree is dirty;
- the pinned observation cache is absent or fails its recorded SHA-256;
- any named WRF file is absent;
- a script/input hash check fails; or
- the wrapper hash is not `db984c0b26c8fde49d7284df1a1cf14ecf5bbf0b55f420f144099f93f234c676`.

Stop after submission if Slurm does not report `COMPLETED` and `0:0`, stderr is nonempty, any required return file is empty, or the return hashes fail.
Do not substitute a current observation download, another run directory, synthetic data, or an older locator/profile render.

## Login-node setup

Run only Git, small-file hashes, path checks, submission, and scheduler monitoring on the login node.
The wrapper performs every Python and WRF read on the allocated compute node.

```bash
hostname -f

AIR_BASE="$HOME/gits/latex-jrl-mjd-mdpiair-2026"
BRC_BASE="$HOME/gits/brc-tools"

git -C "$AIR_BASE" fetch --prune origin
git -C "$BRC_BASE" fetch --prune origin

SOURCE_REF="$(git -C "$AIR_BASE" rev-parse origin/jrl/codex-v3-integration)"
BRC_REF=69ddbe07af2e38e5e2d4f12f681bb360ff506a1a

printf 'SOURCE_REF=%s\n' "$SOURCE_REF"
printf 'BRC_REF=%s\n' "$BRC_REF"

AIR_WT="$HOME/worktrees/air-v3-finish-${SOURCE_REF:0:12}"
BRC_WT="$HOME/worktrees/brc-tools-v3-finish-${BRC_REF:0:12}"

test ! -e "$AIR_WT"
test ! -e "$BRC_WT"
mkdir -p "$HOME/worktrees"

git -C "$AIR_BASE" worktree add --detach "$AIR_WT" "$SOURCE_REF"
git -C "$BRC_BASE" worktree add --detach "$BRC_WT" "$BRC_REF"

test "$(git -C "$AIR_WT" rev-parse HEAD)" = "$SOURCE_REF"
test "$(git -C "$BRC_WT" rev-parse HEAD)" = "$BRC_REF"
test -z "$(git -C "$AIR_WT" status --porcelain=v1 --untracked-files=all)"
test -z "$(git -C "$BRC_WT" status --porcelain=v1 --untracked-files=all)"

sha256sum "$AIR_WT/verification/slurm/run_v3_finishing_pass.slurm"
```

Compare the printed `SOURCE_REF` with the exact hash in the Akamai transition message.
If it differs, stop and fetch again; do not guess which branch is newer.

## Submit once

```bash
AIR_PYTHON=/uufs/chpc.utah.edu/common/home/u0737349/software/pkg/miniforge3/envs/brc-tools-2026/bin/python

SUBMIT_RESULT="$(sbatch --parsable \
  --export=ALL,MANUSCRIPT_DIR="$AIR_WT",BRC_TOOLS_DIR="$BRC_WT",V3_FINISH_SOURCE_REF="$SOURCE_REF",BRC_TOOLS_REF="$BRC_REF",AIR_PYTHON="$AIR_PYTHON" \
  "$AIR_WT/verification/slurm/run_v3_finishing_pass.slurm")"
JOB_ID="${SUBMIT_RESULT%%;*}"

printf 'JOB_ID=%s\n' "$JOB_ID"
RESULT_ROOT="/scratch/general/vast/$USER/latex_jrl_20260715_v3_finishing_pass/$JOB_ID"
printf 'RESULT_ROOT=%s\n' "$RESULT_ROOT"
```

Do not submit a second copy while the first is pending or running.

## Monitor to a terminal state

```bash
squeue -j "$JOB_ID"
sacct -X -j "$JOB_ID" --format=JobID,JobName%24,State,ExitCode,Elapsed,MaxRSS,NodeList
```

After completion:

```bash
test -s "/scratch/general/vast/$USER/latex_jrl_v3_finish_${JOB_ID}.out"
test ! -s "/scratch/general/vast/$USER/latex_jrl_v3_finish_${JOB_ID}.err"
test -s "$RESULT_ROOT/command_trace.log"
test -s "$RESULT_ROOT/return_output_sha256.txt"
sha256sum --check "$RESULT_ROOT/return_output_sha256.txt"
test -s "$RESULT_ROOT/return/verification/provenance/v3-finishing-pass-${JOB_ID}.json"
```

The provenance JSON must say `promotion_performed: false` and every returned image must say `candidate_unreviewed`.

## Numerical checks before the return commit

Use the pinned Python only on an allocation if parsing is needed.
The quick login-node checks below read small CSV files and JSON only.

```bash
wc -l \
  "$RESULT_ROOT/return/verification/data/bulk_theta_contrast_feb0102_gfs2way_vs_nam2way_d02_14to18.csv" \
  "$RESULT_ROOT/return/verification/data/bulk_theta_contrast_feb0102_gfs2way_vs_nam2way_d02_14to18_summary.csv" \
  "$RESULT_ROOT/return/verification/data/theta_profiles_horsepool_gfs_nam_12z_13z.csv" \
  "$RESULT_ROOT/return/verification/data/terrain_cmp11_d02_d03_16z_summary.csv"
```

Including headers, the bulk-theta files must have 16 and 4 lines, respectively, and the terrain summary must have 5 lines.
The profile table length depends on the archived vertical grid, but it must contain both cases and both valid times with no missing source path.

## Create the immutable CHPC return

The compute job has already built a repo-shaped return tree containing only selected candidates, exact tables, and one provenance JSON.
Copy that tree into the clean detached manuscript worktree only after all scheduler, hash, and small-table checks pass.

```bash
git -C "$AIR_WT" switch -c jrl/chpc-20260715-v3-finishing-return
cp -a "$RESULT_ROOT/return/." "$AIR_WT/"

git -C "$AIR_WT" status --short
git -C "$AIR_WT" diff --check

git -C "$AIR_WT" add \
  verification/figures/candidates/wrf_inversion_index_feb0102_gfs2way_vs_nam2way_d02_14to18.png \
  verification/figures/candidates/wrf_inversion_index_feb0102_gfs2way_vs_nam2way_d02_14to18.pdf \
  verification/figures/candidates/wrf_geographic_locator_d01_d03.png \
  verification/figures/candidates/wrf_geographic_locator_d01_d03.pdf \
  verification/figures/candidates/theta_profiles_horsepool_gfs_nam_12z.png \
  verification/figures/candidates/theta_profiles_horsepool_gfs_nam_12z.pdf \
  verification/figures/candidates/theta_profiles_horsepool_gfs_nam_13z.png \
  verification/figures/candidates/theta_profiles_horsepool_gfs_nam_13z.pdf \
  verification/figures/candidates/wrf_terrain_cmp11_d02_d03_16z.png \
  verification/figures/candidates/wrf_terrain_cmp11_d02_d03_16z.pdf \
  verification/data/bulk_theta_contrast_feb0102_gfs2way_vs_nam2way_d02_14to18.csv \
  verification/data/bulk_theta_contrast_feb0102_gfs2way_vs_nam2way_d02_14to18_summary.csv \
  verification/data/theta_profiles_horsepool_gfs_nam_12z_13z.csv \
  verification/data/terrain_cmp11_d02_d03_16z_summary.csv \
  "verification/provenance/v3-finishing-pass-${JOB_ID}.json"

git -C "$AIR_WT" diff --cached --name-only
git -C "$AIR_WT" commit \
  -m "figures: return bounded v3 finishing pass" \
  -m "Co-Authored-By: Codex <noreply@openai.com>"
git -C "$AIR_WT" push -u origin jrl/chpc-20260715-v3-finishing-return
```

The staged list must contain exactly the 15 paths named above.
Do not add Slurm logs, Matplotlib caches, unselected temperature companions, raw WRF data, or scratch manifests to Git.

## CHPC return message

Report all of the following before handing the baton back to Akamai:

- `SOURCE_REF`, `BRC_REF`, return branch, and full return commit;
- job ID, node, `State`, `ExitCode`, elapsed time, and `MaxRSS`;
- stdout, stderr, and `RESULT_ROOT` paths;
- observation-cache hash result and return-bundle hash-check result;
- the four CSV line counts;
- the exact 15 staged paths; and
- any warning, rejection, rerun, or deviation.

Do not claim visual admission on CHPC merely because the job completed.

## Akamai admission pass

On Akamai, first verify that the return commit has exactly the dispatched source as its parent.
Then integrate the one return commit into `jrl/codex-v3-integration` and inspect the PNG and PDF versions at useful resolution.

The minimum visual checks are:

- bulk theta: no 8 K line, five hourly points per series, correct X6/X5 labels, and no free-air-inversion wording;
- locator: legible station/town labels, correct roads and rivers, no transects or coordinate ticks, and a coherent d01--d03 inset;
- profiles: identical axes, only X6/X5, correct 12/13 UTC labels, gray below-terrain region, and `2200 m crest reference` wording; and
- terrain: one clean 2-by-2 composite, fixed map and section scales, correct X0-minus-X4 sign, section tracks shown on the d03 map, summaries restricted to unsmoothed shared above-terrain support, no engine watermark, and no drainage/ranking claim.

Cross-check the bulk-theta and terrain summary values against their plots and inspect the profile CSV for the two cases, two times, d03 sources, finite heights, and finite potential temperatures.

Only after that review may Akamai:

1. add or update figure/data manifest rows and hashes;
2. point the v3 appendix profile panels at the new candidate paths;
3. remove the corresponding rewrite gates if every admission requirement is complete; and
4. decide whether the bulk-theta and locator candidates have earned dual promotion.

Run `make check`, `make rewrite-check`, `make v3-check`, `make smoke`, and `git diff --check`, then inspect every changed v3 PDF page.
`main.tex` must remain unchanged until a separate, explicit audited-manuscript promotion decision.
