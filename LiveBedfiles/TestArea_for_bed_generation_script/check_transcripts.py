#!/usr/bin/env python3
"""Verify that every transcript ID appears somewhere in the BED output (any column)."""
from __future__ import annotations

import argparse
from pathlib import Path


def load_lines(path: Path) -> list[str]:
    if not path.is_file():
        raise FileNotFoundError(f"{path} does not exist")
    return [line.rstrip("\n") for line in path.read_text().splitlines() if line.strip()]


def find_missing_transcripts(transcripts: list[str], bed_path: Path) -> list[str]:
    if not bed_path.is_file():
        raise FileNotFoundError(f"{bed_path} does not exist")
    bed_text = bed_path.read_text()
    return [tid for tid in transcripts if tid not in bed_text]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check that every line in transcripts appears in out.bed."
    )
    parser.add_argument(
        "--transcripts",
        default="transcripts.txt",
        type=Path,
        help="Path to transcripts.txt (default: %(default)s)",
    )
    parser.add_argument(
        "--bed",
        default="out.bed",
        type=Path,
        help="Path to out.bed (default: %(default)s)",
    )
    args = parser.parse_args()

    transcripts = load_lines(args.transcripts)
    missing = find_missing_transcripts(transcripts, args.bed)

    if missing:
        print("Missing lines:")
        for line in missing:
            print(line)
        exit(1)

    print("All transcript lines are present in bed file.")


if __name__ == "__main__":
    main()
