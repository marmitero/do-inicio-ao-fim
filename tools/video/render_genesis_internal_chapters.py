#!/usr/bin/env python3
"""Render four internal-only GENESIS-001 chapter animatics from tracked manifests.

This tool intentionally creates a review artifact, not a final publishable video. It
uses a slow Ken Burns movement over registered illustration candidates and keeps the
story order defined in SCRIPT_DRAFT.md. The source audio is grouped in the same ten
segments as AUDIO_DRAFT_MANIFEST_v02.csv, so scene changes inside one spoken segment
are proportional to the approved planning durations, not sample-accurate edit marks.

Requirements:
  * FFmpeg with libx264 and AAC support. Supply its path via FFMPEG_BIN when it is
    not installed in PATH.
  * Internal Arena draft audio and locally generated image candidates must exist.

All output is intentionally written under video/, which is ignored by Git.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FPS = 24
WIDTH = 1280
HEIGHT = 720

# (scene ID, candidate image relative path, estimated narrative seconds). The order
# must mirror the canonical script; a repeated visual is deliberate and documented
# in the chapter assembly manifest.
CHAPTERS = [
    (
        "CH01_ORIGENS_E_O_JARDIM",
        "Origens e o jardim",
        [
            ("01", "AI-ASSET-0023_grain-egypt-replacement_v01.png", 25),
            ("02", "AI-ASSET-0024_patriarch-journey-replacement_v01.png", 25),
            ("03", "AI-ASSET-0025_creation-light-replacement_v01.png", 30),
            ("04", "AI-ASSET-0026_garden-limit-replacement_v01.png", 40),
        ],
        ["01", "02"],
    ),
    (
        "CH02_RUPTURA_RECOMECOS_E_BABEL",
        "Ruptura, recomeços e Babel",
        [
            ("05", "AI-ASSET-0027_post-exile-replacement_v01.png", 35),
            ("06", "AI-ASSET-0009_brothers-field_v01.png", 30),
            ("07", "AI-ASSET-0003_storm-ark_v01.png", 35),
            ("08", "AI-ASSET-0010_after-storm-covenant_v01.png", 40),
        ],
        ["03", "04"],
    ),
    (
        "CH03_PROMESSA_E_A_CASA_DE_JACO",
        "A promessa e a casa de Jacó",
        [
            ("09", "AI-ASSET-0004_babel-city_v01.png", 30),
            ("10", "AI-ASSET-0024_patriarch-journey-replacement_v01.png", 35),
            ("11", "AI-ASSET-0019_promise-night-tent_v01.png", 45),
            ("12", "AI-ASSET-0020_valley-fork-tent-dawn_v01.png", 30),
            ("13", "AI-ASSET-0015_mountain-test-revised_v01.png", 45),
            ("14", "AI-ASSET-0021_jacob-dream-light_v01.png", 40),
            ("15", "AI-ASSET-0012_jacob-night-river_v01.png", 30),
        ],
        ["05", "06", "07"],
    ),
    (
        "CH04_JOSE_E_A_PROMESSA_ABERTA",
        "José e a promessa aberta",
        [
            ("16", "AI-ASSET-0018_joseph-dry-cistern_v01.png", 45),
            ("17", "AI-ASSET-0023_grain-egypt-replacement_v01.png", 35),
            ("18", "AI-ASSET-0017_reconciliation-hall-revised_v01.png", 40),
            ("19", "AI-ASSET-0017_reconciliation-hall-revised_v01.png", 45),
            ("20", "AI-ASSET-0024_patriarch-journey-replacement_v01.png", 30),
            ("21", "AI-ASSET-0022_family-provision-still-life_v01.png", 20),
            ("22", "AI-ASSET-0019_promise-night-tent_v01.png", 20),
        ],
        ["08", "09", "10"],
    ),
]

AUDIO_DIRECTORY = ROOT / "audio/GENESIS-001/internal-chapter-draft"
IMAGE_DIRECTORY = ROOT / "assets/generated/GENESIS-001"
OUTPUT_DIRECTORY = ROOT / "video/GENESIS-001/internal-chapter-draft"


def ffmpeg_path() -> str:
    configured = os.environ.get("FFMPEG_BIN")
    if configured:
        candidate = Path(configured)
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return str(candidate)
        raise RuntimeError(f"FFMPEG_BIN is not an executable file: {configured}")
    discovered = shutil.which("ffmpeg")
    if discovered:
        return discovered
    raise RuntimeError(
        "FFmpeg was not found. Install it outside this repository or set FFMPEG_BIN."
    )


def audio_duration_seconds(ffmpeg: str, path: Path) -> float:
    result = subprocess.run(
        [ffmpeg, "-hide_banner", "-i", str(path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    match = re.search(r"Duration: (\d+):(\d+):(\d+(?:\.\d+)?)", result.stderr)
    if not match:
        raise RuntimeError(f"Could not read duration from {path}: {result.stderr[-500:]}")
    hours, minutes, seconds = match.groups()
    return int(hours) * 3600 + int(minutes) * 60 + float(seconds)


def assets_for_audio_segments(scenes: list[tuple[str, str, int]], audio_segments: list[str], durations: list[float]):
    """Assign planning-duration-weighted visual time to each spoken segment."""
    # Scene count encoded by the known historical ten audio segments.
    scenes_per_segment = {
        "01": 2, "02": 2, "03": 2, "04": 2, "05": 2,
        "06": 2, "07": 3, "08": 2, "09": 3, "10": 2,
    }
    planned = []
    cursor = 0
    for segment, audio_duration in zip(audio_segments, durations):
        count = scenes_per_segment[segment]
        group = scenes[cursor:cursor + count]
        if len(group) != count:
            raise RuntimeError(f"Scene/audio grouping mismatch at segment {segment}")
        cursor += count
        planned_total = sum(scene[2] for scene in group)
        for scene_id, image_name, planned_seconds in group:
            allocated = audio_duration * planned_seconds / planned_total
            planned.append((scene_id, IMAGE_DIRECTORY / image_name, allocated))
    if cursor != len(scenes):
        raise RuntimeError("Not all scenes were assigned to a spoken segment")
    return planned


def render_chapter(ffmpeg: str, chapter) -> Path:
    slug, _title, scenes, audio_segment_ids = chapter
    # Segment scene labels retain direct traceability in the ignored filenames.
    known_audio_names = {
        "01": "GENESIS-001_SEG-01_SCN-01-02_voice-00_internal.mp3",
        "02": "GENESIS-001_SEG-02_SCN-03-04_voice-00_internal.mp3",
        "03": "GENESIS-001_SEG-03_SCN-05-06_voice-00_internal.mp3",
        "04": "GENESIS-001_SEG-04_SCN-07-08_voice-00_internal.mp3",
        "05": "GENESIS-001_SEG-05_SCN-09-10_voice-00_internal.mp3",
        "06": "GENESIS-001_SEG-06_SCN-11-12_voice-00_internal.mp3",
        "07": "GENESIS-001_SEG-07_SCN-13-15_voice-00_internal.mp3",
        "08": "GENESIS-001_SEG-08_SCN-16-17_voice-00_internal.mp3",
        "09": "GENESIS-001_SEG-09_SCN-18-20_voice-00_internal.mp3",
        "10": "GENESIS-001_SEG-10_SCN-21-22_voice-00_internal.mp3",
    }
    audio_paths = [AUDIO_DIRECTORY / known_audio_names[segment] for segment in audio_segment_ids]
    missing = [str(path.relative_to(ROOT)) for path in audio_paths if not path.is_file()]
    if missing:
        raise RuntimeError("Missing internal audio: " + ", ".join(missing))

    audio_durations = [audio_duration_seconds(ffmpeg, path) for path in audio_paths]
    visual_items = assets_for_audio_segments(scenes, audio_segment_ids, audio_durations)
    missing_images = [str(path.relative_to(ROOT)) for _, path, _ in visual_items if not path.is_file()]
    if missing_images:
        raise RuntimeError("Missing registered image candidates: " + ", ".join(missing_images))

    command = [ffmpeg, "-y", "-hide_banner"]
    # One looping video input per scene followed by the spoken segment inputs.
    for _scene_id, image_path, duration in visual_items:
        command += ["-loop", "1", "-framerate", str(FPS), "-t", f"{duration:.6f}", "-i", str(image_path)]
    for audio_path in audio_paths:
        command += ["-i", str(audio_path)]

    visual_filters = []
    for index, (_scene_id, _image_path, duration) in enumerate(visual_items):
        # The modest pan/zoom is an animatic movement, never a claim of camera footage.
        visual_filters.append(
            f"[{index}:v]scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=increase,"
            f"crop={WIDTH}:{HEIGHT},"
            f"zoompan=z='min(zoom+0.00042,1.075)':"
            f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={WIDTH}x{HEIGHT}:fps={FPS},"
            f"setsar=1,format=yuv420p,fade=t=in:st=0:d=0.25,"
            f"fade=t=out:st={max(0, duration - 0.25):.6f}:d=0.25[v{index}]"
        )
    visual_labels = "".join(f"[v{i}]" for i in range(len(visual_items)))
    visual_filters.append(f"{visual_labels}concat=n={len(visual_items)}:v=1:a=0[vout]")
    first_audio_index = len(visual_items)
    audio_labels = "".join(f"[{first_audio_index + i}:a]" for i in range(len(audio_paths)))
    visual_filters.append(f"{audio_labels}concat=n={len(audio_paths)}:v=0:a=1[aout]")

    output = OUTPUT_DIRECTORY / f"GENESIS-001_{slug}_INTERNAL_DRAFT.mp4"
    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    command += [
        "-filter_complex", ";".join(visual_filters),
        "-map", "[vout]", "-map", "[aout]",
        "-c:v", "libx264", "-preset", "medium", "-crf", "22",
        "-pix_fmt", "yuv420p", "-r", str(FPS),
        "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart",
        "-metadata", "title=GENESIS-001 internal chapter draft",
        "-metadata", "comment=INTERNAL REVIEW ONLY. Arena-origin media may not be used commercially or published without a separate rights review.",
        str(output),
    ]
    print(f"Rendering {slug}: {len(visual_items)} visual beats, {sum(audio_durations):.3f}s")
    subprocess.run(command, check=True)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--chapter",
        action="append",
        choices=[chapter[0] for chapter in CHAPTERS],
        help="Render only this chapter slug. Repeat to render several chapters.",
    )
    args = parser.parse_args()
    selected = [chapter for chapter in CHAPTERS if not args.chapter or chapter[0] in args.chapter]
    try:
        ffmpeg = ffmpeg_path()
        print(f"Using FFmpeg: {ffmpeg}")
        outputs = [render_chapter(ffmpeg, chapter) for chapter in selected]
    except (RuntimeError, subprocess.CalledProcessError) as error:
        print(f"Render failed: {error}", file=sys.stderr)
        return 1
    print("Rendered internal review chapters:")
    for output in outputs:
        print(output.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
