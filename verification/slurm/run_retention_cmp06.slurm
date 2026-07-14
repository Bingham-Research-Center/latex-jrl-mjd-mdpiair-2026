#!/bin/bash
#SBATCH --job-name=air_cmp06
#SBATCH --account=lawson-np
#SBATCH --partition=lawson-np
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=64G
#SBATCH --time=0-00:30:00
#SBATCH --output=/scratch/general/vast/%u/latex_jrl_cmp06_%j.out
#SBATCH --error=/scratch/general/vast/%u/latex_jrl_cmp06_%j.err

# ANA-20 / Supplement C2: recompute CMP06 (X9 minus X0, two-way minus one-way
# feedback at fine 3-arcsecond terrain) on the frozen DES-02/03 definitions used
# for the default-terrain feedback result.  Run identity follows
# verification/provenance/run-inventory.csv; the pair orientation matches the
# CMP06 row in verification/provenance/comparison-inventory.csv.
set -euo pipefail

PY=/uufs/chpc.utah.edu/common/home/u0737349/software/pkg/miniforge3/envs/brc-tools-2026/bin/python
REPO=/uufs/chpc.utah.edu/common/home/u0737349/gits/latex-jrl-mjd-mdpiair-2026
ARCHIVE=/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive
OBS=/scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/obs_basin_2013_feb0102.parquet
OUT=${CMP06_OUT_DIR:-/scratch/general/vast/u0737349/latex_jrl_cmp06_${SLURM_JOB_ID}}

X9=${ARCHIVE}/pelican2013_nam_3_1_333m_75lev_twoway_terrain3s/full6h/run_20260710T084413Z
X0=${ARCHIVE}/pelican2013_nam_3_1_333m_75lev_oneway_terrain3s/full6h/run_20260708T021809Z

for path in "$PY" "$REPO" "$OBS" "$X9" "$X0"; do
  test -r "$path"
done
mkdir -p "$OUT"
export MPLCONFIGDIR="/scratch/general/vast/$USER/mpl-cmp06-${SLURM_JOB_ID}"
mkdir -p "$MPLCONFIGDIR"

cd "$REPO"
echo "start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "host=$(hostname -f)"
echo "head=$(git rev-parse HEAD)"
echo "out=$OUT"

"$PY" verification/scripts/analyze_wrf_retention.py \
  --run "x9=$X9" \
  --run "x0=$X0" \
  --display "x9=NAM two-way fine terrain (X9)" \
  --display "x0=NAM one-way fine terrain (X0)" \
  --pair x9,x0 \
  --glob 'wrfout_d02_2013-02-02_*' \
  --stations verification/data/stations_2013_selection.csv \
  --obs "$OBS" \
  --start 2013-02-02T14:00:00 \
  --end 2013-02-02T18:00:00 \
  --agl-bottom 50 \
  --agl-top 500 \
  --agl-step 25 \
  --block-length 2 \
  --bootstrap-resamples 20000 \
  --seed 20130202 \
  --out-dir "$OUT"

sha256sum "$OUT"/* > "$OUT/artifact_sha256.txt"
echo "done_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
