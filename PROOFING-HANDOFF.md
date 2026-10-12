# Proof-return handoff — 6 October 2026

**The requested proof edits and author visual check are complete; final reply approval and delivery remain. Nothing has been submitted or made public by Codex.**

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
| Draft journal replies | `PROOFER-RETURN-REPLIES.md`; one proposed reply for each of the 23 MDPI/EE notes |
| John's final review route | `PROOFER-FINAL-REVIEW.md`; terse microtasks, files and PDF pages before approval |
| Return ZIP | `dist/air-4472509-proof-return-20261011.zip`; corrected TeX/PDF/template/eleven figures; ignored by Git |
| Decisions/evidence/history | `notes/proof-query-catalogue.md`; master register, not superseded by the table |
| Intake/recovery | `proof-package/intake.json`, `proof-package/edit-recovery-20261006.json`, `proof-package/working-copy.json` |
| Terrain/software evidence | `proof-package/terrain-source-evidence-20261006.json`, `proof-package/software-version-evidence-20261006.json` |

The reply-table locators match working TeX SHA-256 `1a9b07bea5821956813ac0e1317e45967392b47628bd5d508ef4167cdcce74c3`. The 11 October comment-only edits rebuilt to 18 pages with identical extracted PDF text. PDF pages use compiled labels/source metadata; **there are no printed PDF line numbers**, so the table marks them “—”. Refresh the map if TeX or layout changes. Codex did not load/render the PDF.

## NEXT — final replies and return assembly

1. John confirmed on 11 October that pages 7–8, resized Figures 5–9 (pages 9–12), Tables A2–A6 (pages 14–15), and back matter (page 16) are clear. A1 was already approved. The author visual check under MDPI05b is complete for this PDF.
2. The reply table's 50 current-proof rows are checked; PUB01 remains open. MDPI04a's approved reply is scoped to the incomplete multi-network instrument inventory while retaining documented provider facts. Named AI models/CLI use remain author-confirmed, without a per-session/snapshot claim.
3. John approved all 23 replies in `PROOFER-RETURN-REPLIES.md` on 11 October. Use `PROOFER-FINAL-REVIEW.md` for his review of the assembled return, then obtain final approval before sending. Source comments are not printed replies.
4. The corrected TeX/PDF/support ZIP is in `dist/`; ZIP integrity and an isolated 18-page build passed. ZIP SHA-256: `0473c9da4ad9234e0e790973ca86dbbd0c7f1f05bda3fcfbe68b9367f832dded`. Root `main.tex`/`submission-package` integration, required Make checks/package refresh, protected-main PR/merge and journal submission remain separate actions.
5. **PUB01 after confirmed proof submission:** make the repository public as John has instructed, with his selected provenance prepared; verify unauthenticated access and reconcile availability wording with the final published proof. Current Data Availability gives `https://github.com/Bingham-Research-Center/latex-jrl-mjd-mdpiair-2026` and says it will be publicly available after proof submission. Last live API check (6 October): private. Timing is authorised; do not change visibility before submission.

## Continue the agreed batch pattern

Name the catalogue code, make minimal changes with standalone `% JRL:` replies, preserve publisher notes and original files, validate, sync the three proof documents, commit with John/Codex attribution and push immediately. Do not ask again for already agreed edits or release timing. Preserve unrelated dirt and other worktrees/archives.

John owns visual PDF review to save tokens. Codex checks source/logs/auxiliary metadata and never marks legibility approved from a successful build. Existing underfull boxes, header-height and PDF-string template warnings remain; no undefined citation/reference, duplicate-label, overfull-box, oversized-float or narrow-column warning in the latest build.

Build only after source changes, or when locators require fresh metadata:

```sh
cd /uufs/chpc.utah.edu/common/home/u0737349/worktrees/air-proofs-round1/proof-package/working
module load texlive/20260330
latexmk -pdf -interaction=nonstopmode -halt-on-error air-4472509-done.tex
```

The proof PDF and return ZIP are ignored: a Git push transfers the corrected source/docs, not those generated artifacts. Transfer `dist/air-4472509-proof-return-20261011.zip` explicitly if reviewing on another host. Root Make targets validate later repository integration, not this working proof.

Latest substantive batches, all pushed: `37baff3` (Section 3.4/Figure 4 and A1 approval), `93a2a0c` (Conflicts of Interest break), `2fddf48` (repository URL/release timing). Detailed earlier commits, provider checks and historical visual inspections remain in the catalogue. The 11 October update changes one source comment; printed manuscript content is unchanged.

Final-check handoff/reply-table commit: `124a552d3751cab0680ed976873318a02aaa2e06`; pushed to `origin/jrl/proofs-round1`. Source and original proof files remain unchanged.
