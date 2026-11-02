#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Minimal binary-safe implementation of cat for files and stdin."""
from __future__ import annotations
import argparse
import shutil
import sys
from pathlib import Path

def cat(paths: list[str], output=None, input_stream=None) -> int:
    output = output if output is not None else sys.stdout.buffer
    input_stream = input_stream if input_stream is not None else sys.stdin.buffer
    status = 0
    for path in paths or ["-"]:
        try:
            if path == "-":
                shutil.copyfileobj(input_stream, output)
            else:
                with Path(path).open("rb") as source:
                    shutil.copyfileobj(source, output)
        except (OSError, ValueError) as exc:
            print(f"cat: {path}: {exc}", file=sys.stderr)
            status = 1
    return status

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", help="Files to concatenate; - reads standard input")
    args = parser.parse_args()
    try:
        return cat(args.files)
    except BrokenPipeError:
        return 1

if __name__ == "__main__":
    sys.exit(main())
