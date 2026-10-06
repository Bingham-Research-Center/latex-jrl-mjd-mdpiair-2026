# First proof query catalogue — 5 October 2026

Catalogue complete: **22 MDPI comments and one English-editor note**, with compound requests split below.
The initial catalogue proposed responses with all follow-ups open; the 6 October recovery checkpoint below records the author decisions now present in the working source.
The production notice is retained as an acknowledgement item.

This catalogue follows [AGENTS.md](../AGENTS.md) and [PROOFING-HANDOFF.md](../PROOFING-HANDOFF.md) in the active `jrl/proofs-round1` worktree, inspected at `277cfa629f92e3e495cdb33fc9c371cea4c5e621`.
The received baseline is commit `92b14d2`; all 33 received files are preserved.
The source and PDF hashes match [intake.json](../proof-package/intake.json):

- Source SHA-256: `45d002c574a824223f5b07f38bf9ebaee2f92199a2406eaf23e867c90c20104e`.
- PDF SHA-256: `5743cb0541bf6484e96b6085623a1883028cc286b53800ac02c2d915ed2f343a` (18 pages, independently checked with `pdfinfo`).

Source line numbers refer to the unchanged [received TeX](../proof-package/air-4472509-english/air-4472509-done.tex).
Pages refer to the [supplied PDF](../proof-package/air-4472509-english/air-4472509-done.pdf), identified by text extraction and the supplied auxiliary file; they are locators, not a visual sign-off.
Exact publisher comment text is retained in code blocks, including original spelling and spacing except trailing whitespace.
The initial 5 October catalogue claimed no manuscript correction, compilation, full visual proof audit, bibliographic verification or author confirmation; the recovery checkpoint below records subsequent saved author decisions and validation.

## Author editing recovery — 6 October 2026

Recovery commit: `19d2452f921531a8acc46beb451b40e11b863df5` (saved edits, editing paths, decisions and validation).

John saved edits into `proof-package/air-4472509-english/air-4472509-done.tex` while intending to edit the working proof.
Those edits are now in [the working manuscript](../proof-package/working/air-4472509-done.tex); the received file is restored to its intake hash.
An exact saved-source backup and patch were verified before restoration; [the recovery receipt](../proof-package/edit-recovery-20261006.json) records paths and hashes.
Only one newly added trailing space was removed during transfer; all substantive author edits and publisher queries were retained.
The editing/build instructions are now explicit in both proof-folder READMEs and the restart handoff.
The working proof builds to 18 pages under `texlive/20260330`; affected pages 1–5 were inspected with no observed clipping or overlap introduced by the edits.
Known duplicate Table A5 labels, template warnings and unresolved draft text remain; this is not a full proof audit.
Checks and hashes are recorded in the recovery receipt.

## Author citation preference — 6 October 2026

John explicitly requests formal in-text citations for WRF/WPS, software and data sources, with verified paper/software DOIs where available, rather than website-only references, acknowledgements-only mentions or passing references.
Do not use manuscript footnotes; retain a bibliography URL and access date when no suitable DOI exists, without substituting a DOI for a different resource.
Recommendation, not yet an accepted TeX edit: put software use, citations and verified versions in Methods; keep personal and institutional thanks in Acknowledgements.
The working source already cites DOI-bearing entries for WRF, NumPy, SciPy, pandas, xarray and Matplotlib; the Python-package citations currently occur in Acknowledgements.
A targeted source check found no `\footnote{` or `\footnotetext{` calls; `\footnotesize` is table typography and is not a footnote.
Implement this policy incrementally through MDPI04b, MDPI18 and MDPI22, preserving publisher query quotations and the received bundle.
No new manuscript wording or software version was accepted or implemented in this advice session.

## Walkthrough: where to edit and how to batch the work

Active worktree: `/uufs/chpc.utah.edu/common/home/u0737349/worktrees/air-proofs-round1`, branch `jrl/proofs-round1`.
**Edit [the working manuscript](../proof-package/working/air-4472509-done.tex).**
The complete copy is ready; its [creation receipt](../proof-package/working-copy.json) records a byte-for-byte match for all 33 received files before corrections.
Keep the [received source](../proof-package/air-4472509-english/air-4472509-done.tex) and supplied PDF unchanged.
Root `main.tex` is the later integration target.
The README inherited inside both proof folders names the wrong source; compile `air-4472509-done.tex`.

This document combines the walkthrough and previous query catalogue; keep individual decisions in the detailed entries below rather than a competing checklist.
The batches are a suggested resolution order, not approval to invent missing facts or accept publisher changes.
Each individual subquery retains its own status even when related work shares a commit.

| Batch | Individual queries / issues | Work and completion evidence | Current state |
| --- | --- | --- | --- |
| 1 — Author facts and choices | EE01; MDPI01a/b, MDPI02, MDPI03; AI-use highlights | Confirm title, names, affiliations, ORCIDs, emails, emphasis and applicable AI identifiers from John/saved decisions. Record each exact decision. | Open |
| 2 — Citation order and cross-references | MDPI05a/b, MDPI08c, MDPI09; duplicate Table A5 label | Repair first-citation order and placement, verify appendix-table references, retain one canonical continued-table label; build and inspect cross-references/pages. | Open |
| 3 — Figures and captions | MDPI06, MDPI08a/b, MDPI11–16 and their subqueries | Inspect queried overlap; verify markers, panels, shading and dashed lines against registered evidence; apply precise captions and inspect resulting pages. | Open |
| 4 — Mathematical/table formatting | MDPI10, MDPI17 | Audit notation and Table A4 borders/row associations against source and PDF, then record inspection and decisions. | Open |
| 5 — Software/equipment provenance | MDPI04a/b, MDPI18; applicable software highlights | Recover actual run/analysis versions and provider instrument facts with exact provenance; record unavailable information explicitly. | Open |
| 6 — Bibliographic additions/removal | MDPI19, MDPI20a/b, MDPI21, MDPI22; McKinney highlight | Verify publication/conference metadata and removed Herbie DOI; correct embedded references as warranted, preserving Paperpile-owned files. | Open |
| 7 — Production notice and final proof audit | MDPI07; all preceding queries | Record acknowledgement; compile the working source, inspect all pages against the supplied PDF, and reconcile replies/remaining author decisions. | Open |

For each issue, extend its detailed entry with: applied change or confirmed no-change decision; exact evidence; checks/PDF pages; proposed or final reply; remaining author decision; and correction commit hash.
Commit one verified issue or small related batch promptly, with query IDs and validation in the commit body.
Use John's identity and `Co-Authored-By: Codex <noreply@openai.com>` on every commit.
A subsequent status commit can record the preceding correction hash.

Build from the working directory after actual proof corrections:

```sh
cd /uufs/chpc.utah.edu/common/home/u0737349/worktrees/air-proofs-round1/proof-package/working
latexmk -pdf -interaction=nonstopmode -halt-on-error air-4472509-done.tex
```

The working PDF and copied compilation outputs are ignored; the received PDF remains the immutable comparison.
Setup checks verify copy integrity, query quotations and paths; they do not resolve any proof query or establish a successful new compilation.

## Query index

| ID | TeX line | Supplied PDF page | Topic |
| --- | ---: | --- | --- |
| [EE01](#ee01) | 19 | 1 | Title change |
| [MDPI01](#mdpi01) | 23 | 1 | Names, affiliations and ORCIDs |
| [MDPI02](#mdpi02) | 28 | 1 | Added email addresses |
| [MDPI03](#mdpi03) | 69 | 2 | Research-question italics |
| [MDPI04](#mdpi04) | 93 | 3 | Methods: equipment details and software versions |
| [MDPI05](#mdpi05) | 110 | 3 | Figure/table citation order and placement |
| [MDPI06](#mdpi06) | 131 | 3 | Figure 1: overlapping content |
| [MDPI07](#mdpi07) | 154 | 4 | Production position/size notice |
| [MDPI08](#mdpi08) | 181 | 4 | Figure 2: overlap, markers and placement |
| [MDPI09](#mdpi09) | 204 | 5; repeated on 8 | Appendix table citation format |
| [MDPI10](#mdpi10) | 213 | 5–6; throughout | Mathematical typography |
| [MDPI11](#mdpi11) | 275 | 7 | Figure 3: overlapping content |
| [MDPI12](#mdpi12) | 293 | 8 | Figure 4: separate panel descriptions |
| [MDPI13](#mdpi13) | 318 | 9 | Figure 5: panels and shading |
| [MDPI14](#mdpi14) | 337 | 9 | Figure 6: shading |
| [MDPI15](#mdpi15) | 356 | 10 | Figure 7: panels and shading |
| [MDPI16](#mdpi16) | 392 | 11 | Figure 8: overlap and dashed lines |
| [MDPI17](#mdpi17) | 543 | 14 | Table A4: added border lines |
| [MDPI18](#mdpi18) | 655 | 15; possible continuation on 16 | Software versions in acknowledgements |
| [MDPI19](#mdpi19) | 735 | 16 | Reference 12: EGU conference dates |
| [MDPI20](#mdpi20) | 765 | 16–17 | References 17 and 31: publisher locations |
| [MDPI21](#mdpi21) | 835 | 17 | Reference 29: conference location and dates |
| [MDPI22](#mdpi22) | 894 | 17 | Reference 39: removed Herbie DOI |

## Detailed register

“Outstanding” names the evidence or decision needed before sending a final reply.
Reading an existing caption provides a candidate explanation, not independent verification of the plotted feature.

<a id="ee01"></a>

### EE01 — Title change

Source line 19; supplied PDF page 1.

```text
%EE: Attention: title altered
```

The proof title is “WRF Cold-Pool Sensitivities Relevant to Winter Ozone Modelling in the Uinta Basin”. Root main.tex line 17 has “Winter-Ozone”; the visible title change removes that hyphen.

**EE01: Author accepted — 6 October saved edit.**

Author decision/reply: Accept the title with “Winter Ozone”; the working source records `% JRL: accepted.` immediately after the original English-editor note.

Outstanding: Final proof audit; this acceptance is recorded from John’s saved source comment.

<a id="mdpi01"></a>

### MDPI01 — Names, affiliations and ORCIDs

Source line 23; supplied PDF page 1.

```text
%MDPI: 1. Please carefully check the accuracy of names and affiliations. 2. Please confirm if need keep the orcid of authors.
```

The proof lists John R. Lawson (1,2; corresponding author), Michael J. Davies (1), Loknath Dhar (1,3), and Seth N. Lyman (1,3). Affiliations are Bingham Research Center, Utah State University, Vernal, UT 84078, USA (1); Department of Mathematics and Statistics, Utah State University, Logan, UT 84322, USA (2); and Department of Chemistry and Biochemistry, Utah State University, Logan, UT 84322, USA (3).

**MDPI01a: Open — author facts.**

Proposed response/action: Confirm the displayed author names, order, superscripts, affiliations and correspondence details, or supply exact corrections.

Outstanding: John/saved author decisions must confirm these personal details. Correspondence is john.lawson@usu.edu at source line 32.

**MDPI01b: Open — author facts.**

Proposed response/action: Retain each displayed ORCID only after the author confirms that it belongs to them and should appear.

Outstanding: John: 0000-0003-0305-4090; Michael: 0009-0009-9083-6568 (received source lines 21–24). John’s saved edit adds `orcidauthorC` (0009-0002-4536-5778) and `orcidauthorD` (0000-0001-8493-9522), but does not attach `orcidC`/`orcidD` to the author line. Display and author mapping remain to be completed/confirmed; the migration preserves the macros as supplied.

<a id="mdpi02"></a>

### MDPI02 — Added email addresses

Source line 28; supplied PDF page 1.

```text
%MDPI: We added these email addresses here according to those submitted online at susy.mdpi.com. Please confirm.
```

The three added addresses are michael.davies@usu.edu (M.J.D.), a02391298@usu.edu (L.D.), and seth.lyman@usu.edu (S.N.L.).

**MDPI02: Author confirmed — 6 October saved edit.**

Author decision/reply: The working source records `% JRL: This is correct.` directly after the publisher’s email query; the three displayed addresses are retained.

Outstanding: Final proof audit; confirmation is John’s saved source comment, not independent verification against SuSy.

<a id="mdpi03"></a>

### MDPI03 — Research-question italics

Source line 69; supplied PDF page 2.

```text
%MDPI: Please confirm if the italics are necessary; if not, please remove them.
```

The italicised question ends at source line 70.

**MDPI03: Author confirmed retention — 6 October saved edit.**

Author decision/reply: Retain the italics; the working source records `% JRL: Please keep: preference for emphasis.` under the preserved publisher query.

Outstanding: Final proof audit.

<a id="mdpi04"></a>

### MDPI04 — Methods: equipment details and software versions

Source line 93; supplied PDF page 3.

```text
%MDPI: For this section, please double check that the following details are provided for all cases: 1. Company names and addresses (city, country) of the instruments and equipment used. For USA or Canadian companies, please provide the state name as well (e.g., city name, abbreviated state name, USA/Canada). 2. For software: Please state the version number of the software.
```

The Methods section uses provider observations and numerical modelling. WRF 4.8.0 is already stated at lines 143 and 156; WRF Preprocessing System is named at line 190 without a version.

**MDPI04a: Open — evidence check.**

Proposed response/action: Identify the equipment to which this request applies and add only documented manufacturer names and locations; explain any unavailable provider instrument metadata.

Author position in the saved edit: Instrument information cannot be supplied from the multi-network Synoptic Data aggregation alone.

Outstanding: Final response wording and any applicable documented provider instrument facts; do not infer manufacturers from the aggregator’s name.

**MDPI04b: Open — provenance check.**

Proposed response/action: Supply versions used for the reported simulations, preprocessing, retrieval and analysis from the corresponding archived environments.

Saved draft: The working source now says WPS 4.8.0 and retains `[WRF/WPS ref]` and `[what?]` terrain placeholders. The nearby author comment describes intended additions, not verified completion.

Outstanding: Verify WRF and WPS provenance and complete the WPS citation and fine/default/coarse terrain-source descriptions. Coordinate with MDPI18; today’s installed versions and cited software-paper versions are not evidence of the versions used.

6 October citation advice: retain `Skamarock2019` for WRF, as recommended by [NCAR's citation guidance](https://www2.mmm.ucar.edu/wrf/users/citing_wrf.html), DOI [10.5065/1dfh-6p97](https://doi.org/10.5065/1dfh-6p97).
For the WPS description, recommend Powers et al. (2017), *The Weather Research and Forecasting Model: Overview, System Efforts, and Future Directions*, *Bulletin of the American Meteorological Society*, 98, 1717–1737, DOI [10.1175/BAMS-D-15-00308.1](https://doi.org/10.1175/BAMS-D-15-00308.1); the [publisher record](https://journals.ametsoc.org/view/journals/bams/98/8/bams-d-15-00308.1.xml) explicitly describes WPS.
Proposed wording, pending author agreement and actual preprocessing-version evidence: “The terrain datasets were ingested using the WRF Preprocessing System (WPS), version [verified version] [Powers et al., 2017].”
A targeted search of the paper's `verification/provenance/` found no recorded WPS version; `run-inventory.csv` records WRF 4.8.0, which does not verify WPS 4.8.0.
The saved WPS version remains unverified; next obtain an archived preprocessing log, build/source record or equivalent record linked to these runs.
Terrain-source provenance remains independently open. Citation verification does not close it.
Validation: live branch `jrl/proofs-round1` and clean starting tree checked; working source and relevant embedded entries inspected; NCAR citation guidance and Powers publisher search record checked. Documentation only: no TeX change, new build or PDF inspection.

<a id="mdpi05"></a>

### MDPI05 — Figure/table citation order and placement

Source line 110; supplied PDF page 3.

```text
%MDPI: Figures/Tables citation should be numbered in order of appearance. We detected Figure 3 citation appear after Figure 1,  Figure 6 after Figure 3, order wrong. Please rearrange and ensure all citations appear in numerical order, and please put figures after its first citation.
```

First figure citations are 1, 3, 6, 2, 4, 5, 7, 8, 9 (reference lines 109, 111, 112, 116, 286, 304, 351, 387, 411). First table citations are 1, A6, A1, A2, A3, A4, A5 (lines 151, 205, 305, 307, 311, 329, 350). These sequences were checked against the supplied .aux and source, with figure/table numbers also checked in extracted PDF text.

**MDPI05a: Open — technical correction.**

Proposed response/action: Reconcile first citations with numerical order throughout. A candidate figure fix is to move the premature Figure 3 and Figure 6 callouts to the relevant Results passages while preserving the Methods descriptions; check the appendix table sequence too.

Outstanding: Review the resulting reading order and all cross-references in a working copy. No renumbering or relocation has yet been applied.

**MDPI05b: Open — layout check.**

Proposed response/action: Place figures after their first citations and check the rebuilt layout and table placement throughout.

Outstanding: A compiled working copy and page inspection after resolving citation order. MDPI08c repeats this request for Figure 2 and other figures.

<a id="mdpi06"></a>

### MDPI06 — Figure 1: overlapping content

Source line 131; supplied PDF page 3.

```text
%MDPI: Please confirm whether the overlapping content in this figure affects scientific understanding and if it does, please revise it.
```

Geographic/sampling locator; label fig:v3-locator. Assets: wrf_geographic_locator_d01_d03.pdf and wrf_nested_domains_d01_d03.png.

**MDPI06: Open — visual check.**

Proposed response/action: Inspect both panels at final print size; identify and repair any overlap that obscures labels or scientific content, or describe the specific harmless overlap if no correction is needed.

Outstanding: Visual assessment of the supplied figure and any derivative. Registered figure provenance and both admission manifests govern any replacement.

<a id="mdpi07"></a>

### MDPI07 — Production position/size notice

Source line 154; supplied PDF page 4.

```text
%MDPI: Please note that changes to the position/size of figures or tables may occur during the production stage, in order to ensure the correct order or readability.
```

Attached to Table 1 (tab:v3-family), but the notice applies to figures and tables generally.

**MDPI07: Open — notice/acknowledgement.**

Proposed response/action: Proposed reply: “Noted; please retain legibility and the order of first citation.”

Outstanding: Acknowledgement can accompany the final proof reply. This is a production notice, not evidence that any particular relocation or resize has been accepted.

<a id="mdpi08"></a>

### MDPI08 — Figure 2: overlap, markers and placement

Source line 181; supplied PDF page 4.

```text
%MDPI: 1. Please confirm whether the overlapping content in this figure affects scientific understanding and if it does, please revise it.  2. Please confirm whether an explanation of the triangles and squares needs to be added to the figure caption. 3. Figure 2 is not after first citation due to the citation order wrong, please revise citation order and put it after first citation. Same as other figrues, please check all.
```

Episode context; label fig:v3-episode-context; asset episode_context_snow_ozone_janfeb2013.pdf. The current caption identifies hollow markers as the seven site-days with less than 75% within-day coverage, but does not identify triangle/square meanings.

**MDPI08a: Open — visual check.**

Proposed response/action: Inspect the satellite and ozone panels and repair any overlap that obscures information.

Outstanding: Final-size visual review and, if needed, a derivative based on the registered original inputs.

**MDPI08b: Open — evidence/caption check.**

Proposed response/action: Add explicit meanings for triangles and squares, distinguishing marker shape from hollow-marker coverage coding.

Outstanding: Read the actual panel legends and registered plotting provenance before assigning meanings. Do not guess that all marker shapes represent coverage.

**MDPI08c: Open — technical/layout check.**

Proposed response/action: Resolve Figure 2’s citation/placement as part of MDPI05, then check all figures.

Outstanding: The source-level Figure 2 callout at line 116 precedes its figure block at lines 178–188; the independently confirmed defect is non-numerical first-citation order. Final layout still needs inspection.

<a id="mdpi09"></a>

### MDPI09 — Appendix table citation format

Source line 204; supplied PDF page 5; repeated on 8.

```text
%MDPI: We revised the appendix table citation format, please confirm. same as below.
```

The edited pattern is “Appendix A Table A6” at lines 204–205, with highlighted repetitions for Table A2 at line 307 and Table A3 at line 311.

**MDPI09: Open — reference/editorial check.**

Proposed response/action: Accept a consistent journal appendix/table citation format once every reference resolves to the intended table.

Outstanding: Verify all occurrences after any reordering under MDPI05; confirm the final wording with John. Preserve the referenced content.

<a id="mdpi10"></a>

### MDPI10 — Mathematical typography

Source line 213; supplied PDF page 5–6; throughout.

```text
%MDPI: Reminder: Variables/values; greek letters: please keep them in consistent (italic or normal, bold or not, subscript, superscript) in whole text (including in equations) if necessary. Same for the next occurrences. Please check all equations below.
```

The note begins at the definition of S_{50:500}; its scope includes all equations, inline expressions, captions and tables.

**MDPI10: Open — notation audit.**

Proposed response/action: Check consistent variable/Greek-letter styling, vector/scalar distinctions, units, subscripts, superscripts and averaging bars throughout.

Outstanding: Compare each notation choice against the defined quantity and registered evidence. In particular preserve endpoint difference, vector magnitude, scalar speed and height averaging as distinct quantities; inspect typeset equations after edits.

<a id="mdpi11"></a>

### MDPI11 — Figure 3: overlapping content

Source line 275; supplied PDF page 7.

```text
%MDPI: Please confirm whether the overlapping content in this figure affects scientific understanding and if it does, please revise it.
```

Observed temperature series; label fig:v3-observed; asset obs_temp_timeseries_feb0102.pdf. Its caption already states that shading indicates approximate local night.

**MDPI11: Open — visual check.**

Proposed response/action: Inspect station labels, legend, annotations and axes at print size; revise any overlap that hides information.

Outstanding: Visual confirmation and registered provenance for any figure derivative. This comment does not request a new interpretation of the night shading.

<a id="mdpi12"></a>

### MDPI12 — Figure 4: separate panel descriptions

Source line 293; supplied PDF page 8.

```text
%MDPI: Please note that each subfigure should be described separately in the caption., e.g., (a) xxx; (b) xxx.
```

Controlled-comparison effects; label fig:v3-effects; asset fig_common_pipeline_effects.pdf.

**MDPI12: Open — evidence/caption check.**

Proposed response/action: Describe each panel separately using the lettering actually present in the figure, including its diagnostic and units.

Outstanding: Inspect panel labels/order and the registered plotting definition. Preserve the existing description of whiskers as descriptive block-sensitivity intervals for five dependent hourly medians.

<a id="mdpi13"></a>

### MDPI13 — Figure 5: panels and shading

Source line 318; supplied PDF page 9.

```text
%MDPI: 1. Please note that each subfigure should be described separately in the caption., e.g., (a) xxx; (b) xxx.  2. Please confirm whether an explanation of the shadow area needs to be added to the figure caption.
```

Station-column diagnostics; label fig:v3-retention; asset wrf_retention_ventilation_d02_14to18.pdf. The caption already mentions medians and interquartile ranges, and distinguishes solid/two-way from dashed/one-way lines.

**MDPI13a: Open — evidence/caption check.**

Proposed response/action: Describe the potential-temperature endpoint-difference and layer-mean wind-vector-magnitude panels separately using their actual lettering.

Outstanding: Verify panel lettering and ordering from the figure.

**MDPI13b: Open — evidence/caption check.**

Proposed response/action: Explicitly connect the plotted central curves and shaded bands to their statistics; the current caption suggests medians and interquartile ranges.

Outstanding: Confirm the shading statistic and station population against the registered figure/generator before writing the final explanation; do not relabel these as confidence intervals.

<a id="mdpi14"></a>

### MDPI14 — Figure 6: shading

Source line 337; supplied PDF page 9.

```text
%MDPI: Please confirm whether an explanation of the shadow area needs to be added to the figure caption.
```

Mountain Home-minus-Pariette Draw surface potential-temperature index; label fig:v3-bulk-theta; asset wrf_inversion_index_feb0102_gfs2way_vs_nam2way_d02_14to18.pdf. The existing caption does not define shading.

**MDPI14: Open — evidence/caption check.**

Proposed response/action: Add the shading’s exact meaning once established from the figure and plotting provenance.

Outstanding: The source caption alone does not identify the shaded area. Do not infer uncertainty, night or an interquartile range from other figures. Preserve the horizontally separated surface-index interpretation.

<a id="mdpi15"></a>

### MDPI15 — Figure 7: panels and shading

Source line 356; supplied PDF page 10.

```text
%MDPI: 1. Please note that each subfigure should be described separately in the caption., e.g., (a) xxx; (b) xxx.  2. Please confirm whether an explanation of the shadow area needs to be added to the figure caption.
```

Heat deficit; label fig:v3-heatdeficit-traj; asset wrf_heat_deficit_d02_13to18.pdf. The caption names four-run trajectories and seven-definition sensitivity envelopes without explicit panel-by-panel mapping.

**MDPI15a: Open — evidence/caption check.**

Proposed response/action: Describe each panel separately, distinguishing the four trajectories from the two paired GFS-minus-NAM contrasts.

Outstanding: Confirm actual panel lettering/order and primary-definition curves from the registered figure.

**MDPI15b: Open — evidence/caption check.**

Proposed response/action: State explicitly which shading depicts the seven-definition sensitivity envelope and identify any other shaded region independently.

Outstanding: Check the generator’s envelope statistic and each shaded feature. Keep 1300 UTC as orientation only and 1400–1800 UTC as the retained window; do not describe these envelopes as sampling confidence intervals.

<a id="mdpi16"></a>

### MDPI16 — Figure 8: overlap and dashed lines

Source line 392; supplied PDF page 11.

```text
%MDPI: 1. Please confirm whether the overlapping content in this figure affects scientific understanding and if it does, please revise it.  2.  Please confirm whether an explanation of the dashed line needs to be added to the figure caption.
```

Terrain comparison; label fig:v3-terrain-cmp11; asset wrf_terrain_cmp11_d02_d03_16z.pdf. The caption describes panels (a)–(d) and a 2200 m crest reference, but does not explicitly map dashed lines to features.

**MDPI16a: Open — visual check.**

Proposed response/action: Inspect maps, section panels, labels and colour bars, and repair overlap that obscures content.

Outstanding: Final-size visual assessment and registered inputs for any derivative.

**MDPI16b: Open — evidence/caption check.**

Proposed response/action: Explain the dashed line or lines explicitly in the caption, using panel-specific definitions where necessary.

Outstanding: Identify every dashed feature from the figure/generator; do not assume that a map transect and a section crest reference share one meaning. A crest reference must not become an observed inversion top.

<a id="mdpi17"></a>

### MDPI17 — Table A4: added border lines

Source line 543; supplied PDF page 14.

```text
%MDPI: we added border lines in table, please confirm.
```

Surface, spatial and vertical corroboration; label tab:v3-surface-summary. Source lines 551 onward contain additional horizontal rules.

**MDPI17: Open — visual/editorial check.**

Proposed response/action: Accept the added rules if the PDF shows clear row grouping and all entries remain correctly associated.

Outstanding: Inspect the typeset table and compare entries with the source. The first four rows remain station-based and the last four footprint-based.

<a id="mdpi18"></a>

### MDPI18 — Software versions in acknowledgements

Source line 655; supplied PDF page 15; possible continuation on 16.

```text
%MDPI: Please state which version of the software was used. Same as below.
```

Explicit highlights cover NumPy, SciPy, pandas, xarray and Matplotlib (lines 655–656). Polars is named without a highlight; Herbie and SynopticPy appear immediately above (line 654). Claude and OpenAI Codex are highlighted in the AI declaration at line 660 without a separate comment.

**MDPI18: Open — provenance/author facts.**

Proposed response/action: Add the verified versions used for the named analysis/plotting software; coordinate the broader software inventory with MDPI04b. Review the AI highlights separately before interpreting “Same as below”.

Author citation preference, 6 October: cite software in Methods with DOI-bearing bibliography entries where available. Moving the existing acknowledgement citations and adding verified versions remain proposed edits; this query remains open.

Outstanding: Archived analysis and plotting environments may differ by stage/figure. Record package, actual version, task/date and exact provenance source. If unavailable, record the gap for John rather than insert a current version. AI product/model identifiers require author/session evidence where applicable; the source note does not explicitly define the scope of those highlights.

<a id="mdpi19"></a>

### MDPI19 — Reference 12: EGU conference dates

Source line 735; supplied PDF page 16.

```text
%MDPI: we added the date of conference, please confirm.
```

Stajner2022-uw; the inserted dates are “23–27 May 2022” for the EGU General Assembly 2022, Vienna.

**MDPI19: Open — bibliographic verification.**

Proposed response/action: Confirm the added dates only after checking the cited abstract and official conference record; supply corrected dates if they differ.

Outstanding: Authoritative abstract/conference metadata. No external date verification has been performed for this catalogue.

<a id="mdpi20"></a>

### MDPI20 — References 17 and 31: publisher locations

Source line 765; supplied PDF page 16–17.

```text
%MDPI: we added location of the publisher, please confirm. same as below.
```

Skamarock2019 (reference 17) gains “Boulder, CO, USA” at line 765. The “same as below” scope includes the highlighted “Reston, VA, USA” for DanielsonGesch2011 (reference 31), line 847.

**MDPI20a: Open — bibliographic verification.**

Proposed response/action: Confirm the NCAR technical report’s publisher location against its publication record.

Outstanding: The cited NCAR/TN-556+STR record or title/publication page, rather than a present-day address.

**MDPI20b: Open — bibliographic verification.**

Proposed response/action: Confirm the USGS Open-File Report 2011–1073 publisher location against its publication record.

Outstanding: The report’s publication record/title page. This follow-up is linked to the original comment and is not counted as an additional MDPI comment.

<a id="mdpi21"></a>

### MDPI21 — Reference 29: conference location and dates

Source line 835; supplied PDF page 17.

```text
%MDPI: we added the location and date of conference, please confirm.
```

Tewari2004; the added text is “Seattle, WA, USA, 11–15 January 2004” for the 20th Conference on Weather Analysis and Forecasting/16th Conference on Numerical Weather Prediction.

**MDPI21: Open — bibliographic verification.**

Proposed response/action: Verify the exact cited meeting, location and dates together, then confirm or supply the correction.

Outstanding: Official conference programme or the cited proceedings/paper. Do not treat a plausible city/date as verified evidence.

<a id="mdpi22"></a>

### MDPI22 — Reference 39: removed Herbie DOI

Source line 894; supplied PDF page 17.

```text
%MDPI: we removed the unnecessary doi link, and only keep the website, please confirm.
```

Herbie retains its GitHub URL and access date at line 895. The proof does not show the deleted DOI.

**MDPI22: Open — bibliographic/author decision.**

Proposed response/action: Recover and verify the removed identifier and decide whether it is a relevant software/archive DOI before agreeing to delete it.

Author citation preference, 6 October: prefer a verified software/archive DOI to a website-only entry. This does not yet approve restoring the unidentified deleted DOI; recover and verify its target first.

Outstanding: Compare with the submitted reference or Paperpile export, then verify the identifier’s target. If it identifies the software release used, retain a persistent citation as appropriate; otherwise explain the correction. Do not hand-edit paperpile.bib.

## Highlighted material without a separate comment

These items do not increase the count of 22 MDPI comments.

| Item | Source/PDF locator | Relationship and required follow-up | Status |
| --- | --- | --- | --- |
| Figure 6 and Figure 2 callouts | Lines 112 and 116; p. 3 | Within the citation-order scope of MDPI05. | Open; linked above |
| Appendix Table A2 and A3 callouts | Lines 307 and 311; p. 8 | Within “same as below” under MDPI09. | Open; linked above |
| Claude and OpenAI Codex | Line 660; p. 16 | Possible continuation of the software-version request; explicit model/version requirements are not stated. Preserve the AI-use disclosure and verify author/session facts before adding identifiers. | Open; scope/author facts |
| USGS publisher location | Line 847; reference 31, p. 17 | Within “same as below” under MDPI20; tracked as MDPI20b. | Open; linked above |
| McKinney conference location/dates | Line 919; reference 43, p. 18 | Highlighted “Austin, TX, USA, 28 June–3 July 2010” has no attached comment. Verify the exact cited proceedings and official event metadata before confirming this editorial addition. | Open; bibliographic verification |

## Incidental source issue

`tab:v3-heatdeficit` is defined twice (lines 578 and 596), with the second definition attached to a continued Table A5.
The supplied `.aux` repeats the label and the supplied `.log` reports it as multiply defined (lines 1326 and 1329).
This is an observed source/log issue, not an additional publisher query or a new build result.
When corrections begin, retain one canonical cross-reference label, preserve the continued table and verify its references in the rebuilt PDF.

## Next resolution pass

1. Complete the remaining author facts for MDPI01 and any AI identifiers; retain the title, email and emphasis decisions recovered from John’s saved source comments for EE01, MDPI02 and MDPI03.
2. Use the complete `proof-package/working/` copy already created; preserve the received baseline and record corrections in this register.
3. Resolve citation order, mathematical/appendix formatting and the duplicate label in that copy; inspect the queried figures using their registered evidence before drafting precise caption changes.
4. Recover versions from the actual analysis provenance and verify bibliographic additions/removal against authoritative records. Do not substitute current software versions or assume the publisher’s changes are correct.
5. Build `air-4472509-done.tex` in the working copy and inspect all pages against the supplied PDF; update each follow-up with the applied change, evidence, final reply and any remaining author decision.

The received source embeds its bibliography: changing a `.bib` file alone cannot resolve its reference queries.
Keep Paperpile-owned and template files unchanged, and preserve original figure evidence.
Root manuscript/package integration remains a separate requested step under the handoff.
