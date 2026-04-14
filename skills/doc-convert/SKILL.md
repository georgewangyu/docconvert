---
name: doc-convert
description: Convert documents between authoring and analysis formats for agent workflows. Use when you need LaTeX-to-PDF rendering, or when you need to normalize mixed document types (docx, html, epub, rtf, tex, txt, pdf) into Markdown for downstream LLM processing.
---

# Doc Convert

## Overview

Use this skill to run deterministic local document conversions with the scripts bundled in this skill folder.

## Quick Start

1. Convert LaTeX to PDF:
   `bash scripts/latex_to_pdf.sh /path/to/input.tex /path/to/output.pdf`
2. Convert document to Markdown:
   `python3 scripts/convert_to_markdown.py /path/to/input.docx -o /path/to/output.md`

## Tasks

### LaTeX to PDF

- Run `scripts/latex_to_pdf.sh`.
- Prefer `tectonic` when available.
- Fall back to `pdflatex` when `tectonic` is unavailable.

### Mixed Formats to Markdown

- Run `scripts/convert_to_markdown.py`.
- For most formats, use `pandoc` output with `gfm` Markdown.
- For PDF input, use `pdftotext` extraction and wrap output as Markdown text.

## Supported Inputs

- LaTeX to PDF: `.tex`
- To Markdown: `.docx`, `.html`, `.htm`, `.epub`, `.rtf`, `.tex`, `.txt`, `.pdf`, `.md`

## Notes

- Keep conversion local-first for privacy and reproducibility.
- Install missing system dependencies before retrying failed conversions.
- Extend converter paths in `scripts/convert_to_markdown.py` when a new format is required.
