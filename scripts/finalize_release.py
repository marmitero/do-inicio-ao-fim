#!/usr/bin/env python3
"""Finalização de release do GENESIS-001: narração + música ambiente (~10%) + vento,
SEM legenda queimada. O proprietário insere a legenda por conta própria depois.

Custo zero (ADR-016): reutiliza a música e o vento já gerados no projeto (sem
áudio de terceiros). Termos Arena aprovados (ADR-023); publicação manual.
"""
from __future__ import annotations
import csv, hashlib, os, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)

def ff() -> str:
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return "ffmpeg"

FF = ff()
CLEAN = Path("video/GENESIS-001/GENESIS-001_v04_clean.mp4")
MUSIC = Path("assets/music/GENESIS-001_music_bed_v01.m4a")
WIND = Path("assets/sfx/GENESIS-001_wind_desert_v01.m4a")
FINAL = Path("video/GENESIS-001/GENESIS-001_final.mp4")
MUSIC_VOL = 0.10   # ~10%, para não sobrepor a voz

def run(cmd):
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if r.returncode != 0:
        print("FAILED:", " ".join(str(c) for c in cmd)[:180])
        print(r.stdout[-1600:])
        raise SystemExit(1)

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def scene_starts():
    rows = list(csv.DictReader(open("content/long/GENESIS-001/AUDIO_DRAFT_MANIFEST_v03.csv", encoding="utf-8")))
    starts, t = {}, 0.0
    for r in rows:
        starts[int(r["segment_id"].split("-")[-1])] = t
        t += float(r["duration_seconds"])
    return starts, t

def main():
    starts, total = scene_starts()
    wind_start = starts[7]
    mus_out = total - 6
    flt = (
        "[0:a]anull[voice];"
        f"[1:a]volume={MUSIC_VOL},afade=t=in:d=5,afade=t=out:st={mus_out:.2f}:d=7[mus];"
        f"[2:a]adelay={int(wind_start*1000)},volume=0.09,afade=t=in:d=2,afade=t=out:st=16:d=3[wind];"
        "[voice][mus][wind]amix=inputs=3:duration=first:normalize=0,alimiter=limit=0.95[out]"
    )
    cmd = [FF, "-y", "-i", str(CLEAN), "-i", str(MUSIC), "-i", str(WIND),
           "-filter_complex", flt, "-map", "0:v", "-map", "[out]",
           "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", str(FINAL)]
    run(cmd)
    probe = subprocess.run([FF, "-i", str(FINAL)], stderr=subprocess.PIPE, text=True)
    m = re.search(r"Duration: (\d+:\d+:\d+\.\d+)", probe.stderr)
    print("final:", FINAL)
    print("  duration:", m.group(1) if m else "unknown")
    print("  sha256:", sha(FINAL))
    print("  bytes:", os.path.getsize(FINAL))

if __name__ == "__main__":
    main()
