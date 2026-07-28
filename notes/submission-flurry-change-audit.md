# Submission-flurry change audit

Status: prepared 28 July 2026, for John to adjudicate.

This audits every non-figure change that the 16 July 2026 submission flurry made to
`main.tex`, so it can be reverted if unintended. The flurry is the 16 July commit cluster
`f9028dd`…`5595f64`; the last pre-flurry commit is `58cbdd3` (15 July).

## Bottom line

**The submitted `main.tex` was already identical to your own author file
`jrl_manuscript.tex` in everything except two figures** (now restored). The reorganization
you noticed in the PDF — Methods/Results re-titling and re-splitting, the tables-only
appendix, British English, UTC notation — is present *identically* in your author file, so
it was your editorial pass, not a change imposed on a file you were not watching.

Concretely, the entire text diff between the shipped `main.tex` and your author file
`jrl_manuscript.tex` was **69 lines**, and all of it was:

1. the single-panel vs two-panel **locator** (Figure 1) — restored to two panels;
2. the **terrain/cross-section composite** missing from the body — restored to
   §Terrain-Source Brackets as Figure 8;
3. three **trailing-whitespace-only** lines (the shipped file was the cleaner one).

After the restoration, `main.tex` and `jrl_manuscript.tex` differ only by the required
`figures/` paths (vs `verification/figures/candidates/`), the dropped `\IfFileExists`
render-pending guards, and the `-supplement` label suffix. **There is no non-figure text to
revert.**

## What was actually lost, and how it was restored

| Item | Shipped `main.tex` | Your author file | Action taken |
|---|---|---|---|
| Figure 1 locator | single combined image | two panels (a) geographic + (b) nested domains | Restored as two panels; panel (b) = `wrf_nested_domains_d01_d03.png`, promoted to `figures/` |
| Terrain composite | absent (results only in Supplement Table S2) | Figure in §Terrain-Source Brackets | Restored as Figure 8 = `wrf_terrain_cmp11_d02_d03_16z.pdf`, promoted to `figures/` |

Both images were promoted into `figures/`, added to `figures/submission-files.txt`, and
recorded in `figures/MANIFEST.md`. `make submission-check` passes.

## The flurry's structural rewrite (pre-flurry → submitted), section by section

These are the real editorial changes the flurry made to `main.tex`. **Each also appears in
your author file**, so each is corroborated as intended — but this is where to look if any
re-titling or prose rewrite reads as not yours (it may be a rewrite your author pass
accepted without close review).

### Methods (6 → 7 subsections)

| Pre-flurry (`58cbdd3`) | Submitted / author file |
|---|---|
| Case, Observations, and Evaluation **Sample** | Case, Observations, and Evaluation **Domains** |
| WRF **Experiment Matrix** | WRF **Configuration and Archived Simulation Family** |
| Secondary Controlled Contrasts and Design Exclusions | **Controlled Contrasts and Estimands** |
| *(part of the row above)* | **Design Exclusions: Resolution and Legacy Context** *(split out as its own subsection)* |
| Surface, **Retention, and Ventilation** Diagnostics | Surface and **Common-AGL** Diagnostics |
| Aggregation and Short-Sample **Interpretation** | **Pairing,** Aggregation, and Short-Sample **Sensitivity** |
| Footprint-Integrated Heat Deficit | *(unchanged)* |

### Results (7 → 10 subsections)

| Pre-flurry | Submitted / author file |
|---|---|
| Observed Episode Context | *(unchanged)* |
| Observed Surface-Temperature Context | *(unchanged)* |
| Controlled Responses on a Common Pipeline | Common-Pipeline Contrasts **at a Glance** |
| Response to the Driving-Data Product | Driving-Product Response **in the Common Lower Layer** |
| — | **Surface and Spatial Corroboration** *(new)* |
| Footprint Heat Deficit: A Weaker State… | *(unchanged)* |
| Response to Nest Feedback + Secondary Process and Terrain Treatments | **split into three:** Process Treatments on the Fine-Terrain Branch · Nest-Feedback Robustness across Two Terrain Regimes · Terrain-Source Brackets |

### Discussion (unchanged)

The four subsections are identical pre- and post-flurry.

### Appendix — explains the "moving to/from appendix" you remember

| | Pre-flurry `58cbdd3` | Submitted / author file |
|---|---|---|
| Title | "Evidence Tables and Supplied-State **Profiles**" | "Data Tables and Secondary Diagnostics" |
| Tables | 6 (heat-deficit, process-effects, surface-summary, spatial-summary, fine-feedback, terrain-summary) | 3 (effects, surface-summary, heat-deficit) |
| Figures | **1 — the Horsepool θ profiles lived here** | none — the θ profiles moved **into §4.1 Discussion** (Figure 9) |
| Terrain numbers | in-appendix table | moved to **Supplement Table S2** |

The deeper history: the 13 July "maximal" draft (`_manuscript_v3.tex`, 16 figures) held even
more in its appendix plus a temporary "Supplementary Material" section (the five X8
deficit-transport figures). Your **14 July author review** (recorded in
`notes/manuscript-v3-structure-and-domain-review.md`) deliberately trimmed that appendix,
moved the profiles to Discussion, routed the terrain summary to the Supplement, and dropped
the X8 packet. So the slimmer appendix was your decision, made two weeks before submission.

## Global formatting passes (intended; present in author file)

- `2e806f5` **Adopt British English** — spelling normalized manuscript-wide.
- `bc6332a` **Standardise UTC notation** — "14:00–18:00 UTC" → "1400–1800 UTC" (four-digit,
  no colon). *(This is why I corrected the restored terrain caption from "16:00 UTC" to
  "1600 UTC" — it was copied from the pre-standardization draft.)*

## Nothing to revert — but optional polish

There is no unintended non-figure change to undo. If you want, separately consider:

1. **Figure 1 layout.** The two panels are side-by-side at half-width, which makes panel
   (b)'s finer labels small. Stacking them full-width would improve legibility.
2. **Panel (b) is raster** (`.png`); the other main figures are vector. A vector re-render
   is the clean fix (CHPC).
3. **Inset redundancy in panel (a).** The reused locator keeps its baked-in nesting inset,
   which duplicates panel (b). The clean fix is an inset-free re-render of panel (a) via
   `plot_wrf_transect_locator.py` (CHPC).
4. **Section re-titles / prose.** If any Methods/Results re-title above reads as not yours,
   that is the only place the flurry rewrote wording; say which and I will restore the
   pre-flurry phrasing.
