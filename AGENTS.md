# AI guide — MDPI Air proof

Status: John confirmed the corrected proof was returned to MDPI on 11 October 2026. The public, immutable source checkpoint is tag `mdpi-air-proof-return-2026-10-11` (`f06ee3d`); `jrl/proofs-round1` carries the proof work and later documentation. No journal submission or preprint task is pending.

Start with `hostname -f`, `git status --short --branch`, and [PROOFING-HANDOFF.md](PROOFING-HANDOFF.md). This worktree is the proof branch; default `main` is an older manuscript snapshot.

## Routes

| Task | Read first |
| --- | --- |
| Incoming publisher proof | [handoff](PROOFING-HANDOFF.md) → [query catalogue](notes/proof-query-catalogue.md) → relevant received/working source |
| Submitted source | `proof-package/working/air-4472509-done.tex`; embedded bibliography is authoritative |
| Publisher queries/replies | `PROOFER-REPLY-TABLE.md` → `PROOFER-RETURN-REPLIES.md`; saved author decisions govern |
| Claims and figures | `notes/claim-evidence-ledger.md` → exact artefact; `verification/figures/manifest.csv` and `figures/MANIFEST.md` |
| Runs and comparisons | `verification/provenance/run-inventory.csv`, `verification/provenance/comparison-inventory.csv` |
| Earlier revision | `notes/peer-review-round1-return.md`; root `main.tex` is historical for this proof |

## Proof rules

- Preserve `proof-package/air-4472509-english/` unchanged. Treat any new publisher bundle as immutable intake in a new branch/worktree; compare it with the tagged submitted source before editing.
- Keep printed changes minimal, British English, and one sentence per source line. Preserve official names, identifiers, bibliography titles, publisher quotations, and all `%MDPI:`/`%EE:` notes. Put author replies on standalone `% JRL:` lines.
- Author decisions and visual PDF acceptance govern; a successful compile is technical validation only. Do not submit material to MDPI without a new explicit request.
- Build the proof from `proof-package/working/` with `latexmk -pdf -interaction=nonstopmode -halt-on-error air-4472509-done.tex` (`module load texlive/20260330` on CHPC). Check log, references, preserved notes and `git diff --check`. Generated PDF/ZIP files are ignored by Git.
- Never edit `Definitions/` or hand-edit `paperpile.bib`. Keep original evidence and figure inputs. For science claims, follow the ledger: no chemistry, basin export, inversion depth or multi-day persistence claim without new evidence.
- Preserve unrelated dirt and other worktrees. Commit one verified concern at a time as John Lawson <john.rob.lawson@googlemail.com> with `Co-Authored-By: Codex <noreply@openai.com>`; push through a `jrl/<topic>` branch/PR for protected `main`.
