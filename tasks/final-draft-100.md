# Final-draft register: 50 required tasks and 50 high-value opportunities

Frozen 15 July 2026 from the branch, evidence, manuscript, build, and repo-rot
audit in `notes/final-draft-readiness-2026-07-15.md`.

The first 50 rows are the completion path for an author-approved submission.
“Verify or remove” is a valid scientific outcome; a task never requires inventing
support for inherited prose.
The second 50 rows are optional opportunities, not blockers and not permission to
reopen a failed Architecture C gate without new predeclared evidence.

## Required: scientific and evidence closure

| ID | Task | Owner / host | Dependency | Artefact | Definition of done |
|---|---|---|---|---|---|
| FD-01 | Freeze the one-sentence thesis and final working title. | John / Akamai | Read the full 17-page main candidate. | Decision note in readiness record; matching title in `main.tex`. | John can state the claim without chemistry, persistence, or general forecast-ranking language. |
| FD-02 | Cross-check every numeric statement in `main.tex` against its exact CSV, JSON, table, or figure. | Codex, then John / Akamai | Current claim ledger and manifests. | Updated ledger or corrected prose. | Each number has runs, domain, sample, window, units, aggregation, and source; unsupported numbers are removed. |
| FD-03 | Re-audit the four promoted run identities and the matched contrasts. | Michael / CHPC; Codex records | Run and comparison inventories. | Signed review note or inventory corrections. | Michael confirms forcing, feedback, domains, levels, physics, dates, cadence, and archive paths. |
| FD-04 | Verify the WRF 4.8.0 and domain/static-input Methods wording from as-run evidence. | Michael / CHPC | Header and namelist fingerprints. | Configuration review note plus manuscript correction if needed. | Every configuration field is verified or omitted; no build-repo default is used as evidence. |
| FD-05 | Close GFS and NAM analysis-product metadata and source citations. | John / Akamai | Curated bibliography export. | Verified citation rows and Methods citations. | Product names, resolution/cycle wording, archive route, and cited authority agree with inputs. |
| FD-06 | Recover or bound the historical Synoptic request, QC flags, sensor metadata, and reuse terms. | John and Michael / Akamai | Frozen observation cache and provider records. | Observation-provenance note and Methods/Data Availability edit. | Request/QC/licence is reproducible, or the manuscript explicitly states the irrecoverable limit. |
| FD-07 | Verify station inclusion, elevation matching, reporting counts, and missingness. | Codex / Akamai | Station CSVs and observation cache provenance. | Audited station table or ledger note. | The common sample and all exclusions reproduce without inferring values from absent stations. |
| FD-08 | Independently inspect the EPA AQS site/filter/value mapping and low-coverage days. | John / Akamai | DATA39 and AQS provenance JSON. | Human review mark in the figure provenance. | Five site IDs, 295 rows, local dates, ppm-to-ppb conversion, metric label, and seven low-coverage site-days are confirmed. |
| FD-09 | Verify NASA GIBS/MODIS layer identity, date convention, credit, and reuse requirements. | John / Akamai | Registered MODIS provenance. | Final credit/citation text or panel removal. | The browse layer is licensed and labelled as qualitative calendar-day context only. |
| FD-10 | Re-derive the heat-deficit equation, sign, pressure bounds, units, and discrete integration. | Codex, then Michael / Akamai+CHPC | Heat-deficit generator and provenance. | Math-audit note and tests/correction. | Independent calculation reproduces MJ m-2 values and confirms `p_c < p_s` with no sign ambiguity. |
| FD-11 | Confirm the 2200 m crest choice and 2100--2300 m sensitivity bracket. | John and Michael / Akamai | Registered footprint and sensitivity output. | One approved Methods sentence. | The value is framed as predeclared central sensitivity, not an observed inversion top or hydrologic boundary. |
| FD-12 | Audit the 50--500 m common-AGL stability and transport-wind definitions. | Michael / CHPC | Vertical reduction code and matched profiles. | Diagnostic-method approval or correction. | Interpolation, layer bounds, wind magnitude, station/grid matching, and missing-level behaviour are explicit and reproducible. |
| FD-13 | Audit surface-score alignment and aggregation. | Codex / Akamai | `brc-tools` verification code and summary CSVs. | Reproduction log. | Time alignment, station pairing, medians, bias/error signs, units, and sample counts reproduce exactly. |
| FD-14 | Audit the 20,000-draw two-hour circular block procedure. | Codex / Akamai | Registered script and seed behaviour. | Test or method note. | Rerun is deterministic; intervals match; prose calls them descriptive dependence checks, not confidence intervals. |
| FD-15 | Reconcile absolute run magnitudes with every reported matched contrast. | Codex / Akamai | Stability, transport, and heat-deficit tables. | Compact consistency table. | Readers can distinguish absolute state from pair difference; subtraction direction is uniform throughout. |
| FD-16 | Recompute the forcing-by-feedback interaction and both within-source feedback effects. | Codex / Akamai | Four-run factorial summaries. | Reproduction log or corrected table. | Signs and units match Methods and Results; small effects are not described as equivalence. |
| FD-17 | Run a forbidden-claim sweep over title, abstract, body, captions, and supplement. | John + Codex / Akamai | Frozen scope contract. | Zero-hit report or bounded edits. | No proof of chemistry, emissions adequacy, basin export, inversion depth, multi-day persistence, or initial-condition causality remains. |
| FD-18 | Verify that failed/gated comparisons and unpromoted figures do not enter `main.tex`. | Codex / Akamai | Gate review and both figure manifests. | Manuscript-contract report. | Every main figure is dual-promoted and no C3/C5/C6/X8 diagnostic becomes a result by wording. |
| FD-19 | Separate controlled experiments, heterogeneous context, observations, and literature in every inference. | John + Codex / Akamai | Claim ledger. | Claim-language pass. | Each paragraph signals its evidence class and avoids cross-class causal comparison. |
| FD-20 | Obtain Michael's scientific and provenance review of the promoted Results. | Michael / CHPC or PDF review | Completed technical audit packet. | Dated comments and disposition table. | Every comment is accepted, revised, or rejected with reason before coauthor circulation. |

## Required: citations and persuasive writing

| ID | Task | Owner / host | Dependency | Artefact | Definition of done |
|---|---|---|---|---|---|
| FD-21 | Export John's small, complete Paperpile bibliography once. | John / Akamai | Final intended citation set. | Replacement `paperpile.bib`. | Export contains all intended sources and no hand-authored keys; the old file is replaced wholesale. |
| FD-22 | Record the export date/hash and generated keys without normalising the file. | Codex / Akamai | Complete export. | Bibliography provenance note. | Hash and key inventory are committed; file content remains Paperpile-owned. |
| FD-23 | Resolve every citation and remove every unused accidental entry. | Codex / Akamai | Stable Paperpile export. | Citation audit report. | All manuscript keys resolve, every retained citation is used intentionally, and build logs have no citation warnings. |
| FD-24 | Verify each literature-dependent sentence against the underlying source passage. | John + Codex / Akamai | Critiques/extracts and source PDFs. | Passage-to-sentence ledger. | Every claim has page/section support and caveats; critiques are routes, not cited substitutes. |
| FD-25 | Add only the authoritative model, forcing-product, observation, and satellite citations the final Methods requires. | John / Akamai | Verified sources and stable bibliography. | Cited Methods and Data Availability text. | No citation is guessed, and every product statement has the narrowest correct authority. |
| FD-26 | Tighten the Introduction around problem, gap, test, and contribution. | John / Akamai | Frozen thesis. | Revised Introduction. | Each paragraph advances the argument; historical detail that does not motivate the estimands is removed. |
| FD-27 | Edit Methods into a reproducible order from design to data to diagnostics to uncertainty. | John + Codex / Akamai | Evidence closure. | Revised Methods. | A technically competent reader can reproduce the reported comparisons without consulting v3 prose. |
| FD-28 | Make Results claim-first while keeping absolute states separate from contrasts. | John / Akamai | Number audit. | Revised Results. | Every subsection opens with the tested result, reports scale and limits, and defers interpretation to Discussion. |
| FD-29 | Make Discussion persuasive without causal overreach. | John + Loknath + Seth / Akamai | Results frozen. | Reviewed Discussion. | Supplied-state offset, small feedback response, Air relevance, alternative explanations, and design limits form one coherent argument. |
| FD-30 | Align Conclusions sentence-by-sentence with Results and Discussion. | John / Akamai | Frozen Results. | Revised Conclusions. | No conclusion introduces a new mechanism, time scale, comparison, or policy implication. |
| FD-31 | Confirm the current journal abstract limit and edit the abstract to it. | John / Akamai | Final Results and Conclusions. | Final abstract plus word-count record. | Abstract states question, design, principal magnitudes, interpretation, and limits within the verified journal limit. |
| FD-32 | Approve final title and keywords with all coauthors. | All authors / asynchronous | Frozen thesis and abstract. | Approval record and front matter. | Title promises only the tested window and keywords are specific, searchable, and nonredundant. |
| FD-33 | Complete a British-English, terminology, symbols, and semantic-line-break pass. | John + Codex / Akamai | Stable prose. | Clean source diff. | Terms, capitalisation, units, hyphenation, notation, and one-sentence-per-source-line style are consistent. |
| FD-34 | Make every main figure and table caption stand alone. | John + Codex / Akamai | Final panels and tables. | Caption pass. | Captions identify data, runs, domain, time, statistic, uncertainty/coverage marker, and interpretive limit without hidden claims. |
| FD-35 | Split v3's temporary Appendix B review layout into a real separate supplement only if retained. | John / Akamai | Final main/supplement decision. | Separate supplement source/PDF or explicit drop decision. | No provisional candidate panel is smuggled into the journal package under the review-layout convention. |

## Required: figures, front matter, and submission

| ID | Task | Owner / host | Dependency | Artefact | Definition of done |
|---|---|---|---|---|---|
| FD-36 | Freeze both figure manifests and all promoted hashes. | Codex / Akamai | Final figure selection. | Updated manifests. | Every main figure has matching inputs, generator, commit/hash, visual review, narrative role, and promoted status in both records. |
| FD-37 | Inspect every figure at final print dimensions. | John / Akamai | Final PDF build. | Figure-review checklist. | Text, symbols, line weights, legends, annotations, and panel labels remain legible at journal size. |
| FD-38 | Check colour accessibility and greyscale failure modes. | John + Codex / Akamai | Final figure set. | Accessibility review note or revised assets. | Series remain distinguishable for common colour-vision deficiencies and a monochrome print does not reverse meaning. |
| FD-39 | Verify raster resolution, vector preservation, crop boxes, and embedded fonts. | Codex / Akamai | Final assets. | Preflight report. | Each asset meets journal requirements without accidental downsampling or clipped labels. |
| FD-40 | Close locator, MODIS, and any third-party figure credit/permission language. | John / Akamai | Source/licensing audit. | Caption credits and permission record. | Every non-original component has required attribution and can legally ship in the source package. |
| FD-41 | Confirm names, order, affiliations, ORCIDs, email, and corresponding author. | All authors / asynchronous | Final author list. | Completed front matter. | Every author explicitly approves their metadata and order; no placeholder remains. |
| FD-42 | Agree and encode CRediT roles. | All authors / asynchronous | Author contribution discussion. | Author Contributions statement. | Each role is accurate, approved, and consistent with contribution records. |
| FD-43 | Confirm funding numbers, acknowledgments, facilities, and required sponsor wording. | John + coauthors / Akamai | Institutional records. | Final Funding and Acknowledgments text. | Grant/facility statements are complete and approved; no guessed number or omitted required disclaimer remains. |
| FD-44 | Finalise conflicts, AI-use disclosure, and all applicable institutional statements. | John / Akamai | Journal policy and author confirmation. | Completed declarations. | Each required declaration is present, truthful, current, and free of template text. |
| FD-45 | Freeze Data Availability, Code Availability, archive constraints, and planned persistent links. | John + Michael / Akamai+CHPC | Release decision and licences. | Final availability statement and release manifest. | A reader knows what is public, restricted, derived, available on request, or archived, with no promise the team cannot meet. |
| FD-46 | Run the complete final-draft validation at a frozen commit. | Codex / Akamai | Stable manuscript, bib, figures, and manifests. | Saved validation summary. | `make final-draft-check`, JSON/CSV checks, hash checks, and `git diff --check` all pass from a clean tree. |
| FD-47 | Build the allowlisted package in an independent clean environment. | Codex or Michael / clean host | Frozen commit and toolchain record. | Independent build log and PDF. | The staged source builds with pdfLaTeX/BibTeX without relying on ignored files, repo caches, or undeclared sibling content. |
| FD-48 | Inspect the source ZIP and separate supplement package by hand. | John + Codex / Akamai | Successful independent build. | Package inventory checklist. | Every referenced source/figure is present; notes, drafts, candidates, verification data, Git files, and local JRL artefacts are absent. |
| FD-49 | Circulate dated main and supplement PDFs and close coauthor comments. | John / asynchronous | Technically frozen review candidate. | Comment/disposition register and approvals. | Michael approves provenance/diagnostics; Loknath and Seth approve chemistry framing; all authors approve the final text. |
| FD-50 | Publish the reviewed Git state and execute the submission handoff. | John / GitHub+Akamai | All required approvals and package checks. | Merged PR, release tag, archived package hash, and submission record. | Protected `main` contains the approved source, the tag matches the submitted package, and the journal receipt is recorded. |

## Optional: high-value scientific opportunities

These are deliberately nonblocking.
Start one only when its payoff clearly exceeds the cost and its design does not
retrofit a failed gate.

| ID | Opportunity | Likely payoff | Cost / dependency | Stop rule |
|---|---|---|---|---|
| HV-01 | Separate initialisation from lateral-boundary influence with a new controlled design. | Stronger mechanism attribution. | New WRF experiments and predeclared estimands. | Stop if the final paper does not need causal source attribution. |
| HV-02 | Extend the matched factorial beyond the five-hour window. | Tests persistence rather than short-window state. | New integrations and observation alignment. | Stop if configuration drift prevents a clean extension. |
| HV-03 | Add a genuinely comparable no-signal or ordinary-winter control period. | Shows episode specificity. | New case selection and complete matched inputs. | Stop if the control differs in more than the intended regime. |
| HV-04 | Test additional crest heights outside the registered bracket. | Broader heat-deficit robustness. | New predeclared sensitivity analysis. | Stop if it becomes post-hoc threshold hunting. |
| HV-05 | Compare alternative basin footprints. | Tests geographic dependence. | Defensible masks and repeated reductions. | Stop if footprint definitions follow desired results. |
| HV-06 | Test adjacent reporting windows. | Shows timing sensitivity. | Multiple-comparison discipline. | Stop if five-hour claims are already sufficient. |
| HV-07 | Build a separately justified d03 interior evaluation sample. | Tests transfer to the chemistry-scale grid. | Station coverage and representativeness analysis. | Never substitute it for the frozen d02 common sample. |
| HV-08 | Stratify surface error by station elevation and sub-basin. | Exposes cancellation in basin medians. | Adequate per-stratum sample size. | Stop when strata become too sparse to interpret. |
| HV-09 | Add circular wind-direction diagnostics with calm-wind handling. | Richer ventilation evaluation. | Direction QC and circular statistics. | Stop if calm conditions make direction mostly undefined. |
| HV-10 | Design a clean YSU-versus-MYJ/Eta comparison. | Tests PBL/surface-layer sensitivity. | Same-case controlled run plus scheme-aware diagnostics. | Do not reuse the current diagnostic as a general scheme ranking. |
| HV-11 | Revisit the radiation response with suitable observations. | Could convert a failed measurement-limited gate into evidence. | Radiation observations and a predeclared criterion. | Preserve the existing failure unless new independent evidence exists. |
| HV-12 | Design a controlled terrain-resolution experiment. | Separates static terrain from other X4/X0 changes. | New WPS/WRF pair with identical remaining settings. | Stop if vertical grid, geometry, or cadence also change. |
| HV-13 | Compare modelled snow with a quantitative snow product. | Tests a key cold-pool boundary condition. | Cloud-screened retrieval and scale matching. | Do not treat the current MODIS browse image as that product. |
| HV-14 | Add upper-air observations at defensible times/locations. | Directly evaluates vertical structure. | Sounding provenance and representativeness. | Stop if timing/location mismatch overwhelms the comparison. |
| HV-15 | Regenerate the withheld observational inversion diagnostic without the 8 K reference. | Could strengthen observed context. | Frozen cache and full metadata review. | Keep withheld if it still implies measured inversion depth. |
| HV-16 | Evaluate nudging only with held-out observations. | Defensible assimilation-sensitivity result. | Assimilated-station inventory and new design. | Stop if verification is not independent. |
| HV-17 | Add new comparative evidence before revisiting X8 convergence. | Tests fine-scale transport context. | Controlled comparator and matched geometry. | Current within-run packet remains noncomparative until then. |
| HV-18 | Pursue a formally closed X8 deficit budget. | Stronger process understanding. | Complete terms, boundary conditions, and numerical residual audit. | Stop if missing terms dominate closure. |
| HV-19 | Define and calculate basin-boundary transport fluxes. | Directly tests export/retention language. | Defensible boundary and three-dimensional flux method. | Do not call canyon-gate diagnostics basin export. |
| HV-20 | Add a longer observation-only ozone/meteorology context timeline. | Better episode narrative. | Data completeness and noncausal framing. | Stop if it distracts from the modelled window. |

## Optional: code, reproducibility, narrative, and repo efficiency

| ID | Opportunity | Likely payoff | Cost / dependency | Stop rule |
|---|---|---|---|---|
| HV-21 | Move reusable paper-script kernels into `brc-tools`. | Less duplicate scientific code. | Stable API and tests. | Keep manuscript-specific orchestration here. |
| HV-22 | Add unit tests for heat-deficit pressure integration and units. | Protects the central derived metric. | Small synthetic columns with analytic answers. | Tests must not replace real-data reproduction. |
| HV-23 | Add property tests for circular-block resampling. | Guards wraparound and seed behaviour. | Statistical test design. | Avoid claiming inferential validity from code correctness. |
| HV-24 | Define schemas for run, comparison, data, and figure manifests. | Earlier rot detection. | Schema maintenance. | Do not make handoff edits harder than the errors prevented. |
| HV-25 | Add a cross-manifest admission checker. | Prevents candidate leakage. | Stable IDs and path rules. | Keep the explicit allowlist as final authority. |
| HV-26 | Automate provenance hashes and deterministic timestamps. | Cheaper artefact registration. | Carefully bounded generator wrapper. | Never rewrite immutable execution records. |
| HV-27 | Freeze a portable analysis environment or lockfile. | Easier independent reproduction. | Cross-host package reconciliation. | Avoid pinning system-specific CHPC modules as universal. |
| HV-28 | Add CI for fast checks and contract validation. | PR feedback before human review. | Private-repo runner policy. | Keep heavy WRF/data work off CI. |
| HV-29 | Add perceptual regression checks for promoted figures. | Detects accidental visual drift. | Baselines and tolerance tuning. | Human inspection remains mandatory. |
| HV-30 | Add a manuscript linter for semantic lines, forbidden claims, and placeholders. | Faster final passes. | Curated rules and exceptions. | Do not let keyword matches replace scientific review. |
| HV-31 | Expand the literature comparison matrix with newly published peer-reviewed work. | Stronger positioning. | Current search and passage verification. | Stop when additions do not change framing or methods. |
| HV-32 | Add a compact theory paragraph on supplied-state versus developed error. | Clarifies the main interpretation. | Verified forecast-sensitivity sources. | Omit if citations cannot support the distinction. |
| HV-33 | Draft a graphical abstract. | Journal communication value. | Final story and figure permissions. | Do not create a new scientific claim. |
| HV-34 | Draft a plain-language public summary. | Stakeholder accessibility. | Approved final manuscript. | Publish only after coauthor review. |
| HV-35 | Prepare a one-panel table-of-contents graphic. | More efficient visual entry point. | Journal requirement and final assets. | Skip if MDPI Air does not use one. |
| HV-36 | Build a likely-reviewer objection matrix. | Faster revision response. | Final claims and limitations. | Keep it outside the submission package. |
| HV-37 | Test alternate titles with domain experts. | Better precision/discoverability. | Small review exercise. | John retains final choice; do not reopen the thesis. |
| HV-38 | Expand reproducibility details in a methods supplement. | Keeps main prose lean. | Separate supplement decision. | Include only details that are stable and verified. |
| HV-39 | Build a reviewer-reserve table of null and contradictory results. | Demonstrates honest search and guards cherry-picking. | Registered evidence only. | Do not overload the main paper. |
| HV-40 | Publish the full sensitivity-definition table. | Makes heat-deficit robustness transparent. | Final supplement space. | Skip if the registered summary is already sufficient. |
| HV-41 | Archive completed handoffs and stale prompts after merge. | Cleaner cold starts. | Final branch/tag. | Preserve immutable evidence and decision history. |
| HV-42 | Add a lightweight repo-rot check for stale dates, missing routes, and dead task pointers. | Sustains control-plane accuracy. | Small maintained script. | Report before mutating subjective archive choices. |
| HV-43 | Add an `AGENTS.md` route/link validator. | Prevents broken cold starts. | Simple path checks. | It must stay fast and avoid broad-tree loading. |
| HV-44 | Prune merged remote branches after the final tag. | Reduces branch ambiguity. | Confirmed PR merge and donor preservation. | Never delete legacy or execution refs without John's explicit approval. |
| HV-45 | Tag the minimum compatible `brc-tools` analysis state. | Clearer cross-repo reproducibility. | Maintainer agreement. | A paper-local commit pin remains sufficient if no release is useful. |
| HV-46 | Consolidate duplicated AQS/MODIS helper behaviour into tested reusable APIs. | Less paper-local maintenance. | Clear general-use contract. | Keep paper-specific site and narrative choices here. |
| HV-47 | Generate bounded CHPC dispatch packets from a template. | Safer cross-host work. | Stable packet schema. | Require an immutable source ref and one task per dispatch. |
| HV-48 | Mirror the final task register in machine-readable data. | Easier dashboards and validation. | Avoid dual-source drift. | Markdown remains authoritative unless automation proves reliable. |
| HV-49 | Automate release-bundle hashing and DOI-deposit metadata. | Fewer publication handoff errors. | Chosen repository and credentials. | Never publish restricted input paths or private data. |
| HV-50 | Build a reproducible coauthor-review bundle with PDF, claim map, figures, and change summary. | Faster, more focused review. | Frozen review commit. | Keep verification internals out unless a reviewer needs them. |
