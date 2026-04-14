#!/usr/bin/env python3
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

MARKDOWN_EXTENSIONS = {
    ".md",
    ".markdown",
    ".mdown",
    ".mkd",
}


def require_binary(name: str) -> None:
    if shutil.which(name) is None:
        raise RuntimeError(f"Missing dependency: '{name}' is required.")


def convert_markdown_to_rtf(input_path: Path, output_path: Path) -> None:
    require_binary("pandoc")
    subprocess.run(
        ["pandoc", str(input_path), "-f", "markdown", "-t", "rtf", "-o", str(output_path)],
        check=True,
        capture_output=True,
        text=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert Markdown documents to Rich Text Format (.rtf)."
    )
    parser.add_argument("input", type=Path, help="Path to input Markdown file")
    parser.add_argument("-o", "--output", type=Path, help="Path to output RTF file")
    args = parser.parse_args()

    input_path = args.input.resolve()
    if not input_path.exists() or not input_path.is_file():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        return 1

    if input_path.suffix.lower() not in MARKDOWN_EXTENSIONS:
        supported = sorted(MARKDOWN_EXTENSIONS)
        print(
            f"Unsupported input extension '{input_path.suffix.lower()}'. Supported: {supported}",
            file=sys.stderr,
        )
        return 1

    output_path = args.output.resolve() if args.output else input_path.with_suffix(".rtf")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        convert_markdown_to_rtf(input_path, output_path)
    except subprocess.CalledProcessError as exc:
        message = exc.stderr.strip() or str(exc)
        print(f"Conversion failed: {message}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"Conversion failed: {exc}", file=sys.stderr)
        return 1

    print(f"Generated rich text: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
