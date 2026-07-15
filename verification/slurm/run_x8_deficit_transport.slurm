#!/bin/bash
#SBATCH --job-name=air_x8_deficit
#SBATCH --account=lawson-np
#SBATCH --partition=lawson-np
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=96G
#SBATCH --time=0-02:00:00
#SBATCH --output=/scratch/general/vast/%u/latex_jrl_x8_deficit_%j.out
#SBATCH --error=/scratch/general/vast/%u/latex_jrl_x8_deficit_%j.err

# Build a manuscript-owned, returnable evidence packet from the archived X8 d04 run.
# Raw figures and CSVs remain beside the run in lawson-group6; this job never edits a
# Git checkout or changes figure-admission status.

set -euo pipefail
umask 002

: "${SLURM_JOB_ID:?submit this file with sbatch}"
: "${MANUSCRIPT_DIR:?set MANUSCRIPT_DIR to the clean pinned manuscript checkout}"
: "${MANUSCRIPT_REF:?set MANUSCRIPT_REF to its exact commit}"
: "${BRC_TOOLS_DIR:?set BRC_TOOLS_DIR to the clean pinned brc-tools checkout}"
: "${BRC_TOOLS_REF:?set BRC_TOOLS_REF to its exact commit}"

EXPECTED_BRC_TOOLS_REF=548fee49aaa2376f7212ca6646f561d7c31ad8a2
PY="${AIR_PYTHON:-$HOME/software/pkg/miniforge3/envs/brc-tools-2026/bin/python}"
X8_RUN=/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive/pelican2013_nam_d04_111m_50lev_oneway_terrain3s/full6h/run_20260709T041225Z_d04only3s_ts12
ROOT="${X8_DEFICIT_ROOT:-$X8_RUN/analysis/x8-deficit-transport/job_${SLURM_JOB_ID}}"
RAW="$ROOT/raw"
RETURN="$ROOT/return"
CONFIG="$MANUSCRIPT_DIR/verification/config/figures/pelican2013_d04.toml"
SCRIPT="$MANUSCRIPT_DIR/verification/scripts/analyze_x8_deficit_transport.py"

case "$(hostname -f)" in
    *.chpc.utah.edu) ;;
    *) printf 'refusing non-CHPC host: %s\n' "$(hostname -f)" >&2; exit 2 ;;
esac

test -x "$PY"
test -r "$CONFIG"
test -r "$SCRIPT"
test "$(git -C "$MANUSCRIPT_DIR" rev-parse HEAD)" = "$MANUSCRIPT_REF"
test "$(git -C "$BRC_TOOLS_DIR" rev-parse HEAD)" = "$BRC_TOOLS_REF"
test "$BRC_TOOLS_REF" = "$EXPECTED_BRC_TOOLS_REF"
test -z "$(git -C "$MANUSCRIPT_DIR" status --porcelain=v1 --untracked-files=all)"
test -z "$(git -C "$BRC_TOOLS_DIR" status --porcelain=v1 --untracked-files=all)"

mkdir -p "$RAW/figures" "$RAW/data" "$RETURN"
export MPLCONFIGDIR="$ROOT/mpl-cache"
export XDG_CACHE_HOME="$ROOT/xdg-cache"
export PYTHONPATH="$BRC_TOOLS_DIR${PYTHONPATH:+:$PYTHONPATH}"
export PYTHONUNBUFFERED=1
export OMP_NUM_THREADS=1
mkdir -p "$MPLCONFIGDIR" "$XDG_CACHE_HOME"

mapfile -t WRF_INPUTS < <(find "$X8_RUN" -maxdepth 1 -type f -name 'wrfout_d04_2013-02-02_*' | sort)
test "${#WRF_INPUTS[@]}" -eq 37
for path in "${WRF_INPUTS[@]}"; do
    test -r "$path"
done

METADATA="$ROOT/job_metadata.txt"
{
    printf 'request_id=20260715-x8-deficit-transport\n'
    printf 'started_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    printf 'host=%s\n' "$(hostname -f)"
    printf 'slurm_job_id=%s\n' "$SLURM_JOB_ID"
    printf 'manuscript_ref=%s\n' "$MANUSCRIPT_REF"
    printf 'brc_tools_ref=%s\n' "$BRC_TOOLS_REF"
    printf 'x8_run=%s\n' "$X8_RUN"
    printf 'result_root=%s\n' "$ROOT"
    printf 'python=%s\n' "$PY"
    printf 'python_version=%s\n' "$($PY --version 2>&1)"
    printf 'script_sha256=%s\n' "$(sha256sum "$SCRIPT" | cut -d' ' -f1)"
    printf 'config_sha256=%s\n' "$(sha256sum "$CONFIG" | cut -d' ' -f1)"
    printf 'wrapper_sha256=%s\n' "$(sha256sum "$MANUSCRIPT_DIR/verification/slurm/run_x8_deficit_transport.slurm" | cut -d' ' -f1)"
} > "$METADATA"

record_exit() {
    code=$?
    {
        printf 'finished_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
        printf 'exit_code=%s\n' "$code"
    } >> "$METADATA"
    sha256sum "$METADATA" > "$ROOT/job_metadata.sha256"
}
trap record_exit EXIT

TRACE="$ROOT/command_trace.log"
"$PY" -c 'import matplotlib.font_manager' 2>>"$TRACE"
exec 3>>"$TRACE"
export BASH_XTRACEFD=3
PS4='+ $(date -u +%Y-%m-%dT%H:%M:%SZ) ${BASH_SOURCE}:${LINENO}: '
set -x

cd "$MANUSCRIPT_DIR"
"$PY" verification/scripts/analyze_x8_deficit_transport.py \
    --config "$CONFIG" \
    --run-dir "$X8_RUN" \
    --domain 4 \
    --start 2013-02-02T12:00:00 \
    --end 2013-02-02T18:00:00 \
    --retained-start 2013-02-02T14:00:00 \
    --map-valid 2013-02-02T15:00:00 \
    --out-dir "$RAW/figures" \
    --data-out-dir "$RAW/data"

set +x
exec 3>&-

sha256sum "${WRF_INPUTS[@]}" > "$ROOT/wrf_input_sha256.txt"
stat --printf='%n\t%s\t%y\t%i\n' "${WRF_INPUTS[@]}" > "$ROOT/wrf_input_stats.tsv"

RETURN_MANIFEST="$ROOT/return_manifest.tsv"
{
    printf 'source\tdestination\trole\n'
    for name in \
        x8_deficit_transport_map_15z \
        x8_deficit_transport_gates_12to18 \
        x8_deficit_convergence_15z \
        x8_deficit_bulk_15z \
        x8_deficit_budget_12to18
    do
        printf 'raw/figures/%s.png\tverification/figures/candidates/%s.png\treview-supplement-render\n' "$name" "$name"
        printf 'raw/figures/%s.pdf\tverification/figures/candidates/%s.pdf\treview-supplement-vector\n' "$name" "$name"
    done
    printf 'raw/data/x8_deficit_transport_timeseries.csv\tverification/data/x8_deficit_transport_timeseries.csv\texact-10-minute-state-and-transect-values\n'
    printf 'raw/data/x8_deficit_budget_intervals.csv\tverification/data/x8_deficit_budget_intervals.csv\texact-10-minute-tendency-values\n'
    printf 'raw/data/x8_deficit_transport_summary.csv\tverification/data/x8_deficit_transport_summary.csv\tbounded-summary-values\n'
} > "$RETURN_MANIFEST"

while IFS=$'\t' read -r source destination role; do
    test "$source" = source && continue
    test -s "$ROOT/$source"
    install -D -m 0644 "$ROOT/$source" "$RETURN/$destination"
done < "$RETURN_MANIFEST"

export ROOT RETURN RETURN_MANIFEST MANUSCRIPT_REF BRC_TOOLS_REF X8_RUN SLURM_JOB_ID
"$PY" - <<'PYTHON_PROVENANCE'
import csv
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

root = Path(os.environ["ROOT"])
returned_root = Path(os.environ["RETURN"])


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


with Path(os.environ["RETURN_MANIFEST"]).open(newline="") as stream:
    manifest_rows = list(csv.DictReader(stream, delimiter="\t"))

returned = []
for row in manifest_rows:
    destination = returned_root / row["destination"]
    returned.append(
        {
            **row,
            "sha256": sha256(destination),
            "bytes": destination.stat().st_size,
            "review_status": "candidate_unreviewed",
        }
    )

wrf_inputs = []
with (root / "wrf_input_sha256.txt").open() as stream:
    for line in stream:
        digest, path = line.rstrip("\n").split("  ", 1)
        source = Path(path)
        wrf_inputs.append({"path": path, "sha256": digest, "bytes": source.stat().st_size})

record = {
    "request_id": "20260715-x8-deficit-transport",
    "created_utc": datetime.now(timezone.utc).isoformat(),
    "compute_status": "commands_completed",
    "promotion_performed": False,
    "slurm_job_id": os.environ["SLURM_JOB_ID"],
    "host": os.uname().nodename,
    "manuscript_source_ref": os.environ["MANUSCRIPT_REF"],
    "brc_tools_ref": os.environ["BRC_TOOLS_REF"],
    "x8_run": os.environ["X8_RUN"],
    "domain": "d04",
    "window": "2013-02-02 12:00-18:00 UTC; 12:00-14:00 spin-up context; 14:00-18:00 retained",
    "definitions": {
        "crest_m_msl": 2200.0,
        "active_deficit_min_k": 0.25,
        "minimum_heat_deficit_mj_m2": 0.1,
        "edge_margin_cells": 15,
        "map_valid_utc": "2013-02-02T15:00:00",
        "horizontal_convergence": "-div_h(F)",
        "unresolved": "finite-difference storage minus endpoint-mean horizontal convergence",
        "transect_sign": "west-to-east lines; positive is southward",
    },
    "wrf_inputs": wrf_inputs,
    "command_authority": "verification/slurm/run_x8_deficit_transport.slurm at manuscript_source_ref",
    "command_trace": str(root / "command_trace.log"),
    "job_metadata": str(root / "job_metadata.txt"),
    "returned_files": returned,
    "admission_note": (
        "X8 is multiply confounded context. Akamai must inspect and register every "
        "figure; no resolution, validation, basin-export, or closed-budget claim follows."
    ),
}
destination = returned_root / "verification/provenance" / (
    f"x8-deficit-transport-{os.environ['SLURM_JOB_ID']}.json"
)
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text(json.dumps(record, indent=2) + "\n")
print(f"wrote {destination}")
PYTHON_PROVENANCE

find "$RAW" -type f -print0 | sort -z | xargs -0 sha256sum > "$ROOT/raw_output_sha256.txt"
find "$RETURN" -type f -print0 | sort -z | xargs -0 sha256sum > "$ROOT/return_output_sha256.txt"
printf 'RETURN_ROOT=%s\n' "$RETURN"
