# First-round peer-review revision handoff

## Authority and scope

- Reviewer-source truth: `/home/johnrobertlawson/reviews/lawson-ozone-wrf-mdpiair-2026/_peer-review/comments.md`.
- Author decisions: `/home/johnrobertlawson/reviews/lawson-ozone-wrf-mdpiair-2026/peer-review-decisions.md`.
- Response draft: `/home/johnrobertlawson/reviews/lawson-ozone-wrf-mdpiair-2026/response-to-reviewers.md`.
- Manuscript base: audited root `main.tex` on `jrl/peer-review-round1`, branched from `bf38e91a2cc1f5e007cdf37c9613ee1afa16fdff`.
- Selective donor only: `/home/johnrobertlawson/reviews/lawson-ozone-wrf-mdpiair-2026/version_1p5/main.tex`.

Do not replace root `main.tex` wholesale with 1p5. Do not resurrect the former separate supplement. Preserve failed scientific gates as failed.

## Agreed revision

- Keep the result to one 2 February 2013 case and the 1400--1800 UTC retained window.
- Describe `S50:500` as a potential-temperature endpoint difference in kelvin.
- Describe `U50:500` as the magnitude of the layer-mean horizontal wind vector, with no transport or ventilation interpretation.
- Add the scalar-speed and vector/scalar alignment check from existing output.
- Add station identities, coordinates, elevations, cell separations, and default-terrain offsets.
- Keep the X0--X4 terrain figure in the main text as a descriptive, support-dependent response with no ranking or mechanism.
- Use verified peer-reviewed sources and narrowly qualified agency-report lineage.
- Integrate only the appendix material needed by the main argument; submit no separate supplement.

## CHPC-only return

The Akamai host has no `/uufs` mount. Submit `verification/slurm/run_peer_review_layer_sensitivity.slurm` from a clean checkout pinned to the revision commit. It reads the four accepted archived runs and calculates the 50--500, 50--250, and 100--500 m layers at 10, 25, and 50 m increments. It runs no WRF simulation and writes a repo-shaped return bundle in scratch.

Import only the returned pair summaries and metadata after checking hashes, the pinned commit, complete station/hour coverage, and metric definitions. Record the imported paths in `notes/peer-review-round1-return.md`; then update the manuscript and response only if the layer result changes or materially qualifies the primary interpretation.

## Pull and execute on CHPC

Remote: `origin` at `https://github.com/Bingham-Research-Center/latex-jrl-mjd-mdpiair-2026.git`.
Delivery branch: `jrl/peer-review-round1`.
Immutable analysis source: `658bd005e20401f9ad8c8e88c5c2b506bb60e1a8`.
That commit contains the complete calculation; the later delivery commit adds these instructions only.

From a clean CHPC checkout of this repository, repair local tracking and fast-forward the delivery branch:

```bash
(
    set -euo pipefail
    test -z "$(git status --porcelain=v1 --untracked-files=all)"
    git fetch origin
    if git show-ref --verify --quiet refs/heads/jrl/peer-review-round1; then
        git switch jrl/peer-review-round1
        git branch --set-upstream-to=origin/jrl/peer-review-round1
        git pull --ff-only
    else
        git switch --track origin/jrl/peer-review-round1
    fi
)
```

If the checkout is dirty or the branch has diverged, preserve it and use a separate worktree at the source commit.
The following submission block creates that worktree even when the delivery checkout is clean, so later writing-branch changes cannot alter a queued job's inputs.
Run it from this repository after fetching the delivery branch, and leave the worktree untouched until the job finishes.

```bash
(
    set -euo pipefail
    export REVIEW_SENSITIVITY_SOURCE_REF=658bd005e20401f9ad8c8e88c5c2b506bb60e1a8
    git cat-file -e "$REVIEW_SENSITIVITY_SOURCE_REF^{commit}"
    git worktree add --detach ../mdpi-air-review-layers-658bd00 "$REVIEW_SENSITIVITY_SOURCE_REF"
    cd ../mdpi-air-review-layers-658bd00
    export MANUSCRIPT_DIR="$PWD"
    export AIR_PYTHON="${AIR_PYTHON:-$HOME/software/pkg/miniforge3/envs/brc-tools-2026/bin/python}"
    export PYTHONDONTWRITEBYTECODE=1
    export MPLCONFIGDIR="/scratch/general/vast/$USER/latex_jrl_review_layers_mpl"
    test -w "/scratch/general/vast/$USER"
    test -x "$AIR_PYTHON"
    mkdir -p "$MPLCONFIGDIR"
    "$AIR_PYTHON" -c 'import matplotlib, numpy, pandas, polars, xarray, netCDF4'
    "$AIR_PYTHON" verification/scripts/analyze_wrf_retention.py --help >/dev/null
    bash -n verification/slurm/run_peer_review_layer_sensitivity.slurm
    test -z "$(git status --porcelain=v1 --untracked-files=all)"
    job_id=$(sbatch --parsable --export=ALL verification/slurm/run_peer_review_layer_sensitivity.slurm)
    job_id=${job_id%%;*}
    printf 'source_ref=%s\ncheckout=%s\njob_id=%s\n' \
        "$REVIEW_SENSITIVITY_SOURCE_REF" "$MANUSCRIPT_DIR" "$job_id" \
        | tee "/scratch/general/vast/$USER/latex_jrl_review_layers_${job_id}.submission.txt"
)
```

Inspect the wrapper's account, partition, Python and archive paths before submission.
If the worktree destination already exists, inspect its commit and cleanliness instead of overwriting it.
Set `AIR_PYTHON` to an existing suitable CHPC environment if the default is unavailable.
The wrapper checks the CHPC hostname, exact source commit, clean worktree, and four archive directories before calculation.
Its archive paths match the X6/X10/X5/X3 rows in `verification/provenance/run-inventory.csv`.

All repository inputs are tracked: the wrapper, `analyze_wrf_retention.py`, its local imports `plot_obs_feb0102.py` and `reduce_wrf_to_stations.py`, and `verification/data/stations_2013_selection.csv`.
This calculation does not import sibling `brc-tools` source or read the writing host's review folder or observation parquet.
Its external requirements are Slurm, the Python packages checked above, and the four existing CHPC WRF archives.
No WRF integration is authorised.

Monitor the printed job ID with `squeue -j JOB_ID` and `sacct -j JOB_ID --format=JobID,State,ExitCode,Elapsed` until terminal.
Inspect `/scratch/general/vast/$USER/latex_jrl_review_layers_JOB_ID.out` and the matching `.err`.
With no `REVIEW_SENSITIVITY_ROOT` override, outputs are under `/scratch/general/vast/$USER/latex_jrl_review_layers/JOB_ID/`.
Require nine pair-summary CSVs, nine metadata JSONs and the run manifest under `return/`, plus the sibling `return_sha256.txt`; check that checksum file on CHPC with `sha256sum -c` before transfer.
Each calculation must cover four runs, 11 stations and all five retained hours, with the requested layer and interpolation increment.
Inspect each diagnostic PDF/PNG under `raw/` on CHPC; these scratch figures are not manuscript promotions.
Return the submission record, terminal scheduler state, stdout/stderr, checksum file and small `return/` bundle together so the source commit and job remain attached to the results.
No manuscript or response edits are part of this CHPC dispatch.

## Stop rules

- Do not infer a cause for Seep Ridge without verified exposure or quality-control evidence.
- Do not treat the horizontal station network as free-air validation.
- Do not infer initial-versus-lateral forcing, basin export, chemistry response, inversion depth, persistence, or product superiority.
- Leave externally dependent response items visibly `PENDING` until verified.
