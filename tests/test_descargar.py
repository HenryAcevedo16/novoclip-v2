from fastapi.testclient import TestClient
import app as A
import pipeline as P


def test_descargar_devuelve_mp4_y_limpia(tmp_path, monkeypatch):
    def fake(url, wd, opts, progress=None):
        wd.mkdir(parents=True, exist_ok=True)
        f = wd / "video.mp4"
        f.write_bytes(b"datos")
        return f, 'Mi short: "genial"/1'
    monkeypatch.setattr(P, "download_plain", fake)
    c = TestClient(A.app)
    r = c.post("/api/descargar", data={"url": "https://youtube.com/shorts/abc"})
    assert r.status_code == 200 and r.content == b"datos" and "mp4" in r.headers["content-disposition"]
    assert not list((A.JOBS_DIR / "_descargas").glob("*/video.mp4"))   # se borra al terminar


def test_descargar_valida_enlace_y_errores(monkeypatch):
    c = TestClient(A.app)
    assert c.post("/api/descargar", data={"url": "hola"}).status_code == 400
    def boom(*a, **k):
        raise RuntimeError("sign in to confirm you're not a bot")
    monkeypatch.setattr(P, "download_plain", boom)
    r = c.post("/api/descargar", data={"url": "https://youtu.be/x"})
    assert r.status_code == 502 and "bot" in r.json()["detail"]
