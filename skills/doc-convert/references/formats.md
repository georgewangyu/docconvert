# Format Notes

## Current implementation

- Primary normalization path: `pandoc` to GitHub-flavored Markdown (`gfm`)
- Markdown authoring export path: `pandoc` to Rich Text Format (`.rtf`)
- PDF fallback path: `pdftotext` plain-text extraction

## Practical caveats

- PDF conversion quality depends on source PDF structure
- Complex tables and multi-column layouts may need post-editing
- Scanned PDFs require OCR for high quality conversion

## MCP migration notes

Keep script entry points stable so the same functionality can be wrapped behind a future MCP server without changing behavior.
