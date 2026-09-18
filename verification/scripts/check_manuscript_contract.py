#!/usr/bin/env python3
"""Validate the audited manuscript against its explicit submission inputs."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


FIGURE_RE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")
CITE_RE = re.compile(r"\\cite(?:p|t)?\{([^}]+)\}")
BIB_KEY_RE = re.compile(r"@[A-Za-z]+\s*\{\s*([^,\s]+)\s*,")
FORBIDDEN = {
    r"\footnote": "footnote (use a bibliography citation or acknowledgement)",
    r"\rewritegate": "visible rewrite gate",
    r"\diagnosticnote": "visible diagnostic note",
    "verification/figures/candidates": "candidate-figure path",
    "REVIEW-LAYOUT ONLY": "review-layout marker",
    "PAPERPILE-TODO": "unresolved bibliography placeholder",
}


def read_figure_list(path: Path) -> list[str]:
    figures: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        item = raw.strip()
        if item and not item.startswith("#"):
            figures.append(item)
    if len(figures) != len(set(figures)):
        raise ValueError(f"duplicate entries in {path}")
    return figures


def validate(tex_path: Path, bib_paths: list[Path], figure_list_path: Path) -> None:
    tex = tex_path.read_text(encoding="utf-8")
    bib = "\n".join(path.read_text(encoding="utf-8") for path in bib_paths)
    allowed = read_figure_list(figure_list_path)
    referenced = sorted(set(FIGURE_RE.findall(tex)))

    errors: list[str] = []
    for token, description in FORBIDDEN.items():
        if token in tex:
            errors.append(f"{description}: {token}")

    allowed_set = set(allowed)
    referenced_set = set(referenced)
    for figure in referenced:
        if not figure.startswith("figures/"):
            errors.append(f"figure is outside figures/: {figure}")
        if figure not in allowed_set:
            errors.append(f"figure is not allowlisted: {figure}")
        if not Path(figure).is_file():
            errors.append(f"referenced figure is missing: {figure}")
    for figure in allowed:
        if figure not in referenced_set:
            errors.append(f"allowlisted figure is not referenced: {figure}")
        if not Path(figure).is_file():
            errors.append(f"allowlisted figure is missing: {figure}")

    cited = {
        key.strip()
        for group in CITE_RE.findall(tex)
        for key in group.split(",")
        if key.strip()
    }
    bib_keys = set(BIB_KEY_RE.findall(bib))
    for key in sorted(cited - bib_keys):
        errors.append(f"citation key is missing from bibliography inputs: {key}")

    if errors:
        raise SystemExit("Manuscript contract failed:\n- " + "\n- ".join(errors))
    print(
        f"Manuscript contract: OK ({len(referenced)} figures, "
        f"{len(cited)} citation keys)"
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tex", type=Path, required=True)
    parser.add_argument("--bib", type=Path, action="append", required=True)
    parser.add_argument("--figure-list", type=Path, required=True)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    validate(args.tex, args.bib, args.figure_list)


if __name__ == "__main__":
    main()
