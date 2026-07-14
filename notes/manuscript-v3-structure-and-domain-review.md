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
| New Figure 1 locator | working two-panel structure now in v3 | Panel (b) uses `figures-draft/nested_domains.png`; regenerate panel (a), remove all unused transects, and restyle both panels without latitude/longitude axes. |
| New episode-context figure | add after locator | Pair a verified 1--3 February MODIS snow/true-color view with January--February observed ozone and a marked 2 February line. |
| Observed four-station evolution | keep | Required surface-weather context; do not call it a vertical profile. |
| Station pseudo-profiles | remove | Horizontally displaced sites do not form an observed inversion profile. |
| Common-pipeline contrast panel | keep, with shorter explanation | It shows the response hierarchy on one common pipeline without declaring a winner. |
| Common-AGL retention/ventilation | keep two panels; regenerated | Stability and transport wind are load bearing; the scheme-dependent PBL-height panel was removed on 14 July. |
| Two-site bulk-theta panel | appendix option only | The surface index survives in Appendix A data; restore a line-free image only if it adds information beyond the table. |
| Driving spatial maps | editorial review only | The gate failed; retain the registered d02 map temporarily for the patchiness it shows, then choose supplement or reserve. |
| Figure 6 terrain sections | replace previous driving section | Use matched d03 north--south and east--west X0-minus-X4 sections at 16 UTC; retain as an exploratory candidate until a CMP11 d03 gate exists. |
| Heat-deficit trajectory | Appendix A; regenerated | Scientifically useful support, but too secondary for the main sequence; compact shared-style render inspected on 14 July. |
| CMP08 table; map/section removed | Appendix A table | Main text retains the direct metric tradeoff; unreadable maps stay archived. |
| CMP07 registered aspect panel | Appendix A figure | Interesting measurement-limited null; no main-text figure. |
| Default/fine feedback maps | omit from manuscript | Quantitative bounds are sufficient; near-null maps add pages more than information. |
| CMP09 terrain panel | omit from manuscript | Failed gate and two near-null panels. If revived, regenerate only terrain difference and elevation-band response as a compact appendix figure. |
| CMP11 top-down heat deficit | carry d02 and d03 for review | d02 supplies basin-wide context, including Browns Park, Split Mountain, and Tavaputs canyons; d03 supplies inner-basin detail. Hold time, sign, crest, and scale fixed. |
| Remaining terrain engine gallery | archive | No other gallery panel currently answers a sharper manuscript question. |
| Initialization profiles | regenerate narrowly | Two panels only: X6 and X5 at Horsepool, 12 UTC and 13 UTC, identical axes. Model-only context; the one-hour change is not pure spin-up. |
| Skew-T gallery | archive | No in-basin observed sounding and too many redundant model-only panels. |
| Resolution-confound table | keep in Methods for now | It is a compact design refusal, not a Results experiment. |

## John terrain-figure clarification, 14 July 2026

The fine-terrain-feedback heat-deficit field is no longer a main-figure candidate.
The editorial target is CMP11, X0 minus X4: fine 3-arc-second minus coarse
5-arc-minute static terrain under the same NAM, one-way, YSU/MM5 configuration.

Carry two distinct top-down heat-deficit views until visual review:

- d02 for the basin-wide redistribution pattern and possible upstream storage regions;
- d03 for inner-basin detail on the chemistry-grid-scale nest.

These domains are complementary rather than interchangeable.
Browns Park and the full Split Mountain/Tavaputs setting lie outside d03, so the d03
panel cannot replace the d02 regional view.
Both panels must use 16 UTC, X0-minus-X4 orientation, the 2200 m crest reference, and
the fixed +/-1.6 MJ m-2 display scale.
The current d02 render is an exploratory preview; the d03 product must be generated
from `verification/config/figures/pelican2013_terrain_d03.toml` and inspected on CHPC.

The top-down field can motivate, but cannot establish, a reservoir/drainage mechanism.
A defensible mechanism test needs time-resolved heat deficit, common-support cold-air
mass or volume, outlet-normal transport, and vertical velocity/turbulence near an
independently defined pool top.
Moist-convection language additionally requires humidity, cloud-water, precipitation,
and stability evidence.

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

### Bounded CHPC commands from John's figure review

Refresh the d02 CMP11 top-down heat-deficit difference without changing the audited
default case configuration:

```bash
sbatch verification/slurm/pelican_figures.slurm \
  --case nam_terrain3s,nam_terrain5m \
  --figure heatdeficit_map \
  --time 16 \
  --output-dir /scratch/general/vast/$USER/latex_jrl_cmp11_d02_review
```

Generate the matched d03 top-down field and both d03 terrain sections from the bounded
two-run configuration:

```bash
PELICAN_FIGURE_CONFIG="$PWD/verification/config/figures/pelican2013_terrain_d03.toml" \
sbatch verification/slurm/pelican_figures.slurm \
  --case fine,coarse \
  --figure difference,heatdeficit_map \
  --time 16 \
  --output-dir /scratch/general/vast/$USER/latex_jrl_cmp11_d03_review
```

Generate only the two driving-product profiles at initialization and one hour later:

```bash
sbatch verification/slurm/pelican_figures.slurm \
  --case gfs,nam \
  --figure profile \
  --lead 0,1 \
  --output-dir /scratch/general/vast/$USER/latex_jrl_gfs_nam_profiles_review
```

After visual inspection, copy and rename only the selected files into `figures-draft/`
using the filenames already wired in `_manuscript_v3.tex`.
Record the exact command, Slurm job, input paths, generator commit, config hash, and
output hash in `figures-draft/HARVEST.md`.
Registration and promotion remain separate decisions.

## Figure-to-text audit

| Figure material | Insight now stated in body/caption | Remaining gap |
|---|---|---|
| Two-panel locator | d02 carries the full network; d03 is an interior nest, not a validation target | Final geographic labels, north arrow, scale bar, and removal of legacy transects |
| Observed temperature evolution | Recurring floor-to-bench separation changes through the diurnal cycle | Provider QC, sensor metadata, and reuse conditions |
| Common-pipeline effects | Driving-product response dominates shared lower-layer metrics; pressure/wind error prevent an overall ranking | Register and restyle the working plot |
| Retention/ventilation | Caption now carries the approximate 3.6 K and 0.8--1.0 m s-1 separations | Independent vertical observation remains absent |
| Driving-product map | Early patchiness and the failed sign-share criterion are explicit | Editorial main/supplement/reserve decision |
| CMP11 d03 sections | Caption will state fine-minus-coarse sign and prohibit drainage/wave inference | CHPC render, inspection, and a declared d03 terrain gate |
| CMP11 d02/d03 top-down heat deficit | Sign, domain roles, named regional features, common crest/scale, and single-time limitation are explicit | d03 render plus time-resolved/common-support quantification |
| Horsepool 12/13 UTC profiles | Planned caption distinguishes initialized state from one-hour evolution and states the no-observation limit | CHPC render and actual profile interpretation |
| Heat-deficit trajectory | State offset versus within-window change is explicit | Longer controlled integrations before persistence claims |
| Slope-radiation diagnostic | Aspect response and measurement-limited failed gate are explicit | Slope-corrected flux output if revisited |

### Unused-figure triage after visual review

| Candidate | Decision | Why |
|---|---|---|
| `theta2m_terrain-3arcsec-5arcmin_16z.png` | strong supplement/reviewer-reserve candidate | The d03 +/-4 K local response is visually strong and can connect the top-down heat-deficit field to surface thermal structure, but it has no declared CMP11 gate and should not displace the requested heat-deficit views. |
| `wrf_upper_700hPa_gfs_minus_nam2way_d02` | reviewer reserve | The 14/16 UTC positive driving-product response is coherent and weakens by 18 UTC, which is useful origin context; 700 hPa intersects terrain and the initial-versus-boundary source remains unresolved. |
| `wrf_upper_500hPa_gfs_minus_nam2way_d02` | archive | The response changes sign and is less coherent, adding little beyond the lower-layer and 700 hPa diagnostics. |
| Engine `heat_deficit_timeseries.png` | do not use | The audited ANA-16 trajectory supersedes this exploratory point/engine product. |
| Remaining skew-T, feedback, slope, and gallery panels | archive unless a new question is declared | They are redundant, near-null, measurement limited, or model-only and would add pages without sharpening the current terrain/driving-state story. |

## Remaining bounded work

1. Generate and inspect the clean geographic panel for the two-panel locator.
2. Run the bounded d02/d03 CMP11 and two-member profile commands above; inspect before copying.
3. Harvest the least-cloudy 1--3 February MODIS candidate and record its granule provenance.
4. Reconcile Horsepool/UBWOS and AQS ozone coverage before choosing sites or aggregation.
5. Rerender the Appendix A slope-radiation diagnostic without coordinate axes.
6. Update the remaining candidate hashes only after CHPC visual inspection.

Failed gates remain failed throughout these trims.
No d03 result should be added until the common support and sample are declared.
