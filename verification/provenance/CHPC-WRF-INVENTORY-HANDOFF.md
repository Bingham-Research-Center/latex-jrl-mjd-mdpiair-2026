# Legacy WRF publication-lineage inventory

This is the task-specific runbook for bounded Trang/OSIP/archive-publication
lookups. The general CHPC bootstrap, figure workflow, and task-packet contract
live in `rewrite/CHPC-CODEX-PROMPT.md`.

Do not run this inventory for an ordinary X0--X10 path or figure question.
Start from the canonical run/comparison rows and exact archive paths for those
tasks. A full core, extended, and header inventory was already completed on
9 July 2026; its summary is `CHPC-WRF-INVENTORY-RESULTS.md`. Rerun only when a
LOOKUP packet names a question that the existing evidence bundle cannot answer.

The script is read-only. Its default/core pass queries only the rclone remote on
a login node. Shared-filesystem traversal and NetCDF header reads occur only in
`--headers-only` mode inside a Slurm allocation.

## 0. Pin the request

The writing-host task packet must supply:

- a `REQUEST_ID` and exact `SOURCE_REF`;
- the relationship being tested, such as `config_equivalent`,
  `produced_output`, `produced_figure`, `evaluated_in`, or `unknown`;
- bounded archive roots or candidate paths;
- the required return artifacts and stop conditions.

Use a clean checkout/worktree at `SOURCE_REF`. Do not switch to `main` by
default, and do not disturb a dirty CHPC checkout. Record the manuscript-repo
commit before running the script.

## 1. Remote metadata on a login node

```bash
hostname -f
cd <clean-manuscript-checkout-at-SOURCE_REF>
git status --short --branch
git rev-parse HEAD

module load rclone
rclone version
rclone listremotes

export OUT="$HOME/wrf_provenance_<REQUEST_ID>"
bash verification/provenance/chpc_wrf_publication_inventory.sh --out "$OUT"
```

This core pass inventories the selected legacy Trang/WRF_SIP roots and captures
small candidate namelists. It does not walk John's shared WRF archive.

Run the broader remote prefixes only when the task packet explicitly needs
them:

```bash
bash verification/provenance/chpc_wrf_publication_inventory.sh \
  --extended --out "$OUT"
```

The current script avoids the `rclone lsf --time-format` option that broke the
historic run under CHPC rclone 1.57. Still record the loaded rclone version and
inspect every `status/*.summary`; a partially failed inventory is not success.

## 2. Local header fingerprints in an allocation

Only run this stage when the question needs current local-run fingerprints:

```bash
salloc -A lawson-np -p lawson-np -N 1 -n 1 --mem=4G -t 00:30:00
module load netcdf-c
cd <clean-manuscript-checkout-at-SOURCE_REF>

bash verification/provenance/chpc_wrf_publication_inventory.sh \
  --headers-only --header-limit <bounded-count> --out "$OUT"
exit
```

Header mode refuses to run without `SLURM_JOB_ID`. It inventories the local
archive inside the allocation, then opens at most the requested number of
representative wrfout files. Increase the limit only to cover named run
families; do not use it as an unbounded archive crawl.

## 3. Validate and return small evidence

```bash
find "$OUT/status" -maxdepth 1 -type f -print -exec sed -n '1,20p' {} \;
test -s "$OUT/report-index.tsv"

tar -C "$(dirname "$OUT")" -czf "$OUT.tgz" "$(basename "$OUT")"
sha256sum "$OUT.tgz"
```

Return the archive path and checksum out of band. Do not commit the generated
bundle because it contains private archive listings and namelist contents. The
minimum useful return set is:

- `report-index.tsv` and `run.log`;
- `status/`;
- relevant `manifests/*.tsv` and `*.directories.txt`;
- `configs.sha256` and `config-key-values.txt`;
- `header-samples.tsv` and relevant `headers/*.fingerprint.txt`.

Do not return raw WRF output. Reconciliation must keep storage labels,
configuration evidence, produced outputs, figures, and publication identity as
separate claims until a machine fingerprint proves each join.
