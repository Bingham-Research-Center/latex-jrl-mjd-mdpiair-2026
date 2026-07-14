#!/bin/bash
#SBATCH --job-name=air_ana18s
#SBATCH --account=lawson-np
#SBATCH --partition=lawson-np
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=64G
#SBATCH --time=0-00:30:00
#SBATCH --output=/scratch/general/vast/%u/latex_jrl_ana18s_%j.out
#SBATCH --error=/scratch/general/vast/%u/latex_jrl_ana18s_%j.err

# ANA-18 station-pipeline leg: matched surface and common-AGL summaries for the
# process pairs CMP07 (X1-X0, slope radiation/shading) and CMP08 (X2-X1,
# MYJ/Eta versus YSU/MM5) on the frozen DES-02/03 definitions.  Run identity
# follows verification/provenance/run-inventory.csv.  PBLH is scheme dependent
# across X2/X1 and enters only with that caveat.
set -euo pipefail

PY=/uufs/chpc.utah.edu/common/home/u0737349/software/pkg/miniforge3/envs/brc-tools-2026/bin/python
REPO=/uufs/chpc.utah.edu/common/home/u0737349/gits/latex-jrl-mjd-mdpiair-2026
ARCHIVE=/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive
OBS=/scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/obs_basin_2013_feb0102.parquet
OUT=${ANA18S_OUT_DIR:-/scratch/general/vast/u0737349/latex_jrl_ana18s_${SLURM_JOB_ID}}

X0=${ARCHIVE}/pelican2013_nam_3_1_333m_75lev_oneway_terrain3s/full6h/run_20260708T021809Z
X1=${ARCHIVE}/pelican2013_nam_3_1_333m_75lev_oneway_terrain3s_slope/full6h/run_20260710T003606Z
X2=${ARCHIVE}/pelican2013_nam_3_1_333m_75lev_oneway_terrain3s_slope_myj/full6h/run_20260710T003606Z

for path in "$PY" "$REPO" "$OBS" "$X0" "$X1" "$X2"; do
  test -r "$path"
done
mkdir -p "$OUT"
export MPLCONFIGDIR="/scratch/general/vast/$USER/mpl-ana18s-${SLURM_JOB_ID}"
mkdir -p "$MPLCONFIGDIR"

cd "$REPO"
echo "start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "host=$(hostname -f)"
echo "head=$(git rev-parse HEAD)"
echo "out=$OUT"

"$PY" verification/scripts/analyze_wrf_retention.py \
  --run "x0=$X0" \
  --run "x1=$X1" \
  --run "x2=$X2" \
  --display "x0=NAM one-way fine terrain (X0 control)" \
  --display "x1=X0 plus slope radiation/shading (X1)" \
  --display "x2=X1 with MYJ/Eta (X2)" \
  --pair x1,x0 \
  --pair x2,x1 \
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
