# NOTES — new cold-pool advection figures, 111 m d04 run (CHPC session, 2026-07-15)

Context for deciding what goes into the manuscript. This session built a **cold-pool
advection proxy** in brc-tools and productized it as three new figure-engine families,
validated on the 111 m canyon-resolving run
(`pelican2013_nam_d04_111m_50lev_oneway_terrain3s`, NAM one-way, 3-arcsec terrain,
d01=3 km → d04=111 m, 50 levels, 2013-02-02 12–18 UTC, d03/d04 written every 10 min).

## The diagnostic: integrated deficit transport (IDT)

The proxy is the wind-weighted companion of the heat-deficit map we already use:

    H = (c_p/g) ∫ max(θ_crest − θ, 0) dp          heat deficit, J m⁻²  (existing)
    F = (c_p/g) ∫ max(θ_crest − θ, 0) · u_h dp    deficit transport, W m⁻¹  (new)

i.e. the IVT analogue for cold-pool air: clipping at θ_crest (2200 m ASL reference,
same per-column interpolation as every heat-deficit figure) confines the transport to
the pool itself. Because H and F share one kernel, they close a budget,

    ∂H/∂t = −∇·F + diabatic residual,

which makes the proxy *checkable* rather than heuristic — and the residual itself is
interpretable (radiative cooling vs daytime erosion). Derived scalars available for
free: deficit-weighted transport velocity U_D = F/H (an effective advection speed of
the pool), cold-pool depth h (top of the θ<θ_crest layer), and a bulk Froude
|U_D|/√(g(Δθ̄/θ_crest)h) for the canyon-flushing question.

**Validation on the 111 m run (interior box, crest 2200 m):**

- 15→16Z: mean dH/dt +0.251 vs −∇·F +0.239 MJ m⁻² h⁻¹ — residual +0.012. That hour's
  pool deepening was almost purely advective import.
- 16→17Z: dH/dt −0.466 vs −∇·F −0.219 — residual −0.247 = post-sunrise diabatic
  erosion, right sign and hour (≈ 9–10 am MST).
- Point-wise correlation between dH/dt and −∇·F is low at grid scale (0.05) but rises
  monotonically with averaging scale (0.35 at 5 km): features advect ~18 km per hourly
  snapshot, so this is temporal sampling, not error. The 10-min d03/d04 output would
  support a much tighter closure figure if we want one for the paper.
- Cold-pool depth at 15Z: median 529 m, p90 634 m AGL — sensible against the
  ~1550 m floor / 2200 m crest geometry.

Implementation: `brc_tools/nwp/wrf_output.py` (`deficit_flux_field`,
`deficit_flux_divergence`, `cold_pool_depth_field`, `transect_deficit_flux`),
brc-tools commits `1089add` (diagnostics) and `cf41892` (figure families).

## New figure families (engine `scripts/wrf_figures.py`, config `verification/config/figures/pelican2013_d04.toml`)

1. **`deficitflux_map`** — F quivers (MW m⁻¹, fixed 5 MW key) over the H field
   (viridis, fixed 0–8 MJ m⁻²). The "where is the cold pool going" map; the configured
   canyon transect lines are drawn on it. Per case+hour →
   `<run>/full-figures/<case>/deficitflux_map/`.
2. **`deficitflux_div`** — advective ∂H/∂t = −∇·F (MJ m⁻² h⁻¹, RdBu_r ±2, red =
   advection deepening the pool, display-only ~2-cell smoothing). Shows the
   convergence zones where drainage piles cold air. Per case+hour →
   `.../deficitflux_div/`.
3. **`deficitflux_transect`** — canyon-gate export Φ(t) = ∫F·n̂ ds (GW), one line per
   case, at 10-min resolution (it uses every wrfout, not just the hourly leads) →
   `compare/deficitflux_transect/`.

## Canyon gates (defined from the d04 model terrain, not eyeballed)

Latitude-row scans of d04 HGT found three coherent incisions ≥130 m below their flanks
along the northern escarpment; names are best-guess geographic attribution:

| transect | lon (gate) | cut depth | attribution |
|---|---|---|---|
| `ashley_gate` | −109.607 | ~154 m | Ashley/Dry Fork canyon |
| `steinaker_gate` | −109.522 | ~129 m | Steinaker / US-191 gap |
| `brush_gate` | −109.394 | ~213 m | Brush Creek canyon |
| `escarpment_base` | −109.66→−109.36 | (23 km line) | total southward injection at 40.47°N |

All lines run west→east, so **positive Φ = southward = down-canyon export into the
basin**. Endpoints live in `[[transects]]` blocks in `pelican2013_d04.toml`.

## Also fixed this session

- The `surface` family previously emitted only the 4-nest `*_multidomain_*` panels, so
  d04 never got a free-standing 300-DPI surface figure (it was a quarter-width subplot).
  New `surface_single_domains = ["inner"]` knob emits `{var}_{case}_d04_{HH}z.png`
  beside each panel (brc-tools `7d421bb`).

## First results (rendered 2026-07-15, job 13968920 → full6h run dir `full-figures/`)

- **Escarpment-base Φ(t)** (10-min cadence): positive (into-basin) export ~+30–45 GW
  through ~13:30Z (late-night drainage), a sharp reversal to **−80 GW northward** at
  14:30–15:30Z — the morning up-slope transition (~7:30–8:30 am MST) pulling deficit
  air back toward the escarpment — then relaxation to ≈0 by 18Z. There is a
  ~30-min oscillation right after init (12–13Z); treat the first hour as spin-up
  before interpreting it as a drainage pulse/seiche.
- **deficitflux_map 15Z**: coherent counter-clockwise sweep of the pool's transport,
  strongest F (~10–15 MW m⁻¹) along the eastern flank; the H field banks against the
  SE floor. Reads exactly like an IVT map, as intended.
- **deficitflux_div 15Z** (1 km display smoothing): broad advective deepening
  (+0.5–1.5 MJ m⁻² h⁻¹) with embedded erosion streaks — matches the +0.24 box-mean.

## Manuscript candidates (my ranking)

1. **Φ(t) at the three gates + escarpment base** — a single panel that quantifies
   nocturnal cold-air injection through the canyons at 10-min cadence; directly
   supports the "advection vs in-situ cooling" mechanism framing, and the budget
   closure numbers above give it a rigor statement for the text.
2. **deficitflux_map at 2–3 key hours** — the IVT-style visual is immediately read by
   reviewers; pairs naturally with the existing heatdeficit_map (same colour scale).
3. **deficitflux_div at one pre-dawn hour** — shows *where* advection builds the pool
   (canyon mouths / escarpment base) vs where it erodes it; more specialist, could go
   to supplementary.
4. The budget-closure scatter/statement (dH/dt vs −∇·F) is probably a sentence + a
   number in the text rather than a figure, unless we re-do it at 10-min cadence where
   it should close much more tightly.

Caveats for the text: hydrostatic mass weighting (ρdz = −dp/g) inside a nonhydrostatic
111 m run is standard for column integrals but worth a clause; θ_crest is the *local*
crest-level θ per column (Whiteman convention), so F is not defined above rim terrain;
the gate attributions (Ashley/Steinaker/Brush) should be double-checked against a map
before naming them in a caption.
