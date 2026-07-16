SHELL := /bin/bash

MAIN := main
SUPPLEMENT := supplement
REWRITE_MAIN := _manuscript_test
V3_MAIN := _manuscript_v3
STAGE := dist/mdpi-air-submission
SUPPLEMENT_STAGE := dist/mdpi-air-supplement
PYTHON ?= python
BRC_TOOLS_DIR ?= $(abspath ../brc-tools)
BRC_TOOLS_ENV ?= brc-tools
CONDA ?= conda
BRC_TOOLS_REQUIRED_REF ?= 548fee4
SMOKE_PYTHON ?= $(CONDA) run --no-capture-output -n $(BRC_TOOLS_ENV) python
MPLCONFIGDIR ?= /tmp/mdpi-air-matplotlib
SUBMISSION_FIGURE_LIST ?= figures/submission-files.txt
SUPPLEMENT_FIGURE_LIST ?= figures/supplement-files.txt

.PHONY: pdf supplement-pdf rewrite-pdf v3-pdf clean rewrite-clean v3-clean check rewrite-check v3-check \
	smoke-preflight smoke manuscript-contract-check final-draft-check submission submission-check supplement supplement-check submission-draft-check

pdf:
	latexmk -pdf -interaction=nonstopmode -halt-on-error $(MAIN).tex

supplement-pdf:
	latexmk -pdf -interaction=nonstopmode -halt-on-error $(SUPPLEMENT).tex

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

smoke-preflight:
	@test -d "$(BRC_TOOLS_DIR)/brc_tools" || { \
		echo "Missing sibling brc-tools checkout: $(BRC_TOOLS_DIR)" >&2; \
		exit 1; \
	}
	@git -C "$(BRC_TOOLS_DIR)" merge-base --is-ancestor "$(BRC_TOOLS_REQUIRED_REF)" HEAD || { \
		echo "brc-tools HEAD must contain $(BRC_TOOLS_REQUIRED_REF)" >&2; \
		exit 1; \
	}
	@env PYTHONPATH="$(BRC_TOOLS_DIR)" $(SMOKE_PYTHON) -c \
		"import brc_tools, polars; print('brc-tools smoke environment: OK')"

smoke: smoke-preflight
	bash -n verification/slurm/run_v3_finishing_pass.slurm
	bash -n verification/slurm/run_x8_deficit_transport.slurm
	bash -n verification/slurm/pelican_figures.slurm
	mkdir -p "$(MPLCONFIGDIR)"
	env MPLCONFIGDIR="$(MPLCONFIGDIR)" XDG_CACHE_HOME="$(MPLCONFIGDIR)" PYTHONPATH="$(BRC_TOOLS_DIR)" $(SMOKE_PYTHON) verification/scripts/analyze_x8_deficit_transport.py --help >/dev/null
	env MPLCONFIGDIR="$(MPLCONFIGDIR)" PYTHONPATH="$(BRC_TOOLS_DIR)" $(SMOKE_PYTHON) verification/scripts/smoke_test_runs_feb0102.py
	env MPLCONFIGDIR="$(MPLCONFIGDIR)" $(SMOKE_PYTHON) verification/scripts/smoke_test_locator.py
	env MPLCONFIGDIR="$(MPLCONFIGDIR)" PYTHONPATH="$(BRC_TOOLS_DIR)" $(SMOKE_PYTHON) verification/scripts/smoke_test_terrain_cmp11_supplement.py
	env MPLCONFIGDIR="$(MPLCONFIGDIR)" PYTHONPATH="$(BRC_TOOLS_DIR)" $(SMOKE_PYTHON) verification/scripts/smoke_test_profile_table.py
	env MPLCONFIGDIR="$(MPLCONFIGDIR)" PYTHONPATH="$(BRC_TOOLS_DIR)" $(SMOKE_PYTHON) verification/scripts/smoke_test_cross_sections.py
	env MPLCONFIGDIR="$(MPLCONFIGDIR)" $(SMOKE_PYTHON) verification/scripts/smoke_test_upper_air.py
	env MPLCONFIGDIR="$(MPLCONFIGDIR)" $(SMOKE_PYTHON) verification/scripts/smoke_test_retention.py

manuscript-contract-check:
	$(PYTHON) verification/scripts/check_manuscript_contract.py \
		--tex $(MAIN).tex \
		--bib paperpile.bib \
		--figure-list $(SUBMISSION_FIGURE_LIST)

final-draft-check: check rewrite-check v3-check smoke manuscript-contract-check

submission: check manuscript-contract-check
	rm -rf $(STAGE)
	mkdir -p $(STAGE)/Definitions
	cp $(MAIN).tex paperpile.bib $(STAGE)/
	@while IFS= read -r file; do cp "$$file" "$(STAGE)/$$file"; done < <(git ls-files Definitions)
	@while IFS= read -r figure; do \
		[[ -z "$$figure" || "$$figure" == \#* ]] && continue; \
		mkdir -p "$(STAGE)/$$(dirname "$$figure")"; \
		cp "$$figure" "$(STAGE)/$$figure"; \
	done < $(SUBMISSION_FIGURE_LIST)
	cd dist && zip -qr mdpi-air-submission.zip mdpi-air-submission
	@echo "Wrote dist/mdpi-air-submission.zip"

submission-check: submission
	@if ! command -v gs >/dev/null 2>&1; then \
		test -s Definitions/logo-mdpi-eps-converted-to.pdf || { \
			echo "Ghostscript is unavailable and no cached MDPI logo conversion exists" >&2; \
			exit 1; \
		}; \
		cp Definitions/logo-mdpi-eps-converted-to.pdf $(STAGE)/Definitions/; \
		echo "Using cached logo conversion for local staging-tree check; ZIP remains source-clean"; \
	fi
	cd $(STAGE) && latexmk -pdf -interaction=nonstopmode -halt-on-error $(MAIN).tex
	@test -s $(STAGE)/$(MAIN).pdf
	@! find $(STAGE) -type f \( \
		-path '*/verification/*' -o \
		-path '*/drafts/*' -o \
		-name 'AGENTS.md' -o \
		-name '*.py' -o \
		-name '*.sh' \
	\) | grep -q .
	@echo "Independent submission build: OK"

supplement: supplement-pdf
	rm -rf $(SUPPLEMENT_STAGE)
	mkdir -p $(SUPPLEMENT_STAGE)
	cp $(SUPPLEMENT).tex $(SUPPLEMENT).pdf $(SUPPLEMENT_STAGE)/
	@while IFS= read -r figure; do \
		[[ -z "$$figure" || "$$figure" == \#* ]] && continue; \
		mkdir -p "$(SUPPLEMENT_STAGE)/$$(dirname "$$figure")"; \
		cp "$$figure" "$(SUPPLEMENT_STAGE)/$$figure"; \
	done < $(SUPPLEMENT_FIGURE_LIST)
	cd dist && zip -qr mdpi-air-supplement.zip mdpi-air-supplement
	@echo "Wrote dist/mdpi-air-supplement.zip"

supplement-check: supplement
	cd $(SUPPLEMENT_STAGE) && latexmk -pdf -interaction=nonstopmode -halt-on-error $(SUPPLEMENT).tex
	@test -s $(SUPPLEMENT_STAGE)/$(SUPPLEMENT).pdf
	@! find $(SUPPLEMENT_STAGE) -type f \( \
		-path '*/verification/*' -o \
		-path '*/drafts/*' -o \
		-name 'AGENTS.md' -o \
		-name '*.py' -o \
		-name '*.sh' \
	\) | grep -q .
	@echo "Independent supplement build: OK"

submission-draft-check: final-draft-check submission-check supplement-check
