# Proofing restart — 5 October 2026

Start here:
```sh
cd /uufs/chpc.utah.edu/common/home/u0737349/worktrees/air-proofs-round1
git status --short --branch
```
Read `AGENTS.md` and `proof-package/intake.json`, then only the source/PDF and evidence needed for the immediate query.

## State

- Branch `jrl/proofs-round1`, local only; created from live-verified GitHub `main` at `5ce57e6`.
- Baseline commit `92b14d2`: all 33 received files copied and committed unchanged, plus intake receipt; byte-for-byte comparison passed.
- Received source/PDF: `proof-package/air-4472509-english/air-4472509-done.{tex,pdf}`; PDF is 18 pages.
- Source has 22 `%MDPI:` comment occurrences (several contain multiple requests) and one `%EE:` title-change note; no corrections or confirmations have been made.
- Source embeds its bibliography. The inherited README's `main.tex`/`main.bbl` instructions are stale.
- No compilation, full visual proof audit, pruning, push, merge or journal submission has been performed in this proofing session.

## Next work

1. The [proof query catalogue](notes/proof-query-catalogue.md) now records all 22 `%MDPI:` comments and the `%EE:` title note, with exact quotations, source/PDF locators, proposed responses and outstanding evidence/author facts. All follow-ups remain open; begin resolution from that register. It also records unassigned highlights and the duplicate Table A5 label.
2. Copy the received directory to `proof-package/working/`; edit/compile only that copy. Preserve editorial queries and the received baseline.
3. Verify software versions against the actual analysis provenance; do not insert versions from today's environment. Confirm personal details and editorial acceptance from John/saved decisions.
4. Build `air-4472509-done.tex` in the working directory and inspect all pages against the supplied PDF. Resolve scientific wording against the claim ledger and exact artefacts only.
5. When integration is requested, update root `main.tex`/package deliberately, run required Make checks, inspect PDFs, then use a PR into protected `main`.

## Git and other checkout

- Original checkout remains `/uufs/chpc.utah.edu/common/home/u0737349/gits/latex-jrl-mjd-mdpiair-2026` on `jrl/peer-review-round1`; its uploaded `proof-package/` and `notes/print-review-checklist-2026-09-16.md` remain untracked. Do not remove them during cleanup.
- Local `main` is still `f0c945b`; GitHub `main` was `5ce57e6`. Recheck live remote tips before promotion/pruning.
- PR #8 squash commit `309e532` has the same file tree as `jrl/peer-review-round1` at `5129714`; ancestry reports alone therefore overstate unmerged work. Do not merge every old branch.
- Pruning candidates already reachable from verified `origin/main`: local `jrl/chpc-figure-inventory`, `jrl/consolidate-study-truth`; remote `jrl/paperpile-refresh-20260918`, `prep-final-latex`. Archive other tips before deletion; two old finishing branches have linked worktrees, and the July figure-review tip needs its own check.
- Review decisions/replies live outside Git at `~/reviews/lawson-ozone-wrf-mdpiair-2026/` on the writing host. Earlier roadmap approval statements are not proof acceptance.
