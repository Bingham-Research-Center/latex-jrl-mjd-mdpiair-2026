SHELL := /bin/bash

MAIN := main
STAGE := dist/mdpi-air-submission
SUBMISSION_FIGURES ?=

.PHONY: pdf clean check smoke submission

pdf:
	latexmk -pdf -interaction=nonstopmode -halt-on-error $(MAIN).tex

clean:
	latexmk -c $(MAIN).tex

check: pdf
	git diff --check -- . ':(exclude)Definitions/**'
	@test -s $(MAIN).pdf
	@! rg -n "fake_(cool|warm)|2 February 2026|2--February--2026" $(MAIN).tex figures

smoke:
	conda run -n brc-tools env PYTHONPATH="$$HOME/brc-tools" python verification/scripts/smoke_test_runs_feb0102.py
	conda run -n brc-tools python verification/scripts/smoke_test_cross_sections.py
	conda run -n brc-tools python verification/scripts/smoke_test_upper_air.py

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
