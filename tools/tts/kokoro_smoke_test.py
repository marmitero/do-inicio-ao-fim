#!/usr/bin/env python3
"""Generate reproducible local Kokoro TTS audition clips, not final production audio.

Dependencies are intentionally optional and are not committed to the repository:
  pip install 'kokoro>=0.9.4' soundfile
The exact model files/voices must be downloaded from the official source, reviewed for
license, and recorded in the content TTS log before any final production use.
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text-file", type=Path, required=True, help="UTF-8 narration text file")
    parser.add_argument("--output-dir", type=Path, required=True, help="Ignored local output directory")
    parser.add_argument("--voices", nargs="+", default=["pm_alex", "pm_santa"])
    parser.add_argument("--language", default="p", help="Kokoro language code; p is pt-BR")
    parser.add_argument("--speed", type=float, default=0.95)
    parser.add_argument("--repo-id", default="hexgrad/Kokoro-82M")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        import numpy as np
        import soundfile as sf
        from kokoro import KPipeline
    except ImportError as exc:
        print(
            "Missing optional runtime dependency. Create an isolated environment and install "
            "kokoro plus soundfile; do not vendor them into this repository.",
            file=sys.stderr,
        )
        print(f"Import error: {exc}", file=sys.stderr)
        return 2

    text = args.text_file.read_text(encoding="utf-8").strip()
    if not text:
        print("Text file is empty.", file=sys.stderr)
        return 2
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pipeline = KPipeline(lang_code=args.language, repo_id=args.repo_id)

    for voice in args.voices:
        parts = [audio for _, _, audio in pipeline(text, voice=voice, speed=args.speed, split_pattern=r"\n+")]
        if not parts:
            print(f"No audio returned for voice {voice}.", file=sys.stderr)
            return 1
        merged = np.concatenate(parts)
        output = args.output_dir / f"kokoro_{voice}_smoke-test.wav"
        sf.write(output, merged, 24000)
        digest = hashlib.sha256(output.read_bytes()).hexdigest()
        duration = len(merged) / 24000
        print(f"voice={voice}")
        print(f"output={output}")
        print(f"duration_seconds={duration:.2f}")
        print(f"sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
