#!/bin/bash
#SBATCH --job-name=pelican_figures
#SBATCH --account=lawson-np
#SBATCH --partition=lawson-np
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=96G
#SBATCH --time=0-02:00:00
# Route job logs to scratch, not into any repo checkout (keeps the tree clean).
#SBATCH --output=/scratch/general/vast/%u/pelican_figures_%j.out
#SBATCH --error=/scratch/general/vast/%u/pelican_figures_%j.err

# Publication figures for the pelican2013 WRF cold-pool cases.  The engine + CLI
# live in brc-tools; this wrapper only supplies the manuscript's figure config
# (verification/config/figures/pelican2013.toml by default).
# and the CHPC job environment.
#   sbatch verification/slurm/pelican_figures.slurm                        # all cases/figures/times
#   sbatch verification/slurm/pelican_figures.slurm --figure section,surface --time 12,18
#   sbatch verification/slurm/pelican_figures.slurm --figure surface --lead 1
#   sbatch verification/slurm/pelican_figures.slurm --lead 0,1,6 --skip-existing
# Extra args after the script are forwarded to scripts/wrf_figures.py.  --lead selects
# by forecast lead hour (init + N) and overrides the default --time all below;
# --skip-existing skips figures already newer than their wrfout (idempotent re-runs).

set -euo pipefail

# Login env does NOT carry into batch jobs; call the env python directly.
PY=~/software/pkg/miniforge3/envs/brc-tools-2026/bin/python
BRC_TOOLS=~/gits/brc-tools
MANUSCRIPT=~/gits/latex-jrl-mjd-mdpiair-2026
CASE="${PELICAN_FIGURE_CONFIG:-$MANUSCRIPT/verification/config/figures/pelican2013.toml}"

# Writable matplotlib cache (else every run rebuilds it / errors) + pre-populated
# cartopy Natural-Earth data (compute nodes may lack outbound network).
export MPLCONFIGDIR="/scratch/general/vast/$USER/mpl-$SLURM_JOB_ID"
mkdir -p "$MPLCONFIGDIR"
# Persistent basemap cache wins (stage once via brc-tools scripts/fetch_basemap.dtn.slurm);
# fall back to the purgeable scratch dir.  brc_tools.visualize.basemap reads either.
export CARTOPY_DATA_DIR="${BRC_TOOLS_BASEMAP_DIR:-/scratch/general/vast/$USER/cartopy}"
export PYTHONPATH="$BRC_TOOLS:${PYTHONPATH:-}"

# Figures route out of every repo: per-case -> <run>/full-figures/, cross-case ->
# $BRC_WRF_ARCHIVE/pelican2013_pub_figures/compare/.  Override the archive root if the
# case TOML's archive_dir is stale:
# export BRC_WRF_ARCHIVE=/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive

cd "$BRC_TOOLS"
echo "=== pelican_figures start $(date -u +%Y-%m-%dT%H:%M:%SZ) on $(hostname) ==="

# Soundings need a network node: run brc-tools scripts/fetch_soundings.py on a
# login/DTN node first, then add: --sounding-cache /scratch/general/vast/$USER/soundings_*.parquet
"$PY" scripts/wrf_figures.py --config "$CASE" --case all --figure all --time all "$@"

echo "=== pelican_figures done $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
