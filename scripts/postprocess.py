#!/usr/bin/env python3
"""Pós-processamento GENESIS-001: cama musical ambiente, SFX de vento, thumbnail e mux final.

Custo zero (ADR-016): todos os assets são gerados no projeto com ffmpeg livre,
sem áudio de terceiros (zero risco de licença). Tudo é rascunho interno (ADR-020).
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
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

CLEAN = Path("video/GENESIS-001/GENESIS-001_v02_clean.mp4")
CLEAN_SRT = Path("video/GENESIS-001/GENESIS-001_v02_clean.srt")
FINAL = Path("video/GENESIS-001/GENESIS-001_v02_final.mp4")
FINAL_SRT = Path("video/GENESIS-001/GENESIS-001_v02_final.srt")
MUSIC = Path("assets/music/GENESIS-001_music_bed_v01.m4a")
WIND = Path("assets/sfx/GENESIS-001_wind_desert_v01.m4a")
THUMB = Path("thumbnails/GENESIS-001_thumbnail_v01.png")
THUMB_SRC = Path("assets/generated/GENESIS-001/AI-ASSET-0001_creation-light_v01.png")

def run(cmd):
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if r.returncode != 0:
        print("FAILED:", " ".join(str(c) for c in cmd)[:180])
        print(r.stdout[-1600:])
        raise SystemExit(1)

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def music_bed():
    MUSIC.parent.mkdir(parents=True, exist_ok=True)
    dur = 360
    flt = (
        "[0:a]tremolo=f=0.10:d=0.25,volume=0.30[a0];"
        "[1:a]tremolo=f=0.13:d=0.30,volume=0.22[a1];"
        "[2:a]tremolo=f=0.11:d=0.20,volume=0.16[a2];"
        "[3:a]tremolo=f=0.12:d=0.25,volume=0.12[a3];"
        "[4:a]tremolo=f=0.17:d=0.35,volume=0.06[a4];"
        "[5:a]lowpass=f=400,volume=0.08[a5];"
        "[a0][a1][a2][a3][a4][a5]amix=inputs=6:duration=longest:normalize=0,"
        "aecho=0.8:0.88:1200:0.25,aecho=0.6:0.7:700:0.2,lowpass=f=1500,"
        "alimiter=limit=0.9,volume=0.7,"
        "afade=t=in:d=5,afade=t=out:st=353:d=7"
    )
    cmd = [FF, "-y",
        "-f", "lavfi", "-i", f"sine=frequency=55:duration={dur}",
        "-f", "lavfi", "-i", f"sine=frequency=110:duration={dur}",
        "-f", "lavfi", "-i", f"sine=frequency=164.81:duration={dur}",
        "-f", "lavfi", "-i", f"sine=frequency=220:duration={dur}",
        "-f", "lavfi", "-i", f"sine=frequency=329.63:duration={dur}",
        "-f", "lavfi", "-i", f"anoisesrc=color=pink:duration={dur}:amplitude=0.03",
        "-filter_complex", flt,
        "-c:a", "aac", "-b:a", "160k", str(MUSIC)]
    run(cmd)
    print("music bed:", MUSIC, sha(MUSIC))

def wind_sfx():
    WIND.parent.mkdir(parents=True, exist_ok=True)
    cmd = [FF, "-y",
        "-f", "lavfi", "-i", "anoisesrc=color=brown:duration=20:amplitude=0.6",
        "-af", "highpass=f=120,lowpass=f=700,tremolo=f=0.25:d=0.5,volume=0.6,afade=t=in:d=2,afade=t=out:st=16:d=3",
        "-c:a", "aac", "-b:a", "96k", str(WIND)]
    run(cmd)
    print("wind sfx:", WIND, sha(WIND))

def thumbnail():
    from PIL import Image, ImageDraw, ImageEnhance, ImageFont
    THUMB.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(THUMB_SRC).convert("RGBA")
    w, h = im.size
    scale = max(1280 / w, 720 / h)
    nw, nh = int(w * scale + 0.5), int(h * scale + 0.5)
    im = im.resize((nw, nh), Image.LANCZOS)
    left, top = (nw - 1280) // 2, (nh - 720) // 2
    im = im.crop((left, top, left + 1280, top + 720))
    im = ImageEnhance.Brightness(im).enhance(0.94)
    im = ImageEnhance.Contrast(im).enhance(1.06)
    im = ImageEnhance.Color(im).enhance(1.05)

    title_font = ImageFont.truetype(FONT, 108)
    sub_font = ImageFont.truetype(FONT, 52)
    draw = ImageDraw.Draw(im)

    def draw_centered(y, text, font, pad):
        bbox = draw.textbbox((0, 0), text, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        x = (1280 - tw) // 2
        draw.rectangle([x - pad, y - pad, x + tw + pad, y + th + pad], fill=(0, 0, 0, 100))
        draw.text((x - bbox[0], y - bbox[1]), text, font=font, fill=(255, 255, 255, 255))

    draw_centered(215, "GÊNESIS", title_font, 26)
    draw_centered(352, "Como Tudo Começou", sub_font, 14)
    im.convert("RGB").save(THUMB)
    print("thumbnail:", THUMB, sha(THUMB))

def scene_starts():
    rows = list(csv.DictReader(open("content/long/GENESIS-001/AUDIO_DRAFT_MANIFEST_v03.csv", encoding="utf-8")))
    starts, t = {}, 0.0
    for r in rows:
        n = int(r["segment_id"].split("-")[-1])
        starts[n] = t
        t += float(r["duration_seconds"])
    return starts

def mux():
    starts = scene_starts()
    wind_start = starts[7]
    probe = subprocess.run([FF, "-i", str(CLEAN)], stderr=subprocess.PIPE, text=True)
    m = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", probe.stderr)
    total = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    mus_out = total - 6
    flt = (
        "[0:a]anull[voice];"
        f"[1:a]volume=0.16,afade=t=in:d=5,afade=t=out:st={mus_out:.2f}:d=7[mus];"
        f"[2:a]adelay={int(wind_start*1000)},volume=0.09,afade=t=in:d=2,afade=t=out:st=16:d=3[wind];"
        "[voice][mus][wind]amix=inputs=3:duration=first:normalize=0,alimiter=limit=0.95[out]"
    )
    cmd = [FF, "-y", "-i", str(CLEAN), "-i", str(MUSIC), "-i", str(WIND),
           "-filter_complex", flt, "-map", "0:v", "-map", "[out]",
           "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", str(FINAL)]
    run(cmd)
    probe = subprocess.run([FF, "-i", str(FINAL)], stderr=subprocess.PIPE, text=True)
    m = re.search(r"Duration: (\d+:\d+:\d+\.\d+)", probe.stderr)
    print("final:", FINAL, "duration", m.group(1) if m else "?", sha(FINAL), os.path.getsize(FINAL))
    # copy captions alongside final
    FINAL_SRT.write_text(CLEAN_SRT.read_text(encoding="utf-8"), encoding="utf-8")
    print("captions:", FINAL_SRT)

if __name__ == "__main__":
    music_bed()
    wind_sfx()
    thumbnail()
    mux()
