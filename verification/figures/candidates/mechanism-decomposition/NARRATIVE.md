# Cold-pool mechanism decomposition (exploratory figure set)

**Status:** exploratory prototypes (2026-07-11), not yet publication-grade. Built to test
whether the pelican2013 factorial can be reframed from a *list of sensitivities* into a
*mechanistic decomposition*. For the manuscript agent: this is a candidate results thread,
with caveats flagged below before any of it enters the paper.

X-codes are defined in `verification/figures/archive-inventory.md` (Table 1). Reference
control = **X0** (NAM, 1-way, fine terrain).

## Headline reframe
The three figures together say the cold pool decomposes along **three independent axes**:

> **IC sets the floor intensity (via ventilation); terrain sets the rim geometry and pool
> capacity; nesting-feedback and PBL/radiation physics are second-order (slopes only).**
> The volume (capacity) of the pool is nearly **geometry-locked** — the experiments move its
> **intensity**, not its extent (coarse terrain is the one exception: it shrinks the basin and
> intensifies the floor).

The single most quotable finding: **GFS does not lack a cold pool — it fails to *maintain*
one.** At 12Z its Horsepool pool is *deeper* than NAM's (6.5 vs 4.2 MJ m⁻²); by 18Z it has
ventilated and collapsed to 2.8. The 16Z snapshot that the paper currently leans on catches
GFS mid-collapse and misreads it as "GFS is simply warmer."

## The three figures

### `fig_heatdeficit_map_16z.png` — WHERE the pool lives, and what moves it
2×2, d02, 16Z. Vectorized Whiteman heat deficit (MJ m⁻²) over the whole grid (the spatial
extension of `brc_tools ... cold_pool_heat_deficit`), plus three difference maps on
per-panel symmetric scales.
- **Control:** pool is a floor-hugging feature along the drainage axis (Ouray–Horsepool–
  Roosevelt–Vernal), zero at the crest rim.
- **IC (X6−X5):** coherently blue **basin-wide** (~2.5 MJ m⁻²) — GFS erodes the whole floor.
- **Terrain (X0−X4):** signal on the **rim/slopes/tributaries**, floor near-neutral.
- **Feedback (X9−X0):** ±0.2 MJ m⁻² (10× smaller), floor speckle ≈ numerical noise.

### `fig_phase_portrait.png` — HOW each knob moves the pool
2×2, one panel per experimental knob (IC / nesting / terrain / physics); each run's diurnal
trajectory (12→18Z) through **strength (Horsepool heat deficit) × ventilation (10 m wind)**.
Same axes across panels.
- **IC:** GFS (X6/X10) sweeps from deep/calm to weak/windy — *ventilated collapse*. NAM
  (X5/X3) stays compact.
- **Nesting/feedback (X3/X5/X0/X9)** and **physics (X0/X1/X2)**: trajectories overlap —
  **null at the floor**.
- **Terrain:** X4 (coarse) rides offset-high (stronger, calmer floor).
- Read rule: a knob that *slides* runs along one curve acts through mixing; a knob that
  *shifts* the curve is a thermodynamic/terrain offset mixing can't explain.

### `fig_reservoir_anatomy.png` — capacity vs strength
2×2, d02. Trapped-pool air = cells below crest with θ-deficit ≥ 2 K.
- **Capacity vs intensity (money panel):** three regimes — NAM cluster (large vol, moderate
  intensity); X4 coarse (smaller vol, higher intensity); X6 GFS (weak). *Reservoir ≠ strength.*
- **Hypsometric / pyramid:** cold air is weakly-cold and voluminous high in the basin
  (1900–2100 m), with a tongue of intense (5–7 K) air lower down.
- Pool **volume is nearly geometry-locked**; experiments move intensity, not extent.

## Honest caveats (must resolve before publication)
- **Prototype metrics.** The heat-deficit integral uses an approximate crest boundary; the
  reservoir volume uses an arbitrary 2 K θ-deficit threshold (chosen to exclude the weak
  near-crest background stratification — results are threshold-sensitive).
- **Point vs field.** The phase portrait is a single-point (Horsepool) diagnostic; a
  basin-mean would be more robust and is worth checking.
- **Spin-up.** The 12Z volume/deficit is an initialization state; the 12→13Z jump in the
  erosion panel is spin-up, not physics — start interpretation at 13Z.
- **Reproducibility.** Scripts are in this directory (`*.py`, run against `brc-tools`
  `brc_tools.nwp.wrf_output`); they are standalone prototypes, **not** engine families yet.

## Suggested path to publication
1. Promote the heat-deficit field to a proper `heatdeficit_map` engine family in brc-tools
   (like the `thetaz` family) so it is TOML-driven and reproducible across cases/times.
2. Re-do the phase portrait with a basin-mean strength metric; add the erosion-rate as an
   explicit dH/dt.
3. If the "IC = ventilated collapse" result survives (2), it is a strong standalone result and
   reframes the IC section (currently narrative b) from static-warm-bias to a maintenance-
   failure mechanism.
