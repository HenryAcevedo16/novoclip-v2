import shutil, subprocess
from pathlib import Path
import pytest
import pipeline as P


def test_outro_len_y_evento_ass(tmp_path):
    o = P.Options(outro_text="Sígueme @canal", outro_secs=99)
    assert P.outro_len(o) == 4.0 and P.outro_len(P.Options()) == 0.0
    ass = tmp_path / "a.ass"
    P.build_ass([], P.Clip(index=1, start=0, end=4, title="t"), o, 1080, 1920, "track", ass, outro_at=4.0)
    assert "0:00:04.00,0:00:08.00" in ass.read_text(encoding="utf-8") and "SÍGUEME" in ass.read_text(encoding="utf-8").upper()
    P.build_ass([], P.Clip(index=1, start=0, end=4, title="t"), P.Options(), 1080, 1920, "track", ass, outro_at=4.0)
    assert "Dialogue: 2," not in ass.read_text(encoding="utf-8")


@pytest.mark.skipif(not shutil.which("ffmpeg"), reason="sin ffmpeg")
def test_render_con_tarjeta_alarga_el_clip(tmp_path):
    src = tmp_path / "s.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "testsrc=duration=2:size=540x960:rate=30",
                    "-f", "lavfi", "-i", "sine=f=440:duration=2", "-shortest", "-c:v", "libx264", "-c:a", "aac", str(src)], check=True)
    tr = {"segments": [{"start": 0, "end": 1.5, "text": "hola", "words": [{"w": "hola", "s": 0.2, "e": 0.6}]}], "language": "es"}
    o = P.Options(device="cpu", zoom=False, music=False, jumpcuts=False, outro_text="FIN", outro_secs=1.0)
    (tmp_path / "o").mkdir()
    r = P.render_clip(src, P.Clip(index=1, start=0.0, end=2.0, title="t"), tr, o, tmp_path / "o", P.probe(src))
    assert abs(r.out_duration - 3.0) < 0.1
