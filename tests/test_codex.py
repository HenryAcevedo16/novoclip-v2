import json, stat, sys
import pytest
from pydantic import BaseModel
import pipeline as P


class R(BaseModel):
    titulo: str


def _fake(tmp_path, body, code=0, err=""):
    f = tmp_path / "codex"
    f.write_text(f"""#!{sys.executable}
import sys
a = sys.argv[1:]
sys.stdin.read()
if "-i" in a and {code!r} == 99:
    sys.stderr.write("unexpected argument -i"); sys.exit(2)
if {code!r} not in (0, 99):
    sys.stderr.write({err!r}); sys.exit({code!r})
open(a[a.index("-o") + 1], "w").write({body!r})
""", encoding="utf-8")
    f.chmod(f.stat().st_mode | stat.S_IEXEC)
    return str(f)


def test_codex_responde_y_se_elige(tmp_path, monkeypatch):
    monkeypatch.setenv("NOVOCLIP_CODEX_CLI", _fake(tmp_path, 'Claro: {"titulo": "hola"}'))
    monkeypatch.setattr(P, "_AI_PROVIDER", "codex")
    assert P.ai_backend() == "codex" and P.backend_name("codex").startswith("Codex")
    assert P._ask_codex("p", R).titulo == "hola"
    assert P.ai_sources_status()["codex"]["ok"]


def test_codex_sin_sesion_da_mensaje_claro(tmp_path, monkeypatch):
    monkeypatch.setenv("NOVOCLIP_CODEX_CLI", _fake(tmp_path, "", code=1, err="not logged in, please login"))
    with pytest.raises(RuntimeError, match="codex login"):
        P._ask_codex("p", R)


def test_codex_reintenta_sin_imagenes(tmp_path, monkeypatch):
    monkeypatch.setenv("NOVOCLIP_CODEX_CLI", _fake(tmp_path, '{"titulo": "ok"}', code=99))
    assert P._ask_codex("p", R, images=[("f", b"x")]).titulo == "ok"


def test_codex_no_instalado(monkeypatch):
    monkeypatch.delenv("NOVOCLIP_CODEX_CLI", raising=False)
    monkeypatch.setattr(P.shutil, "which", lambda n: None)
    monkeypatch.setattr(P, "_AI_PROVIDER", "codex")
    assert P.ai_backend() is None


def test_codex_modelo_por_rol_y_respaldo_sin_modelo(tmp_path, monkeypatch):
    f = tmp_path / "codex"
    f.write_text(f"""#!{sys.executable}
import sys
a = sys.argv[1:]
sys.stdin.read()
if "-m" in a and a[a.index("-m") + 1] == "gpt-5.6-terra" and "{tmp_path}/ok" not in a:
    sys.stderr.write("model not available"); sys.exit(1)
open(a[a.index("-o") + 1], "w").write('{{"titulo": "sin_m"}}')
""", encoding="utf-8")
    f.chmod(f.stat().st_mode | stat.S_IEXEC)
    monkeypatch.setenv("NOVOCLIP_CODEX_CLI", str(f))
    assert P._ask_codex("p", R, role="tech").titulo == "sin_m"      # terra falla -> repite sin -m
    assert P._ask_codex("p", R, role="copy").titulo == "sin_m"      # copy no usa -m
