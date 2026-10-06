# Proof-return handoff — 6 October 2026

**The requested proof edits are applied; final visual/reply approval and delivery remain. Nothing has been submitted or made public by Codex.**

## Start here

```sh
cd /uufs/chpc.utah.edu/common/home/u0737349/worktrees/air-proofs-round1
git status --short --branch
git worktree list
```

Read [AGENTS.md](AGENTS.md), then [PROOFER-REPLY-TABLE.md](PROOFER-REPLY-TABLE.md). Use the [catalogue](notes/proof-query-catalogue.md) only for the relevant exact query, saved author decision or evidence. Do not reopen the complete history for each check.

A worktree is another folder on a separate branch, sharing this repository’s Git history. This folder is on `jrl/proofs-round1`; the original `gits/latex-jrl-mjd-mdpiair-2026` folder is an earlier revision checkout. Proof changes are committed/pushed on the proof branch. They reach `main` through a later deliberate integration/PR; they do not automatically replace root `main.tex` or its submission package.

## Current files and evidence

| Item | Path/state |
| --- | --- |
| Edit/return source | `proof-package/working/air-4472509-done.tex`; embedded 49-entry bibliography |
| Review PDF | `proof-package/working/air-4472509-done.pdf`; 18 pages; ignored by Git |
| Original proof | `proof-package/air-4472509-english/`; all 33 files unchanged from `92b14d2` |
| Final review index | `PROOFER-REPLY-TABLE.md`; 51 rows covering all 23 publisher notes, highlights and later author changes |
| Decisions/evidence/history | `notes/proof-query-catalogue.md`; master register, not superseded by the table |
| Intake/recovery | `proof-package/intake.json`, `proof-package/edit-recovery-20261006.json`, `proof-package/working-copy.json` |
| Terrain/software evidence | `proof-package/terrain-source-evidence-20261006.json`, `proof-package/software-version-evidence-20261006.json` |

The reply-table locators are pinned to source commit `003e67c` and SHA-256 `63b2f1e90a66d5c7b3d72b0ce22c082221b9b0bbff96946703a6c66d044420d6`. PDF pages use compiled labels/source metadata; **there are no printed PDF line numbers**, so the table marks them “—”. Refresh the map if TeX or layout changes. Codex did not load/render the PDF.

## NEXT — MDPI05b, then final replies

1. John checks pages 7–8: Section 3.4’s heading/opening paragraph now precedes unchanged Figure 4 to address the reported gap. Check flow and white space.
2. John checks resized Figures 5–9 (pages 9–12), remaining tables A2–A6 (pages 14–15), and back matter (page 16). A1 is explicitly approved. The manual page break before Conflicts of Interest is removed; it follows Acknowledgements. Prior overlap/placement confirmations remain author decisions; resized-page readability needs John’s final check.
3. Use the reply table as the final checklist: tick each code after checking the current source/PDF and proposed reply. MDPI04a’s aggregator/instrument limitation is recorded, not a complete instrument inventory; retain documented provider facts and the software-version attribution limits. All named AI models/CLI use are author-confirmed; no independent per-session/snapshot claim.
4. Audit that all 22 MDPI notes plus EE01 and highlighted follow-ups have replies, then obtain John’s final return approval. Source comments are not printed replies; assemble the actual journal response deliberately.
5. Assemble the corrected TeX/PDF/support files for return. Root `main.tex`/`submission-package` integration, required Make checks/package refresh, protected-main PR/merge and journal submission remain separate requested actions. Do not submit or merge merely because this checklist exists.
6. **PUB01 after confirmed proof submission:** make the repository public as John has instructed, with his selected provenance prepared; verify unauthenticated access and reconcile availability wording with the final published proof. Current Data Availability gives `https://github.com/Bingham-Research-Center/latex-jrl-mjd-mdpiair-2026` and says it will be publicly available after proof submission. Last live API check (6 October): private. Timing is authorised; do not change visibility before submission.

## Continue the agreed batch pattern

Name the catalogue code, make minimal changes with standalone `% JRL:` replies, preserve publisher notes and original files, validate, sync the three proof documents, commit with John/Codex attribution and push immediately. Do not ask again for already agreed edits or release timing. Preserve unrelated dirt and other worktrees/archives.

John owns visual PDF review to save tokens. Codex checks source/logs/auxiliary metadata and never marks legibility approved from a successful build. Existing underfull boxes, header-height and PDF-string template warnings remain; no undefined citation/reference, duplicate-label, overfull-box, oversized-float or narrow-column warning in the latest build.

Build only after source changes, or when locators require fresh metadata:

```sh
cd /uufs/chpc.utah.edu/common/home/u0737349/worktrees/air-proofs-round1/proof-package/working
module load texlive/20260330
latexmk -pdf -interaction=nonstopmode -halt-on-error air-4472509-done.tex
```

The proof PDF is ignored: a Git push transfers the corrected source/docs, not that generated PDF. Transfer it explicitly if reviewing on another host. Root Make targets validate later repository integration, not this working proof.

Latest substantive batches, all pushed: `37baff3` (Section 3.4/Figure 4 and A1 approval), `93a2a0c` (Conflicts of Interest break), `2fddf48` (repository URL/release timing). Detailed earlier commits, provider checks and historical visual inspections remain in the catalogue. This handoff/table batch changes no manuscript content.
