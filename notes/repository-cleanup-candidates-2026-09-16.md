# Repository cleanup candidates

Read-only inventory, 16 September 2026: nothing deleted or moved.
Sizes describe this checkout; removing tracked files would not shrink existing Git history.

| Priority | Candidate | Proposed action / condition |
| --- | --- | --- |
| 1 | Root LaTeX auxiliaries: 26 ignored files, 0.67 MiB (`.aux`, `.bbl`, `.blg`, `.fdb_latexmk`, `.fls`, `.log`, `.out`) | Remove after the next successful build; keep the current `main.pdf`. |
| 1 | Root `_manuscript_test.pdf`, `_manuscript_v3.pdf`, `supplement.pdf`: 12.72 MiB | Remove these reproducible build copies after confirming the dated review/submission snapshots are retained. Preserve their sources. |
| 1 | `dist/`: 18.63 MiB of staging trees and ZIPs | Remove regenerable staging after checking release retention. Current ZIP hashes differ from the signed-off July record; they are not those recorded originals. |
| 2 | `drafts/jrl-supplement_2026-07-16_submission-draft_7951b3b.pdf`: 0.27 MiB | Exact SHA-256 duplicate of `drafts/jrl-supplement_2026-07-16_submission-draft_a0a1c30.pdf`; retain the latter, which the release record cites. This is the only exact duplicate found across tracked `drafts/` and `figures-draft/`. |
| 2 | July dispatch/status documents under `rewrite/` | Mark/archive completed dispatches and repair their incoming links; keep gate decisions and execution evidence. Specific stale routes are below. |
| 3 | `drafts/`: 92.09 MiB; `figures-draft/`: 19.93 MiB | Review milestone retention and archive obsolete draft assets together with their references. Similar PDF names or sizes do not prove duplication. Preserve exact submitted manuscript and supplement copies. |
| 3 | `verification/figures/candidates/`: 57.80 MiB, 101 files | Review against manifests, source dependencies and CHPC recoverability before archiving. Seven v3 figure references and two archived-author-draft references still point here; no bulk deletion. |
| Separate maintenance | `submission-package/`: 11.00 MiB | Its `main.tex` and PDF differ from the root versions. Refresh with `make package` after revision closure; it is a delivery artefact, not approved rubbish. |

## The main source of navigation clutter

- `rewrite/CHPC-V3-FIGURE-RECOMPUTE-HANDOFF.md` says "active"; `notes/manuscript-v3-integration-plan.md` and `rewrite/CHPC-CODEX-PROMPT.md` record it as completed.
- `rewrite/CHPC-V3-FINISHING-PASS.md` is also completed history.
- `rewrite/README.md` still directs readers to active v3 recomputation and unresolved July figure work.
- `README.md`, `ROADMAP.md` and `tasks/final-draft-100.md` retain July final-draft routing. Reconcile their current-versus-historical roles against the first-round review before pruning them.

The current peer-review handoff has been shortened in place and the return note now distinguishes received results from pending import.
Retain the CHPC archive until the results and all provenance are durably imported.
Preserve `Definitions/`, bibliography, canonical inventories/manifests, the claim ledger, failed-gate records, and source manuscripts.
