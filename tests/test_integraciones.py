"""Integraciones opcionales: subtítulos, proyecto de editor, fallbacks sin dependencias."""
import json
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from io import BytesIO
from pathlib import Path

import pytest

import integraciones as ig

CLIP = {"index": 1, "start": 100.0, "end": 104.0, "file": "01_demo.mp4", "title": "Demo", "duration": 4.0}
WORDS = [{"w": w, "s": 100.0 + i * 0.5, "e": 100.0 + i * 0.5 + 0.4} for i, w in enumerate("uno dos tres cuatro cinco seis".split())]
WORDS = [{"w": "antes", "s": 98.0, "e": 98.4}] + WORDS + [{"w": "despues", "s": 110.0, "e": 110.4}]


@pytest.fixture
def job(tmp_path):
    (tmp_path / "edit").mkdir()
    (tmp_path / "edit" / "01.json").write_text(json.dumps(WORDS), encoding="utf-8")
    return tmp_path


def test_clip_words_relative(job):
    w = ig.clip_words(job, CLIP)
    assert [x["w"] for x in w] == "uno dos tres cuatro cinco seis".split()
    assert w[0]["s"] == 0.0 and w[1]["s"] == 0.5


def _no_pysubs2(monkeypatch):
    monkeypatch.setitem(sys.modules, "pysubs2", None)   # import -> ImportError


def test_srt_fallback_wellformed(job, monkeypatch):
    _no_pysubs2(monkeypatch)
    srt = ig.subs_text(ig.clip_words(job, CLIP), "srt", 3)
    blocks = srt.strip().split("\n\n")
    assert len(blocks) == 2
    assert blocks[0].splitlines()[0] == "1"
    assert re.fullmatch(r"00:00:00,000 --> 00:00:01,400", blocks[0].splitlines()[1])
    assert blocks[0].splitlines()[2] == "uno dos tres"
    assert "00:00:01,500 --> 00:00:02,900" in blocks[1]   # relativo al inicio del clip


def test_ass_fallback_wellformed(job, monkeypatch):
    _no_pysubs2(monkeypatch)
    ass = ig.subs_text(ig.clip_words(job, CLIP), "ass", 3)
    for sec in ("[Script Info]", "[V4+ Styles]", "[Events]"):
        assert sec in ass
    d = [l for l in ass.splitlines() if l.startswith("Dialogue:")]
    assert len(d) == 2 and d[0].startswith("Dialogue: 0,0:00:00.00,0:00:01.40,Default")
    assert d[0].endswith(",uno dos tres")


def test_pysubs2_path_if_installed(job):
    pytest.importorskip("pysubs2")
    srt = ig.subs_text(ig.clip_words(job, CLIP), "srt", 3)
    assert "00:00:00,000 --> 00:00:01,400" in srt and "uno dos tres" in srt


def test_kdenlive_xml_parses():
    x = ig.kdenlive_xml(Path("/x/01_demo.mp4"), 4.0, (1080, 1920), 30.0, Path("/x/01_demo.ass"))
    root = ET.fromstring(x.split("?>", 1)[1])
    assert root.tag == "mlt"
    assert root.find("profile").get("width") == "1080"
    assert root.find("producer/property[@name='resource']").text == "/x/01_demo.mp4"
    assert root.find("producer").get("out") == "119"
    assert root.find("tractor/filter/property[@name='av.filename']").text == "/x/01_demo.ass"
    assert ET.fromstring(ig.kdenlive_xml(Path("a.mp4"), 1.0)).find("tractor/filter") is None


def test_editly_spec_json():
    s = json.loads(json.dumps(ig.editly_spec(Path("/x/01_demo.mp4"), "Demo", 4.0, (1080, 1920), 30.0)))
    layers = s["clips"][0]["layers"]
    assert layers[0] == {"type": "video", "path": "/x/01_demo.mp4"}
    assert layers[1] == {"type": "title", "text": "Demo"} and s["width"] == 1080


def test_status_and_denoise_fallback(monkeypatch, tmp_path):
    monkeypatch.setattr(ig, "_deepfilter_exe", lambda: None)
    st = ig.status()
    assert st["deepfilternet"] is False and st["denoise_ffmpeg"] is True
    assert ig.denoise_audio(tmp_path / "a.mp4", tmp_path / "dn") is None   # -> el render usa afftdn
    assert ig.AFFTDN.startswith("afftdn")


def test_refine_words_silent_without_stable_ts(monkeypatch):
    monkeypatch.setitem(sys.modules, "stable_whisper", None)
    tr = {"language": "es", "segments": [{"words": [{"w": "hola", "s": 0.1, "e": 0.5}]}]}
    before = json.dumps(tr)
    assert json.dumps(ig.refine_words(tr, Path("x.wav"))) == before


def test_endpoints_and_zip(job, monkeypatch, tmp_path):
    pytest.importorskip("fastapi.testclient")
    import app as appmod
    from fastapi.testclient import TestClient
    jd = tmp_path / "jobs"
    wd = jd / "abc"
    (wd / "edit").mkdir(parents=True)
    (wd / "clips").mkdir()
    (wd / "edit" / "01.json").write_text(json.dumps(WORDS), encoding="utf-8")
    (wd / "clips" / "01_demo.mp4").write_bytes(b"x")
    (wd / "result.json").write_text(json.dumps({"clips": [CLIP]}), encoding="utf-8")
    monkeypatch.setattr(appmod, "JOBS_DIR", jd)
    c = TestClient(appmod.app)
    assert c.get("/api/integraciones").json()["denoise_ffmpeg"] is True
    assert "uno dos tres" in c.get("/api/jobs/abc/clips/1/subs?fmt=srt").text
    assert "[Events]" in c.get("/api/jobs/abc/clips/1/subs?fmt=ass").text
    assert c.get("/api/jobs/abc/clips/1/subs?fmt=vtt").status_code == 400
    assert c.get("/api/jobs/abc/clips/9/subs").status_code == 404
    ET.fromstring(c.get("/api/jobs/abc/clips/1/project?fmt=kdenlive").text.split("?>", 1)[1])
    assert json.loads(c.get("/api/jobs/abc/clips/1/project?fmt=editly").text)["clips"]
    z = zipfile.ZipFile(BytesIO(c.get("/api/jobs/abc/zip").content))
    assert "01_demo.srt" in z.namelist() and "01_demo.mp4" in z.namelist()
