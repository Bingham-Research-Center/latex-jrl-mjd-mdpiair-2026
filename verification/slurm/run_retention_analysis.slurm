#!/bin/bash
#SBATCH --job-name=air_retention
#SBATCH --account=lawson-np
#SBATCH --partition=lawson-np
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=64G
#SBATCH --time=0-00:30:00
#SBATCH --output=/scratch/general/vast/%u/latex_jrl_retention_%j.out
#SBATCH --error=/scratch/general/vast/%u/latex_jrl_retention_%j.err

# Manuscript-specific analysis wrapper. WRF identity and execution stay in the
# registered archive and immutable control packets; reusable analysis stays in
# brc-tools. This job reads four accepted runs and writes a small review packet.
set -euo pipefail

PY=/uufs/chpc.utah.edu/common/home/u0737349/software/pkg/miniforge3/envs/brc-tools-2026/bin/python
REPO=/uufs/chpc.utah.edu/common/home/u0737349/gits/latex-jrl-mjd-mdpiair-2026
ARCHIVE=/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive
OBS=/scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/obs_basin_2013_feb0102.parquet
OUT=${RETENTION_OUT_DIR:-/scratch/general/vast/u0737349/latex_jrl_retention_${SLURM_JOB_ID}}

GFS=${ARCHIVE}/pelican2013_gfs_3_1_333m_75lev/full6h/run_20260630T181555Z
GFS1=${ARCHIVE}/pelican2013_gfs_3_1_333m_75lev_oneway/full6h/run_20260710T234000Z
NAM2=${ARCHIVE}/pelican2013_nam_3_1_333m_75lev/full6h/run_20260626T163737Z
NAM1=${ARCHIVE}/pelican2013_nam_3_1_333m_75lev_oneway/full6h/run_20260702T053120Z

for path in "$PY" "$REPO" "$OBS" "$GFS" "$GFS1" "$NAM2" "$NAM1"; do
  test -r "$path"
done
mkdir -p "$OUT"
export MPLCONFIGDIR="/scratch/general/vast/$USER/mpl-retention-${SLURM_JOB_ID}"
mkdir -p "$MPLCONFIGDIR"

cd "$REPO"
echo "start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "host=$(hostname -f)"
echo "head=$(git rev-parse HEAD)"
echo "out=$OUT"

"$PY" verification/scripts/analyze_wrf_retention.py \
  --run "gfs2=$GFS" \
  --run "gfs1=$GFS1" \
  --run "nam2=$NAM2" \
  --run "nam1=$NAM1" \
  --display "gfs2=GFS two-way" \
  --display "gfs1=GFS one-way" \
  --display "nam2=NAM two-way" \
  --display "nam1=NAM one-way" \
  --pair gfs2,nam2 \
  --pair gfs1,nam1 \
  --pair gfs1,gfs2 \
  --pair nam1,nam2 \
  --interaction gfs1,gfs2,nam1,nam2 \
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
