#!/bin/bash
#SBATCH --job-name=air_review_layers
#SBATCH --account=lawson-np
#SBATCH --partition=lawson-np
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=64G
#SBATCH --time=0-01:30:00
#SBATCH --output=/scratch/general/vast/%u/latex_jrl_review_layers_%j.out
#SBATCH --error=/scratch/general/vast/%u/latex_jrl_review_layers_%j.err

# Existing-output calculation requested during first-round peer review. This job
# runs no WRF simulation and never edits the manuscript checkout.
set -euo pipefail
umask 002

: "${SLURM_JOB_ID:?submit this file with sbatch}"
: "${MANUSCRIPT_DIR:?set MANUSCRIPT_DIR to a clean pinned manuscript checkout}"
: "${REVIEW_SENSITIVITY_SOURCE_REF:?set REVIEW_SENSITIVITY_SOURCE_REF to its exact commit}"

PY="${AIR_PYTHON:-$HOME/software/pkg/miniforge3/envs/brc-tools-2026/bin/python}"
ARCHIVE=/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive
ROOT="${REVIEW_SENSITIVITY_ROOT:-/scratch/general/vast/$USER/latex_jrl_review_layers/$SLURM_JOB_ID}"
RAW="$ROOT/raw"
RETURN="$ROOT/return"

GFS2=${ARCHIVE}/pelican2013_gfs_3_1_333m_75lev/full6h/run_20260630T181555Z
GFS1=${ARCHIVE}/pelican2013_gfs_3_1_333m_75lev_oneway/full6h/run_20260710T234000Z
NAM2=${ARCHIVE}/pelican2013_nam_3_1_333m_75lev/full6h/run_20260626T163737Z
NAM1=${ARCHIVE}/pelican2013_nam_3_1_333m_75lev_oneway/full6h/run_20260702T053120Z

case "$(hostname -f)" in
    *.chpc.utah.edu) ;;
    *) printf 'refusing non-CHPC host\n' >&2; exit 2 ;;
esac

test -x "$PY"
test "$(git -C "$MANUSCRIPT_DIR" rev-parse HEAD)" = "$REVIEW_SENSITIVITY_SOURCE_REF"
test -z "$(git -C "$MANUSCRIPT_DIR" status --porcelain=v1 --untracked-files=all)"
for path in "$GFS2" "$GFS1" "$NAM2" "$NAM1"; do test -r "$path"; done

mkdir -p "$RAW" "$RETURN/verification/data" "$RETURN/verification/provenance"
export MPLCONFIGDIR="$ROOT/mpl-cache"
mkdir -p "$MPLCONFIGDIR"
cd "$MANUSCRIPT_DIR"

printf 'layer_bottom_m\tlayer_top_m\tvertical_step_m\toutput\n' > "$ROOT/run_manifest.tsv"
for spec in '50 500 10' '50 500 25' '50 500 50' '50 250 10' '50 250 25' '50 250 50' '100 500 10' '100 500 25' '100 500 50'; do
    read -r bottom top step <<< "$spec"
    key="${bottom}-${top}_step-${step}"
    out="$RAW/$key"
    "$PY" verification/scripts/analyze_wrf_retention.py \
        --run "gfs2=$GFS2" --run "gfs1=$GFS1" \
        --run "nam2=$NAM2" --run "nam1=$NAM1" \
        --display 'gfs2=GFS two-way' --display 'gfs1=GFS one-way' \
        --display 'nam2=NAM two-way' --display 'nam1=NAM one-way' \
        --pair gfs2,nam2 --pair gfs1,nam1 \
        --glob 'wrfout_d02_2013-02-02_*' \
        --stations verification/data/stations_2013_selection.csv \
        --start 2013-02-02T14:00:00 --end 2013-02-02T18:00:00 \
        --agl-bottom "$bottom" --agl-top "$top" --agl-step "$step" \
        --block-length 2 --bootstrap-resamples 20000 --seed 20130202 \
        --out-dir "$out"
    cp "$out/retention_pair_summary.csv" \
        "$RETURN/verification/data/reviewer_layer_${key}_pair_summary.csv"
    cp "$out/retention_analysis_metadata.json" \
        "$RETURN/verification/provenance/reviewer_layer_${key}_metadata.json"
    printf '%s\t%s\t%s\t%s\n' "$bottom" "$top" "$step" "$out" >> "$ROOT/run_manifest.tsv"
done

cp "$ROOT/run_manifest.tsv" "$RETURN/verification/provenance/reviewer-layer-run-manifest.tsv"
find "$RETURN" -type f -print0 | sort -z | xargs -0 sha256sum > "$ROOT/return_sha256.txt"
printf 'source_ref=%s\nreturn=%s\n' "$REVIEW_SENSITIVITY_SOURCE_REF" "$RETURN"
