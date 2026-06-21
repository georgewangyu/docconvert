# DocConvert Vision

DocConvert should be a skill-first document conversion toolkit for local,
deterministic format normalization and rendering.

## Product Thesis

Agent workflows need boring, reliable document primitives. This repo should
make common conversion paths scriptable first, then optionally expose the same
capabilities through a future MCP server or wrapper.

## Goals

- Preserve stable entrypoint scripts for each supported conversion path.
- Keep dependency requirements explicit.
- Favor local conversion for privacy and reproducibility.
- Extend conversion directions by adding small adjacent scripts, not hidden
  side effects.

## Non-Goals

- Do not become a full document-management app.
- Do not hardcode private paths or user-specific defaults.
- Do not hide missing system dependencies behind vague conversion failures.
