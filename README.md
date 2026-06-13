# DocConvert

Skill-first document conversion toolkit.

## Status

This repo is currently a small library of script entrypoints rather than a full
app or server. The immediate value is stable conversion behavior that can be
reused by skills and future wrappers.

Current scope:
- LaTeX to PDF conversion (`.tex -> .pdf`)
- Multi-format to Markdown normalization (`docx/html/epub/rtf/tex/txt/pdf -> .md`)
- Markdown to rich text conversion (`.md -> .rtf`)

## Why this repo exists

Agent workflows need reliable normalization and rendering primitives. This repo starts as a Codex skill and executable scripts, then can evolve into an MCP server.

## Skill location

- `skills/doc-convert/`

## Repo Shape

```text
docconvert/
├── AGENTS.md
├── README.md
└── skills/doc-convert/
    ├── SKILL.md
    └── scripts/
```

## Quick usage

```bash
# LaTeX to PDF
bash skills/doc-convert/scripts/latex_to_pdf.sh ./input.tex ./output.pdf

# Document to Markdown
python3 skills/doc-convert/scripts/convert_to_markdown.py ./input.docx -o ./output.md

# Markdown to Rich Text
python3 skills/doc-convert/scripts/convert_markdown_to_rich_text.py ./input.md -o ./output.rtf
```

## Dependencies

- For LaTeX to PDF: `tectonic` (preferred) or `pdflatex`
- For Markdown-to-RTF and most format-to-Markdown conversions: `pandoc`
- For PDF-to-Markdown fallback: `pdftotext`

## Validation

Run the script that matches the surface you changed. For example:

```bash
bash skills/doc-convert/scripts/latex_to_pdf.sh ./input.tex ./output.pdf
python3 skills/doc-convert/scripts/convert_to_markdown.py ./input.docx -o ./output.md
python3 skills/doc-convert/scripts/convert_markdown_to_rich_text.py ./input.md -o ./output.rtf
```

## Future improvements

- Expose the same conversion capabilities through an MCP server
- Add OCR-based pipelines for scanned PDFs
- Add table-preserving conversion strategies and tests
