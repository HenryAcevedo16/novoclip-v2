"""Integraciones OPCIONALES de NovoClip. Todo falla en silencio si falta la dependencia.

- Subtítulos .srt/.ass por clip (pysubs2 si está; si no, escritor propio).
- Afinado de palabras con stable-ts (stable_whisper).
- Limpieza de audio: DeepFilterNet si está; si no, el filtro FFmpeg `afftdn`.
- Proyecto de editor: .kdenlive/.mlt (XML MLT) y spec JSON de Editly.
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
from pathlib import Path
from typing import Optional
from xml.etree import ElementTree as ET

AFFTDN = "afftdn=nr=12:nf=-30"   # sin dependencias: viene con FFmpeg


def _deepfilter_exe() -> Optional[str]:
    return shutil.which("deep-filter") or shutil.which("deepFilter")


def status() -> dict:
    """Qué hay instalado (para la API y los interruptores de la interfaz)."""
    have = lambda m: importlib.util.find_spec(m) is not None  # noqa: E731
    return {
        "pysubs2": have("pysubs2"),
        "stable_ts": have("stable_whisper"),
        "deepfilternet": bool(_deepfilter_exe()),
        "denoise_ffmpeg": True,   # afftdn siempre disponible como alternativa
    }


# ------------------------------- subtítulos -------------------------------
def clip_words(workdir: Path, clip: dict) -> list:
    """Palabras del clip con tiempos RELATIVOS al inicio (edit/NN.json guarda tiempos absolutos)."""
    f = Path(workdir) / "edit" / f"{int(clip['index']):02d}.json"
    if not f.exists():
        return []
    a, b = float(clip["start"]), float(clip["end"])
    out = []
    for w in json.loads(f.read_text(encoding="utf-8")):
        if a <= w["s"] < b:
            out.append({"w": w["w"], "s": round(w["s"] - a, 3), "e": round(min(w["e"], b) - a, 3)})
    return out


def _lines(words: list, per_line: int = 3) -> list:
    per_line = max(1, int(per_line))
    return [(g[0]["s"], max(g[-1]["e"], g[0]["s"] + 0.05), " ".join(x["w"] for x in g))
            for g in (words[i:i + per_line] for i in range(0, len(words), per_line))]


def _ts(t: float, ass: bool) -> str:
    cs = int(round(max(t, 0) * 100))
    h, r = divmod(cs, 360000)
    m, r = divmod(r, 6000)
    s, c = divmod(r, 100)
    return f"{h}:{m:02d}:{s:02d}.{c:02d}" if ass else f"{h:02d}:{m:02d}:{s:02d},{c * 10:03d}"


def subs_text(words: list, fmt: str = "srt", per_line: int = 3, size: tuple = (1080, 1920)) -> str:
    fmt = "ass" if fmt == "ass" else "srt"
    lines = _lines(words, per_line)
    try:
        import pysubs2
        subs = pysubs2.SSAFile()
        subs.info["PlayResX"], subs.info["PlayResY"] = str(size[0]), str(size[1])
        for s, e, t in lines:
            subs.append(pysubs2.SSAEvent(start=int(round(s * 1000)), end=int(round(e * 1000)), text=t))
        return subs.to_string(fmt)
    except Exception:
        pass    # sin pysubs2 (o falló): escritor propio
    if fmt == "srt":
        return "".join(f"{i}\n{_ts(s, False)} --> {_ts(e, False)}\n{t}\n\n" for i, (s, e, t) in enumerate(lines, 1))
    head = ("[Script Info]\nScriptType: v4.00+\nPlayResX: %d\nPlayResY: %d\n\n[V4+ Styles]\n"
            "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, "
            "Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, "
            "MarginR, MarginV, Encoding\nStyle: Default,Arial,64,&H00FFFFFF,&H000000FF,&H00000000,&H64000000,1,0,0,0,"
            "100,100,0,0,1,4,1,2,40,40,200,1\n\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, "
            "MarginV, Effect, Text\n") % size
    return head + "".join(f"Dialogue: 0,{_ts(s, True)},{_ts(e, True)},Default,,0,0,0,,{t}\n" for s, e, t in lines)


# ------------------------------- proyecto de editor -------------------------------
def probe(mp4: Path) -> tuple:
    """(ancho, alto, fps) del clip con ffprobe; si no hay, 1080x1920 a 30."""
    try:
        o = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                            "stream=width,height,r_frame_rate", "-of", "json", str(mp4)],
                           capture_output=True, text=True, timeout=15).stdout
        s = json.loads(o)["streams"][0]
        n, d = s["r_frame_rate"].split("/")
        return int(s["width"]), int(s["height"]), float(n) / float(d)
    except Exception:
        return 1080, 1920, 30.0


def kdenlive_xml(mp4: Path, duration: float, size: tuple = (1080, 1920), fps: float = 30.0,
                 subs: Optional[Path] = None) -> str:
    """XML MLT mínimo (abre en Kdenlive y Shotcut): el mp4 del clip y, si hay, sus subtítulos."""
    w, h = size
    fr = int(round(fps * 1000)), 1000
    frames = max(1, int(round(duration * fps)))
    mlt = ET.Element("mlt", {"LC_NUMERIC": "C", "version": "7.0.0"})
    ET.SubElement(mlt, "profile", {"description": "NovoClip", "width": str(w), "height": str(h), "progressive": "1",
                                   "sample_aspect_num": "1", "sample_aspect_den": "1", "display_aspect_num": str(w),
                                   "display_aspect_den": str(h), "frame_rate_num": str(fr[0]),
                                   "frame_rate_den": str(fr[1]), "colorspace": "709"})
    prod = ET.SubElement(mlt, "producer", {"id": "clip", "in": "0", "out": str(frames - 1)})
    ET.SubElement(prod, "property", {"name": "resource"}).text = str(mp4)
    ET.SubElement(prod, "property", {"name": "mlt_service"}).text = "avformat"
    pl = ET.SubElement(mlt, "playlist", {"id": "playlist0"})
    ET.SubElement(pl, "entry", {"producer": "clip", "in": "0", "out": str(frames - 1)})
    tr = ET.SubElement(mlt, "tractor", {"id": "tractor0", "in": "0", "out": str(frames - 1)})
    ET.SubElement(tr, "track", {"producer": "playlist0"})
    if subs:
        f = ET.SubElement(tr, "filter", {"mlt_service": "avfilter.subtitles"})
        ET.SubElement(f, "property", {"name": "av.filename"}).text = str(subs)
    ET.indent(mlt)
    return '<?xml version="1.0" encoding="utf-8"?>\n' + ET.tostring(mlt, encoding="unicode")


def editly_spec(mp4: Path, title: str, duration: float, size: tuple = (1080, 1920), fps: float = 30.0) -> dict:
    return {"outPath": str(mp4.with_name(mp4.stem + "_editly.mp4")), "width": size[0], "height": size[1],
            "fps": round(fps, 3), "defaults": {"transition": None},
            "clips": [{"duration": round(duration, 3),
                       "layers": [{"type": "video", "path": str(mp4)},
                                  {"type": "title", "text": title or mp4.stem}]}]}


# ------------------------------- audio y palabras -------------------------------
def denoise_audio(media: Path, tmpdir: Path) -> Optional[Path]:
    """Audio limpio con DeepFilterNet (wav); None si no está instalado o falla -> se usa afftdn."""
    exe = _deepfilter_exe()
    if not exe:
        return None
    try:
        src, out = Path(tmpdir) / "in.wav", Path(tmpdir) / "out"
        out.mkdir(parents=True, exist_ok=True)
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(media), "-vn", "-ar", "48000", "-ac", "1", str(src)],
                       check=True, timeout=300)
        subprocess.run([exe, "-o", str(out), str(src)], check=True, capture_output=True, timeout=600)
        return next(iter(sorted(out.glob("*.wav"))), None)
    except Exception:
        return None


def refine_words(tr: dict, audio: Path, model: str = "base") -> dict:
    """Afina tiempos por palabra con stable-ts. Si falta o falla (o no cuadran las palabras), devuelve `tr` igual."""
    try:
        import stable_whisper
        words = [w for s in tr["segments"] for w in s.get("words", [])]
        if not words:
            return tr
        m = stable_whisper.load_faster_whisper(model if model != "auto" else "base")
        res = m.align(str(audio), " ".join(w["w"] for w in words), language=tr.get("language") or "es")
        new = [w for s in res.segments for w in s.words]
        if len(new) != len(words):      # alineación distinta: mejor los tiempos originales
            return tr
        for w, n in zip(words, new):
            w["s"], w["e"] = round(float(n.start), 3), round(float(n.end), 3)
        return tr
    except Exception:
        return tr
