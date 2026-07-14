# An outsider's critique of `_manuscript_v3.tex`

**Author:** Claude (Fable 5), acting as an outside writing partner, at John's request.
**Date:** 14 July 2026.
**Version reviewed:** `_manuscript_v3.tex` at HEAD `29854aa`. The archived review PDF
(`drafts/manuscript-v3_2026-07-14_terrain-heat-deficit-review.pdf`) was built from
`f995f5b`; the only tex change since then is the three-line episode-context rewrite-gate
update in `29854aa` (MODIS candidate now in hand). So yes — the current tex **is** the
version rendered into the `*heat-deficit*.pdf`, to within that one scaffolding note.
I read the rendered PDF page by page as well as the source.

**Scope.** Narrative, argument strength, structure, figures, and evidence use.
References and citation mechanics are ignored per instruction (the Paperpile handoff is
its own track). I respect the repo's standing rules throughout: failed gates stay
failed, nothing here proposes promoting gated material without new evidence, and every
"the draft never says X" claim below was checked against the tex directly, not taken
from summaries. I did not rerun any analysis; I did cross-check the draft's numbers
against the committed artifacts.

**A trust statement first.** Every load-bearing number I spot-checked — the stability
and transport-wind contrasts and their hourly ranges, the T2/wind/pressure surface
table, the heat-deficit means, changes, envelopes, and footprint geometry, the
sign-shares, the CMP06/CMP07/CMP08 tables, the terrain RMS values, the radiation TSK
contrast, and the station-elevation match — reconciles exactly with
`verification/data/*.csv` and the ANA-16..20 provenance JSONs. The quantitative spine
of this draft is, as far as I can tell, flawless. Everything below is about what the
paper *says*, not whether its numbers are right.

---

## 1. Overall verdict

This is an unusually honest, unusually well-audited working draft with a real result
inside it, wrapped in a presentation that currently works against the result three
ways.

**What is genuinely strong:**

1. **The design is the right design.** A clean 2×2 driving-product × nest-feedback
   matrix, with the product contrast required to replicate under both feedback modes
   before it counts, is exactly how to make a case-study sensitivity claim robust. The
   replication framing ("the response must recur under both feedback settings") is the
   best structural idea in the paper and deserves to be named louder.
2. **The pre-declared-gate discipline is rare in this literature and is itself a
   contribution.** Criteria fixed in committed scripts before outputs were read;
   near-miss failures preserved rather than rescued (the spatial gate failed by as
   little as ~0.001 in sign share and is still reported as failed). Most WRF
   evaluation papers do the opposite. Right now this discipline is presented as
   internal process scaffolding; Section 5 below argues it should be elevated into the
   paper's methodological identity.
3. **The heat-deficit distinction — a state offset, not faster loss — is the most
   publishable sentence in the paper.** It converts what could have been an
   overclaimed "GFS erodes the cold pool" story into a sharper, defensible claim, and
   it demonstrably came from a falsification test that failed as declared.
4. **The negative design finding (the false resolution ladder, Table 3) is genuinely
   useful** to the community and is written with admirable clarity.

**The three core problems:**

- **P1. The title and abstract promise what the gates emptied.** "Cold-Pool
  *Structure* and *Evolution*" names, almost exactly, the two main-slot results that
  failed their gates: the spatial/vertical-structure gate (ANA-19 → Main C3 empty) and
  the maintenance/evolution gate (ANA-16 → Main C4 empty). What the paper actually
  delivers is a replicated five-hour *state contrast* plus bounds. The repo's own
  title genealogy (`notes/narrative-and-hypotheses.md`) shows "Retention" was retired
  for precisely this reason, and flagged the title for coauthor revisit — that
  revisit is now due. Candidate directions in §3.1 below.
- **P2. The paper is more neutral than its own evidence.** The draft repeatedly and
  correctly says "no single surface score ranks the products," then stops. But every
  temperature-linked measure it reports points the same way: GFS per-run T2 biases of
  +2.09/+2.51 °C against NAM's +0.40/+0.60 °C (numbers that exist in `main.tex:173`
  and the ledger but were dropped from v3); GFS absolute T2 error worse by
  +1.41/+1.50 °C; and the observed bench-minus-floor θ index (12.63–20.21 K) that NAM
  sits *inside* (16.44–18.07 K) while GFS sits *entirely below* (7.35–11.74 K). GFS
  wins only surface pressure, by ≲0.14 hPa. A precisely-scoped sentence — "on the
  temperature-linked measures that define a cold pool at the surface, the NAM-driven
  state is the more credible one; its vertical structure remains unvalidated" — is
  fully supported and much more informative than symmetric agnosticism. Right now the
  reader must assemble the paper's most consequential inference alone, from an
  appendix table.
- **P3. The prose reads as an audit record, not an argument.** Eleven X codes, twelve
  CMP codes, twelve C-numbers, four ANA gate names, and two Slurm job IDs appear in
  manuscript prose and captions, including a Results section *title* ("Terrain-Source
  Brackets (CMP09–CMP11)"). The repo's own structure review says run identity belongs
  in provenance, not manuscript-facing narrative. An outside reader needs the levers
  (driving product, feedback, scheme, radiation, terrain source) — not the ledger.

Secondary, but important: the episode itself is barely present (no synoptic setting,
no ozone number, no observed snow statement — §4.6), the absolute magnitudes that make
the contrasts interpretable live only inside figures (§4.4), and several figures'
narrative weight exceeds their admission status (§6).

---

## 2. The story as told vs. the story available

**As told,** the arc is: here is an archive of runs; here is how we organize its
contrasts; the product contrast is biggest and replicates; the heat deficit shows a
state offset; the other knobs are small or failed their gates; many things remain
unshown. The connective tissue is the archive ("The archive is not a chronological
experiment sequence…", `_manuscript_v3.tex:71`, before "the archive" has even been
introduced as a concept). The reader tours a filing system.

**Available,** with the same evidence and no new claims, is a question-driven arc:

1. *Does the driving product change the lower-layer state a chemistry model would
   receive?* — Yes: warmer, ~3.6 K less stable over 50–500 m, ~2× the transport wind,
   ~30 % less footprint heat deficit; replicated under both feedback modes.
2. *Which supplied state looks more like the observed cold pool?* — At the surface,
   NAM, on every temperature-linked measure; pressure marginally favors GFS; wind is
   a wash. Vertically: unknown, and say so once, plainly.
3. *Is the difference an evolution difference?* — No. Both products *gain* deficit
   through the window; the pre-declared faster-loss test failed 0/14. It is an
   inherited offset, present by 13:00 UTC (~1.7 MJ m⁻² in the committed trajectory).
4. *Can any tested internal knob rival it?* — No. PBL/surface-layer swap: an order of
   magnitude smaller and metric-mixed. Slope radiation: invisible at the floor,
   measurement-limited on the walls. Feedback: near-null twice. Default-vs-fine
   terrain: failed its gate. This is a response *hierarchy*, and it is the paper's
   most actionable finding for practitioners.
5. *What would it take to matter for ozone?* — The next-experiment paragraph the
   draft already has, minus the repetition.

Notice that this is nearly the existing section order (§3.3 → §3.4 → §3.5 → §3.6–3.8).
The bones are right. The problem is voice and emphasis, not architecture: each section
currently opens with provenance status ("gate executed and failed", "restored for
editorial review") where it should open with the scientific question, and the
hierarchy — the one thing a WRF-Chem practitioner will quote — is stated once
(§3.2, §4.3) but never given a consequence. One added Discussion paragraph would do
it: *for this case, the choice of driving product moved the supplied stability by an
amount ~30× the PBL-scheme response on the same pipeline; winter-ozone hindcast
evaluations that sweep physics but fix the driving product are sweeping the smaller
axis.* That sentence is supportable line-by-line from Table A1 and Table A3 (with the
cross-branch caveat the draft already states in §2.3).

**On P2, to be fair to the draft:** the refusal to rank is principled — pressure does
flip, wind error does change sign, and inversion depth is unvalidated. The critique is
not "declare NAM better." It is that the draft already implicitly ranks (why else
report GFS's *warm* bias and *smaller* deficit against a *cold-pool* target?) while
declining to say the conditional sentence out loud. Reviewers will either draw the
inference themselves and wonder why you didn't, or — worse — ask you to defend
neutrality you don't actually hold. Scope it ("temperature-linked, surface-anchored,
this case, this window") and say it.

---

## 3. Section-by-section

### 3.1 Title

See P1. Three directions, in increasing order of assertiveness:

- Keep the retired runner-up, which is accurate and modest: *"Short-Window Response of
  WRF Cold-Pool Structure to Driving Data and Nest Feedback during a Uinta Basin
  Winter Ozone Episode"* (already flagged for coauthor revisit in
  `notes/narrative-and-hypotheses.md`).
- Lead with the mechanism-shaped finding: *"A State Offset, Not Faster Loss:
  Driving-Data Control of the WRF Cold-Pool State in a Uinta Basin Winter Ozone
  Case."* ("Control" is defensible here because the claim is about the supplied
  state, not attribution within the bundle — but check comfort level.)
- Lead with the hierarchy: *"Driving Data Outweigh Tested Physics Choices in WRF
  Simulations of a Uinta Basin Cold Pool."*

Any of these beats the current title, which promises structure validation and
evolution — the two things §5 and the abstract explicitly disclaim.

### 3.2 Abstract

151 words — good; there is headroom under MDPI's ~200 for the two missing things:

- **Context for the magnitudes.** "About 3.6 K less stable" lands only if the reader
  knows the base state. One clause fixes it: "…about 3.6 K less stable from 50 to
  500 m — roughly a third of the NAM members' 10–12 K fixed-layer stability…"
  (readable off Figure 4; exact members' values are in `retention_hourly_summary.csv`).
- **The method identity.** "Pre-declared criteria" / "predeclared gates" appears
  nowhere in the abstract, yet it is the paper's strongest shield and its most novel
  process feature. One sentence: "Both heat-deficit criteria were fixed before any
  output was inspected; the faster-loss criterion failed and is reported as failed."
- The final sentence is a five-item negation list with a zeugma ("does not isolate…,
  validate inversion depth or event-scale persistence, or predict ozone"). Split it:
  one sentence for the design boundary (initial vs. lateral forcing), one for the
  validation boundary (no vertical observation; no chemistry).

### 3.3 Introduction

- The literature framing (compensating errors; labels are not levers) is strong and
  well-chosen — genuinely good writing.
- The paragraph at `_manuscript_v3.tex:71–77` is the insider-speak peak: "The archive
  is not a chronological experiment sequence… we organize it by the lever that each
  contrast can identify." An outside reader does not know there is an archive, why it
  would be chronological, or what X0–X10 are. Recast in experiment language: "We
  assembled eleven simulations into four controlled contrasts…" and move the
  provenance-code system entirely into Methods (one sentence there suffices).
- The four questions are good but arrive as unnumbered prose across two paragraphs,
  with the heat-deficit question appended as a rider. Number them (Q1–Q4), and map
  each Results subsection to one — the paper is *already* organized this way; make it
  legible.
- **Missing: a novelty sentence.** Neemann bundled physics changes; Ahmadov fixed
  meteorology and scaled emissions; Matichuk changed several levers at once; Tran
  varied nudging. None crossed driving product with feedback under matched physics
  for this case. The draft is entitled to say plainly: "To our knowledge this is the
  first controlled driving-product × nest-feedback comparison for a Uinta Basin
  winter-ozone case, evaluated under pre-declared criteria." Say it.
- **Missing: why GFS-vs-NAM in 2026.** A reader will ask why a 2013-era product
  comparison matters now (NAM's operational sunset is public knowledge; ERA5/HRRR
  exist). The durable answer is already implicit in the paper: the *lesson* is not
  "prefer NAM" but "the driving-data bundle is a first-order axis that compensating
  surface scores hide" — which transfers to any product pair, including
  reanalysis-driven hindcasts of the episodes this community still simulates.
  One or two sentences in the Introduction (and one in Conclusions) close this.
- Unused ammunition for the framing already sits in `notes/literature/`:
  Tran's ~10 °C peak nighttime warm bias and the collapsed ~18 m MYJ PBL heights
  behind episode-mean scores (`tran-2018-fdda/critique.md`), and Matichuk's
  177-paired-profile census behind the met–ozone decoupling claim
  (`matichuk-claim-rows.md`). Both make the draft's "aggregate scores can obscure a
  failure to retain the layer" sentence concrete instead of abstract. (Citation
  wording can wait for the Paperpile batch; the numbers are verified in the notes.)

### 3.4 Methods

Mostly excellent: the estimand-first structure, the explicit product-bundle caveat,
and the d02/d03 coverage reasoning (C03) are model methods writing. Gaps:

- **"Block-sensitivity intervals" are used (Fig. 3 caption, Tables A3/A6) but never
  defined.** The definition exists in the lineage — `main.tex:143`: a two-hour
  circular moving-block resample of the five hourly medians, repeated 20,000 times,
  descriptive only. v3 dropped the sentence but kept the term. Two sentences in §2.5
  restore it; without them the whiskers in Figure 3 are uninterpretable.
- **The eleven "registered basin waypoints" (§2.6) appear from nowhere.** Say in one
  sentence what they are, how they were chosen, and where they are registered
  (they live in the figure-config TOMLs and the ANA-16/19 footprint records).
- **No station table.** Names, networks, elevations, and periods of record are
  committed (`verification/data/stations_2013_selection.csv`); the draft names only
  two stations in prose, and elevations surface only inside Figure 2's legend. A
  small table (or appendix table) also quietly satisfies part of the observation-
  provenance gate.
- **The 2200 m crest choice is undefended.** One sentence on why 2200 m (relation to
  rim height / bench elevations; Mountain Home at 2228 m is nearby context) plus the
  observation that the 2100/2300 m variants are in the sensitivity family would
  pre-empt an easy referee question.
- The spin-up choice is honestly flagged as unevaluated (`:91`). Fine for a working
  draft; expect a referee to ask for the 1-hour and 3-hour variants. Cheap to add to
  a future recompute batch; not a blocker.
- Table 2's "Status and gate" column mixes scientific role with audit status and
  produces the tallest, hardest-to-read cells in the paper (p. 6 of the PDF). Split
  "what it isolates" (keep) from "gate outcome" (append to the appendix), or the
  table teaches codes before it teaches design.

### 3.5 Results

- **§3.2 (effects panel) is the right figure in the right place with the wrong
  status.** Figure 3 carries the paper's summary claim (the hierarchy) and is
  labeled "not yet registered or promoted." Registering it is already on the repo's
  list; treat that as blocking for coauthor circulation, since this figure — not the
  retention figure — is what most readers will remember.
- **Absolute values are figure-only.** Text and tables report contrasts (Δ), never
  levels. From the renders: NAM stability ~10–12 K vs GFS ~6–8.5 K (Fig. 4a); GFS
  transport wind ~1.6–3.2 m s⁻¹ vs NAM ~0.7–1.4 (Fig. 4b) — i.e., GFS roughly
  *doubles* the transport wind, which "0.8–1.0 m s⁻¹ faster" understates; NAM deficit
  ~4.2 MJ m⁻² vs GFS ~2.5–3.2 (Fig. 8a). One sentence of levels per result section
  makes every contrast interpretable and costs three lines total. (Also note both
  transport winds are *weak* in absolute terms — worth saying, since "faster" could
  otherwise read as "ventilated.")
- **The hour-by-hour structure is reported but never read.** Two committed, opposite
  trends: the station-median stability separation *grows* through the window (−0.90 K
  at 14:00 UTC to −5.36 K at 17:00, `retention_pair_hourly.csv`; visible in Fig. 4),
  while the footprint deficit gap *narrows* into 16:00 UTC (−1.50 → −0.97 MJ m⁻²,
  Table A2; visible in Fig. 8b) — and the spatial sign-share *rises* (0.64 → 0.93).
  The draft quotes all three ranges and interprets none. Either add two sentences of
  reading (e.g., the layer separation organizes as the morning boundary layer
  develops, while the integrated deficit gap partially closes as GFS gains deficit)
  — or state explicitly that hour-to-hour evolution is observed but not interpreted.
  Right now the numbers invite a question the text pretends not to hear.
- **§3.4 is the structurally weakest section.** It contains: a one-sentence orphan
  paragraph with a stray duplicate label (`:339–341`); the spatial result; **two
  parked figures that belong elsewhere** — Figure 6 (CMP11 terrain sections, subject
  of §3.8) and Figure 7 (spin-up profiles); and Figure 7 is **never cited anywhere in
  the text** (label at `:407`, zero `\ref{fig:v3-spinup-profiles}` — it will render as
  an unexplained figure in every build). Move Figure 6's shell into §3.8, give
  Figure 7 either a home (§3.3, one sentence on initialization contrast, model-only)
  or the reserve pile, and merge the stray paragraph.
- **ANA-16 is the missing gate name.** The intro scaffolding block names "ANA-17,
  ANA-18, ANA-19, ANA-20" as "the analysis gates named in this draft" — and indeed
  ANA-16 appears nowhere in the tex, even though §3.5 and Table A2 report exactly its
  criteria and outcomes (7/7 weaker-state, 0/7 faster-loss). Since the draft names
  its other gates, name this one; it is the paper's most important gate, and the
  scaffolding sentence is currently self-referentially false once you notice.
- **The heat-deficit difference-in-change envelope is the one place the appendix
  under-reports the sensitivity family.** Table A2 reports "Difference in change
  (primary) +0.17/+0.17" — but the committed family
  (`heat_deficit_pair_summary.csv`) spans **−0.066 to +0.319**, and under the 2100 m
  crest *both* pairs are negative (GFS gained *less* than NAM). This does not touch
  the gate outcome (faster-loss failed because GFS's change is positive everywhere),
  and it actually *strengthens* the paper's own point — there is no robust
  evolution difference in either direction. The draft prints envelopes for the level
  differences; print the envelope for the change difference too, exactly as honestly.
- **C-number hygiene is inconsistent.** CMP-family claims carry ledger tags in prose;
  the heat-deficit result (C26) and the pressure metric-dependence argument (C27) —
  the two *newest* arguments — never do. Either drop manuscript-facing C-numbers
  entirely (my preference; see P3) or tag uniformly. Also, Table 2 cites C19, which
  the ledger marks *provisional/superseded* ("refining C19" is technically fine, but
  the admission rule says provisional stays out of prose — "(C32)" alone is cleaner).
- **CMP08 is undersold by one detail.** The gate record shows the transport-wind
  block interval (+0.069..+0.126 m s⁻¹) *excludes zero* — the strongest statement
  available that the scheme response is detectable rather than noise. Table A3 gives
  means and sign counts only. Add the interval column for CMP07/CMP08 as Table A6
  already does for CMP06; consistency between the two process tables is currently
  broken in exactly the place where it matters.
- **Feedback sign conventions flip between tables.** Table A1 reports one-way −
  two-way; Table A6 (CMP06) reports two-way − one-way (X9−X0), with the orientation
  stated in the caption. Both are internally correct; jointly they invite a sign
  error by any reader comparing them. Align them, or add the negated row.
- §3.8's verbal reading of Figure 10 ("Blue dominates much of the central basin") is
  generous for such a speckled field (see §6). The committed per-cell area fractions
  (`heat_deficit_trajectory.csv`: `area_fraction_ge_*`) could quantify "dominates" as
  a descriptive statistic without inventing a CMP11 gate — or soften the verb.

### 3.6 Discussion

- §4.1 and §4.2 are good — §4.2 especially ("state offset… A longer integration
  through at least one complete diurnal cycle is required") is exactly the right
  register.
- **The near-miss deserves one sentence of texture.** The spatial gate failed at
  14:00–15:00 UTC by margins of 0.001–0.025 in sign share (one pair-hour at 0.666 vs
  the 2/3 criterion). Saying so is not rescuing the gate — the draft's "preserving
  failed criteria is more informative than rescuing them" stance is right and should
  stay — but "failed, narrowly, at the two earliest hours, then passed strongly"
  is the honest shape of the result, and it sets up the already-permitted future
  gate (16–18 UTC coherence, predeclared afresh) that the gate review contemplates.
- **The unmentioned diagnostic lead.** The ANA-19 sections record "strongest warming
  in the lowest ~300 m, a cool band near rim level, and a secondary elevated warm
  layer near 2500–3200 m MSL" (`rewrite/HYBRID-GATE-REVIEW.md`), explicitly labeled
  an unanalyzed lead. The draft never mentions it. As a *labeled lead* in the
  future-work paragraph it is admissible and genuinely interesting (a rim-level cool
  band is exactly where product vertical-level differences would bite). John's call;
  flagging that the draft chose silence where the record has a lead.
- **§4.3's second paragraph is the draft's longest and most exhausting** — the
  requirements dump ("Testing that story requires matched d02 and d03 heat-deficit
  trajectories, a common-support cold-air volume or mass diagnostic, outlet-normal
  transport, and time-resolved sections… Vertical-velocity and turbulence
  diagnostics… cloud water, precipitation, humidity, and stability diagnostics…").
  All true; none of it needs to arrive as one breathless sentence pair. Convert to
  two short sentences naming the two or three *decisive* missing diagnostics and push
  the full list to the (already excellent) exclusion list in the CHPC handoff.
- **The terrain-redistribution story gets more airtime than its status supports.**
  Two main-text figures (10, 11) plus a named hypothesis (upstream reservoirs, Browns
  Park / Split Mountain / Tavaputs) for a contrast with *no declared gate*, in a
  paper whose fine-terrain gate *failed*. The text's caveats are impeccable — but
  narrative weight is a claim of its own. Either scope §3.8 + §4.3 down to "the
  controlled bracket exists, the response is large and terrain-correlated
  (0.50–0.67), and it motivates a predeclared future gate," or accept that reviewers
  will treat the redistribution hypothesis as a finding and ask you to defend it.
  The d03 renders (pending) should inform which; see §7.
- **Repetition audit.** "State offset, not faster loss" appears ~5 times (abstract,
  §3.5 heading + text, §4.2 title + text, conclusions); the product-bundle caveat 3
  times (§2.3, §4.1, conclusions); the PBLH-is-scheme-dependent caveat ~5 times; "not
  confidence intervals" 3 times. Twice each is enough — say it once where it lands
  hardest, once in conclusions. A dedicated *Limitations* paragraph in §4.4 would
  absorb most of the repetition pressure.
- **Missing: the practitioner paragraph** (see §2, item 4). §4.1 gestures ("more
  consistent with dilution") but never lands the operational sentence: what should a
  coupled-model study *do differently tomorrow* because of this paper? Answer: treat
  driving data as a swept axis, not a fixed choice; and don't let surface scores
  arbitrate cold-pool credibility. Both are fully supported.
- The next-experiment list (§4.4) omits the one lever the notes flag as declared but
  untested: data assimilation (thread 5 in `notes/narrative-and-hypotheses.md`) — odd,
  because Tran is cited for exactly that sensitivity. One clause fixes it.

### 3.7 Conclusions

Accurate, and the strongest single paragraph in the paper — but it ends on
requirements ("The next experiment requires…"), i.e., on what this paper did *not*
do. End instead on what it *established*: the supplied-state result, the offset
distinction, the hierarchy, and the transferable methodological lesson (bundles
beat labels; gates beat post-hoc thresholds). The negation inventory ("does not
identify… validate… establish… calculate… predict") can compress to one sentence
pointing at the Limitations paragraph.

---

## 4. Figures — audit against the renders

Census: **2 promoted, 4 registered diagnostics, 4 exploratory engine renders, 5
pending files** (per `figures/MANIFEST.md`, `verification/figures/manifest.csv`,
`figures-draft/HARVEST.md`). Only the two promoted figures currently satisfy the
repo's own admission rule — fine for a working draft, but the gap between narrative
weight and admission status is itself a finding of this review.

| # | Content | Status | Notes from the rendered PDF |
|---|---|---|---|
| 1 | Locator, 2 panels | (a) diagnostic, (b) exploratory | The weakest page in the render. Panels use two different terrain colormaps; (a) carries the flagged legacy transects and lat/lon ticks; station labels illegible at print size; (b) has engine-red annotations and tiny fonts. The rewrite-gate's replacement spec is right; note the two panels should also share one colormap and scale language. Pending CHPC product 5. |
| 2 | Observed 2 m T, 4 stations | **promoted** | Clean, legible, elevations in legend. X-axis is local time (MST) while the entire analysis is UTC — add dual labeling or a UTC top axis to spare readers the arithmetic. |
| 3 | Effects panel | **unregistered working figure** | Carries the paper's summary claim; register + restyle is blocking (see §3.5). CMP08's pressure marker sits at the right panel edge (+6.3 Pa) — check for clipping when registering. Caption currently repeats §3.2 nearly verbatim; trim one of the two. |
| 4 | Stability + transport wind series | **promoted** | The paper's evidentiary core and it shows the absolute levels the text omits. Consider annotating the mean separation on-panel. |
| 5 | Spatial Δθ maps | diagnostic (failed gate C30) | Restored deliberately; the caption's failed-gate language is exactly right. Has lat/lon ticks the style contract says maps should drop. Disposition (main/supplement/reserve) is John's call; my outsider vote: supplement — the mean-coherent-but-patchy point is made adequately by Table A5, and a failed-gate diagnostic in the main text invites more referee attention than it earns. |
| 6 | d03 terrain sections | placeholder | Wired for CHPC product 3; currently parked in §3.4 — move to §3.8. |
| 7 | Horsepool 12/13 UTC profiles | placeholder | **Orphan: never cited in text.** Wire a citation or drop to reserve when the render lands. |
| 8 | Heat-deficit trajectories | diagnostic (ANA-16) | Strong figure; the 13Z-context / 14Z-decision boundary (dotted line) is a nice touch. The demote-to-appendix→restore-to-main history resolved correctly: it belongs in the main text — it carries the offset-vs-loss distinction. |
| 9 | GFS−NAM deficit map | exploratory engine render | Informative but stylistically foreign (in-plot title block, "red = 1st deeper" jargon, watermark, lat/lon axes). Registration + restyle before circulation, as its rewrite-gate already says. |
| 10 | CMP11 terrain deficit map | exploratory engine render | Same styling issues; also visually *noisy* — "blue dominates the central basin" is a generous verbal summary of a salt-and-pepper field. Support with committed area-fraction statistics or soften (§3.5). |
| 11 | CMP11 d03 deficit map | placeholder | Pending product 3; caption guardrails already good. |
| A1 | Radiation screen | diagnostic (failed gate C31) | Effective four-panel design — the blank ΔSWDOWN map *makes* the measurement-limitation argument visually. Keep in appendix. Pending restyle (product 6) is cosmetic only. |

Layout: pages 5, 12, 15, 17 are one-third to two-thirds blank (the `[H]` floats +
placeholder boxes). Harmless in a working draft; will resolve at production. Table 2
is the least readable object in the paper (see §3.4).

---

## 5. The buried lede: make the gate protocol a named method

The single highest-leverage revision available, in my view: promote the pre-declared
gate discipline from scaffolding-note status to a short, named Methods subsection
("Pre-declared evaluation criteria," ~10 lines: criteria fixed in committed scripts
before output inspection; each criterion's pass/fail binding; failures reported,
never relaxed; new hypotheses require newly declared criteria). Then let Results
refer to it naturally ("this criterion was fixed before inspection and failed").

Three reasons:

1. It converts every failed gate from an awkward admission into a demonstration of
   the method working. The paper currently *has* this defense but stores it in a
   bracketed diagnostic note that a submission revision would delete.
2. It is the honest answer to the referee question the draft will otherwise face
   repeatedly: "why do you show a figure whose test failed?" Answer: because the
   protocol distinguishes evidence from illustration, and says which is which.
3. It is transferable — arguably more transferable than the case result — and it is
   the thing this paper does that Neemann/Ahmadov/Matichuk/Tran did not.

This costs ~10 lines and removes the need for most per-figure status apologetics.

---

## 6. Missed nuggets

Checked against the tex; each is absent from the draft and available in the repo.
None requires new computation; items marked ⚠ need a scoping decision.

**From committed data (`verification/data/`):**

1. **Per-run absolute T2 biases** (+2.09/+2.51 GFS vs +0.40/+0.60 °C NAM) — in
   `main.tex:173` and the ledger; dropped from v3. Restores the level context and
   powers the P2 sentence.
2. **Member absolute levels for S, U, H** (`retention_hourly_summary.csv`,
   `heat_deficit_trajectory.csv`) — currently figure-only (see §3.5).
3. **Difference-in-change envelope** −0.066..+0.319 MJ m⁻² across the seven
   definitions (`heat_deficit_pair_summary.csv`) — Table A2 gives primary only.
4. **The 13:00 UTC offset** (~1.7 MJ m⁻², committed as trajectory context) — one
   clause strengthens "already present by 14:00 UTC" to "present at least an hour
   before the decision window opens."
5. **Station metadata table** (`stations_2013_selection.csv`: names, networks,
   elevations 1465–2228 m, periods of record) — see §3.4.
6. **Snow, solar, and visibility observation availability**
   (`proxies_2013_availability.csv`): SWE and snow depth usable at 23 stations;
   solar (cloud proxy) at 25; visibility (fog/inversion proxy) at K74V/KPUC/KVEL.
   One Methods/Results sentence turns "snow-covered" from an adjective into an
   observation — *without* waiting for the MODIS/ozone panel. ⚠ scope: descriptive
   context only, no new claim.
7. **Per-station structure** (`retention_station_timeseries.csv`,
   `surface_skill_station_timeseries.csv`, 220 rows each): which stations carry the
   GFS warm bias (floor vs bench) is answerable and currently unasked. ⚠ possibly
   supplement material; the medians hide it.
8. **CMP08 block intervals** (gate record) — see §3.5.
9. Unused committed quantities worth one "available but not analyzed" line in §4.4:
   2 m specific humidity and 10 m wind direction (per-station CSVs), scalar
   layer-mean wind speed alongside the vector transport wind, RMSE/correlation
   scores, per-cell heat-deficit area fractions.

**From notes/ and the gate record:**

10. **The two-site index has no committed CSV** (`notes/manuscript-v3-rationale.md`
    flags it as "the one v3 number set without a committed CSV"; values live only in
    `verification/figures/chpc-figure-inventory-2026-07-10.md:349`). Since Table A4
    prints these numbers — and P2 leans on them — commit the derived CSV (or wire the
    CHPC overlay job to emit it). This is the only place the draft's own
    number-admission rule is currently bent.
11. **X3's index range (16.27–17.59 K) exists too** (same inventory file) — the
    one-way NAM member also sits inside the observed range; strengthens the
    replication texture of the P2 sentence, and X2's value gives the CMP08 aside a
    two-site texture (C19's 18.49 vs 17.18 K bulk-theta contrast).
12. **The 2500–3200 m elevated warm layer** (ANA-19 record) — see §3.6.
13. **Tran and Matichuk specifics** — see §3.3.
14. **The 700 hPa GFS−NAM panels** (candidates, "reviewer reserve" per the structure
    review): the draft never characterizes the synoptic-scale difference between the
    products *at all*, which leaves "the design cannot assign the response to
    components" feeling less motivated than it is. Even one sentence — the product
    contrast is not confined to the boundary layer early in the window (registered
    diagnostic) — plus the reserve figure would help; ⚠ keep it a diagnostic aside.
15. **Episode framing numbers** in `notes/literature/`: observed episodes exceed
    100 ppb ozone (vs the 45–50 ppb modeled-failure anchor in the Tran critique);
    the draft contains no ozone concentration anywhere. Until the ozone panel lands,
    one literature-anchored sentence in §1 gives the reader a number to care about.

---

## 7. The pending CHPC batch, read against the draft

(`rewrite/CHPC-V3-FIGURE-RECOMPUTE-HANDOFF.md`, return record still "Pending CHPC
execution." The handoff itself is excellent — tight scope, hashes, exclusions.)

Product-by-product, from the manuscript's point of view:

1. **Line-free bulk-theta overlays (X6/X5 promote-on-pass; X3/X5 stays candidate).**
   **Wiring gap:** if the X6/X5 overlay passes and is re-promoted, the manuscript has
   **no figure slot for it** — `wrf_inversion_index` appears zero times in the tex.
   Given P2, this figure (model vs observed bench-minus-floor index, NAM inside the
   observed band, GFS below it) is arguably the paper's best missing visual: decide
   *now* whether it enters §3.4 or the appendix, and wire the slot so the promotion
   isn't orphaned. Also note the same job's temperature-series companions stay in
   scratch by design — fine.
2. **d02 CMP11 heat-deficit rerender.** Replaces the engine render behind Figure 10;
   improves styling, not status (still no gate). The §3.8 narrative-weight question
   (§3.6 above) is unchanged by a prettier version.
3. **d03 CMP11 map + sections.** Fills Figures 6 and 11. Two risks worth
   pre-deciding: (a) if the d03 inner-basin structure *contradicts* the d02 reading
   (sign flips at 333 m), §3.8's redistribution story needs rewording the draft
   hasn't reserved — draft one contingency sentence now; (b) the captions promise a
   fixed ±1.6 MJ m⁻² / ±4 K comparability contract — good — but remember d03 covers
   neither Browns Park nor Split Mountain, so the "localized positive features"
   claims remain d02-only either way.
4. **X6/X5 Horsepool profiles (12/13 UTC).** Fills Figure 7 — which is currently
   uncited (§3.5). Decide its argumentative job before it lands: as drafted it
   shows the products' initialized vertical structure difference (model-only), which
   most naturally supports §3.3/§4.1's "the offset is inherited," not §3.4. Wire the
   citation where the argument needs it.
5. **Locator rerender.** Fixes the paper's worst page (Figure 1). The spec in the
   handoff matches the critique above; add "shared colormap across panels" if it's
   not already implied by the style contract.
6. **Radiation restyle.** Cosmetic by contract (numerical differences are a stop
   condition — good). No narrative impact.

**Cross-cutting:**

- The handoff's exclusions (no multi-day run, no new gates, no vertical-velocity or
  moist diagnostics, MODIS/ozone are separate tasks) mean **nothing in this batch can
  strengthen any claim** — it is presentation-and-candidates only. The draft's prose
  should therefore not be waiting on CHPC for anything argumentative; every revision
  in §§1–6 of this critique can proceed now.
- **The episode-context figure is half-unblocked as of `29854aa`:** the MODIS 7-2-1
  snow panel exists as a registered candidate (Terra granule 18:15–18:20 UTC — note
  it falls at the *end* of the analysis window, a nice coincidence worth stating in
  the caption; the GIBS daily-layer caveat is already recorded). The ozone companion
  remains the blocker, and the committed 2013 Synoptic pull has **zero usable ozone**
  (`proxies_2013_availability.csv`: `ozone_concentration … usable=false`) — so that
  panel depends on an external acquisition (AQS/UBOS route named in the structure
  review) that no current dispatch covers. If ozone data acquisition slips, consider
  publishing the snow panel alone with a literature-anchored ozone sentence rather
  than holding the episode-context figure hostage.
- If any product-group's checks fail on CHPC, the manuscript is unaffected except
  for placeholders — the `\IfFileExists` wiring degrades gracefully. The only
  failure with narrative cost is product 1 (the overlay stays withheld and P2 keeps
  relying on an appendix table sourced from an uncommitted CSV — one more reason to
  commit that CSV regardless).

---

## 8. Anticipated referee pushback (MDPI *Air*)

1. *"One case, five hours."* Defensible if owned in one place (Limitations) rather
   than re-apologized in every section; the replication-across-feedback framing is
   the best counterweight — use the word "replicated" more.
2. *"No vertical observation."* Already disclosed repeatedly. The two-site index
   partially substitutes at the surface; the P2 sentence makes that value explicit
   instead of leaving the index as an orphan appendix row.
3. *"Descriptive statistics only, n=5 dependent hours."* Fine *if* the
   block-sensitivity interval is defined (§3.4) and the "deterministic descriptive
   contrasts, not inferential estimates" stance is stated once, prominently.
4. *"Why is a failed-gate figure in the main text?"* Answered structurally by §5
   (named protocol); otherwise expect to relitigate it per-figure.
5. *"Why GFS vs NAM in 2026?"* §3.3's transferability answer.
6. *"You show a big terrain response and refuse to interpret it."* The §3.8 scope
   decision (§3.6 above) should be made deliberately before submission, not by
   default.
7. *"Where's the ozone?"* The abstract's last line already disarms this; the
   episode-context figure (or its interim literature sentence) softens it further.
8. *"The paper is hard to read."* P3. The X/CMP/C/ANA/job-ID load is the single most
   likely source of a "major revision: clarity" verdict. The fix is cheap and purely
   editorial.

---

## 9. Prioritized recommendations

**A. Argument-level (do before coauthor circulation):**
1. Retitle (§3.1) and add the abstract's method-identity + magnitude-context
   sentences (§3.2).
2. Write the P2 conditional-ranking sentence, restore the per-run biases, and commit
   the two-site-index CSV (nuggets 1, 10).
3. Add the practitioner-consequence paragraph to §4.1/§4.3 (§2 item 4).
4. Name ANA-16; print the difference-in-change envelope; add CMP08 intervals; align
   feedback sign conventions (§3.5).
5. Elevate the gate protocol into Methods (§5).

**B. Structural:**
6. De-code the prose: levers in text, codes in Methods §2.2–2.3 + appendix only;
   rename §3.8 ("Terrain-source brackets" without the CMP parenthetical); split
   Table 2's role/status columns.
7. Repair §3.4: merge the stray paragraph, relocate Figures 6 and 7, cite Figure 7.
8. Consolidate repeated caveats into one Limitations paragraph in §4.4; end the
   Conclusions on the established result, not the requirements list.

**C. Evidence dressing (cheap, no new claims):**
9. One sentence of absolute levels per result (stability, wind, deficit).
10. Two sentences reading (or explicitly declining to read) the hourly trends.
11. Snow/visibility observation sentence from the committed availability table.
12. Waypoint provenance + station table + 2200 m crest justification in Methods.

**D. Cuts:**
13. Table 3 (resolution-ladder confounds) → appendix; keep the two-sentence design
    lesson in §2.4. (Keep the finding; demote the table.)
14. Figure 5 → supplement (outsider vote; John's call per the rewrite-gate).
15. Trim Figure 3's caption (currently duplicates §3.2) and the §4.3 requirements
    dump.

**E. Protect (do not do):**
16. Do not reopen or soften any failed gate (ANA-16 maintenance leg, ANA-19 P1,
    ANA-17 CMP09, ANA-18 R1); the near-miss texture (§3.6) is reporting, not rescue.
17. Do not let the redistribution hypothesis harden into a finding without its own
    predeclared gate; no post-hoc CMP10/CMP11 criteria.
18. Do not present the two-site index, transport wind, or heat-deficit proxy as
    inversion depth, export, or observed volume — the draft's current wording on all
    three is correct; preserve it through revision.
19. Keep the "deterministic descriptive contrasts" framing; do not let a revision
    smuggle in inferential language.

---

## 10. Line-level nitpicks

| Location (tex) | Issue |
|---|---|
| `:33–38` | Abstract: zeugma in final sentence; no baseline for "3.6 K"; "about 3.6 K" + "0.8–1.0 m s⁻¹" fine, but see §3.2 additions. |
| `:46–53` | Scaffolding block says "the analysis gates named in this draft (ANA-17…ANA-20)" — false by omission of ANA-16 once its outcomes are reported; fix even in working-draft mode. |
| `:57` | "the meteorological question is therefore not only whether 2 m temperature has a small mean error" — good sentence; consider making it the abstract's opening move too. |
| `:71` | "The archive…" — define or de-jargon (§3.3). |
| `:91` | Spin-up sensitivity unevaluated — candidate for a future recompute batch; fine as disclosed. |
| `:96` | "clamp to the boundary" — plain-language gloss ("fall outside the usable interior") would help non-WRF readers; the PDF caption already does this better than the text. |
| `:101` | θ formula: note κ=0.2854 is Poisson's constant for dry air (one word: "dry-air"). |
| `:186` | "robustness checks rather than a coequal thesis" — excellent; keep verbatim. |
| `:262–264` | Whiteman/Adler methods lineage: fine pending keys; add the 2200 m crest justification here (§3.4). |
| `:266–267` | Waypoints unexplained (§3.4). |
| `:300` | "Figure 3 answers one question:" — strong construction; consider using this move to open §3.5 and §3.8 too. |
| `:312–313` | "block-sensitivity intervals" undefined; "not yet registered or promoted" — register before circulation. |
| `:339–341` | Stray one-sentence paragraph + duplicate `\label{sec:v3-spatial}` mid-section. |
| `:342` | "+1.79 and +1.76 °C" — add per-run levels (nugget 1) so the contrast has an anchor. |
| `:385–408` | Figure 7 uncited (orphan); also sits in the wrong section. |
| `:416` | "This is evidence of a state offset already present at 14:00 UTC" — cite the 13:00 UTC committed context value (~1.7 MJ m⁻²) to push the offset before the window. |
| `:444` | CMP08: add the zero-excluding interval (§3.5). |
| `:449–451` | CMP07's flux limitation ("missing surface heat fluxes") is stated here and again in §4.3 (`:543`, "slope-corrected radiative or surface-flux diagnostic") — keep one. |
| `:469` | "physically informative enough to retain" — the phrase concedes the admission rule is being bent; §5's protocol framing removes the need for this apologia. |
| `:529–531` | Near-miss margins (§3.6). |
| `:547–548` | Requirements dump (§3.6). |
| `:566` | "Only then should selected meteorological states be crossed with emissions and chemical mechanisms" — good; add the FDDA lever to the preceding sentence (§3.6). |
| `:571–576` | Conclusions: end on the result (§3.7). |
| Fig. 2 | MST axis vs UTC analysis — dual-label. |
| Fig. 3 | CMP08 pressure marker at panel edge — check clipping at registration. |
| Table 2 | Split role vs gate-status columns (§3.4). |
| Table A2 | Add difference-in-change envelope row (§3.5). |
| Table A3 | Add interval columns to match Table A6 (§3.5). |
| Tables A1/A6 | Feedback sign conventions flipped between tables (§3.5). |

---

## Closing note

The hard part of this paper — the design, the discipline, the numbers — is done and
done well. What remains is a writing problem with a clear shape: the draft currently
narrates its *process* (archives, gates, codes, admissions) where it should narrate
its *findings*, and it withholds the two most valuable sentences it has already
earned: *the supplied states differ by more than any tested physics choice*, and *on
every temperature-linked surface measure, the NAM-driven state is the credible one*.
Both are scoped, gated, and sitting in the appendix. Move them into the light, name
the gate protocol as a method, fix the title, and this becomes a paper referees will
trust precisely because of the parts that currently read as bookkeeping.

*— Fable 5, 14 July 2026. This document is advisory; it changes no manuscript text,
no figure status, and no gate outcome.*
