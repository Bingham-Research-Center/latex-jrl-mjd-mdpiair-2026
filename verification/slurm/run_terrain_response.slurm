#!/bin/bash
#SBATCH --job-name=air_ana17
#SBATCH --account=lawson-np
#SBATCH --partition=lawson-np
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=64G
#SBATCH --time=0-00:40:00
#SBATCH --output=/scratch/general/vast/%u/latex_jrl_ana17_%j.out
#SBATCH --error=/scratch/general/vast/%u/latex_jrl_ana17_%j.err

# ANA-17 / Main C5: terrain-source geometry response for CMP09 (X3-X0), with the
# X4 lineage check gating CMP10/CMP11.  Run identity follows
# verification/provenance/run-inventory.csv.
set -euo pipefail

PY=/uufs/chpc.utah.edu/common/home/u0737349/software/pkg/miniforge3/envs/brc-tools-2026/bin/python
REPO=/uufs/chpc.utah.edu/common/home/u0737349/gits/latex-jrl-mjd-mdpiair-2026
ARCHIVE=/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive
BRC_TOOLS=/uufs/chpc.utah.edu/common/home/u0737349/gits/brc-tools
OUT=${ANA17_OUT_DIR:-/scratch/general/vast/u0737349/latex_jrl_ana17_${SLURM_JOB_ID}}

X0=${ARCHIVE}/pelican2013_nam_3_1_333m_75lev_oneway_terrain3s/full6h/run_20260708T021809Z
X3=${ARCHIVE}/pelican2013_nam_3_1_333m_75lev_oneway/full6h/run_20260702T053120Z
X4=${ARCHIVE}/pelican2013_nam_3_1_333m_75lev_oneway_terrain5m/full6h/run_20260707T182414Z

for path in "$PY" "$REPO" "$BRC_TOOLS" "$X0" "$X3" "$X4"; do
  test -r "$path"
done
mkdir -p "$OUT"
export PYTHONPATH="$BRC_TOOLS:${PYTHONPATH:-}"
export MPLCONFIGDIR="/scratch/general/vast/$USER/mpl-ana17-${SLURM_JOB_ID}"
mkdir -p "$MPLCONFIGDIR"

cd "$REPO"
echo "start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "host=$(hostname -f)"
echo "head=$(git rev-parse HEAD)"
echo "out=$OUT"

"$PY" verification/scripts/analyze_terrain_response.py \
  --run "x0=$X0" \
  --run "x3=$X3" \
  --run "x4=$X4" \
  --domain 2 \
  --stations verification/data/stations_2013_selection.csv \
  --start 2013-02-02T14:00:00 \
  --end 2013-02-02T18:00:00 \
  --out-dir "$OUT"

sha256sum "$OUT"/* > "$OUT/artifact_sha256.txt"
echo "done_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
