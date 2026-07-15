# Final-draft readiness review — 15 July 2026

## Verdict

`jrl/codex-v3-integration` is the best branch from which to start the final
author draft.
It contains the selected Architecture C lineage, every substantive CHPC return,
the X8 review packet, the literature closure, hardened build checks, independently
reproduced episode context, and the audited manuscript promotion.
Do not merge another live branch into it before author review.

The manuscript lineages are now deliberately different:

- `main.tex` is the 17-page final-draft starting point: the central argument,
  evidence tables, and only dual-promoted figures.
- `_manuscript_v3.tex` is the 26-page maximal caretaker record: it preserves
  diagnostic terrain, radiation, and X8 material without promoting those claims.
- ignored `jrl_manuscript.tex` is an exact local copy of v3 for John's last-Codex
  review and is not part of Git or the submission package.
- `_manuscript_test.tex` remains the experimental blank-slate scaffold.

The manuscript audit anchor is `59fa4a0`.
The preceding verified concerns are `234ec7c` (build/submission hardening) and
`a29fd68` (independent ozone-context reproduction).

## Branch and PR audit

| Ref | Finding | Disposition |
|---|---|---|
| `jrl/codex-v3-integration` | Contains `main`, literature closure, the finishing return, X8, and the current manuscript state. | Continue here; PR into protected `main`. |
| `origin/jrl/chpc-20260715-v3-finishing-return` | Already an ancestor of the current branch. | Donor history only. |
| `origin/jrl/chpc-20260714-v3-figure-review` | Its bounded return was integrated by an equivalent Akamai commit, so the remote commit itself is not an ancestor. | Do not merge; preserve as execution history. |
| `jrl/ref-obs-expansion-2026-07` | Two reference-only commits add exploratory prose and preview Parquets. | Leave unmerged; see options below. |
| `main` and `prep-final-latex` | Both remain at `f0c945b`, before all current integration work. | Neither is a better drafting base. |
| `legacy/*` | Old donor histories contain unreviewed scaffold and figure work. | Read-only archaeology; never merge wholesale. |

At the audit snapshot, PR #6 was open and GitHub considered the branch mergeable,
but protected review left it blocked and no status checks were reported.
Push this branch and update that PR; do not merge it until the required register is
closed far enough for coauthor review.

## Cross-repository audit

| Repository | Current evidence | Rule for this paper |
|---|---|---|
| `../brc-tools` | Clean `main` at `2e1f84b`; contains X8 work from PR #37 and the AQS client from PR #38. The manuscript accepts `548fee4` or newer. Targeted verification previously passed 47 tests; the final AQS rerun passed 6 tests. | Reusable download, reduction, verification, and plotting code lives here. Record the exact commit for every generated artifact. |
| `../lawson-davies-air-wrf-2026` | Legacy donor at `7009711` on `jrl/first-draft`, with John's existing change to `FIRST-50-MICROTASKS.md`. | Leave untouched. This repository supersedes its manuscript and checklist; mine history only through explicit evidence routes. |
| Historical `brc-wrf` references | No current sibling checkout is present on this writing host. Old run rows retain commit labels from execution time. | Those labels are provenance notes, not a live source of truth. Run identity comes from the paper inventories, WRF headers, namelist fingerprints, and immutable CHPC packets. |
| Any `wrf-chpc` checkout on another host | Build/toolchain context may differ from the paper's as-run WRF 4.8.0 cases. | Never use a build-repo version or default as production-run evidence. |

No sibling repository was edited during this review.

## Science and mathematics audit

The defensible paper is a short-window deterministic sensitivity study.
Its primary result is a repeatable GFS-versus-NAM supplied-state offset under
both feedback settings, not a general ranking of forecast systems and not a
causal attribution to initial rather than lateral boundary conditions.
The strongest matched signals are about 3.6 K weaker common-AGL stability,
0.8--1.0 m s-1 stronger transport flow, and about 1.2 MJ m-2 less heat deficit
for the GFS-driven pair.
The within-source feedback effects are much smaller over the five-hour window.

The promoted heat deficit now uses

`H = (c_p/g) integral[p_c to p_s] max(theta_crest - theta(p), 0) dp`,

with `p_c < p_s`, a fixed registered footprint, and a predeclared central
2200 m crest value within a 2100--2300 m sensitivity bracket.
The paper reports a state offset; the faster-loss gate failed and remains failed.
The two-hour circular-block intervals are labeled descriptive dependence checks,
not confidence intervals from five independent hours.

The AQS panel reproduces 295 EPA-reported daily summaries for five selected sites.
It marks low within-day coverage and makes no threshold, attainment, chemistry,
WRF-validation, or meteorological-causation claim.
The MODIS panel is qualitative calendar-day browse context, not a quantitative
snow retrieval.

Before submission, the remaining evidence work is verification or removal:
historical Synoptic request/QC/licensing, exact product/model citations, final
author review of configurations and interpretation, and release metadata.
No new WRF integration is required to begin the final draft.

## Code, figures, and package audit

- `make final-draft-check` unifies manuscript, rewrite, v3, smoke, and contract
  checks; `make submission-check` validates the clean allowlisted package.
- The submission contract admits nine exact figure files and five current
  bibliography keys. Candidate and X8 figures cannot leak into `main.tex`.
- The episode-context generator is deterministic and records input, script, and
  output hashes. The final PDF passed full-resolution and manuscript-layout review.
- The 17-page main and 26-page v3 PDFs have no undefined citations/references or
  overfull/underfull boxes. Dated review snapshots are under `drafts/`.
- `paperpile.bib` remains intentionally untouched pending John's complete small
  export. The final package must never be repaired by guessed keys.
- The final 15 July rerun passed `make final-draft-check` and
  `make submission-check`; the four live CSV registries are rectangular, the
  edited JSON and shell files parse, and all 100 task IDs occur exactly once.

## Narrative audit

The title and abstract now lead with the tested short-window sensitivity rather
than promise cold-pool persistence or ozone chemistry.
Methods state the estimands and exact window before interpretation.
Results separate absolute run states from matched contrasts.
Discussion distinguishes a supplied-state offset from loss, exposes the small
feedback response, and states what the design cannot show.
The final author pass should shorten where possible, add only verified citations,
and preserve the negative gates; it should not expand the paper merely because v3
contains more panels.

## The dead-end observation branch, in plain language

### Option 1 — merge it

**Pro:** fastest way to inherit all exploratory notes and previews.

**Con:** it also imports reference-only prose, large preview Parquets, mixed source
quality, and claims that would need to be audited again.

### Option 2 — cherry-pick selected commits

**Pro:** preserves the branch's history while limiting the import.

**Con:** its useful idea has already been reproduced more cleanly from current EPA
AirData with hashes, tests, coverage markers, and narrower claims.

### Option 3 — reproduce the useful result independently and leave the branch alone

**Pro:** gives the paper useful episode context with a clean provenance boundary and
no inherited draft debt.

**Con:** duplicates some exploratory effort and deliberately leaves the old branch
as historical clutter until post-merge cleanup.

### Option 4 — omit the observation expansion

**Pro:** produces the leanest meteorology-only paper.

**Con:** removes useful visual context for why 2 February belongs to the episode and
makes the Air-facing motivation more abstract.

**Chosen path:** Option 3.
Keep `jrl/ref-obs-expansion-2026-07` unmerged and read-only.
The current branch independently reproduces only the defensible AQS/MODIS context.
John can still choose Option 4 during figure review by removing the promoted context
panel and its bounded prose; no scientific result depends on that panel.

## Start the final draft

1. Read `main.tex` as an author, not as an evidence-mining document.
2. Work through the required rows of `tasks/final-draft-100.md` in order, beginning
   with the thesis/title and number audit.
3. Use `_manuscript_v3.tex` only as a donor when a required row identifies a gap.
4. Treat every `HV` row as optional; none is permission to reopen a failed gate.
5. Circulate the dated main snapshot after the first author pass, then record
   Michael's provenance review and Loknath/Seth's chemistry-framing review.
