#!/usr/bin/env python3
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

PANDOC_EXTENSIONS = {
    ".docx",
    ".html",
    ".htm",
    ".epub",
    ".rtf",
    ".tex",
    ".txt",
    ".pptx",
    ".odt",
}


def require_binary(name: str) -> None:
    if shutil.which(name) is None:
        raise RuntimeError(f"Missing dependency: '{name}' is required.")


def convert_with_pandoc(input_path: Path, output_path: Path) -> None:
    require_binary("pandoc")
    subprocess.run(
        ["pandoc", str(input_path), "-t", "gfm", "-o", str(output_path)],
        check=True,
    )


def convert_pdf_to_markdown(input_path: Path, output_path: Path) -> None:
    require_binary("pdftotext")
    tmp_txt = output_path.with_suffix(".tmp.txt")
    try:
        subprocess.run(["pdftotext", str(input_path), str(tmp_txt)], check=True)
        content = tmp_txt.read_text(encoding="utf-8", errors="ignore")
        output_path.write_text(content.strip() + "\n", encoding="utf-8")
    finally:
        if tmp_txt.exists():
            tmp_txt.unlink()


def convert(input_path: Path, output_path: Path) -> None:
    ext = input_path.suffix.lower()

    if ext == ".md":
        output_path.write_text(
            input_path.read_text(encoding="utf-8", errors="ignore"),
            encoding="utf-8",
        )
        return

    if ext == ".pdf":
        convert_pdf_to_markdown(input_path, output_path)
        return

    if ext in PANDOC_EXTENSIONS:
        convert_with_pandoc(input_path, output_path)
        return

    supported = sorted(PANDOC_EXTENSIONS | {".pdf", ".md"})
    raise RuntimeError(
        f"Unsupported input extension '{ext}'. Supported: {supported}"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert documents to Markdown.")
    parser.add_argument("input", type=Path, help="Path to input document")
    parser.add_argument("-o", "--output", type=Path, help="Path to output Markdown file")
    args = parser.parse_args()

    input_path = args.input.resolve()
    if not input_path.exists() or not input_path.is_file():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        return 1

    output_path = args.output.resolve() if args.output else input_path.with_suffix(".md")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        convert(input_path, output_path)
    except Exception as exc:
        print(f"Conversion failed: {exc}", file=sys.stderr)
        return 1

    print(f"Generated Markdown: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
