# Manuscript v3 experiment structure and domain review

Status: active structural review, 14 July 2026.

This note records why the maximal draft is ordered as it is, what should be cut
next, and what the current d02 evidence does and does not establish.
It does not change any gate outcome or promote any figure.

## Vocabulary

- `X*` identifies a simulation configuration or run.
- `CMP*` identifies a contrast between runs.
- The scientific experiment is the lever isolated by a controlled contrast.
- X3/X5/X6/X10 form the **default-terrain driving-product/feedback matrix**.
- Avoid manuscript-facing use of `factorial` unless the statistical design itself
  must be discussed; the term is technically defensible but unhelpful here.

The run graph is more informative than its numeric order:

```text
                         driving product
              X5 NAM two ---------------- X6 GFS two
                 |                            |
  default        | feedback                   | feedback
  terrain        |                            |
              X3 NAM one ---------------- X10 GFS one
                 |
                 | terrain source
                 |
  fine        X0 NAM one ---- X1 slope ---- X2 MYJ/Eta
  terrain        |
                 | feedback
                 |
              X9 NAM two

  coarse      X4 NAM one, joined to X3 and X0 by terrain-source brackets
```

X7/X0/X8 are not a resolution branch because the members differ in many design
dimensions at once.

## Ordering rule

Manuscript order follows four questions, not run creation date or identifier:

1. What changes on the common station/common-AGL pipeline, and by how much?
2. Which repeated contrast best bears on the cold-pool state supplied to chemistry?
3. Which secondary process response is coherent enough to add information?
4. Which small, failed, or confounded comparisons are useful only as robustness,
   diagnostic, or design findings?

The resulting Results order is:

1. observed surface context;
2. all common-pipeline contrasts on one effect-size display;
3. driving-product response and its surface, vertical, and heat-deficit evidence;
4. PBL/surface-layer and slope-radiation treatments;
5. nest-feedback robustness at default and fine terrain;
6. terrain-source brackets.

The prohibited apparent resolution ladder is handled as a design exclusion in
Methods and a short design lesson in Discussion, not as a Results experiment.

This still lets the driving-product result lead because it is the largest repeated
response on the Air-relevant lower-layer metrics, not because X3/X5/X6/X10 were
audited first.

## d02 versus d03

### Confirmed reason for d02

All controlled X0--X6/X9/X10 simulations archived d02 and d03 output.
The current d02 choice is therefore not forced by missing d03 files.

d02 contains the eleven-station floor-to-bench network.
The roughly 50 by 48 km d03 excludes most bench and basin-end stations: seven of
eleven station mappings clamp to its boundary, leaving only four usable interior
columns (USU07, USU02, USU08, and KVEL).
Using d03 alone would change both grid spacing and station sample.

The defensible present statement is:

> d02 is the common domain for the full-network evaluation estimand; d03 transfer
> has not been tested.

It is not defensible to say that d02 is the better grid, that 1 km is sufficient,
or that a d02 response has the same magnitude or ordering at 333 m.

### Could d02 undervalue a configuration?

Potentially, but the current archive analysis cannot identify that outcome.
A 1 km field can smooth slope, tributary, drainage, terrain-edge, and nest-boundary
responses, so the concern is most material for CMP07, CMP09--CMP11, and possibly
the feedback contrasts.
The same concern is weaker for a basin-wide driving-product offset, but even that
must be tested rather than assumed.

The opposite failure is also possible: d03 can make a detailed pattern look more
credible while providing poorer observation coverage and a smaller spatial target.
The right question is whether a controlled **contrast transfers between nests**,
not whether a visually finer field is automatically a better simulation.

### Proposed domain-transfer gate

Run this on CHPC from the archived d02/d03 outputs; no new WRF integration is
needed.

1. Define a d03-interior polygon with a fixed boundary buffer before viewing
   contrast fields.
2. Restrict d02 to that same geographic support.
3. Conservatively aggregate d03 to the d02 support for area statistics; do not
   compare raw cell counts or unmatched masks.
4. For the station leg, use the same four interior stations on both domains.
5. Compute each selected contrast on each domain first, then compare
   `[X_a-X_b]_d03 - [X_a-X_b]_d02`.
6. Predeclare sign-retention and material-magnitude-change criteria for 2 m
   potential temperature, 50--500 m stability, transport wind, and one
   process-specific spatial metric.
7. Report a split verdict: station-sample transfer and area/structure transfer.

Start with CMP01/CMP02, CMP08, CMP07, and one feedback contrast.
Add a terrain bracket only after its d03 terrain-support and mask definitions are
fixed.
This is a nest/domain-transfer analysis, not an independent grid-spacing experiment.

## Figure trim ledger

| Material | Current decision | Reason / next action |
|---|---|---|
| Observed four-station evolution | keep | Only promoted observed event-context panel; do not call it a vertical profile. |
| Station pseudo-profiles | supplement or remove | Visually tempting but horizontally displaced and not an observed inversion. |
| Common-pipeline contrast panel | keep in maximal draft; register before circulation | Now includes CMP01--CMP08 rows that share the frozen pipeline instead of privileging the default-terrain matrix. |
| Common-AGL retention/ventilation | keep | Load-bearing Air-relevant result and promoted. |
| Two-site bulk-theta panel | withheld | Restore only after line-free CHPC regeneration, hash update, inspection, and a distinct role. |
| Driving spatial maps/sections | keep one registered map panel; reserve the section | ANA-19 failed its conjunction; the retained map displays the failed floor-coherence criterion and its margin is explicit. |
| Upper-air panels | remove unless they explain a retained lower-layer result | Diagnostic context currently exceeds its evidential role. |
| Heat-deficit trajectory | conditional keep | Supports the weaker-state and failed faster-loss criteria; it is the defensible heat-deficit figure. |
| Engine heat-deficit map/time series | remove from coauthor draft | Different or unaudited reductions duplicate the registered trajectory. |
| CMP08 table; map/section removed | keep the quantitative item only | Strongest coherent non-driving result; the exploratory render is unreadable at manuscript scale and has no predeclared spatial criterion. |
| CMP07 registered aspect panel | keep as diagnostic | Shows why the station null is not treatment inertness and documents the measurement-limited gate. |
| CMP07 sunrise/late-morning and heat-deficit renders | removed from manuscript | Redundant once the registered aspect panel is present. |
| Default/fine feedback maps | remove from coauthor draft | Quantitative bounds are sufficient; near-null maps add pages more than information. |
| CMP09 registered terrain panel | conditional diagnostic keep | It records a failed predeclared gate honestly. |
| Terrain engine map/section/heat-deficit gallery | remove from coauthor draft | No gate-passed claim; retain reproducibly outside the manuscript. |
| Initialization profiles/skew-Ts | removed from manuscript | Model-only, no colocated sounding, and cannot separate initial from boundary influence. |
| Resolution-confound table | Methods, supplement, or one Discussion paragraph | Useful design refusal, but not a Results experiment. |

## Next structural trim

Completed in this pass: combined the two feedback sections, removed their map
gallery, reduced terrain to the registered failed-gate panel, removed redundant
CMP07/heat-deficit/spatial galleries, and removed model-only initialization and
station pseudo-profile figures; moved the resolution-confound table into Methods;
deleted the catch-all small-findings queue after routing its supported points; and
moved the threshold-sensitive heat-deficit mechanism hypotheses out of manuscript
prose until a longer, predeclared analysis exists.

1. Reassess the domain locator after the prose is stable; keep it only if readers
   still need the d02/d03 geometry to understand the estimand.

Failed gates remain failed throughout these trims.
No d03 result should be added until the common support and sample are declared.
