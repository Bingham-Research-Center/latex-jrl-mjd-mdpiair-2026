# Architecture C hybrid handoff

**Status update — 14 July 2026:** this gate-closing specification is complete and retained
as decision history.
All five gates were executed and frozen in `rewrite/HYBRID-GATE-REVIEW.md`.
The active route is `notes/manuscript-v3-integration-plan.md`; do not rerun the copy-ready
prompt below as current work.

**Prepared 13 July 2026 for the next writing-host session.**

**Historical decision:** John selected Architecture C, the hybrid package in
`rewrite/RESULTS-ARCHITECTURE-DECISION-PACKET.md`.
Do not reopen the A/B/C choice.
The next phase at the time was targeted evidence-gate closure; that phase is now complete.

## Frozen editorial structure

- Main C1, the observed event, and Main C2, the confirmed driving-state response,
  are the fixed anchors. Their existing metadata and coauthor-wording gates still
  apply.
- Main C3 must show where and at what height the driving-state response occurs.
- Main C4 must earn any cold-pool maintenance claim with a validated heat-deficit
  trajectory.
- Main C5 may contain one terrain result only if a controlled, terrain-aware result
  survives analysis.
- Main C6 may contain one of CMP07 slope/shading or CMP08 PBL/surface-layer only if
  it adds a coherent, nonredundant process decision.
- Supplement C2 bounds feedback under default and fine terrain; feedback is not the
  paper's thesis.
- X7/X8 and heterogeneous legacy/nudging runs remain design context, not controlled
  sensitivities.

No figure count is guaranteed.
If a gate fails, drop or demote the slot rather than filling it with a suggestive
render.

## Gate-closing order

| Order | Slot and question | Exact work | Stop condition |
|---|---|---|---|
| 1 | Main C4 / ANA-16: does the cold pool remain weaker in the GFS-driven members after spin-up? | Freeze the heat-deficit definition, crest/reference surface, integration volume, masks, units, domain, and retained window; verify the 13--18 UTC trajectories and reasonable boundary/threshold sensitivities from exact X6/X5 and X10/X3 inputs. | No maintenance wording unless the post-spin-up result is reproducible and robust enough for a confirmed claim-ledger row. |
| 2 | Main C3 / ANA-19: is the confirmed driving-state response coherent over the basin floor and shallow layer? | Select matched 14/16/18 UTC maps and sections by a stated rule; verify common-AGL interpolation, terrain/mask behavior, sign, source paths, and consistency with the promoted retention metrics. | No spatial/vertical promotion from visual inspection alone or from a single cherry-picked time. |
| 3 | Main C5 / ANA-17: does terrain add a distinct geometry result? | Analyse CMP09 (X3-minus-X0) first with predeclared floor/rim/tributary and elevation-aware diagnostics. Use CMP10/CMP11 only if the X4 lineage is resolved. | Omit C5 if the result is aggregate-only, redundant with C3/C4, or still depends on unresolved X4 identity. |
| 4 | Main C6 / ANA-18: does radiation or PBL/surface-layer treatment add one distinct process result? | Screen both CMP07 and CMP08 on their predeclared radiation/energy and common-AGL/flux diagnostics; compare coherence, provenance, and editorial information gain before choosing at most one main result. | A small or null result may go to Supplement C4; do not choose from appearance or aggregate bias alone. |
| 5 | Supplement C2 / ANA-20: is the small feedback response robust at fine terrain? | Recompute CMP06 on the same matched surface, common-AGL, and process definitions used for the default-terrain feedback result; compare effect magnitude honestly with the driver response. | Keep as a table or compact supplement result; do not elevate it because its factorial is complete. |

Use existing immutable outputs first.
Do not submit a new WRF integration for these gates.
If the writing host cannot read a required artifact, route one bounded task through
`rewrite/CHPC-CODEX-PROMPT.md`; do not infer the answer from filenames or archive
coverage.

## Required writeback before prose

Create or maintain `rewrite/HYBRID-GATE-REVIEW.md` with one row for C3, C4, C5,
C6, and supplement C2 containing:

- exact reader question and comparison ID;
- exact runs, domain, sample, time window, inputs, command, and output hash;
- numerical result and visually inspected finding;
- claim-ledger and figure-manifest status;
- pass, fail, or unresolved decision with the falsifier and remaining gate;
- main, supplement, reserve, or dropped disposition.

Write facts first to the authoritative run/data/claim/figure record that owns them.
Register and inspect a selected figure before promotion.
Bring the completed gate review and proposed final C spine to John before changing
`main.tex` or `_manuscript_test.tex`.

## Copy-ready prompt for the next session

```text
Run hostname -f and git status --short --branch. Read AGENTS.md and ROADMAP.md, then read
rewrite/HYBRID-ARCHITECTURE-HANDOFF.md completely and the Architecture C section plus
fallback rules in rewrite/RESULTS-ARCHITECTURE-DECISION-PACKET.md. Work from the exact
committed source ref supplied for the session, and preserve any unrelated dirty checkout.

John selected Architecture C, the hybrid Results package. Treat that as frozen: do not
reopen architectures A/B, do not let the completed feedback factorial become the thesis,
and do not edit main.tex or _manuscript_test.tex yet. C1 and C2 are the fixed anchors;
C3--C6 and supplement C2 remain evidence-gated.

Close the gates in the handoff's order, beginning with ANA-16 and Main C4: validate the
productized heat-deficit definition, masks, units, exact X6/X5 and X10/X3 inputs,
post-spin-up trajectory, and reasonable boundary/threshold sensitivities. Then close the
C3 spatial/common-AGL gate, test CMP09 before any X4-dependent terrain claim, screen both
CMP07 and CMP08 before selecting at most one C6 process result, and finally bound CMP06 as
a supplement result. Use existing outputs; do not launch a new WRF integration.

Use archive-inventory.md only for figure existence, the run/comparison inventories for
identity and design, the manifests for admission, and the claim ledger plus exact
artifacts for prose-ready facts. Record exact runs, domain, sample, window, commands,
hashes, small/null findings, falsifiers, and stale notes. If required data are CHPC-only,
issue a bounded task through rewrite/CHPC-CODEX-PROMPT.md rather than guessing.

Maintain rewrite/HYBRID-GATE-REVIEW.md with pass/fail/unresolved decisions and final
main/supplement/reserve/dropped dispositions. Bring that evidence-gated C spine to me
before changing manuscript prose or promoting figures.
```
