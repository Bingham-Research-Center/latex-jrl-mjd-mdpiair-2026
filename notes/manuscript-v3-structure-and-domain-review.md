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
| New Figure 1 locator | replace current render | Two panels: basin geography and observation sites; d01--d03 nesting. Remove all unused transects and latitude/longitude axes. |
| New episode-context figure | add after locator | Pair a verified 1--3 February MODIS snow/true-color view with January--February observed ozone and a marked 2 February line. |
| Observed four-station evolution | keep | Required surface-weather context; do not call it a vertical profile. |
| Station pseudo-profiles | remove | Horizontally displaced sites do not form an observed inversion profile. |
| Common-pipeline contrast panel | keep, with shorter explanation | It shows the response hierarchy on one common pipeline without declaring a winner. |
| Common-AGL retention/ventilation | keep two panels; regenerated | Stability and transport wind are load bearing; the scheme-dependent PBL-height panel was removed on 14 July. |
| Two-site bulk-theta panel | appendix option only | The surface index survives in Appendix A data; restore a line-free image only if it adds information beyond the table. |
| Driving spatial maps/sections | omit from manuscript | The gate failed and the six maps duplicate a split verdict carried more clearly by Appendix Table A5. |
| Heat-deficit trajectory | Appendix A; regenerated | Scientifically useful support, but too secondary for the main sequence; compact shared-style render inspected on 14 July. |
| CMP08 table; map/section removed | Appendix A table | Main text retains the direct metric tradeoff; unreadable maps stay archived. |
| CMP07 registered aspect panel | Appendix A figure | Interesting measurement-limited null; no main-text figure. |
| Default/fine feedback maps | omit from manuscript | Quantitative bounds are sufficient; near-null maps add pages more than information. |
| CMP09 terrain panel | omit from manuscript | Failed gate and two near-null panels. If revived, regenerate only terrain difference and elevation-band response as a compact appendix figure. |
| Terrain engine gallery | archive | No gate-passed claim requires it. |
| Initialization profiles/skew-Ts | archive | Model only, no colocated sounding, and cannot separate initial from boundary influence. |
| Resolution-confound table | keep in Methods for now | It is a compact design refusal, not a Results experiment. |

## John review pass, 14 July 2026

Completed in `_manuscript_v3.tex`:

- shortened the abstract from an audit inventory to six manuscript-level sentences;
- removed Methods 2.7 and 2.8;
- combined the old Results 3.4 and 3.5 into a short surface/spatial corroboration section;
- moved old Tables 4--6 first into Appendix A, followed by surface, spatial, feedback, and terrain audit tables;
- moved the heat-deficit and slope-radiation figures to Appendix A;
- removed the six-panel spatial map and four-panel terrain figure from the manuscript;
- reduced number-heavy Results subsections to direct findings with Appendix pointers; and
- replaced eleven Discussion subsections with four: lower-layer state, state offset, bounded secondary experiments, and next-experiment limits.

## Figure-production contract

All regenerated figures use the shared manuscript style in
`verification/scripts/plot_obs_feb0102.py`: 6.3-inch full width, sans-serif 9 pt
base text, editable TrueType PDF text, no in-panel manuscript titles, consistent
Okabe--Ito colors, and 600 dpi PNG companions.

Maps suppress latitude/longitude labels and ticks.
They retain a north arrow, scale bar, named geographic features where needed, and
one shared color bar per comparable panel group.
Map limits and display hours remain fixed before rerendering.

Figure 1 requires a paper-specific CHPC render after the geographic source files
are fixed.
The present `plot_wrf_transect_locator.py` has already been changed to remove the
unused transects and coordinate axes; it remains an interim one-panel generator.
The replacement must add a separate d01--d03 domain panel and a geographic panel
with observation sites, named towns, major roads, rivers, basin floor, and mountain
ranges.

For the snow panel, prefer MODIS Terra Collection 6.1 data covering 1--3 February
2013.
Use `MOD09GA.061` for a reproducible surface-reflectance true-color composite or
`MOD10A1.061` for an explicit daily 500 m snow product, select the least-cloudy
date before final layout, and record granule IDs and QA handling.
The reusable download, crop, QA, and RGB/snow rendering code belongs in `brc-tools`;
this repository should retain only the paper configuration, exact command, hashes,
and admitted output.

For ozone, first inventory the 2013 Horsepool/UBWOS archive and EPA AQS coverage.
The candidate regulatory series is parameter 44201 at verified Uinta Basin sites,
but no site should enter the figure until the monitor identity, units, standard,
quality flags, local/UTC handling, missingness, and averaging rule are fixed.
Plot January--February 2013 in ppb, mark 2 February with a red line and short
annotation, and do not imply that the ozone series validates the modeled layer.

## Remaining bounded work

1. Generate and inspect the two-panel locator on CHPC.
2. Harvest the least-cloudy 1--3 February MODIS candidate and record its granule provenance.
3. Reconcile Horsepool/UBWOS and AQS ozone coverage before choosing sites or aggregation.
4. Rerender the Appendix A slope-radiation diagnostic without coordinate axes.
5. Update the remaining candidate hashes only after CHPC visual inspection.

Failed gates remain failed throughout these trims.
No d03 result should be added until the common support and sample are declared.
