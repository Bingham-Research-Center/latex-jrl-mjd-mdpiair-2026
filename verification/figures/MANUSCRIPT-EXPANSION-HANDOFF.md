# Manuscript figure-expansion handoff (workstream D)

**Written 2026-07-12.** This is a self-contained brief for executing the manuscript
figure expansion in a **fresh session** (or by the LaTeX/manuscript agent) with clean
context. It was deliberately *not* executed inline: D is editorial surgery on `main.tex`
and is best done with uncluttered context. Everything it depends on (the render, the
engine family, the pointers) is already done and verified — see "Foundation" below.

The author's instruction that shaped this doc: *"I want too much, so I can choose what
makes the cut."* → this brief lists the **superset** of promotable figures with a
recommendation on each; curate down, don't treat it as a build order.

---

## Foundation already in place (do not redo)

- **Full engine render verified.** All 9 pelican2013 3-domain (333 m) runs have complete
  per-run `full-figures/` (surface 35 + upperair 14 + sections 14 + thetaz 3); 10/10
  `[[differences]]` families complete in `compare/`. 1 km rung complete for its single-run
  TOML.
- **Stale study-repo pointers fixed** (brc-tools `CLAUDE.md` + `/wrf-full-figures` skill now
  point here, at `latex-jrl-mjd-mdpiair-2026/verification/`).
- **New `heatdeficit_map` engine family productized** (the mechanism-decomposition
  heat-deficit prototype → reproducible TOML family) and **rendered across the whole matrix**
  (SLURM job 13930807, COMPLETED 2026-07-12, 133 figures):
  - per-case field maps → `<run>/full-figures/heatdeficit_map/heatdeficit_<case>_<HH>z.png`
    (9 runs × 7 hrs = 63)
  - difference maps → `…/pelican2013_pub_figures/compare/heatdeficit_map/heatdeficit_<tag>_<HH>z.png`
    (10 pairs × 7 hrs = 70), with fixed ±MJ scales on the three headline pairs
    (`GFS-NAM` ±2.5, `terrain-3arcsec-5arcmin` ±1.6, `2way-1way-terrain3s` ±0.2).
  - The mechanism reframe is now *reproducible*, not a one-off script — validated on real
    GFS/NAM 16Z: GFS−NAM is coherently blue basin-wide ("GFS erodes the whole floor").

Archive root: `/uufs/chpc.utah.edu/common/home/lawson-group6/jrlawson/wrf_archive`
(`$BRC_WRF_ARCHIVE`). Compare root: `<archive>/pelican2013_pub_figures/compare/`.

---

## Current manuscript state (`main.tex`)

3 promoted figures, all vector PDF in `figures/`:
1. `obs_temp_timeseries_feb0102.pdf` — Fig `observed-evolution` (§ Observed Cold-Pool Context)
2. `wrf_inversion_index_feb0102_gfs2way_vs_nam2way_d02_14to18.pdf` — Fig `bulk-contrast`
   (§ Response to Driving Analysis across Feedback Modes)
3. `wrf_retention_ventilation_d02_14to18.pdf` — Fig `retention-ventilation` (same §)

**Key structural opening:** `\subsection{Response to Nest Feedback}` (≈ `main.tex:151`)
currently has **no figure** — a natural home for a feedback panel.

Narrative spine = "Narrative A" (driving-state response robust to nest feedback), per
`notes/figure-strategy.md`. That doc's own recommendation is to stay lean and add at most
L04; the author has chosen to go broader here.

---

## Promotion gate (mechanics — every added figure needs this)

1. **Source PNG** lives in the archive (`compare/…` or `<run>/full-figures/…`). It is *not*
   manuscript-eligible until promoted.
2. **Vectorize**: the promoted figures are PDF. The engine emits 300-DPI PNG. Either (a)
   re-render the chosen figure to PDF (add a `--format`/savefig path — the engine currently
   hardcodes PNG, so this needs a one-line renderer tweak *or* a PNG→PDF wrap), or (b) for
   the analysis-script figures (L04, retention-style), save PDF directly like
   `plot_wrf_retention.py` does. **Note:** promoted figs so far come from the repo-local
   `verification/scripts/*.py` (direct PDF), not the brc-tools engine — see caveat under
   each tier.
3. **Copy** to `figures/<name>.pdf` (+ keep the PNG in `verification/figures/candidates/`).
4. **Add a `manifest.csv` row** — 14 columns:
   `figure_id,run_ids,input_data,valid_window,generator,generator_commit,host,output_path,synthetic,provenance_status,style_status,narrative_role,status,notes`
   with `status=promoted`, `synthetic=false`, `input_data` carrying the source wrfout /
   data-file `sha256=…`, `generator` = the exact script/command, `generator_commit` = the
   git short-SHA, `host` = the render host + Slurm job id, and `notes` carrying the output
   PNG/PDF sha256. (Copy the format of the three existing `promoted` rows.)
5. **Register in `figures/MANIFEST.md`** (the manuscript admission list).
6. **Visual/provenance review**, then `\includegraphics` into `main.tex` with a `\label`.

This rigor is why promotion is deliberate — budget ~20–30 min per figure.

---

## The superset — curate down

Grounded in `notes/figure-strategy.md` (L-codes) plus the new `heatdeficit_map` family.
"Effort" is beyond the already-rendered PNG (promotion + any new script/vectorize).

| ID | Figure | Source (rendered PNG unless noted) | Target § | Recommendation | Effort |
|----|--------|-----------------------------------|----------|----------------|--------|
| **L04** | Factorial effect-size panel (forcing rows × feedback cols + interaction, one scale) | **New script** from `verification/data/retention_{pair,interaction}_summary.csv` | Response to Driving Analysis (or its own para) | **Top single add** — no new WRF, honest one-scale summary | Med (new `verification/scripts/plot_effect_size.py` + promote) |
| **L05** | GFS−NAM 2 m-θ diff map, one hour (e.g. 16Z) | `compare/diff_gfs_nam/theta2m_GFS-NAM_16z.png` | Response to Driving Analysis | Strong "where" panel; pick **one** hour | Low (promote + vectorize) |
| **L07** | GFS−NAM EW/NS θ sections, one hour | `compare/diff_gfs_nam/section_{ew,ns}_GFS-NAM_16z.png` | Results or Supplement | "Is the response shallow/basin-confined?" — 2-panel select | Low–Med |
| **FB** | Feedback diff map/section (bounded null) | `compare/diff_feedback/…_2way-1way_16z.png` | **Response to Nest Feedback** (fills the empty subsection) | Fills the figureless subsection; shows feedback ≪ forcing | Low |
| **HD-field** | `heatdeficit_map` control field (where the pool lives) | `<nam_terrain3s run>/full-figures/heatdeficit_map/heatdeficit_nam_terrain3s_16z.png` | Discussion (mechanism) | Mechanism context; drainage-axis pool | Low |
| **HD-IC** | `heatdeficit_map` GFS−NAM diff ("GFS erodes the floor") | `compare/heatdeficit_map/heatdeficit_GFS-NAM_16z.png` | Discussion (mechanism) | **Mechanism headline** — reframes IC section | Low |
| **HD-terr / HD-fb** | `heatdeficit_map` terrain (`terrain-3arcsec-5arcmin`) + feedback (`2way-1way-terrain3s`) diffs | `compare/heatdeficit_map/…_16z.png` | Discussion | The 3-axis decomposition (terrain on rim, feedback null) | Low |
| **L12** | Cold-pool heat-deficit **time series** ("fails to maintain") | `compare/heatdeficit/heat_deficit_timeseries.png` | Discussion | Pairs with HD-IC: GFS deeper at 12Z → collapsed by 18Z | Low |
| L06 | GFS−NAM **1-way** diff map (survives feedback change) | `compare/diff_gfs_nam_oneway/…` | Results/Supplement | Pair same hour with L05 or omit | Low |
| L10 | d02/d03 terrain + station + transect locator | `verification/figures/candidates/wrf_transect_locator_d02_d03.*` | Methods | If domain choice confuses reviewers | Low (already candidate) |
| L14 | MYJ/Eta diff (`diff_myj_eta`) | `compare/diff_myj_eta/…` | Discussion reserve | PBL sensitivity; verdict-blocked | Reserve |
| L15/L16/L17 | Terrain ladder / X9 feedback / resolution ladder | external | — | **Hold.** L17 resolution ladder is **confounded — do not use as a sensitivity figure** | — |

---

## Per-tier execution notes

### Tier 1 — L04 effect-size panel (the recommended single add)
- **What**: a compact panel showing the two forcing effects, two feedback effects, and their
  interaction on one comparable scale, for stability / transport wind / T2 error / PBLH.
- **Inputs (already verified, no new WRF)**: `verification/data/retention_pair_summary.csv`
  and `retention_interaction_summary.csv` (the exact "DATA17/19/24/26" labels are in
  `verification/figures/chpc-figure-inventory-2026-07-10.md`). These are the same tables that
  back the promoted `wrf_retention_ventilation` figure.
- **Build**: new `verification/scripts/plot_effect_size.py` (save PDF directly, like the other
  `verification/scripts/plot_*.py`), then promote. This is *not* a brc-tools engine family —
  it's a manuscript-specific summary panel, so it belongs in `verification/scripts/`.
- **Caption draft**: *"Factorial effect sizes for the matched 14–18 UTC window: the
  driving-analysis (GFS−NAM) main effect under each feedback mode, the nest-feedback main
  effect under each analysis, and their interaction, for 50–500 m stability, fixed-layer
  transport wind, 2 m-temperature error, and PBL height. Bars share one standardized scale;
  the block interval is descriptive of the short sample."*

### Tier 2 — spatial (L05) + feedback (FB)
- L05: promote one hour of `diff_gfs_nam/theta2m_GFS-NAM_16z.png` into the driving-analysis
  section. Caption: *"GFS-minus-NAM 2 m potential-temperature difference on d02 at 16 UTC;
  the driving-state response is a coherent basin-floor signal (red = GFS warmer)."*
- FB: promote `diff_feedback/theta2m_2way-1way_16z.png` (or its section) into the empty
  **Response to Nest Feedback** subsection. Caption: *"Two-way-minus-one-way 2 m
  potential-temperature difference (NAM) at 16 UTC on the small-signal scale (±3 K); the
  feedback response is bounded and an order of magnitude below the driving-state response."*
- **Vectorize caveat**: these come from the brc-tools engine (PNG). Simplest path: add a
  `--format pdf` option to `scripts/wrf_figures.py` (the renderers already take `dpi`; PDF is
  a one-line `savefig` suffix change), or wrap PNG→PDF for just the promoted few.

### Tier 3 — mechanism reframe (highest payoff)
- Now backed by the **reproducible** `heatdeficit_map` family (not the prototype). Before
  writing, **confirm the prototype's numbers survive** on the rendered family: eyeball
  `compare/heatdeficit_map/heatdeficit_GFS-NAM_{12,16,18}z.png` (GFS should be *deeper* than
  NAM at 12Z, collapsed by 18Z — the "fails to maintain" arc) against `compare/heatdeficit/
  heat_deficit_timeseries.png`.
- Figures: **HD-field** (control, where the pool lives) + **HD-IC** (GFS−NAM, erodes the
  floor) + **L12** (time series, fails to maintain). Optionally HD-terr + HD-fb to show the
  three-axis decomposition (terrain acts on the rim; feedback is floor speckle ≈ noise).
- **Narrative move**: reframe the IC discussion from "GFS has a static warm bias" to
  "**GFS does not lack a cold pool — it fails to maintain one**" (ventilated collapse). Source
  synthesis: `verification/figures/candidates/mechanism-decomposition/NARRATIVE.md`.
- **Caveats to state honestly** (from NARRATIVE.md): approximate crest integration boundary;
  the 16Z snapshot catches GFS mid-collapse; the phase-portrait/reservoir prototypes remain
  single-point/threshold-sensitive and are **not** productized (only the heat-deficit *map*
  is). Keep chemistry/ozone claims out of scope.

---

## Open decisions for the author
1. **Which tier / which figures make the cut** (the point of the superset above).
2. **Vectorization approach** for engine PNGs (add `--format pdf` to the engine vs. wrap the
   chosen few). Recommend adding `--format pdf` — reusable, ~one line per renderer.
3. **Does the mechanism reframe survive** the rendered (vs prototype) numbers? Tier 3 is
   greenlit only if yes.

## Cleanup / gotchas
- **21 stale mislabeled PNGs** in `compare/diff_terrain_fine/` (`*terrain-900m-30m*`,
  superseded by the `terrain-900m-90m` tag). Regenerable; safe to delete but not yet done
  (needs author authorization — it's the shared archive):
  `rm <archive>/pelican2013_pub_figures/compare/diff_terrain_fine/*terrain-900m-30m*.png`
- `heatdeficit_map` is also available for the **1 km** and **d04** rungs (their TOMLs now set
  `heatdeficit_domain = "d02"`); render with
  `PELICAN_FIGURE_CONFIG=…/pelican2013_1km.toml sbatch verification/slurm/pelican_figures.slurm --figure heatdeficit_map` if wanted (low priority — resolution ladder is confounded).
- Engine + how-to: brc-tools `docs/WRF-FIGURE-ENGINE.md`; family list now includes
  `heatdeficit_map` (config keys `heatdeficit_domain`, per-pair `hd_limit`).
- The brc-tools working tree has **uncommitted** changes from this session (the new family +
  doc/skill edits) and the study repo has **uncommitted** TOML edits (config knobs). Neither
  was committed — commit when ready.
