#!/usr/bin/env python3
"""Render GENESIS-001 draft v01: per-scene Ken Burns clips + concat + draft captions.

Free/open tooling (ffmpeg via imageio-ffmpeg) per ADR-016 (cost zero).
Produces:
  video/GENESIS-001/GENESIS-001_draft_v01.mp4
  video/GENESIS-001/GENESIS-001_draft_v01.srt
"""
from __future__ import annotations
import csv, hashlib, os, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)

def ffmpeg_exe() -> str:
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return "ffmpeg"

FF = ffmpeg_exe()
FPS = 30
W, H = 1920, 1080

MANIFEST = "content/long/GENESIS-001/AUDIO_DRAFT_MANIFEST_v03.csv"
SCRIPT = "scripts/long/GENESIS-001/SCRIPT_DRAFT.md"
IMG_DIR = Path("assets/generated/GENESIS-001")
TMP = Path("video/GENESIS-001/tmp")
OUT_DIR = Path("video/GENESIS-001")
OUT_VIDEO = OUT_DIR / "GENESIS-001_v02_clean.mp4"
OUT_SRT = OUT_DIR / "GENESIS-001_v02_clean.srt"

# scene -> image filename (primary). 13 and 19 are placeholders pending regeneration.
SCENE_IMAGE = {
 1: "AI-ASSET-0006_grain-egypt_v01.png",
 2: "AI-ASSET-0020_one-story_v01.png",
 3: "AI-ASSET-0001_creation-light_v01.png",
 4: "AI-ASSET-0007_garden-limit-revised_v01.png",
 5: "AI-ASSET-0008_garden-exile_v01.png",
 6: "AI-ASSET-0009_brothers-field_v01.png",
 7: "AI-ASSET-0003_storm-ark_v01.png",
 8: "AI-ASSET-0010_after-storm-covenant_v01.png",
 9: "AI-ASSET-0004_babel-city_v01.png",
 10: "AI-ASSET-0005_patriarch-journey_v01.png",
 11: "AI-ASSET-0021_tent-night-stars_v01.png",
 12: "AI-ASSET-0022_road-fork-dawn_v01.png",
 13: "AI-ASSET-0015_mountain-test-revised_v01.png",
 14: "AI-ASSET-0005_patriarch-journey_v01.png",
 15: "AI-ASSET-0012_jacob-night-river_v01.png",
 16: "AI-ASSET-0018_joseph-cistern-dry_v01.png",
 17: "AI-ASSET-0006_grain-egypt_v01.png",
 18: "AI-ASSET-0006_grain-egypt_v01.png",
 19: "AI-ASSET-0017_reconciliation-hall-revised_v01.png",
 20: "AI-ASSET-0005_patriarch-journey_v01.png",
 21: "AI-ASSET-0023_hands-food-night_v01.png",
 22: "AI-ASSET-0006_grain-egypt_v01.png",
}
PLACEHOLDERS = {}

def load_scenes():
    rows = list(csv.DictReader(open(MANIFEST, encoding="utf-8")))
    scenes = []
    for r in rows:
        scenes.append({
            "scene": int(r["segment_id"].split("-")[-1]),
            "audio": r["relative_path"],
            "duration": float(r["duration_seconds"]),
        })
    return scenes

def load_narration():
    text = open(SCRIPT, encoding="utf-8").read()
    parts = re.split(r"(?m)^## (SCN-GENESIS-001-\d\d)\b", text)
    out = {}
    for i in range(1, len(parts), 2):
        sid = parts[i]
        body = parts[i+1]
        m = re.search(r"-\s*\*\*Narração:\*\*\s*\n\s*>\s*(.*?)(?=\n- )", body, re.S)
        if m:
            nar = " ".join(l.strip() for l in m.group(1).splitlines() if l.strip())
            out[int(sid.split("-")[-1])] = re.sub(r"\s+", " ", nar).strip()
    return out

def run(cmd):
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if r.returncode != 0:
        print("CMD FAILED:", " ".join(cmd)[:200])
        print(r.stdout[-1500:])
        raise SystemExit(1)

def split_cues(text, maxlen=100):
    sents = re.split(r"(?<=[.!?]) +", text)
    cues, cur = [], ""
    for s in sents:
        if len(cur) + len(s) + 1 <= maxlen:
            cur = (cur + " " + s).strip()
        else:
            if cur: cues.append(cur)
            cur = s
    if cur: cues.append(cur)
    return cues

def srt_ts(t):
    ms = int(round(t*1000))
    h, rem = divmod(ms, 3600000); m, rem = divmod(rem, 60000); s, ms = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def main():
    TMP.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    scenes = load_scenes()
    narration = load_narration()

    # 1) per-scene clips
    clips = []
    for sc in scenes:
        n = sc["scene"]
        img = IMG_DIR / SCENE_IMAGE[n]
        if not img.exists():
            print(f"missing image for scene {n}: {img}")
            raise SystemExit(1)
        dur = sc["duration"]
        frames = int(round(dur * FPS)) + 5
        zoom = "min(1.0+0.0004*on,1.12)" if n % 2 == 1 else "max(1.12-0.0004*on,1.0)"
        vf = (f"scale={W}:{H}:force_original_aspect_ratio=increase,"
              f"crop={W}:{H},"
              f"zoompan=z='{zoom}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={W}x{H}:fps={FPS}")
        out = TMP / f"scene_{n:02d}.mp4"
        cmd = [FF, "-y", "-i", str(img), "-i", sc["audio"],
               "-filter_complex", f"[0:v]{vf},format=yuv420p[v]",
               "-map", "[v]", "-map", "1:a",
               "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
               "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
               "-t", f"{dur:.3f}", "-shortest", str(out)]
        run(cmd)
        clips.append(out)
        print(f"scene {n:02d} rendered ({dur:.2f}s)")

    # 2) concat
    lst = TMP / "concat.txt"
    with open(lst, "w") as fh:
        for c in clips:
            fh.write(f"file '{c.resolve()}'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(OUT_VIDEO)])
    print("concat done ->", OUT_VIDEO)

    # 3) captions (draft, auto-timed proportionally)
    srt, idx, t = [], 0, 0.0
    for sc in scenes:
        n = sc["scene"]
        txt = narration.get(n, "")
        dur = sc["duration"]
        cues = split_cues(txt) or [txt]
        total_chars = sum(len(c) for c in cues) or 1
        start = t
        for c in cues:
            cdur = dur * (len(c) / total_chars)
            idx += 1
            srt.append(f"{idx}\n{srt_ts(start)} --> {srt_ts(start+cdur)}\n{c}\n")
            start += cdur
        t += dur
    with open(OUT_SRT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(srt))
    print("captions ->", OUT_SRT, f"({idx} cues)")

    # 4) verify + hash
    probe = subprocess.run([FF, "-i", str(OUT_VIDEO)], stderr=subprocess.PIPE, text=True)
    m = re.search(r"Duration: (\d+:\d+:\d+\.\d+)", probe.stderr)
    print("video duration:", m.group(1) if m else "unknown")
    sha = hashlib.sha256(open(OUT_VIDEO, "rb").read()).hexdigest()
    print(f"sha256: {sha}")
    print(f"bytes: {os.path.getsize(OUT_VIDEO)}")
    print("placeholders used:", PLACEHOLDERS)

if __name__ == "__main__":
    main()
