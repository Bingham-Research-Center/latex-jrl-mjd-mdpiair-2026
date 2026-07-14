#!/bin/bash
#SBATCH --job-name=air_ana18r
#SBATCH --account=lawson-np
#SBATCH --partition=lawson-np
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=64G
#SBATCH --time=0-00:30:00
#SBATCH --output=/scratch/general/vast/%u/latex_jrl_ana18r_%j.out
#SBATCH --error=/scratch/general/vast/%u/latex_jrl_ana18r_%j.err

# ANA-18 radiation leg: aspect-stratified SWDOWN/GLW/TSK screen for CMP07
# (X1-X0, slope_rad/topo_shading/shadlen only).  Run identity follows
# verification/provenance/run-inventory.csv.
set -euo pipefail

PY=/uufs/chpc.utah.edu/common/home/u0737349/software/pkg/miniforge3/envs/brc-tools-2026/bin/python
REPO=/uufs/chpc.utah.edu/common/home/u0737349/gits/latex-jrl-mjd-mdpiair-2026
ARCHIVE=/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive
BRC_TOOLS=/uufs/chpc.utah.edu/common/home/u0737349/gits/brc-tools
OUT=${ANA18R_OUT_DIR:-/scratch/general/vast/u0737349/latex_jrl_ana18r_${SLURM_JOB_ID}}

X0=${ARCHIVE}/pelican2013_nam_3_1_333m_75lev_oneway_terrain3s/full6h/run_20260708T021809Z
X1=${ARCHIVE}/pelican2013_nam_3_1_333m_75lev_oneway_terrain3s_slope/full6h/run_20260710T003606Z

for path in "$PY" "$REPO" "$BRC_TOOLS" "$X0" "$X1"; do
  test -r "$path"
done
mkdir -p "$OUT"
export PYTHONPATH="$BRC_TOOLS:${PYTHONPATH:-}"
export MPLCONFIGDIR="/scratch/general/vast/$USER/mpl-ana18r-${SLURM_JOB_ID}"
mkdir -p "$MPLCONFIGDIR"

cd "$REPO"
echo "start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "host=$(hostname -f)"
echo "head=$(git rev-parse HEAD)"
echo "out=$OUT"

"$PY" verification/scripts/analyze_radiation_response.py \
  --run "x0=$X0" \
  --run "x1=$X1" \
  --domain 2 \
  --start 2013-02-02T14:00:00 \
  --end 2013-02-02T18:00:00 \
  --out-dir "$OUT"

sha256sum "$OUT"/* > "$OUT/artifact_sha256.txt"
echo "done_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
