# Proof-return handoff — 6 October 2026

**John reports that the proof was submitted to MDPI. His later independent TeX tone pass is checkpointed at `be959eb`; a new local PDF and ZIP await his visual check. Codex has submitted nothing to MDPI and has not uploaded a preprint.**

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
| Return ZIP | `dist/air-4472509-proof-return-author-pass-20261011.zip`; current author-pass TeX/PDF/template/eleven figures; ignored by Git |
| Decisions/evidence/history | `notes/proof-query-catalogue.md`; master register, not superseded by the table |
| Intake/recovery | `proof-package/intake.json`, `proof-package/edit-recovery-20261006.json`, `proof-package/working-copy.json` |
| Terrain/software evidence | `proof-package/terrain-source-evidence-20261006.json`, `proof-package/software-version-evidence-20261006.json` |

The refreshed TeX locators match working source SHA-256 `3dec02cd7aad5da9411977403d4f7b3738d8ba87da096c993a1496447fb4b55e`. The author-pass build remains 18 pages, but printed wording changed after the earlier visual approval. **There are no printed PDF line numbers**; PDF pages are navigation aids until John checks the new PDF. Codex did not render it.

## NEXT — author-pass review and public release

1. John confirmed on 11 October that pages 7–8, resized Figures 5–9 (pages 9–12), Tables A2–A6 (pages 14–15), and back matter (page 16) are clear. A1 was already approved. That approval applies to the earlier PDF; John needs to check the new author-pass PDF.
2. The reply table's 50 current-proof rows are checked; PUB01 is complete. MDPI04a's approved reply is scoped to the incomplete multi-network instrument inventory while retaining documented provider facts. Named AI models/CLI use remain author-confirmed, without a per-session/snapshot claim.
3. John approved the earlier 23 replies on 11 October. The MDPI18 reply was updated after he clarified that Gemini belonged to another project. The local source/ZIP are for review; Codex is not sending them to MDPI. Source comments are not printed replies.
4. The current TeX/PDF/support ZIP is in `dist/`; ZIP integrity and an isolated 18-page build passed. ZIP SHA-256: `4ec9052502a2bc893d01c41ad836010b9c9be779a8323c994e5685a02e10d72b`. Root `main.tex`/`submission-package` integration, required Make checks/package refresh, protected-main PR/merge and journal submission remain separate actions.
5. **PUB01 complete:** John reported proof submission; the GitHub repository was made public on 11 October. Anonymous API, proof-branch and raw-TeX requests succeeded. Data Availability now uses present tense. Default `main` remains older; its review/proof integration is separate.

## Continue the agreed batch pattern

Name the catalogue code, make minimal changes with standalone `% JRL:` replies, preserve publisher notes and original files, validate, sync the three proof documents, commit with John/Codex attribution and push immediately. Do not ask again for already agreed edits or release timing. Preserve unrelated dirt and other worktrees/archives.

John owns visual PDF review to save tokens. Codex checks source/logs/auxiliary metadata and never marks legibility approved from a successful build. Existing underfull boxes, header-height and PDF-string template warnings remain; no undefined citation/reference, duplicate-label, overfull-box, oversized-float or narrow-column warning in the latest build.

Build only after source changes, or when locators require fresh metadata:

```sh
cd /uufs/chpc.utah.edu/common/home/u0737349/worktrees/air-proofs-round1/proof-package/working
module load texlive/20260330
latexmk -pdf -interaction=nonstopmode -halt-on-error air-4472509-done.tex
```

The proof PDF and return ZIP are ignored: a Git push transfers source/docs, not generated artifacts. Transfer `dist/air-4472509-proof-return-author-pass-20261011.zip` explicitly if reviewing on another host. Root Make targets validate later repository integration, not this working proof.

Latest substantive batches, all pushed: `37baff3` (Section 3.4/Figure 4 and A1 approval), `93a2a0c` (Conflicts of Interest break), `2fddf48` (repository URL/release timing). Detailed earlier commits, provider checks and historical visual inspections remain in the catalogue. The 11 October update changes one source comment; printed manuscript content is unchanged.

Final-check handoff/reply-table commit: `124a552d3751cab0680ed976873318a02aaa2e06`; pushed to `origin/jrl/proofs-round1`. Source and original proof files remain unchanged.
