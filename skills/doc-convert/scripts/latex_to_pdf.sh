#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "Usage: $0 <input.tex> [output.pdf]" >&2
  exit 1
fi

INPUT_TEX="$1"
OUTPUT_PDF="${2:-${INPUT_TEX%.tex}.pdf}"

if [[ ! -f "$INPUT_TEX" ]]; then
  echo "Input file not found: $INPUT_TEX" >&2
  exit 1
fi

if [[ "${INPUT_TEX##*.}" != "tex" ]]; then
  echo "Input must be a .tex file: $INPUT_TEX" >&2
  exit 1
fi

INPUT_BASE="$(basename "$INPUT_TEX")"
OUTPUT_ABS="$OUTPUT_PDF"
if [[ "$OUTPUT_ABS" != /* ]]; then
  OUTPUT_ABS="$(pwd)/$OUTPUT_ABS"
fi

mkdir -p "$(dirname "$OUTPUT_ABS")"

if command -v tectonic >/dev/null 2>&1; then
  tectonic --outdir "$(dirname "$OUTPUT_ABS")" "$INPUT_TEX"
  GENERATED="$(dirname "$OUTPUT_ABS")/${INPUT_BASE%.tex}.pdf"
  if [[ "$GENERATED" != "$OUTPUT_ABS" ]]; then
    mv "$GENERATED" "$OUTPUT_ABS"
  fi
  echo "Generated PDF with tectonic: $OUTPUT_ABS"
  exit 0
fi

if command -v pdflatex >/dev/null 2>&1; then
  TMP_DIR="$(mktemp -d)"
  trap 'rm -rf "$TMP_DIR"' EXIT

  cp "$INPUT_TEX" "$TMP_DIR/$INPUT_BASE"
  (
    cd "$TMP_DIR"
    pdflatex -interaction=nonstopmode -halt-on-error "$INPUT_BASE" >/dev/null
    pdflatex -interaction=nonstopmode -halt-on-error "$INPUT_BASE" >/dev/null
  )

  mv "$TMP_DIR/${INPUT_BASE%.tex}.pdf" "$OUTPUT_ABS"
  echo "Generated PDF with pdflatex: $OUTPUT_ABS"
  exit 0
fi

echo "Missing dependency: install 'tectonic' or 'pdflatex' to compile LaTeX." >&2
exit 1
