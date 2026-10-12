# AI guide — MDPI Air repository

Status: John confirmed return of the corrected proof to MDPI on 11 October 2026. The repository is public. The submitted source is tag `mdpi-air-proof-return-2026-10-11` (`f06ee3d`); work continues on `jrl/proofs-round1`. Default `main` and its `main.tex` are older snapshots. No journal action is pending.

Cold start: `hostname -f`, `git status --short --branch`, then [README.md](README.md). For any new publisher proof, use the [proof-branch handoff](https://github.com/Bingham-Research-Center/latex-jrl-mjd-mdpiair-2026/blob/jrl/proofs-round1/PROOFING-HANDOFF.md). Preserve unrelated dirt and existing worktrees.

## Routes

| Task | Read first |
| --- | --- |
| Submitted proof | Tag `mdpi-air-proof-return-2026-10-11` → `proof-package/working/air-4472509-done.tex` |
| Publisher questions | Proof branch `PROOFER-REPLY-TABLE.md` → `notes/proof-query-catalogue.md`; saved author decisions govern |
| Earlier revision | `notes/peer-review-round1-return.md` → `main.tex` on `jrl/peer-review-round1` |
| Claims and figures | `notes/claim-evidence-ledger.md` → exact artefact; `verification/figures/manifest.csv`, `figures/MANIFEST.md` |
| Runs and comparisons | `verification/provenance/run-inventory.csv`, `verification/provenance/comparison-inventory.csv` |
| Root build/package | `Makefile`, `figures/submission-files.txt`, `packaging/README-package.md` |

## Rules

- Treat publisher originals and any new proof intake as immutable. Create a new `jrl/<topic>` branch/worktree for a new round; compare it to the submitted-source tag. Author decisions and visual PDF acceptance govern. Do not submit to MDPI without a new explicit request.
- Keep manuscript edits small, British English, one sentence per source line. Preserve quotations, official names and identifiers. Do not edit `Definitions/` or hand-edit `paperpile.bib`.
- Architecture C is frozen; failed gates stay failed without new predeclared evidence. X6/X10/X5/X3 are the confirmed floor. Keep controlled, observational and literature evidence separate; X8 is within-run context only. No chemistry, emissions-adequacy, basin-export, inversion-depth or multi-day-persistence claim without new evidence.
- Inventories govern designs, archives govern existence, manifests govern figure admission, and the claim ledger plus exact artefacts govern claims. No synthetic output may be promoted.
- For root manuscript changes run `make final-draft-check`, `make submission-check`, inspect PDFs, then `make package`. Proof-branch builds follow that branch's AGENTS.md. Use protected-main PRs and verified commits attributed to John Lawson <john.rob.lawson@googlemail.com> with `Co-Authored-By: Codex <noreply@openai.com>`.
