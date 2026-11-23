import pipeline as P


def test_find_broll_prefiere_tu_carpeta(tmp_path, monkeypatch):
    mi = tmp_path / "mi_material"
    mi.mkdir()
    (mi / "sword_epic.jpg").write_bytes(b"x")
    monkeypatch.setattr(P, "BROLL_DIR", mi)
    assert P.find_broll("legendary Sword", tmp_path / "c").name == "sword_epic.jpg"
    assert P.find_broll("   ", tmp_path / "c") is None


def test_plan_broll_respeta_reglas_y_cache(tmp_path, monkeypatch):
    img = tmp_path / "a.jpg"
    img.write_bytes(b"x")
    monkeypatch.setattr(P, "ai_backend", lambda: "cli")
    monkeypatch.setattr(P, "find_broll", lambda q, c: img)
    calls = []

    def fake(pr, schema, opts, role=None, **k):
        calls.append(1)
        return schema(items=[dict(start=0.2, dur=2, query="a"), dict(start=3, dur=2, query="b"),
                             dict(start=4, dur=2, query="c"), dict(start=9, dur=2, query="d")])
    monkeypatch.setattr(P, "ask_claude", fake)
    words = [{"w": "hola", "s": i * 0.5, "e": i * 0.5 + 0.4} for i in range(30)]
    o = P.Options(use_ai=True, broll=True, broll_max=6)
    clip = P.Clip(index=1, start=0, end=15, title="t")
    r = P.plan_broll(words, 15.0, o, tmp_path / "br", clip)
    assert [round(x[1], 1) for x in r] == [1.5, 9.0]   # sin tapar el gancho ni solaparse
    assert all(x[1] >= 1.5 for x in r)
    P.plan_broll(words, 15.0, o, tmp_path / "br", clip)
    assert len(calls) == 1                                           # el plan se reutiliza
    assert P.plan_broll(words, 15.0, P.Options(use_ai=False), tmp_path / "br", clip) == []
