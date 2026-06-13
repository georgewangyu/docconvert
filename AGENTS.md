# DocConvert Agent Instructions

## Mission

DocConvert is a skill-first document conversion toolkit. Keep the repo focused
on reusable conversion primitives that can later be wrapped by an MCP server or
other automation surface.

## Working Rules

1. Preserve stable script entrypoints for each conversion path.
2. Prefer explicit dependency requirements over hidden setup assumptions.
3. Keep the repo public-safe and data-agnostic; do not hardcode private paths
   or user-specific defaults.

## Validation

Run the smallest relevant conversion path or dependency check for the files you
touch.
