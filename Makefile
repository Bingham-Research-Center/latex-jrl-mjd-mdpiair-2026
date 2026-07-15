SHELL := /bin/bash

MAIN := main
REWRITE_MAIN := _manuscript_test
V3_MAIN := _manuscript_v3
STAGE := dist/mdpi-air-submission
SUBMISSION_FIGURES ?=
PYTHON ?= python
BRC_TOOLS_DIR ?= $(HOME)/brc-tools
MPLCONFIGDIR ?= /tmp/mdpi-air-matplotlib

.PHONY: pdf rewrite-pdf v3-pdf clean rewrite-clean v3-clean check rewrite-check v3-check smoke submission

pdf:
	latexmk -pdf -interaction=nonstopmode -halt-on-error $(MAIN).tex

rewrite-pdf:
	latexmk -pdf -interaction=nonstopmode -halt-on-error $(REWRITE_MAIN).tex

clean:
	latexmk -c $(MAIN).tex

rewrite-clean:
	latexmk -c $(REWRITE_MAIN).tex

check: pdf
	git diff --check -- . ':(exclude)Definitions/**'
	@test -s $(MAIN).pdf
	@! rg -n "fake_(cool|warm)|2 February 2026|2--February--2026" $(MAIN).tex figures

rewrite-check: rewrite-pdf
	git diff --check -- . ':(exclude)Definitions/**'
	@test -s $(REWRITE_MAIN).pdf
	@! rg -n "fake_(cool|warm)|2 February 2026|2--February--2026|8 K CAP threshold" $(REWRITE_MAIN).tex

v3-pdf:
	latexmk -pdf -interaction=nonstopmode -halt-on-error $(V3_MAIN).tex

v3-clean:
	latexmk -c $(V3_MAIN).tex

v3-check: v3-pdf
	git diff --check -- . ':(exclude)Definitions/**'
	@test -s $(V3_MAIN).pdf
	@! rg -n "fake_(cool|warm)|2 February 2026|2--February--2026|8 K CAP threshold|fail(s|ed|ure)? to maintain|maintenance failure|basin volume" $(V3_MAIN).tex

smoke:
	mkdir -p "$(MPLCONFIGDIR)"
	env MPLCONFIGDIR="$(MPLCONFIGDIR)" PYTHONPATH="$(BRC_TOOLS_DIR)" $(PYTHON) verification/scripts/smoke_test_runs_feb0102.py
	env MPLCONFIGDIR="$(MPLCONFIGDIR)" $(PYTHON) verification/scripts/smoke_test_locator.py
	env MPLCONFIGDIR="$(MPLCONFIGDIR)" $(PYTHON) verification/scripts/smoke_test_cross_sections.py
	env MPLCONFIGDIR="$(MPLCONFIGDIR)" $(PYTHON) verification/scripts/smoke_test_upper_air.py
	env MPLCONFIGDIR="$(MPLCONFIGDIR)" $(PYTHON) verification/scripts/smoke_test_retention.py

submission: check
	rm -rf $(STAGE)
	mkdir -p $(STAGE)/Definitions
	cp $(MAIN).tex paperpile.bib $(STAGE)/
	@while IFS= read -r file; do cp "$$file" "$(STAGE)/$$file"; done < <(git ls-files Definitions)
	@if [[ -n "$(SUBMISSION_FIGURES)" ]]; then \
		mkdir -p $(STAGE)/figures; \
		for figure in $(SUBMISSION_FIGURES); do cp "$$figure" $(STAGE)/figures/; done; \
	fi
	cd dist && zip -qr mdpi-air-submission.zip mdpi-air-submission
	@echo "Wrote dist/mdpi-air-submission.zip"
