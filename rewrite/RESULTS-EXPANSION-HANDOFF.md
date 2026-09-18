# Results and figure-expansion handoff

**Prepared 13 July 2026 for a fresh writing-host session.**

**Execution update, 13 July 2026:** the requested ledger and three architecture packages
now live in `rewrite/RESULTS-ARCHITECTURE-DECISION-PACKET.md`.
John selected Architecture C, the hybrid package, on 13 July 2026.
This audit is retained as decision history; continue through
`rewrite/HYBRID-ARCHITECTURE-HANDOFF.md` and do not repeat the audit or resume manuscript
prose before the selected gates close.

## The correction that starts the next session

The X6/X10/X5/X3 driving-product-by-feedback factorial is the best-audited
**minimum result**, not the scientific scope of the paper.
The existing `_manuscript_test.tex` and `rewrite/blueprint.md` deliberately reduced the
paper to that minimum and then allowed the feedback comparison to dominate the story.
That editorial decision is reopened.

The archive contains X0--X10, including controlled pairs for slope-aware radiation,
PBL/surface-layer treatment, three terrain sources, and feedback at fine terrain.
It also contains spatial, vertical, upper-air, profile, heat-deficit, and station/domain
diagnostics that can carry smaller findings on the way to a larger mechanistic result.
The next session should discover the broadest defensible paper from those materials and
then curate it; it should not begin by defending a two-figure manuscript.

`main.tex` remains the audited review baseline.
`_manuscript_test.tex` remains a useful minimum scaffold, but it is not a scope decision
and should not be expanded until the result/figure architecture below has been audited.

## Decision the next session must produce

Before rewriting prose, answer these questions:

1. Which distinct scientific questions in X0--X10 already have controlled comparisons?
2. Which small findings are confirmed, which are analysis-ready, and which are merely
   visually suggestive?
3. Which figures add a new scientific decision rather than another view of the same
   four-run result?
4. What belongs in a richer main Results section, what belongs in a supplement, and what
   is useful only as a design limitation or reviewer reserve?
5. Does the existing evidence support a configuration-sensitivity paper, a cold-pool
   maintenance/mechanism paper, or a layered combination of the two?

Do not impose a figure count before that audit.
A six- or eight-figure paper is acceptable if every figure advances a separate supported
step; a polished archive image is not sufficient reason to include one.

## Read order and authority

Read only the named routes first:

1. `AGENTS.md`, `README.md`, and `ROADMAP.md`.
2. This handoff.
3. `verification/provenance/run-inventory.csv` and
   `verification/provenance/comparison-inventory.csv`.
4. `verification/figures/archive-inventory.md` and
   `verification/figures/MANUSCRIPT-EXPANSION-HANDOFF.md`.
5. `notes/claim-evidence-ledger.md`, `verification/figures/manifest.csv`, and
   `figures/MANIFEST.md`.
6. `verification/figures/chpc-figure-inventory-2026-07-10.md`, one relevant section at a
   time, for exploratory findings and exact reduction details.
7. `notes/figure-strategy.md`, `notes/narrative-and-hypotheses.md`, and
   `rewrite/blueprint.md` as drafting history, not as a scope mandate.
8. Open one exact figure, data table, provenance record, critique, or source passage only
   when a candidate claim names the need.

Use this precedence when records disagree:

| Question | Authority | Important distinction |
|---|---|---|
| What a run is | `run-inventory.csv`, then its exact as-run artifact | A directory label is not identity. |
| What a comparison isolates | `comparison-inventory.csv` plus member run rows | Its figure-coverage comments can be stale. |
| Which external figures currently exist | `archive-inventory.md` | This outranks older prose inventories. |
| Which local candidate is tracked | `verification/figures/manifest.csv` | Tracked does not mean admitted. |
| Which figure may enter a manuscript | `figures/MANIFEST.md` plus a matching `promoted` row | Engine PNGs remain diagnostics until promotion. |
| Which numerical claim may enter prose | `claim-evidence-ledger.md` plus the exact analysis artifact | Repeated prose is not corroboration. |
| What a literature source supports | Verified underlying passage | A critique or synthesis is a route, not a citation. |

## Known stale or scope-limited statements

Correct these before inheriting any older plan:

- Older revisions of `notes/figure-strategy.md`,
  `verification/figures/evidence-longlist.md`, and the July 10 inventory said X9 had no
  full figures.
  The current archive record and corrected planning notes say X9 has the complete 63-PNG
  standard set, three `thetaz` panels, seven `heatdeficit_map` fields, and a complete
  21-PNG X9-minus-X0 difference set.
- Those older revisions quoted 247 cross-case PNGs and 42 files in
  `diff_terrain_fine`.
  On 12 July the 21 stale mislabeled terrain files were removed and the compare root was
  verified at 324 PNGs.
- The earlier CMP06 note that X9 lacked a full-figure set is corrected in the comparison
  inventory.
  Its more important status remains current: X9-minus-X0 is controlled but has no frozen
  station/common-AGL analysis or confirmed ledger claim.
- The exploratory mechanism note says `heatdeficit_map` is a standalone prototype.
  The map family has since been productized and rendered across the matrix.
  The phase portrait and reservoir anatomy remain threshold-sensitive prototypes, and the
  maintenance interpretation still needs a ledger-grade post-spin-up check.
- The July 13 blueprint is chronologically new but intentionally narrow.
  It is authoritative for the minimum four-run scaffold, not for the breadth of the paper.
- X4's archive-path lineage caveat remains unresolved even though its figures exist and the
  stale terrain labels were cleaned.

Freshness is therefore field-specific: a newer editorial note does not outrank the archive
catalogue on figure existence, and a newer render does not create a confirmed claim.

## Experiment map: the paper has more than four runs

| ID | Deliberate role or change | Clean comparison | Current opportunity | Non-negotiable limit |
|---|---|---|---|---|
| X0 | NAM, one-way, fine 3-arcsecond terrain, YSU/MM5 control | Reference for X1, X3, X4, and X9 | Best-estimate control; terrain, radiation, physics, and fine-terrain feedback anchor | Source terrain resolution is not model-grid spacing. |
| X1 | X0 plus slope-aware radiation and topographic shading | CMP07: X1-X0 | Local radiation/surface-energy response | Source-code commit unresolved; surface means alone can hide local effects. |
| X2 | X1 with MYJ/Eta instead of YSU/MM5 | CMP08: X2-X1 | Stable-layer and turbulence-treatment response | PBLH is scheme dependent and only X2 exposes `TKE_PBL`. |
| X3 | NAM, one-way, default terrain | CMP02, CMP03, CMP09, CMP10 | One-way driving leg and terrain-source anchor | Default terrain is not the X0 control terrain. |
| X4 | NAM, one-way, deliberately coarse 5-arcminute terrain | CMP10 and CMP11 | Wide terrain bracket and geometry/capacity hypothesis | Archive-name provenance is medium confidence; pressure bias is terrain sensitive. |
| X5 | NAM, two-way, default terrain | CMP01 and CMP03 | Two-way NAM driving leg | Short-window result only. |
| X6 | GFS, two-way, default terrain | CMP01 and CMP04 | Two-way GFS driving leg | GFS-versus-NAM bundles initial and boundary products. |
| X7 | NAM, two-way, 1-km inner grid, 24-hour integration | None clean with X0/X8 | Longer single-configuration context and experiment-design lesson | Not a resolution-sensitivity member. |
| X8 | NAM, one-way, four domains through 111 m, 50 levels | None clean with X0/X7 | Fine-domain structure and representativeness context | Geometry, levels, terrain placement, radiation, and cadence are confounded. |
| X9 | X0 with two-way feedback | CMP06: X9-X0 | Clean fine-terrain feedback replication; complete figures | Rendered is not analysed; source-code commit remains unresolved. |
| X10 | X6 with one-way feedback | CMP02 and CMP04 | One-way GFS driving leg | Same five-hour factorial limit. |

The clean controlled result matrix is not only CMP01--CMP05.
CMP06--CMP11 contain real controlled or configuration-controlled questions; they need
focused analysis and claim gates, not automatic exclusion.
CMP12 and CMP13 remain context/design material rather than sensitivity results.

## Candidate Results threads

The status labels below are deliberate:

- **confirmed**: a ledgered claim can support scoped manuscript prose now;
- **analysis-ready**: the comparison and figures exist, but a named reproducible analysis
  and ledger row are still needed;
- **diagnostic**: useful visual or exploratory number, not yet a manuscript result;
- **context only**: cannot be presented as a controlled effect.

### 1. Observed evolution and what the model grid samples

**Status: confirmed core plus diagnostic extensions.**

Use the multi-day station evolution to establish a spatial floor-to-bench pattern, then
show why d02 rather than d03 is the common evaluation domain.
Small but useful points include the exclusion of most bench stations from d03 and the
modest nearest-cell elevation mismatch at the 11 d02 columns.
The locator can make the grid/station/transect choice legible before any sensitivity result.

Do not rename the horizontally separated stations a vertical profile, observed inversion
depth, or basin-volume measurement.

### 2. Driving-state response in time, space, and height

**Status: confirmed for surface/common-AGL metrics; diagnostic spatial and upper-air
extensions.**

CMP01 and CMP02 establish the repeated GFS-minus-NAM response under both feedback modes.
This thread need not be one omnibus factorial figure.
It can progress through surface error, 50--500 m AGL stability and transport wind, one
matched-hour plan view, a low-level cross-section, and the changing 700/500 hPa context.

The scientific question is how the product-level state differs and evolves, not whether
one nesting option wins.

### 3. Cold-pool maintenance and heat-deficit structure

**Status: analysis-ready hypothesis.**

The productized `heatdeficit_map` family supplies a reproducible field view for all nine
standard cases and ten controlled pairs.
The existing time series and map sequence suggest a stronger story than a static warm
bias: the GFS members may initialize with a substantial pool and then fail to maintain it.
Terrain appears to act more strongly near the rim/slopes, while feedback appears smaller
on the basin floor.

Before prose, freeze the basin/crest definition, units, masks, 13--18 UTC trajectory,
spatial summary, and sensitivity to reasonable definitions.
Recheck the exploratory Horsepool values against the productized output.
Do not use the single-point phase portrait or threshold-defined reservoir volume as evidence
until those diagnostics are separately productized and tested.

### 4. Terrain as geometry and capacity, not a score shortcut

**Status: analysis-ready with an X4 provenance gate.**

CMP09--CMP11 provide default-versus-fine, default-versus-coarse, and fine-versus-coarse
terrain-source brackets on the same WRF grid and baseline physics.
The existing maps and heat-deficit fields can test whether terrain changes the rim,
tributaries, pooling geometry, and near-surface structure differently from the driving-state
response.

This thread should pair terrain differences with model-minus-station elevation and avoid
using pressure bias as a skill ranking.
Resolve X4's archived path lineage before quoting its effect as a manuscript result.

### 5. Slope-aware radiation and topographic shading

**Status: analysis-ready controlled pair.**

CMP07 changes only `slope_rad`, `topo_shading`, and `shadlen`; X0 and X1 are bitwise
identical at initialization.
The exploratory station-mean surface scores are close, but that is not a null result for a
spatially local radiation treatment.
Interrogate `SWDOWN`, `GLW`, `TSK`, near-surface temperature/stability, slope/aspect, and
time evolution in shaded versus exposed regions.

A useful finding may be small and local.
Do not require it to rival the GFS-minus-NAM contrast to earn a concise Results paragraph or
supplement figure.

### 6. PBL and surface-layer treatment

**Status: controlled and provisionally non-negligible; scheme-aware analysis required.**

CMP08 changes MYJ/Eta versus YSU/MM5 while holding the rest of X1/X2 common.
The current matched diagnostic gives a mean two-site bulk theta contrast of 18.49 K for X2
and 17.18 K for X1, so the inherited description of a uniformly small response below
700 m is not established.

Use common-AGL theta, temperature, and wind profiles; surface fluxes; native PBLH with an
explicit scheme caveat; and X2 TKE without treating missing YSU `TKE_PBL` as zero.
This is a process-treatment result, not a raw PBLH contest.

### 7. Nest feedback as a robustness check, not the thesis

**Status: confirmed for the default-terrain factorial and analysis-ready at fine terrain.**

Use CMP03--CMP05 and CMP06 to show how much feedback matters under two forcing products and
two terrain regimes.
This can be one compact supporting panel or a supplement result.
It should not organize the paper merely because it is the most complete factorial.

### 8. Resolution and legacy simulations as honest negative/design findings

**Status: context only.**

X7/X0/X8 can support a useful explanation of why nominal 1 km/333 m/111 m output is not a
resolution experiment.
X7 can also show a longer single-run evolution if clearly labelled as one configuration,
not as evidence that resolution caused its behavior.
Legacy January, nudged, and SIP-era products can motivate design requirements but cannot be
ranked with February X0--X10.

## Small findings worth testing or retaining

| Lead | Present status | Why it could matter | Gate before prose or figure |
|---|---|---|---|
| Four elevation-spanning stations repeatedly separate from 31 January to 3 February | confirmed as surface context, C23 | Establishes that the modeled hours sit inside an evolving event | Observation QC, sensor metadata, licensing, and no inversion-depth wording |
| d03 excludes most bench/end stations; d02 supports the full station/transect sample | confirmed, C03 | Explains the chemistry-grid/evaluation-grid choice | Promote the locator only if it clarifies Methods |
| Default-d02 model-minus-station elevation is median -2.0 m, range -32.4 to +14.3 m | confirmed, C24 | Shows nearest-cell matching is not grossly displaced while preserving representativeness limits | Do not generalize from 11 columns to basin area |
| GFS-minus-NAM surface T2-bias response is +1.79/+1.76 degrees C under two-/one-way feedback | confirmed, C04/C25 | Surface corroboration across both feedback modes | Five hours and fixed d02 stations only |
| GFS-minus-NAM common-AGL stability is -3.63/-3.65 K and transport wind +0.79/+0.99 m s-1 | confirmed, C17/C25 | Main lower-layer response; every hourly median retains sign | Call wind a fixed-layer proxy, not export or residence time |
| Native PBLH does not reproduce the GFS-minus-NAM separation | confirmed, C20 | Prevents a common but simplistic explanatory shortcut | Keep PBLH scheme dependent |
| GFS-minus-NAM 700 hPa theta is more coherent at 14/16 UTC than the mixed, evolving 500 hPa response | diagnostic | A small vertical-context result may distinguish lower-tropospheric from broader synoptic structure | Complete five-hour/profile support and terrain-mask interpretation |
| X1 and X0 have close exploratory station-mean metrics despite a controlled radiation treatment | diagnostic | A local process can disappear in aggregate skill | Analyse radiation, slope/aspect, and spatial/time structure before calling it null |
| X2 bulk contrast is 18.49 K versus 17.18 K for X1 | provisional, C19 | The PBL/surface treatment may be materially interesting | Common-AGL, flux, and scheme-aware turbulence analysis |
| X4's near-zero mean pressure bias coincides with large terrain displacement at some sites | diagnostic | Demonstrates why pressure skill and terrain geometry must be separated | Resolve X4 provenance; quantify elevation adjustment rather than ranking skill |
| Productized heat-deficit maps show a coherent GFS-minus-NAM basin-floor pattern at 16 UTC | diagnostic | Candidate bridge from static bias to maintenance mechanism | Freeze definition and verify the full post-spin-up trajectory |
| X9-minus-X0 figures now exist at fine terrain | analysis-ready | Tests whether the bounded feedback result survives a second terrain regime | Recompute matched station/common-AGL/process summaries and add a ledger row |
| The nominal resolution ladder is confounded | confirmed, C16 | A negative design result can prevent a false but visually tempting conclusion | Label it explicitly as a confound table or context figure, never a sensitivity curve |

This is not a claim list to paste into the manuscript.
It is a queue of paragraph-sized observations that can connect the headline figures if each
survives its stated gate.

## Figure architecture to evaluate, not pre-approve

Build candidate packages from scientific jobs, not legacy L-numbers.
The following is a plausible broad main-text sequence:

1. **Event and sampling geometry:** observed evolution, optionally paired with the d02/d03
   station/domain locator.
2. **Lower-layer state response:** current common-AGL/time-evolution panel, with surface
   skill summarized rather than repeated in many station plots.
3. **Where and how vertically confined in the model:** one matched GFS-minus-NAM map plus
   a shallow common-AGL section or time-height panel.
4. **Maintenance mechanism:** heat-deficit control/difference map and post-spin-up time
   series, if validated.
5. **Terrain response:** a fine/default/coarse panel designed around rim/floor geometry,
   not generic score bars.
6. **Process treatments:** slope/shading and MYJ/Eta effects, either as two focused figures
   or one carefully legible multipanel with distinct diagnostics.
7. **Robustness and bounded nulls:** compact feedback effects across product and terrain,
   preferably secondary to the process story.

Possible supplement/reviewer-reserve material includes station overlays, 500/700 hPa
evolution, additional hours/sections, the full feedback families, terrain-pressure checks,
scheme-aware profiles, and a configuration-confound table for X7/X8.

Do not force every thread into the main text.
Do not demote a controlled, interesting small result merely because its effect is smaller
than the driving-state contrast.

## Work sequence for the new session

1. Create a compact candidate-result ledger with one row per CMP01--CMP13 and columns for
   question, isolated lever, exact artifact, current visual lead, quantitative analysis,
   claim status, figure status, freshness conflict, and next gate.
2. Correct stale coverage statements in canonical planning notes, but do not alter a
   scientific status merely because a render exists.
3. Group the controlled rows into three alternative paper architectures:
   a broad configuration story, a maintenance/mechanism story, and a hybrid.
4. For each architecture propose main, supplement, and reserve figures and state exactly
   what reader decision each figure enables.
5. Present those alternatives to John before rewriting `_manuscript_test.tex`.
6. After a direction is chosen, run only the targeted analyses needed to turn selected
   diagnostic rows into confirmed ledger claims.
7. Register and visually inspect selected figures before promotion; only then restructure
   the experimental manuscript.

The first session deliverable should be a decision packet, not new prose and not a dump of
all 324 external PNGs.

## Superseded copy-ready prompt that produced the decision packet

Do not reuse this prompt for current work; use the prompt in
`rewrite/HYBRID-ARCHITECTURE-HANDOFF.md`.

```text
Work in the private MDPI Air manuscript repo about WRF meteorology for the 2 February 2013
Uinta Basin winter-ozone episode. Run hostname -f, read AGENTS.md and ROADMAP.md, then read
rewrite/RESULTS-EXPANSION-HANDOFF.md completely and follow its authority/freshness rules.

The crucial correction is that X6/X10/X5/X3 are the minimum verified factorial, not the
scope of the paper, and nest feedback must not dominate simply because that factorial is
complete. The archive includes X0--X10 and controlled terrain, slope/shading, PBL/surface-
layer, and fine-terrain-feedback comparisons, plus many spatial/vertical/heat-deficit
diagnostics. Some older notes have stale figure counts or availability statements.

Do not rewrite main.tex or _manuscript_test.tex yet. First build the freshness-aware
candidate-result ledger requested by the handoff for CMP01--CMP13, recover the small
interesting findings as well as headline results, and propose three evidence-gated paper
architectures: broad configuration, cold-pool maintenance/mechanism, and hybrid. For each,
give a main/supplement/reserve figure plan, the exact question answered by every figure,
the supporting artifact, the remaining gate, and any note you found to be stale. Use the
current archive inventory for figure existence, the run/comparison inventories for design,
the manifests for admission, and the claim ledger plus exact artifacts for prose-ready
facts. Preserve confounded X7/X8 and legacy runs as context only.

Then bring the alternatives to me for a scientific/editorial choice before changing the
manuscript. If a cheap local read-only check can resolve ambiguity, do it; route CHPC-only
analysis or rendering through rewrite/CHPC-CODEX-PROMPT.md rather than guessing.
```
