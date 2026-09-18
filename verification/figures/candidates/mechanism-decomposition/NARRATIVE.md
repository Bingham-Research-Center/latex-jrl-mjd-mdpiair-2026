# Cold-pool mechanism decomposition (exploratory figure set)

**Status:** exploratory interpretation, updated 13 July 2026; not claim-grade or
publication-admitted.
The `heatdeficit_map` field has since been productized in the `brc-tools` figure engine and
rendered across all nine standard cases and ten controlled pairs.
The local triptych, Horsepool phase portrait, and threshold-defined reservoir anatomy remain
prototypes.
This note tests whether the pelican2013 matrix can support a mechanistic decomposition; its
leads require the gates below before any enters the paper.

X-codes are defined in `verification/figures/archive-inventory.md` (Table 1). Reference
control = **X0** (NAM, 1-way, fine terrain).

## Headline hypothesis to test
The three prototypes suggest, but do not yet establish, a decomposition along three axes:

> **The driving state may set floor intensity and ventilation, terrain may set rim geometry
> and apparent pool capacity, and nest feedback may be smaller over this short window.**
> The PBL/surface-layer and slope/shading responses remain unresolved rather than
> second-order by default.

The strongest lead to recheck is: **GFS may not lack a cold pool at initialization; it may
fail to maintain one after spin-up.**
The prototype's Horsepool values (6.5 versus 4.2 MJ m⁻² at 12 UTC and 2.8 MJ m⁻² for GFS
at 18 UTC) are not quotable until they are reproduced from the productized output with a
frozen basin/crest definition, masks, units, and post-spin-up trajectory.

## The three figures

### `fig_heatdeficit_map_16z.png` — WHERE the pool may live, and what may move it
2×2, d02, 16Z. Prototype Whiteman heat deficit (MJ m⁻²) over the whole grid, plus
three difference maps on per-panel symmetric scales.
The corresponding single-case and pair fields now exist in the productized
`heatdeficit_map` family; the local composite itself remains a diagnostic.

- **Control:** pool is a floor-hugging feature along the drainage axis (Ouray–Horsepool–
  Roosevelt–Vernal), zero at the crest rim.
- **Driving state (X6−X5; legacy panel label “IC”):** the prototype is coherently blue
  over much of the basin floor on its ~2.5 MJ m⁻² scale; interpret this as a lead to test,
  not initial-condition attribution.
- **Terrain (X0−X4):** signal on the **rim/slopes/tributaries**, floor near-neutral.
- **Feedback (X9−X0):** ±0.2 MJ m⁻² display scale and a speckled floor lead; do not
  label the signal numerical noise without a matched quantitative check.

### `fig_phase_portrait.png` — HOW each knob moves the pool
2×2, one panel per experimental knob (driving state, labelled “IC” in the prototype /
nesting / terrain / physics); each run's diurnal trajectory (12→18Z) through
**strength (Horsepool heat deficit) × ventilation (10 m wind)**.
Same axes across panels.

- **Driving state:** the prototype draws GFS (X6/X10) from deep/calm to weak/windy and
  keeps NAM (X5/X3) more compact; “ventilated collapse” remains the candidate
  interpretation to test after spin-up.
- **Nesting/feedback (X3/X5/X0/X9)** trajectories overlap at this point-scale; the
  **physics (X0/X1/X2)** paths are not a defensible null test without the scheme-aware and
  slope/aspect analyses required by CMP07/CMP08.
- **Terrain:** X4 (coarse) rides offset-high (stronger, calmer floor).
- Read rule: a knob that *slides* runs along one curve acts through mixing; a knob that
  *shifts* the curve is a thermodynamic/terrain offset mixing can't explain.

### `fig_reservoir_anatomy.png` — capacity vs strength
2×2, d02. Trapped-pool air = cells below crest with θ-deficit ≥ 2 K.
- **Capacity vs intensity (money panel):** three regimes — NAM cluster (large vol, moderate
  intensity); X4 coarse (smaller vol, higher intensity); X6 GFS (weak). *Reservoir ≠ strength.*
- **Hypsometric / pyramid:** cold air is weakly-cold and voluminous high in the basin
  (1900–2100 m), with a tongue of intense (5–7 K) air lower down.
- Pool volume appears nearly geometry-locked under this one threshold; that statement is
  explicitly threshold-sensitive and unconfirmed.

## Honest caveats (must resolve before publication)
- **Prototype metrics.** The heat-deficit integral uses an approximate crest boundary; the
  reservoir volume uses an arbitrary 2 K θ-deficit threshold (chosen to exclude the weak
  near-crest background stratification — results are threshold-sensitive).
- **Point vs field.** The phase portrait is a single-point (Horsepool) diagnostic; a
  basin-mean would be more robust and is worth checking.
- **Spin-up.** The 12Z volume/deficit is an initialization state; the 12→13Z jump in the
  erosion panel is spin-up, not physics — start interpretation at 13Z.
- **Reproducibility.** The heat-deficit map is now an engine family under the renderer and
  study TOML recorded in `verification/figures/archive-inventory.md`.
  The phase portrait and reservoir scripts in this directory remain standalone prototypes.

## Suggested path to publication
1. **Completed for rendering, not for claims:** `heatdeficit_map` is TOML-driven and
   rendered across the standard matrix and all ten configured pairs.
2. Freeze the basin/crest definition, units, masks, and reasonable-definition sensitivity;
   verify the full 13--18 UTC trajectory and state explicitly where interpretation starts
   after spin-up.
3. Re-do the phase portrait with a basin-mean strength metric; add the erosion-rate as an
   explicit dH/dt.
4. If the maintenance-failure lead survives those checks and agrees with the common-AGL
   diagnostics, add a claim-ledger row before using it to reframe the driving-state section.
