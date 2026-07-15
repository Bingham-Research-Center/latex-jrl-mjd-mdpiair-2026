#!/bin/bash
#SBATCH --job-name=air_v3_finish
#SBATCH --account=lawson-np
#SBATCH --partition=lawson-np
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=96G
#SBATCH --time=0-02:00:00
#SBATCH --output=/scratch/general/vast/%u/latex_jrl_v3_finish_%j.out
#SBATCH --error=/scratch/general/vast/%u/latex_jrl_v3_finish_%j.err

# One compute-node-only finishing pass for the v3 figure candidates that still
# require archived WRF output or the frozen observation cache.  Raw products and
# a repo-shaped, candidate-only return bundle are written to scratch; this job
# never edits a Git checkout and never promotes a figure.

set -euo pipefail
umask 002

: "${SLURM_JOB_ID:?submit this file with sbatch}"
: "${MANUSCRIPT_DIR:?set MANUSCRIPT_DIR to the clean pinned manuscript worktree}"
: "${BRC_TOOLS_DIR:?set BRC_TOOLS_DIR to the clean pinned brc-tools worktree}"
: "${V3_FINISH_SOURCE_REF:?set V3_FINISH_SOURCE_REF to the exact manuscript commit}"
: "${BRC_TOOLS_REF:?set BRC_TOOLS_REF to the exact brc-tools commit}"

EXPECTED_BRC_TOOLS_REF=69ddbe07af2e38e5e2d4f12f681bb360ff506a1a
PY="${AIR_PYTHON:-$HOME/software/pkg/miniforge3/envs/brc-tools-2026/bin/python}"
OBS_CACHE="${V3_OBS_CACHE:-/scratch/general/vast/u0737349/latex_jrl_chpc_figure_inventory_20260710/obs_basin_2013_feb0102.parquet}"
ROOT="${V3_FINISH_ROOT:-/scratch/general/vast/$USER/latex_jrl_20260715_v3_finishing_pass/$SLURM_JOB_ID}"
RAW="$ROOT/raw"
RETURN="$ROOT/return"

X0_RUN=/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive/pelican2013_nam_3_1_333m_75lev_oneway_terrain3s/full6h/run_20260708T021809Z
X4_RUN=/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive/pelican2013_nam_3_1_333m_75lev_oneway_terrain5m/full6h/run_20260707T182414Z
X6_RUN=/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive/pelican2013_gfs_3_1_333m_75lev/full6h/run_20260630T181555Z
X5_RUN=/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive/pelican2013_nam_3_1_333m_75lev/full6h/run_20260626T163737Z

HOST_FQDN="$(hostname -f)"
case "$HOST_FQDN" in
    *.chpc.utah.edu) ;;
    *) printf 'refusing non-CHPC host: %s\n' "$HOST_FQDN" >&2; exit 2 ;;
esac

mkdir -p "$RAW"/{overlay,locator,profiles,terrain,data} "$RETURN"
METADATA="$ROOT/job_metadata.txt"
touch "$METADATA"

record_exit() {
    code=$?
    {
        printf 'finished_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
        printf 'exit_code=%s\n' "$code"
    } >> "$METADATA"
    sha256sum "$METADATA" > "$ROOT/job_metadata.sha256"
}
trap record_exit EXIT

test -x "$PY"
test -d "$MANUSCRIPT_DIR/.git" -o -f "$MANUSCRIPT_DIR/.git"
test -d "$BRC_TOOLS_DIR/.git" -o -f "$BRC_TOOLS_DIR/.git"

MANUSCRIPT_HEAD="$(git -C "$MANUSCRIPT_DIR" rev-parse HEAD)"
BRC_HEAD="$(git -C "$BRC_TOOLS_DIR" rev-parse HEAD)"
test "$MANUSCRIPT_HEAD" = "$V3_FINISH_SOURCE_REF"
test "$BRC_TOOLS_REF" = "$EXPECTED_BRC_TOOLS_REF"
test "$BRC_HEAD" = "$BRC_TOOLS_REF"
test -z "$(git -C "$MANUSCRIPT_DIR" status --porcelain=v1 --untracked-files=all)"
test -z "$(git -C "$BRC_TOOLS_DIR" status --porcelain=v1 --untracked-files=all)"

{
    printf 'request_id=20260715-v3-finishing-pass\n'
    printf 'started_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    printf 'host=%s\n' "$HOST_FQDN"
    printf 'slurm_job_id=%s\n' "$SLURM_JOB_ID"
    printf 'manuscript_dir=%s\n' "$MANUSCRIPT_DIR"
    printf 'manuscript_ref=%s\n' "$MANUSCRIPT_HEAD"
    printf 'brc_tools_dir=%s\n' "$BRC_TOOLS_DIR"
    printf 'brc_tools_ref=%s\n' "$BRC_HEAD"
    printf 'python=%s\n' "$PY"
    printf 'python_version=%s\n' "$($PY --version 2>&1)"
    printf 'observation_cache=%s\n' "$OBS_CACHE"
    printf 'x0_run=%s\n' "$X0_RUN"
    printf 'x4_run=%s\n' "$X4_RUN"
    printf 'x6_run=%s\n' "$X6_RUN"
    printf 'x5_run=%s\n' "$X5_RUN"
    printf 'result_root=%s\n' "$ROOT"
    printf 'wrapper_sha256=%s\n' "$(sha256sum "$MANUSCRIPT_DIR/verification/slurm/run_v3_finishing_pass.slurm" | cut -d' ' -f1)"
} >> "$METADATA"

cd "$MANUSCRIPT_DIR"

sha256sum --check <<'SHA256_INPUTS'
15da185ede907e4277a497c51d0e671a3f9956c167110aa52aea867a998f69d0  verification/scripts/plot_wrf_vs_obs_feb0102.py
8a2a84b650a47f12a026c4ba64769023c6a7962b236414f3a8d7a36441f24068  verification/scripts/plot_obs_feb0102.py
4c5e76eedf4c3f13a4504da488bba8ac19e999502f157d8f0bf26bda79eaf868  verification/scripts/verify_runs_feb0102.py
83632cd9c8383d06c0282dc751563fde0e99f2dc1f38369dba92f95b112c52c4  verification/scripts/plot_wrf_profile_spinup.py
a11cbee72b1fda1bbc3bbbe99b1ef7300f10a4a30ae31a0b49a25a8cd1304ddc  verification/scripts/plot_wrf_transect_locator.py
78066cc5aa9a214f562f23f88f2a8da2d3b301e96b70b8069d74353ade6c45cc  verification/scripts/plot_terrain_cmp11_supplement.py
fefff6a5b55ee8ef64265920d1f783d1fa1e469a2b79fd3ff9c8cc473142dfe7  verification/data/wrf_gfs_2way_d02_per_station.csv
2d5ae81963e8d0b17f5b4ec464af5cd3db8af30a34625d529d529f214201fb53  verification/data/wrf_nam_2way_d02_per_station.csv
80bf36f23b02065ae61e606932941190977f016e78842aaf447b3bbbbe60256a  verification/data/stations_2013_selection.csv
2d822dfd90a95f6c6cf257e1ce55e467d200de8d74ec7dec68e18501912a66ae  verification/data/locator_context.geojson
276239230cab6bb238404a9a865223e9a791a3e991b5cb3d9a54e31ef66dafed  verification/data/locator_places.csv
ad9d933854fc7067260f1bb398e25aff2e7c286b9df8135a64c9dfa1cf8d2fd7  verification/config/figures/pelican2013.toml
SHA256_INPUTS

printf '%s  %s\n' \
    733181afd09db704aafe2c148cf19b41bca83e8b020b9839768d7618217eeb64 \
    "$OBS_CACHE" | sha256sum --check

WRF_INPUTS=(
    "$X0_RUN/wrfout_d01_2013-02-02_12:00:00"
    "$X0_RUN/wrfout_d02_2013-02-02_12:00:00"
    "$X0_RUN/wrfout_d03_2013-02-02_12:00:00"
    "$X0_RUN/wrfout_d02_2013-02-02_16:00:00"
    "$X0_RUN/wrfout_d03_2013-02-02_16:00:00"
    "$X4_RUN/wrfout_d02_2013-02-02_16:00:00"
    "$X4_RUN/wrfout_d03_2013-02-02_16:00:00"
    "$X6_RUN/wrfout_d03_2013-02-02_12:00:00"
    "$X6_RUN/wrfout_d03_2013-02-02_13:00:00"
    "$X5_RUN/wrfout_d03_2013-02-02_12:00:00"
    "$X5_RUN/wrfout_d03_2013-02-02_13:00:00"
)
for path in "${WRF_INPUTS[@]}"; do
    test -r "$path"
done
stat --printf='%n\t%s\t%y\t%i\n' "${WRF_INPUTS[@]}" > "$ROOT/wrf_input_stats.tsv"

export MPLCONFIGDIR="$ROOT/mpl-cache"
export PYTHONPATH="$BRC_TOOLS_DIR${PYTHONPATH:+:$PYTHONPATH}"
export PYTHONUNBUFFERED=1
export OMP_NUM_THREADS=1
mkdir -p "$MPLCONFIGDIR"

PS4='+ $(date -u +%Y-%m-%dT%H:%M:%SZ) ${BASH_SOURCE}:${LINENO}: '
set -x

"$PY" verification/scripts/plot_wrf_vs_obs_feb0102.py \
    --wrf verification/data/wrf_gfs_2way_d02_per_station.csv \
          verification/data/wrf_nam_2way_d02_per_station.csv \
    --labels 'GFS two-way' 'NAM two-way' \
    --obs "$OBS_CACHE" \
    --min-time 2013-02-02T14:00 \
    --max-time 2013-02-02T18:00 \
    --out-suffix _gfs2way_vs_nam2way_d02_14to18 \
    --out-dir "$RAW/overlay" \
    --data-out-dir "$RAW/data"

"$PY" verification/scripts/plot_wrf_transect_locator.py \
    --wrf-dir "$X0_RUN" \
    --d01-glob 'wrfout_d01_2013-02-02_12:00:00' \
    --d02-glob 'wrfout_d02_2013-02-02_12:00:00' \
    --d03-glob 'wrfout_d03_2013-02-02_12:00:00' \
    --out-dir "$RAW/locator"

"$PY" verification/scripts/plot_wrf_profile_spinup.py \
    --config verification/config/figures/pelican2013.toml \
    --run "gfs=$X6_RUN" \
    --run "nam=$X5_RUN" \
    --valid 2013-02-02T12:00:00 2013-02-02T13:00:00 \
    --out-dir "$RAW/profiles" \
    --data-out-dir "$RAW/data"

"$PY" verification/scripts/plot_terrain_cmp11_supplement.py \
    --fine-run "$X0_RUN" \
    --coarse-run "$X4_RUN" \
    --valid 2013-02-02T16:00:00 \
    --out-dir "$RAW/terrain" \
    --data-out-dir "$RAW/data"

set +x

RETURN_MANIFEST="$ROOT/return_manifest.tsv"
{
    printf 'source\tdestination\trole\n'
    printf '%s\t%s\t%s\n' 'raw/overlay/wrf_inversion_index_feb0102_gfs2way_vs_nam2way_d02_14to18.png' 'verification/figures/candidates/wrf_inversion_index_feb0102_gfs2way_vs_nam2way_d02_14to18.png' 'main-candidate-render'
    printf '%s\t%s\t%s\n' 'raw/overlay/wrf_inversion_index_feb0102_gfs2way_vs_nam2way_d02_14to18.pdf' 'verification/figures/candidates/wrf_inversion_index_feb0102_gfs2way_vs_nam2way_d02_14to18.pdf' 'main-candidate-vector'
    printf '%s\t%s\t%s\n' 'raw/data/bulk_theta_contrast_feb0102_gfs2way_vs_nam2way_d02_14to18.csv' 'verification/data/bulk_theta_contrast_feb0102_gfs2way_vs_nam2way_d02_14to18.csv' 'exact-plotted-values'
    printf '%s\t%s\t%s\n' 'raw/data/bulk_theta_contrast_feb0102_gfs2way_vs_nam2way_d02_14to18_summary.csv' 'verification/data/bulk_theta_contrast_feb0102_gfs2way_vs_nam2way_d02_14to18_summary.csv' 'exact-grouped-summary'
    printf '%s\t%s\t%s\n' 'raw/locator/wrf_geographic_locator_d01_d03.png' 'verification/figures/candidates/wrf_geographic_locator_d01_d03.png' 'main-candidate-render'
    printf '%s\t%s\t%s\n' 'raw/locator/wrf_geographic_locator_d01_d03.pdf' 'verification/figures/candidates/wrf_geographic_locator_d01_d03.pdf' 'main-candidate-vector'
    printf '%s\t%s\t%s\n' 'raw/profiles/theta_profiles_horsepool_gfs_nam_12z.png' 'verification/figures/candidates/theta_profiles_horsepool_gfs_nam_12z.png' 'appendix-candidate-render'
    printf '%s\t%s\t%s\n' 'raw/profiles/theta_profiles_horsepool_gfs_nam_12z.pdf' 'verification/figures/candidates/theta_profiles_horsepool_gfs_nam_12z.pdf' 'appendix-candidate-vector'
    printf '%s\t%s\t%s\n' 'raw/profiles/theta_profiles_horsepool_gfs_nam_13z.png' 'verification/figures/candidates/theta_profiles_horsepool_gfs_nam_13z.png' 'appendix-candidate-render'
    printf '%s\t%s\t%s\n' 'raw/profiles/theta_profiles_horsepool_gfs_nam_13z.pdf' 'verification/figures/candidates/theta_profiles_horsepool_gfs_nam_13z.pdf' 'appendix-candidate-vector'
    printf '%s\t%s\t%s\n' 'raw/data/theta_profiles_horsepool_gfs_nam_12z_13z.csv' 'verification/data/theta_profiles_horsepool_gfs_nam_12z_13z.csv' 'exact-plotted-values'
    printf '%s\t%s\t%s\n' 'raw/terrain/wrf_terrain_cmp11_d02_d03_16z.png' 'verification/figures/candidates/wrf_terrain_cmp11_d02_d03_16z.png' 'appendix-candidate-render'
    printf '%s\t%s\t%s\n' 'raw/terrain/wrf_terrain_cmp11_d02_d03_16z.pdf' 'verification/figures/candidates/wrf_terrain_cmp11_d02_d03_16z.pdf' 'appendix-candidate-vector'
    printf '%s\t%s\t%s\n' 'raw/data/terrain_cmp11_d02_d03_16z_summary.csv' 'verification/data/terrain_cmp11_d02_d03_16z_summary.csv' 'exact-four-row-summary'
} > "$RETURN_MANIFEST"

while IFS=$'\t' read -r source destination role; do
    test "$source" = source && continue
    test -s "$ROOT/$source"
    install -D -m 0644 "$ROOT/$source" "$RETURN/$destination"
done < "$RETURN_MANIFEST"

export ROOT RETURN RETURN_MANIFEST MANUSCRIPT_HEAD BRC_HEAD OBS_CACHE X0_RUN X4_RUN X6_RUN X5_RUN
"$PY" - <<'PYTHON_PROVENANCE'
import csv
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

root = Path(os.environ["ROOT"])
return_root = Path(os.environ["RETURN"])


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


with Path(os.environ["RETURN_MANIFEST"]).open(newline="") as handle:
    rows = list(csv.DictReader(handle, delimiter="\t"))

returned = []
for row in rows:
    source = root / row["source"]
    destination = return_root / row["destination"]
    returned.append({
        **row,
        "source_sha256": sha256(source),
        "destination_sha256": sha256(destination),
        "bytes": destination.stat().st_size,
        "review_status": "candidate_unreviewed",
    })

record = {
    "request_id": "20260715-v3-finishing-pass",
    "created_utc": datetime.now(timezone.utc).isoformat(),
    "compute_status": "commands_completed",
    "promotion_performed": False,
    "manuscript_source_ref": os.environ["MANUSCRIPT_HEAD"],
    "brc_tools_ref": os.environ["BRC_HEAD"],
    "slurm_job_id": os.environ["SLURM_JOB_ID"],
    "host": os.uname().nodename,
    "result_root": str(root),
    "stdout": f"/scratch/general/vast/{os.environ['USER']}/latex_jrl_v3_finish_{os.environ['SLURM_JOB_ID']}.out",
    "stderr": f"/scratch/general/vast/{os.environ['USER']}/latex_jrl_v3_finish_{os.environ['SLURM_JOB_ID']}.err",
    "observation_cache": os.environ["OBS_CACHE"],
    "observation_cache_sha256": "733181afd09db704aafe2c148cf19b41bca83e8b020b9839768d7618217eeb64",
    "runs": {
        "X0_fine_terrain": os.environ["X0_RUN"],
        "X4_coarse_terrain": os.environ["X4_RUN"],
        "X6_gfs_two_way": os.environ["X6_RUN"],
        "X5_nam_two_way": os.environ["X5_RUN"],
    },
    "command_authority": "verification/slurm/run_v3_finishing_pass.slurm at manuscript_source_ref",
    "raw_wrf_input_stats": str(root / "wrf_input_stats.tsv"),
    "returned_files": returned,
    "admission_note": "Akamai must inspect and register every returned figure before any status change; failed gates remain failed.",
}
destination = return_root / "verification/provenance" / f"v3-finishing-pass-{os.environ['SLURM_JOB_ID']}.json"
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text(json.dumps(record, indent=2) + "\n")
print(f"wrote {destination}")
PYTHON_PROVENANCE

find "$RAW" -type f -print0 | sort -z | xargs -0 sha256sum > "$ROOT/raw_output_sha256.txt"
find "$RETURN" -type f -print0 | sort -z | xargs -0 sha256sum > "$ROOT/return_output_sha256.txt"

printf 'RETURN_ROOT=%s\n' "$RETURN"
printf 'PROVENANCE=%s\n' "$RETURN/verification/provenance/v3-finishing-pass-$SLURM_JOB_ID.json"
printf 'RAW_HASHES=%s\n' "$ROOT/raw_output_sha256.txt"
printf 'RETURN_HASHES=%s\n' "$ROOT/return_output_sha256.txt"
