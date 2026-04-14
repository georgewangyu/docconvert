---
name: doc-convert
description: Convert documents between authoring and analysis formats for agent workflows. Use when you need LaTeX-to-PDF rendering, mixed document types normalized into Markdown, or Markdown exported into rich text.
---

# Doc Convert

## Overview

Use this skill to run deterministic local document conversions with the scripts bundled in this skill folder.

## Quick Start

1. Convert LaTeX to PDF:
   `bash scripts/latex_to_pdf.sh /path/to/input.tex /path/to/output.pdf`
2. Convert document to Markdown:
   `python3 scripts/convert_to_markdown.py /path/to/input.docx -o /path/to/output.md`
3. Convert Markdown to rich text:
   `python3 scripts/convert_markdown_to_rich_text.py /path/to/input.md -o /path/to/output.rtf`

## Tasks

### LaTeX to PDF

- Run `scripts/latex_to_pdf.sh`.
- Prefer `tectonic` when available.
- Fall back to `pdflatex` when `tectonic` is unavailable.

### Mixed Formats to Markdown

- Run `scripts/convert_to_markdown.py`.
- For most formats, use `pandoc` output with `gfm` Markdown.
- For PDF input, use `pdftotext` extraction and wrap output as Markdown text.

### Markdown to Rich Text

- Run `scripts/convert_markdown_to_rich_text.py`.
- Use `pandoc` to render Markdown into Rich Text Format (`.rtf`).

## Supported Inputs

- LaTeX to PDF: `.tex`
- To Markdown: `.docx`, `.html`, `.htm`, `.epub`, `.rtf`, `.tex`, `.txt`, `.pdf`, `.md`
- Markdown to rich text: `.md`, `.markdown`, `.mdown`, `.mkd`

## Notes

- Keep conversion local-first for privacy and reproducibility.
- Install missing system dependencies before retrying failed conversions.
- Extend converter paths in `scripts/convert_to_markdown.py` or add adjacent entry-point scripts when a new direction is required.
