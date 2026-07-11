# PBL-scheme choice (YSU) vs Tran et al. (2018) MYJ — justification & draft methods text

**Supporting methods note; not manuscript evidence by itself.** Migrated from
`wrf-nudge-ozone-air2026` commit `caf5c69` and reconciled against
`verification/provenance/run-inventory.csv`, CMP08 in
`verification/provenance/comparison-inventory.csv`, claim C19, and
`verification/provenance/tran-2018-paper-archive-reconciliation.md`.

## The PBL axis isolated by the current bridge

Every Pelican 2013 run shares Tran's Thompson/RRTMG/Noah core, but the Pelican
baseline is not a reproduction of Tran et al.: it also differs in cumulus treatment,
land-use categories, grid, vertical levels, forecast design, and nudging.
The PBL/surface-layer pairing is the one parameterized-physics lever isolated by the
matched X2-minus-X1 bridge.

| WRF option | Our baseline (X0 & most runs) | `…_slope_myj` run (X2) | Tran et al. (2018) |
|---|---|---|---|
| `mp_physics` | Thompson (8) | Thompson (8) | Thompson (8) ✓ |
| `ra_lw/sw_physics` | RRTMG (4) | RRTMG (4) | RRTMG (4) ✓ |
| `sf_surface_physics` | Noah (2) | Noah (2) | Noah (2) ✓ |
| **`bl_pbl_physics`** | **YSU (1)** | **MYJ (2)** | **MYJ (2)** |
| **`sf_sfclay_physics`** | **revised MM5 (1)** | **Eta/MYJ (2)** | **Eta/MYJ (2)** |
| `cu_physics` | 0 (all nests) | 0 | KF (1) on d01 only |
| `num_land_cat` | 21 (MODIS) | 21 | 33 (USGS) |

The bridge therefore asks a narrow question: with slope/shading enabled and the other
Pelican settings held fixed, what changes when **YSU + revised MM5** is replaced by
MYJ+Eta? It does not establish which full configuration is closest to Tran et al. or
which scheme has greater forecast skill.

## Why YSU can remain the baseline while MYJ is a sensitivity

1. **Tran et al. document a scheme--nudging coupling worth testing.** Their diagnosed
   MYJ PBL height reaches the lowest model level (~18 m) during inversions (§3.1.1,
   §3.1.3). In their PBL-gated design, that diagnosis changes the vertical reach of
   nudging; configurations with analysis nudging also have the family's largest warm
   surface biases (+3 to +5 °C) and extreme stratification. This combination motivates
   an explicit MYJ test, but it does not isolate MYJ as the cause or prove YSU is better.
   (Detail:
   `verification/provenance/tran-2018-paper-archive-reconciliation.md` §3.4.)

2. **Our design removes the nudging coupling and turns the scheme into a controlled test.**
   The behavior in Tran involved the PBLH diagnosis *coupling to analysis nudging*. Our
   runs are **free-running (un-nudged)**, so that coupling is absent. That lets us retain YSU
   as the designated baseline **and quantify the MYJ question as an explicit sensitivity
   axis** — exactly what run X2 (`…_slope_myj`, one declared coupled-scheme swap
   represented by two namelist fields relative to X1) provides.
   The current audit does **not** accept the earlier shorthand that the response is simply
   "small and confined below 700 m AGL." X2 changes PBLH, radiation, surface fluxes, and
   the bulk theta contrast; the common-AGL profile and scheme-aware PBLH/TKE analysis is
   still provisional. The safe conclusion is that MYJ/Eta is a material reviewer-reserve
   sensitivity, not that YSU has already won a skill comparison.

3. **Scheme mechanics.** MYJ (`bl=2`) is a local 1.5-order TKE closure that can shut down
   mixing under strong surface-based inversions; YSU (`bl=1`, Hong et al. 2006) is non-local
   with an explicit bulk-Richardson PBL-top diagnosis that does not pin the PBL top to the
   first model level. The Uinta Basin cold-pool WRF literature (Neemann et al. 2015 — in the
   lit queue) reports strong PBL-scheme sensitivity in exactly these conditions.

## Draft methods sentence (drop-in)

> We use the Thompson microphysics, RRTMG radiation, and Noah land-surface schemes also
> used by Tran et al. (2018), together with the Yonsei University (YSU; Hong et al. 2006)
> non-local PBL scheme and revised MM5 surface layer. Tran et al. report that the
> MYJ-diagnosed PBL height reached the lowest model level during basin inversions,
> thereby changing the reach of their PBL-gated nudging. Because our simulations are
> free-running (un-nudged), we treat the PBL scheme as an explicit sensitivity axis
> (run X2) rather than a fixed inheritance.
> The six-hour sensitivity is retained as reviewer reserve and is not used here to claim
> that either scheme has superior forecast skill.

## Consequence for the experiment framing

The MYJ run is a **treatment/sensitivity**, not the control. The designated control
(X0) is the free-running configuration with NAM forcing, one-way nesting, a 3-arcsecond WPS
static terrain grid, and YSU—`pelican2013_nam_3_1_333m_75lev_oneway_terrain3s`.
See `verification/figures/archive-inventory.md` for the X-map and CMP08 in
`verification/provenance/comparison-inventory.csv` for its manuscript role.

## Other (minor) divergences from Tran — for a complete methods paragraph
- **Cumulus:** we run `cu_physics=0` on all nests; Tran used KF on d01. This difference
  must be disclosed and has not been isolated as a sensitivity here.
- **Land categories:** 21-cat MODIS vs Tran's 33-cat USGS. Note if surface-type detail
  enters the argument; otherwise minor.
- **Resolution / levels:** the Pelican configurations use 333 m or 111 m inner nests and
  50 or 75 eta interfaces, while Tran reports a 1.333 km inner grid and 41 mass layers.
  These are configuration differences, not evidence that the confounded resolution
  sequence improves skill.
- **No nudging:** free-running forecasts vs Tran's obs+analysis nudging — central to
  argument #2 above.

## Citations to confirm
- Hong, Noh & Dudhia (2006), *Mon. Wea. Rev.* 134, 2318–2341 — YSU PBL. **(verify)**
- Janjić (1994), *Mon. Wea. Rev.* 122, 927–945 — MYJ. **(verify)**
- Neemann et al. (2015), *Atmos. Chem. Phys.* 15, 135–151 — Uinta Basin cold-pool WRF. **(verify)**
- Tran et al. (2018), *Atmos. Environ.* 177, 75–92 — the reference configuration.
