# WRF archive ↔ Tran et al. (2018): contradictions, corroborations, checks

Working notes for the Michael/Trang provenance thread · 2026-07-07
Migrated from `wrf-nudge-ozone-air2026` commit `caf5c69`.
Sources: Tran et al. (2018), the local supporting critique at
`notes/literature/tran-2018-fdda/critique.md`, and the external ceidwad
`notes/braindumps/DISCUSS-MICHAEL-TRANG-DATA.md` deductions from
`namelist.input_revised_nudge_d03` plus archive listings under
`WRF_TRANG_frozone/`. The full paper extraction was not copied here.

**Evidence boundary.** Archive and path observations below are a 7 July 2026
snapshot. Recheck any open operational question before treating it as current; use
`verification/provenance/run-inventory.csv` for paper-facing run identity.

**Stance.** Neither source is gospel. The paper has demonstrated writing errors — a false blanket significance claim (C10), a wrong reference year (C12), a self-contradicting sign convention (C7), numbers that drift between sections (C19) — and leans on "(not shown)" for load-bearing claims (C5). The archive is partial: the only WPS namelists found are a 2006 case, the `._namelist.wps` hits are AppleDouble stubs, and the fdda coefficients haven't been dumped yet. So every item below states both sides, a verdict on which side logic favours, and the check that settles it. "The paper says" resolves nothing on its own.

## 1 · Not actually conflicts (ruled out by logic)

| Item | Paper | Archive | Resolution |
|---|---|---|---|
| Vertical count | "41 vertical layers" (§2.1) | `e_vert=42` | Same thing. WRF counts level *interfaces* (42) bounding 41 mass layers. Don't let anyone flag this as a mismatch. |
| First layer | "thickness of the lowest vertical layer was 18 m" | first η ≈ 0.9976 | Consistent: Δp ≈ 0.0024·(85 000−5 000) ≈ 190 Pa ≈ 18–19 m at basin surface pressure. Corroborates same-family config. |
| d03 grid spacing | "1.3 km" | 1.333 km (dx=4000/3) | Paper rounds; 3:1 nest ratio of the 4-km domain forces 1.333. |
| Jan/Feb windows | "re-initialized every 5 days... 132-h batch... overlapped 12-h" (§2.2), episode Jan 16–Feb 4 | scored segment "Jan 15–21"; namelist window "Feb 4–10" | The batch cadence *predicts both*: starts Jan 15 12Z, Jan 20 12Z, Jan 25 12Z, Jan 30 12Z, Feb 4 12Z; each 132 h. "Jan 15–21" = batch 1 (spin-up Jan 15 12Z–Jan 16 00Z, scored from Jan 16 — matching the paper's episode start). "Feb 4–10" = batch 5. This also explains the original Feb/Jan mix-up. |

Note the corollary of the last row: **batch 5 postdates the paper's analysis window** (the paper needs only batches 1–4 to cover Jan 16–Feb 4). Its existence is positive evidence the archive contains more than the paper's production — see §3.

## 2 · Corroborated (independent agreement — still not proof)

- **Physics suite and nudging structure.** Thompson (mp=8) / RRTMG (ra=4) / MYJ PBL (bl=2) + MYJ surface layer (sf_sfclay=2) / Noah (sf_surface=2) / KF on d01 only (cu=1,0,0); one-way nesting (feedback=0); obs nudging of T + wind on d03 only; analysis nudging 6-hourly, suppressed inside the PBL, all three domains; 33-category USGS land use (highly distinctive — the paper §2.1 explicitly modified CMAQ to accept WRF's 33 categories). Every namelist-checkable particular of §2.1–2.2 matches. Coincidence is implausible; this is the same modelling system or its direct descendant.
- **Forcing dataset.** Paper: "NAM-12km analysis data (NOAA, 2015)" for IC/BC, and §2.2.2: analysis nudging used "the same dataset used for WRF initial and boundary conditions". Metadata: `interval_seconds=21600` + `num_metgrid_levels=40`. As commonly ungribbed for 2013-era data: NAM-218 → 40 (39 isobaric + surface); GFS-FNL → 27; ERA-Interim → 38; NARR → 30 (and NARR is 3-hourly, excluded twice over). So the metadata *uniquely fits* the paper's claim among the usual candidates. Verdict: NAM-12km is very likely — but the paper is the only source that *names* it, and the paper's QC record is poor, so keep Trang's confirmation on the list; it just becomes a leading question ("NAM-12km, same as IC/BC — right?") instead of an open hunt. Clinchers if paper-independent proof is wanted: WPS prefix/Vtable in any surviving `namelist.wps`, or a `met_em*` file's field provenance.

## 3 · Genuine conflicts (open)

### 3.1 Model top: "14 km AGL" vs p_top = 5000 Pa

Paper §2.1: 41 layers "extending from the surface to 14 km above ground level" (≈140–150 hPa). Namelist: p_top = 5000 Pa ≈ 20.5 km ASL ≈ 19 km AGL over the basin. No reading reconciles them; one is wrong.

- **Weighing:** e_vert and the 18-m first layer match exactly, and 50-hPa tops are ordinary for WRF-CMAQ ⇒ *paper writing error* likelier than a config fork — but a fork can't be excluded, since the archive demonstrably contains post-paper material (§3.3).
- **Settle it:** `P_TOP` (and `ZNW`) in any d03 wrfout header — comes free with the version check (§3.2). One ncdump.
- **For the manuscript:** either way, the paper's config paragraph can't be inherited verbatim — cite Tran et al. (2018) for the design, state archive-verified values.

### 3.2 WRF version: paper "V3.6" vs "WRF3.9" backups

The paper's inputs were retrieved 2015–2016 (its own reference access dates), it was submitted Aug 2017, and WRF 3.9 was released April 2017 — so the *production* runs almost certainly predate 3.9. The "WRF3.9" label therefore marks later activity (re-runs, rebuilds, or just a code directory). The live question is which era produced the archived/scored *output*.

- **Settle it:** `ncdump -h` on one scored wrfout — the global attribute `TITLE` literally reads "OUTPUT FROM WRF V3.x.x MODEL". Cheapest check on this list; do it first.
- **If 3.6.x ⇒** archive = paper-era production. Cite Tran et al. (2018) §2 as the methods source, with archive-verified values where the paper is demonstrably sloppy (§3.1, §4).
- **If 3.9 ⇒** the scored output is *not what the paper evaluated*. Cite the paper for design heritage only; every config fact in the methods must come from the archive, and Table 1 no longer describes these files.
- **Research note:** mostly provenance hygiene — but a clean case study in why "the methods live in the paper" fails; supports the data-availability practices already in train.

### 3.3 Run identity: `WRF_anlnudge` ≈ OAN, and "revised" is unexplained

The namelist has *both* grid nudging (grid_fdda=1) and obs nudging on d03 — in the paper's vocabulary that is **OAN** (its *worst* run for inversion structure), not ANU; the dir name undersells it. The file is called `revised_nudge`, next to batch 5 (past the paper's window, §1), a Pleim–Xiu land-surface sibling the paper never mentions, and `run_PA_anlnudge` — "PA" reads naturally as CMAQ **process analysis**, exactly what the paper's §3.2 defers to "future photochemical study". And the paper itself sketches a nudging revision as future work (§2.2.2): coefficients below 3×10⁻⁴, "targeted" nudging only above ~250 m. A file named `revised_nudge` could literally be that. Verdict: archive ⊇ paper; the scored segment's vintage is unestablished.

- **Settle it (fingerprint):** dump the fdda blocks. Paper's OAN: gt = 3×10⁻⁴ (T,u,v), gq = 1×10⁻⁵, obs coefficient 4×10⁻⁴, radius of influence 100 km, 40-min time window, obs influence spread to model level 3. Exact match ⇒ paper config; smaller/targeted ⇒ the revision. Add these variables to the provenance script's §3 dump.
- **Also:** count namelists per run dir (paper-era production ⇒ 4–5 batch namelists; a lone Feb file ⇒ partial archiving); `OBS_DOMAIN301` files present ⇒ obs nudging really ran; wrfout `XLAT/XLONG` corners vs the namelist's 298×322 (~397×429 km) vs Fig 1's extent, as one more fingerprint.
- **If OAN-as-published ⇒** the paper's own evaluation becomes the citable expected-bias baseline for the scored met: ~+3.0 °C warm at the surface during inversions, worst-in-family inversion structure ("unrealistically extreme stratified stability"), night winds a few m s⁻¹ too fast (Table 1, §3.1.4). For a surface-weather application that is the caveat paragraph pre-written — used with the critique's statistical caveats (C8, C10: the table's significance claims are broken; indicative, not gospel).
- **If the revision ⇒** *no published evaluation of the scored configuration exists.* The manuscript must say so, and probably do its own light verification of the segment.
- **Research note:** if it is the revision, unpublished methodological progress is sitting in the archive — worth asking Trang whether a short follow-up or technical note is warranted. Either way the answer dictates what to nudge (or not) in any future basin runs.

### 3.4 "The inversion is free-running physics" — braindump claim vs paper mechanism

Braindump bottom line: nudging is suppressed in the PBL ⇒ the inversion is un-nudged ⇒ the warm surface bias is a real model failure, not a nudging artifact. The paper's own mechanism says otherwise in cold pools: WRF gates "in the PBL" by the *diagnosed* PBL top, and MYJ pins that at level 1 (~18 m) during inversions (paper §3.1.1, §3.1.3) — so "above the PBL" starts at level 2 (~38 m), and with ~15 levels below 500 m, most of the inversion column **is** nudged toward the 12-km NAM analysis. Consistent with that, the paper's analysis-nudged runs carry the *largest* warm surface biases (+3.0/+5.0 °C vs +1.0 without; Table 1).

- **So:** the scored run's warm bias may be partly a nudging artifact — the opposite of the current line to Michael. It may still be mostly physics (the no-nudge run also runs ~10 °C warm on the coldest nights); attribution needs a comparison.
- **Settle it:** (i) best — find a no-nudging or obs-only sibling for the scored window in the archive and difference it against anlnudge: clean attribution. (ii) cheap partial — the `PBLH` variable in the scored output: pinned at ~18 m through the inversions ⇒ nudging was active from level 2 up, and "free-running" is dead on arrival. (iii) symmetry — the "NAM is warm/moist" *direction* is itself a "(not shown)" paper claim (C5); verify before building on it.
- **For the manuscript:** soften any sentence attributing the bias purely to model physics — "bias in this configuration" until the sibling comparison exists.
- **Research note:** the generative one. The diagnosed-PBLH/nudging coupling is a publishable stable-PBL DA pitfall, and the modern experiment — rerun the 2×2 with HRRR-era analyses, or gate nudging by rim height instead of diagnosed PBLH — is a fundable, basin-relevant follow-on that connects to road-weather verification. It is also where the Tran + Neemann synthesis will point.

## 4 · Paper claims the archive cannot verify (inherit with caution)

- **Stock vs Neemann-modified Thompson.** The paper claims it did *not* apply Neemann's cloud-microphysics modifications (§2.1) — an in-code change, invisible to the namelist (mp_physics=8 either way). Central to the paper's cloud story. Only Trang (or the archived source/executable) can confirm which code the runs used.
- **Snow ICs and surface parameters.** Replacement of NAM snow with observations + SNODAS, modified vegetation parameters and max snow albedo (§2.1) — lives in wrfinput/geo files and code, not the namelist. `num_land_cat=33` corroborates that Neemann-style surface treatment happened, but not the details. Checkable in principle (diff wrfinput `SNOW/SNOWH` against raw NAM); cheaper to ask.
- **NAM warm/moist bias vs sondes.** "(not shown)" twice (C5). If the new manuscript's argument inherits "NAM is biased warm/moist in the basin, therefore …", know that this rests on unpublished data plus Neemann's qualitative "fair to poor".
- **Table 1 statistics.** Sites are listed but hours/QC are not — not recomputable (C18); and the table's own significance claim is false (C10). Don't inherit its numbers as ground truth; treat as indicative.
- **Obs-nudging coefficient/radius/window.** Stated in the paper (§2.2.1) but not yet dumped from the namelist — the cheapest high-value cross-check on the whole list (see §3.3 fingerprint).
- **CMAQ side generally.** Version, dry-deposition mod, SMOKE, inventory, the VOC profile: nothing in the archive scan touches these, and the paper under-documents them (C18). Irrelevant if the manuscript scores meteorology only; flag if chemistry enters.

## 5 · Scoring hygiene for the new manuscript

- **Spin-up clipping.** Batch 1's first 12 h (Jan 15 12Z–Jan 16 00Z) are spin-up the paper excluded. If the scored "Jan 15–21" includes any of Jan 15, those hours contaminate the scores — check the output start time and clip.
- **Segment arithmetic.** "Jan 15–21" read inclusively is 144 h; paper batches are 132 h. Confirm the scored segment's actual start/end from *its own* namelist (not the Feb 4–10 file) — this also tests the paper's "132-h, 12-h overlap" claim against reality.
- **Config continuity.** The paper asserts all four runs kept identical physics and re-init cadence (§2.2) — supports, but does not prove, that the Jan segment matched the Feb namelist. Keep that confirmation on the Trang list.

## 6 · Ask-Trang list (one email, mostly one-liners)

1. Forcing for `WRF_TRANG_frozone`/`WRF_anlnudge`: NAM-12km analyses, same as IC/BC? (leading question per §2 above)
2. Is `namelist.input_revised_nudge_d03` the 2018 paper's OAN configuration, or the post-paper lower-coefficient/"targeted" revision sketched in the paper's §2.2.2?
3. Did the Jan 15–21 segment run the identical config as the Feb 4–10 namelist?
4. WRF version of the archived output — 3.6 as published? (or we read a wrfout `TITLE` ourselves — faster)
5. Thompson microphysics: stock (as the paper claims) or Neemann-modified code?
6. What is `run_PA_anlnudge` — CMAQ process analysis, i.e. the "future work" of the paper's §3.2?

## Cross-references

- Full journal-club critique: `notes/literature/tran-2018-fdda/critique.md` —
  especially C5 (not-shown NAM bias), C7 (sign convention), C8/C10
  (statistics), C18 (reproducibility), and S2 (the collapsed-PBLH/nudging
  coupling that bears on the "free-running physics" question).
- Provenance thread: `~/gits/ceidwad/notes/braindumps/DISCUSS-MICHAEL-TRANG-DATA.md`.
