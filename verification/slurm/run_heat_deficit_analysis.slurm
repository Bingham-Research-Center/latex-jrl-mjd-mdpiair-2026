#!/bin/bash
#SBATCH --job-name=air_heatdeficit
#SBATCH --account=lawson-np
#SBATCH --partition=lawson-np
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=64G
#SBATCH --time=0-01:00:00
#SBATCH --output=/scratch/general/vast/%u/latex_jrl_heatdeficit_%j.out
#SBATCH --error=/scratch/general/vast/%u/latex_jrl_heatdeficit_%j.err

# Architecture C Main C4 / ANA-16. Reads four accepted d02 archives and writes
# one task-scoped evidence packet; it does not run WRF or overwrite figure archives.
set -euo pipefail

PY=/uufs/chpc.utah.edu/common/home/u0737349/software/pkg/miniforge3/envs/brc-tools-2026/bin/python
REPO=/uufs/chpc.utah.edu/common/home/u0737349/gits/latex-jrl-mjd-mdpiair-2026
BRC_TOOLS=/uufs/chpc.utah.edu/common/home/u0737349/gits/brc-tools
ARCHIVE=/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive
OUT=${HEAT_DEFICIT_OUT_DIR:-/scratch/general/vast/u0737349/latex_jrl_heatdeficit_${SLURM_JOB_ID}}

GFS2=${ARCHIVE}/pelican2013_gfs_3_1_333m_75lev/full6h/run_20260630T181555Z
NAM2=${ARCHIVE}/pelican2013_nam_3_1_333m_75lev/full6h/run_20260626T163737Z
GFS1=${ARCHIVE}/pelican2013_gfs_3_1_333m_75lev_oneway/full6h/run_20260710T234000Z
NAM1=${ARCHIVE}/pelican2013_nam_3_1_333m_75lev_oneway/full6h/run_20260702T053120Z

for path in "$PY" "$REPO" "$BRC_TOOLS" "$GFS2" "$NAM2" "$GFS1" "$NAM1"; do
  test -r "$path"
done
mkdir -p "$OUT"
export PYTHONPATH="$BRC_TOOLS:${PYTHONPATH:-}"
export MPLCONFIGDIR="/scratch/general/vast/$USER/mpl-heatdeficit-${SLURM_JOB_ID}"
mkdir -p "$MPLCONFIGDIR"

cd "$REPO"
echo "start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "host=$(hostname -f)"
echo "manuscript_head=$(git rev-parse HEAD)"
echo "manuscript_dirty=$(git status --porcelain | wc -l)"
echo "brc_tools_head=$(git -C "$BRC_TOOLS" rev-parse HEAD)"
echo "brc_tools_dirty=$(git -C "$BRC_TOOLS" status --porcelain | wc -l)"
echo "out=$OUT"

"$PY" verification/scripts/analyze_heat_deficit.py \
  --run "gfs2=$GFS2" \
  --run "nam2=$NAM2" \
  --run "gfs1=$GFS1" \
  --run "nam1=$NAM1" \
  --display "gfs2=GFS two-way" \
  --display "nam2=NAM two-way" \
  --display "gfs1=GFS one-way" \
  --display "nam1=NAM one-way" \
  --pair gfs2,nam2 \
  --pair gfs1,nam1 \
  --mask-run nam1 \
  --domain 2 \
  --start 2013-02-02T13:00:00 \
  --end 2013-02-02T18:00:00 \
  --retained-start 2013-02-02T14:00:00 \
  --retained-end 2013-02-02T18:00:00 \
  --brc-tools-dir "$BRC_TOOLS" \
  --hash-inputs \
  --out-dir "$OUT"

sha256sum "$OUT"/* > "$OUT/artifact_sha256.txt"
echo "done_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
