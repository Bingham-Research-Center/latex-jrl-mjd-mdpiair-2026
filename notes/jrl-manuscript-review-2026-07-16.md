# Review of John's author draft — 16 July 2026

## Verdict

`jrl_manuscript.tex` is more ambitious, more physical, and more recognisably author-led than either caretaker draft.

It does not need another blank-slate rewrite.

The quickest defensible route is to keep its voice and broader purpose, restore the audited definitions and claim boundaries, retain one controlled terrain diagnostic in the Appendix, and consolidate the best X8 material into a compact supplement.

The paper can say more than “one gate passed and another failed.”

It cannot make a failed comparison prove terrain superiority, resolution benefit, drainage, basin export, or chemistry failure.

A useful rule for the final pass is:

> A failed gate limits the claim, not automatically the value or placement of the visualisation.

## Lineage and current state

The local draft is an edit of `_manuscript_v3.tex`, not an edit of `main.tex`.

- The v3-to-John diff contains 198 insertions and 257 deletions across 455 changed lines.
- The draft is about 8,176 raw TeX words, compared with about 8,899 in v3 and 6,102 in `main.tex`.
- John's substantive edits end at `jrl_manuscript.tex:468`.
- Lines 470--765 are byte-identical to the corresponding v3 Conclusion, Appendix, diagnostic figures, and back matter.
- The terrain, radiation, and five X8 figure environments are inherited v3 material, although John's new prose explicitly asks whether they should be promoted.
- The file contains 15 figure environments, 9 tables, and at least 34 visible citation, reference, figure, or author-question markers.
- `jrl_manuscript.tex` is ignored by Git, so the current author work is not versioned.

The draft does not currently compile.

The first fatal error is the unclosed locator caption at lines 100--103.

Source inspection also finds an unclosed `enumerate` at line 63, an unclosed `itemize` at line 415, invalid dollar delimiters inside the display equations at lines 205 and 251, and several `\approx` commands outside math mode.

These are mechanical problems, not reasons to reconsider the manuscript.

## What changed, and what it says about author preference

### The paper became a practitioner-facing sensitivity paper

The title and abstract now aim beyond a bounded GFS--NAM result toward model preparation, complex terrain, grid spacing, terrain, physics, and implications for air-chemistry modelling (`jrl_manuscript.tex:17`, `33--40`).

The Introduction likewise moves from a narrow supplied-state question to a critique of how winter-ozone meteorology has been configured, evaluated, and sometimes overinterpreted (`46--71`).

That ambition is useful, but the current title and abstract claim experiments that the design did not isolate.

### The organisation became question led

The four explicit questions emphasise feedback, terrain, grid viability, and three-dimensional cold-pool structure (`63--67`).

This is a clear preference for a scientific journey rather than a results-led audit.

The surprise is that the strongest supported result, the repeated GFS--NAM driving-product response, is not itself stated cleanly as one of those questions.

### Physical interpretation now matters more than audit vocabulary

The draft repeatedly asks “of what?”, “what does that mean?”, and whether a figure can replace low-value text (`302`, `320`, `324`, `345--362`, `370`, `390`, `406--407`, `425`, `446--458`).

Those comments correctly identify places where repository gate language had leaked into the paper without explaining the atmosphere.

The author preference is for a result to be understandable in terms of stability, transport, terrain, heat storage, and model design before its provenance status is discussed.

### Null and failed-gate results are viewed as science, not waste

The draft wants to retain the sidewall radiation response, the controlled terrain bracket, and the d04 transport/budget material even when they cannot sustain the original gate claim.

That preference is scientifically reasonable.

Null feedback effects are useful robustness information, and a failed station-based radiation gate can still reveal that a spatially localised sidewall signal is invisible to the station metric.

### The draft wants recommendations, not only a case report

The ensemble recommendation, the concern about 111 m viability, and the AI/ML aside show a desire to tell modellers what to do next (`54`, `423`, `456--458`).

The ensemble point could survive in a bounded future-work paragraph with supporting literature.

The AI/ML comparison opens a new paper-sized argument and should be cut from this draft.

### Practical significance is preferred to formal inference

The new aggregation text explicitly prioritises practical effect size in a deterministic single-case design (`212--218`).

That is a good fit for the experiment, provided the block ranges remain labelled as descriptive dependence checks rather than confidence intervals.

## Recommended thesis

The broader paper can remain defensible if it uses one sentence like this as its centre of gravity:

> In this six-hour Uinta Basin case, the driving-data product produced the largest repeated separation in the modelled lower-layer cold-pool state; smaller controlled physics and feedback responses, together with bounded terrain and fine-grid process diagnostics, show both what common station metrics capture and what they can miss.

This gives the GFS--NAM matrix evidentiary priority without reducing the entire paper to four runs.

It also creates a legitimate role for terrain, radiation, and X8 figures without claiming that they passed tests they did not pass.

A broad but supportable title would be:

> WRF Cold-Pool Sensitivities Relevant to Winter-Ozone Modelling in the Uinta Basin

The current title has a spelling error, subject--verb disagreement, and an unsupported causal claim that WRF sensitivity hinders ozone simulations.

## Finish-critical scientific corrections

### 1. Keep “driving-product response,” not “initial-condition effect”

The GFS--NAM treatment bundles the initialised state, native analysis systems, assimilated observations, vertical input information, and lateral-boundary evolution.

It is called an initial-condition effect at lines 34, 53, 318, 417, and 443.

The design does not isolate that effect.

The inherited Conclusion correctly retains the broader limit at line 477.

### 2. Restore the exact integration and retained window

The integrations run from 12:00 to 18:00 UTC, or 05:00 to 11:00 MST.

The retained analysis window is 14:00 to 18:00 UTC, or 07:00 to 11:00 MST.

Both 12:00 and 13:00 UTC are excluded, leaving five hourly samples.

Lines 77--79 currently conflate those windows and say that only the initialised output was excluded.

Line 83 also says four stations lie outside d03; the audited statement is that seven lie outside its usable interior, leaving four usable columns.

### 3. Reconcile terrain-source facts before interpreting terrain

Lines 126, 397, and 404 give incompatible fine/default/coarse source resolutions.

Line 404 also calls static-geography source spacing WRF horizontal grid spacing.

The model grid and the source terrain dataset are different quantities and must stay separate.

The drainage, roughness-wave, stability, and cold-pool-volume mechanism asserted at lines 37 and 450 is not established by the current diagnostic.

The inherited CMP11 caption correctly says that the image shows a modelled response but establishes neither drainage direction nor cold-air-volume change.

### 4. Remove chemistry and inventory conclusions the experiment did not test

Lines 46, 52, and 418 imply that emissions inventories are satisfactory, chemistry models are otherwise trustworthy, meteorology is dominant, or a configuration sets chemistry up for failure.

The paper can instead say that credible meteorology is a prerequisite for chemical attribution amid compensating errors in confinement, emissions, photolysis, deposition, and mechanism.

Ahmadov is useful here precisely because changing emissions while holding meteorology fixed demonstrates that concentration agreement does not identify one unique error source.

### 5. Do not present X8 as a resolution or viability experiment

X8 has no matched control and differs in more than horizontal grid spacing.

The heading at lines 456--458 should become “Within-X8 d04 heat-deficit transport diagnostic” or similar.

It can demonstrate a calculable, temporally resolved process within that run.

It cannot establish accuracy, numerical stability, resolution superiority, basin export, or a 111 m effect.

### 6. Restore heat-deficit reproducibility details

The current rewrite loses several important details at lines 223--232.

- This is an area-normalised atmospheric proxy, not a measured basin-volume heat deficit.
- The primary footprint combines eleven stations and eleven registered waypoints.
- The exact seven definitions must be stated rather than summarised as waypoint changes.
- Feedback-matched GFS--NAM pairs use a common terrain mask.
- The weaker-state and faster-loss criteria were fixed before output inspection.

The current result is plain: every run gains heat deficit from 14:00 to 18:00 UTC while the two GFS curves remain below the two NAM curves.

That is a state offset, not demonstrated loss of cold-pool air parcels.

### 7. Correct the surface and common-AGL variable descriptions

The draft alternates between surface pressure and mean sea-level pressure at lines 80, 190, and 342.

That quantity needs confirmation before the error contrast is interpreted.

Line 195 should refer to model-level wind components interpolated through 50--500 m AGL, not “10-m wind components.”

Line 319 should say NAM is about 3.6 K more stable, not colder by 3.6 K.

Line 385 reports a 0.37 degree Celsius increase in temperature bias, not simply temperature.

### 8. Keep the question-led Introduction inside the evidence envelope

The present design cannot answer whether 333 m and 75 levels are generally stable for complex terrain, validate inversion depth, or decompose a cold pool into observed depth, strength, and surface manifestation.

Those are strong motivations and future experiments, not current research questions.

The ozone-threshold sentence at line 77 also needs regulatory verification and a distinction between the standard in effect in 2013 and a later 70 ppb standard.

The “near the median of case severity” statement at line 267 is not established by the reported series.

## Plain answers to the inline questions

- **What is the common-effects hierarchy?** On the same station/common-AGL metrics, the two driving-product contrasts are farthest from zero, the PBL/surface-layer response is smaller, and feedback and slope-radiation effects cluster near zero. It is a response hierarchy, not an overall configuration ranking.
- **What are the means at lines 320 and 324?** They are five-hour means of hourly spatial medians across the fixed station columns: stability at line 320 and transport-wind speed at line 324.
- **What is the surface contrast at lines 345 and 357?** Mountain Home minus Pariette Draw surface potential temperature.
- **Why is the close NAM value not validation?** It agrees with one horizontally separated two-site index, not a colocated vertical profile, inversion depth, or general model skill.
- **What did the spatial gate mean?** At 14:00--15:00 UTC, only 64--67 percent of footprint cells had the expected sign, below a predeclared two-thirds requirement. Later hours were more coherent. The area mean is robustly signed, but the response was not basin-wide and uniform at every hour.
- **What does “later coherence cannot rescue the gate” mean?** The rule required the threshold at every retained hour. Changing that rule after seeing the later maps would be post hoc. The maps can still be shown descriptively.
- **What does the 13:00 point do in the heat-deficit plot?** It orients the trajectory before the decision window. No criterion or reported effect uses it.
- **Do the Horsepool profiles show spin-up?** They show the initialised profile and one hour of combined model adjustment and boundary evolution. They do not isolate spin-up.
- **What does CMP11 show?** A controlled fine-minus-coarse static-terrain-source response whose spatial pattern depends on domain support and diagnostic. It does not identify drainage, an upstream reservoir, terrain superiority, or a change in basin cold-air volume.
- **Can the radiation image survive?** Yes, as a descriptive supplement showing an aspect-organised skin-temperature response that the station metric misses. It cannot show that slope-aware radiation improved the cold pool because the needed slope-aware forcing or flux variable was not archived.

## Figure disposition

The final paper needs figure roles, not a binary pass/fail wastebasket.

| Role | Meaning | Recommended material |
|---|---|---|
| Core evidence | Directly supports the principal controlled result | Locator, common-effects overview, common-AGL retention/transport, heat-deficit trajectory |
| Physical or stakeholder context | Makes the case and sampled atmosphere understandable without proving causation | AQS/MODIS context, observed temperature evolution, optional two-site surface contrast |
| Controlled diagnostic | Shows a reproducible response while retaining an explicit interpretation limit | CMP11 terrain composite |
| Within-run process context | Shows what was diagnosed in one run without a comparison, validation, or export claim | Compact X8 transport/budget packet |
| Archive/reviewer reserve | Reproducible but too weak, redundant, or easy to overread | X8 bulk Froude panel and redundant single-time maps |

### Main-text recommendation

Do not add all inherited v3 figures to the paper.

Retain the existing core spine.

The first figure to demote if the article must become shorter is the two-site surface contrast, because it is easy to mistake for vertical validation.

The best additional article-Appendix candidate is the controlled CMP11 terrain composite, with its present no-ranking, no-drainage, and no-volume limits retained.

If John explicitly chooses to alter the frozen main-text architecture, the X8 budget is the only X8 panel I would consider for the article body, because it exposes storage, horizontal convergence, and the unresolved term together.

Its claim would still need to remain within-run and descriptive, and it would need normal figure-admission review.

### Supplement recommendation

Use a short separate supplement containing:

1. one consolidated X8 figure containing the transport map and the storage/convergence/residual budget, with the strongest transect time series included only if legible; and
2. optionally the radiation diagnostic.

Keep the controlled CMP11 terrain composite in the article Appendix rather than duplicating it in the supplement.

Defer the X8 Froude panel unless its equations and physical interpretation are made fully reproducible.

The convergence map is optional once the budget figure is present.

## Lean d04 heat-deficit flux follow-up

The most valuable additional analysis does not require another WRF integration.

It is a closed-control-volume accounting exercise using the existing 10 min X8 output.

### Question

Over a fixed interior control volume, how much of the modelled heat-deficit storage tendency is accounted for by resolved horizontal heat-deficit transport, and is that accounting stable to reasonable diagnostic choices?

### Calculation

For one fixed closed polygon on the native d04 grid, calculate:

- stored deficit energy, `E(t) = integral_A H dA`;
- its finite-difference tendency, `dE/dt`;
- net resolved horizontal import, `Q_h = - line_integral_boundary F dot n dl`;
- the equivalent area integral of `-div(F)` as a numerical cross-check; and
- the unresolved residual `R = dE/dt - Q_h`.

The boundary integral is preferable to interpreting several open transects as basin export.

It gives a true closed-volume accounting while retaining the open transects as visual process context.

### Predeclared robustness checks

- Use unsmoothed fields for every number.
- Fix the control volume before inspecting new summaries.
- Repeat the diagnostic for 2100, 2200, and 2300 m crest references.
- Repeat with the registered active-deficit thresholds and two nearby edge crops.
- Verify that the boundary integral and area-integrated divergence agree to a declared numerical tolerance.
- Report cumulative 14:00--18:00 contributions, sign agreement, normalised residual, and timing, not only correlation.
- Report gross boundary throughput and the ratio of absolute net import to gross throughput so that strong exchange with near-zero net transport is distinguishable from weak transport.
- Treat the current `r=0.92` as descriptive association among autocorrelated intervals, not closure or validation.

### Optional scale-consistency check

Apply the same closed polygon and definitions to the X8 parent d03 field and to area-conservatively coarsened d04 fields.

This asks whether the diagnostic's sign and timing survive scale transfer.

It is not a controlled proof that 111 m is superior, because parent and child domains are dynamically coupled and not independent experiments.

### Deliverable

One compact figure should show the fixed control volume on the H/F map and the time series of storage, horizontal import, and residual.

Whether horizontal transport explains most, some, or little of storage is an interesting result.

That makes a null outcome publishable as process information rather than a failed resolution claim.

## Questions for John and coauthors

1. Is the intended centre of the paper a meteorological result with chemistry implications, or a general best-practices paper for preparing chemistry meteorology?
2. Is “initial conditions” a deliberate thesis choice, or can the manuscript consistently use the supported “driving-product response” language?
3. Is the terrain drainage/volume story an author hypothesis, or is there independent evidence that has not yet been registered?
4. Should the compact X8 budget be one main-text process figure, or should CMP11 plus X8 live in a separate supplement?
5. Is the pressure variable surface pressure or mean-sea-level pressure in the observation and model comparison?
6. What are the exact fine/default/coarse terrain sources, and how were terrain and snow fields generated for each run?
7. Does Michael agree with the physical meaning and sign convention of the heat-deficit transport diagnostic?
8. Are the global winter-ozone examples and ensemble recommendation important enough to source now, or should they wait for a later synthesis paper?

## Mechanical and citation cleanup queue

- Close the locator caption and the two open list environments, then remove inline dollar delimiters from the two display equations.
- Replace the undefined `Tran2018-xx` key with the verified Paperpile key if it is the intended source.
- Resolve every `Fig XX`, `Section XX`, `REF`, `CITE`, “OF WHAT?”, and parenthetical author note before coauthor circulation.
- Put every `\approx` inside math mode and repair incomplete table references.
- Apply the repository's British-English rule consistently to words such as “modelling,” “parameterisation,” “initialised,” and “modelled.”
- Remove internal claim IDs and Slurm job numbers from submission prose while retaining them in the reproducibility record.
- Do not guess missing bibliography entries or hand-edit `paperpile.bib`.

## Acronym, shorthand, and unit audit

The abstract must define its abbreviations independently of the body.

At present it expands Weather Research and Forecasting but does not attach `(WRF)`, and it uses GFS, NAM, CMAQ, and WRF-CHEM without expansion at lines 34--38.

The body then uses WRF and GFS/NAM before their full definitions at line 109.

The other priority first-use fixes are:

- Coordinated Universal Time (UTC) before the time-window description;
- US Environmental Protection Agency (EPA) Air Quality System (AQS);
- National Aeronautics and Space Administration (NASA), Global Imagery Browse Services (GIBS), and Moderate Resolution Imaging Spectroradiometer (MODIS);
- planetary boundary layer (PBL), above ground level (AGL), and mean sea-level pressure (MSLP), if MSLP is in fact the sampled variable;
- the MYJ, YSU, MM5, and RRTMG scheme names at first use; and
- root-mean-square (RMS) and root-mean-square error (RMSE) in the Appendix.

VOC, AI, ML, NAAQS, and MST are currently expanded where introduced, although the AI/ML sentence is better removed.

SI symbols such as MJ and GW do not need prose expansions.

The d01--d04 labels should be introduced once as nested computational domains, while internal C- and ANA-identifiers should leave the submission prose rather than receive acronym definitions.

`\approx` is defined by standard LaTeX as a mathematical relation.

The problem is that it appears outside maths mode at lines 110, 126, 229, 324, 342, 368, and 404; line 397 uses it correctly.

`\cdotp` is likewise defined but is used outside maths mode at line 125.

No bespoke shorthand appears undefined.

The custom `\rewritegate`, `\diagnosticnote`, and `\exploratorymark` commands are declared in the preamble, and the remaining journal commands come from the MDPI class or its loaded packages.

A scratch compile with only the structural and maths-mode faults repaired reached completion without an undefined-control-sequence error.

The nominal terrain-source conversions are also wrong.

- 3 arcsec is approximately 90 m north--south, not 30 m.
- 30 arcsec is approximately 900 m, not 90 m.
- 5 arcmin is approximately 9 km, not 900 m.

At approximately 40 degrees north the cells are anisotropic, so the rough east--west by north--south dimensions are 71 by 93 m, 0.71 by 0.93 km, and 7.1 by 9.3 km, respectively.

The audited lineage names the terrain sources as 3 arcsec, 30-arcsec-class, and 5 arcmin, but the exact as-run products still require provenance confirmation before publication.

These source spacings are distinct from the 3 km, 1 km, 333 m, and 111 m WRF computational grids.

## Ten likely-to-accept edits

These are deliberately small enough to approve and apply by batch.

### Batch 1 — build and reader definitions

1. **Close the two lists at lines 63--68 and 415--421.** Insert `\end{enumerate}` after the fourth research question and `\end{itemize}` after the third principal-result bullet. Confidence: certain.
2. **Close the locator caption at lines 100--103.** Add the missing closing brace before `\label{fig:v3-locator}`. Confidence: certain.
3. **Repair maths structure at lines 202--206 and 248--252, then replace text-mode `\approx` and `\cdotp`.** Remove inline dollar delimiters from the two equation environments, move the masking sentence out of the second equation, and use British prose such as “approximately” where no displayed relation is needed. Confidence: certain.
4. **Define the reader-facing acronyms at first use.** Define WRF, GFS, and NAM in the standalone abstract and again at first body use; expand the EPA/AQS, NASA/GIBS/MODIS, PBL/AGL, scheme, RMS, and RMSE terms listed above. Remove or expand CMAQ and WRF-Chem. Confidence: high.

### Batch 2 — audited factual restoration

5. **Restore the exact windows and station-domain facts at lines 77--83.** State that the integrations cover 12:00--18:00 UTC (05:00--11:00 MST), the retained five-hour sample covers 14:00--18:00 UTC (07:00--11:00 MST), and seven stations fall outside the usable d03 interior, leaving four usable columns. Confidence: high.
6. **Correct terrain-source terminology and conversions at lines 119--126 and 397--405.** Keep static-source spacing separate from WRF grid spacing; use the nominal 3 arcsec/90 m, 30 arcsec/900 m, and 5 arcmin/9 km lineage only after confirming the as-run sources. Confidence: certain on the conversion and distinction; high on the source labels pending provenance confirmation.
7. **Restore the surface/common-AGL method at lines 190--195.** Verify surface pressure versus MSLP, then describe model-level horizontal winds, destaggering and rotation, and interpolation from 50 to 500 m above ground level. Do not say that 10 m winds were vertically interpolated. Confidence: high pending the pressure-variable check.
8. **Restore the heat-deficit footprint at lines 223--232.** Reinstate the eleven stations plus eleven waypoints, exact 4,965-cell/5,277 km2 primary footprint, six alternate definitions, common pair masks, and predeclared weaker-state/faster-loss criteria. Use “footprint-mean, vertically integrated heat deficit” for values in MJ m-2. Confidence: high.

### Batch 3 — bounded framing

9. **Replace the title at line 17.** A high-confidence working title is “WRF Cold-Pool Sensitivities Relevant to Winter-Ozone Modelling in the Uinta Basin”. It preserves the broader purpose without claiming a simulated ozone failure. Confidence: high, but explicitly an author choice.
10. **Clarify the principal result at lines 318--325 and make the terminology consistent at lines 34, 36--37, 417, and 443.** Call it a driving-product response rather than an isolated initial-condition effect; say NAM was approximately 3.6 K more stable rather than colder; identify the values as five-hour means of hourly spatial medians; and retain the exact transport-wind magnitudes. Confidence: high.

Batch 1 is mechanical and can be accepted without endorsing any scientific reframing.

Batch 2 restores audited facts while retaining John's prose around them.

Batch 3 is the only batch that makes an overt framing choice.

## Repository simplification

Simplify manuscript lineage and routing, not the evidence base.

### During the author pass

- Keep `main.tex` as the only eventual submission target.
- Treat `jrl_manuscript.tex` as the author-intent donor until its changes are integrated.
- Freeze `_manuscript_v3.tex` as a read-only donor rather than editing both files.
- Keep candidate figures under `verification/` until a deliberate dual-manifest promotion.
- Keep provenance, scripts, and exact derived tables even when they do not enter the paper.

The immediate risk is that the author's current draft is ignored and therefore unversioned.

Before further editing, protect it on a `jrl/<topic>` branch by integrating selected changes into `main.tex` or by making one explicit dated source snapshot outside the submission allowlist.

My preference is to integrate into `main.tex` section by section rather than create another permanent manuscript lineage.

### After the final author draft is merged

- Remove `_manuscript_test.tex` and the temporary rewrite workbench from the active root, relying on Git history for archaeology.
- Remove `_manuscript_v3.tex` after every accepted donor passage and figure disposition has been recorded.
- Retain one short final-readiness note, one ordered closure register, and the evidence/provenance directories.
- Keep only promoted production figures in `figures/`; keep non-promoted reproducible diagnostics in `verification/`.
- Remove ignored routine build products and superseded local manuscript copies only after the author's work is safely versioned.

## Fastest next pass

1. Safeguard the ignored author draft and repair TeX structure.
2. Restore the exact audited time window, treatment names, terrain facts, pressure variable, and heat-deficit definition.
3. Rewrite the title, abstract, questions, and Discussion around the recommended thesis while preserving John's direct voice.
4. Resolve the inline questions using the plain answers above.
5. Choose one X8 disposition and one compact supplement structure.
6. Replace citation placeholders only from the complete Paperpile export and verified passages.
7. Run the final-draft and submission checks and inspect both PDFs.

No new WRF integration is required to finish the author draft.

The closed-volume d04 analysis is a high-value optional addition, not a blocker.
