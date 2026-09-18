#!/bin/bash
#SBATCH --job-name=air_ana19
#SBATCH --account=lawson-np
#SBATCH --partition=lawson-np
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=64G
#SBATCH --time=0-00:40:00
#SBATCH --output=/scratch/general/vast/%u/latex_jrl_ana19_%j.out
#SBATCH --error=/scratch/general/vast/%u/latex_jrl_ana19_%j.err

# ANA-19 / Main C3: spatial and vertical coherence of the driving-product
# response for CMP01 (X6-X5) and CMP02 (X10-X3), with predeclared criteria and
# fixed display hours.  Run identity follows verification/provenance/run-inventory.csv.
set -euo pipefail

PY=/uufs/chpc.utah.edu/common/home/u0737349/software/pkg/miniforge3/envs/brc-tools-2026/bin/python
REPO=/uufs/chpc.utah.edu/common/home/u0737349/gits/latex-jrl-mjd-mdpiair-2026
ARCHIVE=/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive
BRC_TOOLS=/uufs/chpc.utah.edu/common/home/u0737349/gits/brc-tools
OUT=${ANA19_OUT_DIR:-/scratch/general/vast/u0737349/latex_jrl_ana19_${SLURM_JOB_ID}}

X6=${ARCHIVE}/pelican2013_gfs_3_1_333m_75lev/full6h/run_20260630T181555Z
X10=${ARCHIVE}/pelican2013_gfs_3_1_333m_75lev_oneway/full6h/run_20260710T234000Z
X5=${ARCHIVE}/pelican2013_nam_3_1_333m_75lev/full6h/run_20260626T163737Z
X3=${ARCHIVE}/pelican2013_nam_3_1_333m_75lev_oneway/full6h/run_20260702T053120Z

for path in "$PY" "$REPO" "$BRC_TOOLS" "$X6" "$X10" "$X5" "$X3"; do
  test -r "$path"
done
mkdir -p "$OUT"
export PYTHONPATH="$BRC_TOOLS:${PYTHONPATH:-}"
export MPLCONFIGDIR="/scratch/general/vast/$USER/mpl-ana19-${SLURM_JOB_ID}"
mkdir -p "$MPLCONFIGDIR"

cd "$REPO"
echo "start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "host=$(hostname -f)"
echo "head=$(git rev-parse HEAD)"
echo "out=$OUT"

"$PY" verification/scripts/analyze_spatial_response.py \
  --run "x6=$X6" \
  --run "x5=$X5" \
  --run "x10=$X10" \
  --run "x3=$X3" \
  --pair x6,x5 \
  --pair x10,x3 \
  --pair-label 'x6,x5=GFS $-$ NAM (two-way)' \
  --pair-label 'x10,x3=GFS $-$ NAM (one-way)' \
  --mask-run x3 \
  --domain 2 \
  --stations verification/data/stations_2013_selection.csv \
  --figure-config verification/config/figures/pelican2013.toml \
  --start 2013-02-02T14:00:00 \
  --end 2013-02-02T18:00:00 \
  --display-hours 14 16 18 \
  --section-hour 16 \
  --transect USU07 USU03 \
  --out-dir "$OUT"

sha256sum "$OUT"/* > "$OUT/artifact_sha256.txt"
echo "done_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
