# Graph Report - novoclip-v2  (2026-11-22)

## Corpus Check
- 97 files · ~88,553 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 14 file(s) not represented in the graph (top: .bat 7, (none) 5, .example 1)

## Summary
- 1227 nodes · 2968 edges · 68 communities (50 shown, 18 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 41 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3e2ad71c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- app.py
- pipeline.py
- ask_claude
- Code map
- ClipEditor.tsx
- HomeFlow.tsx
- NovoClip ✂️ — tu propia app de clipping
- process
- Clip
- types.ts
- Api
- mock.ts
- create_job
- Options
- integraciones.py
- ProjectDetail.tsx
- Accounts.tsx
- package.json
- _job_age_ref
- pathlib
- extras.ts
- test_reglas.py
- novoclip
- compilerOptions
- server.py
- BrandKit.tsx
- AppShell.tsx
- gen_map.py
- json
- work
- process_live
- _job_dir
- TwitchChat
- AGENTS.md
- STATUS.md
- _QuietLog
- NovoClip · frontend
- mock-data.ts
- subprocess
- CLAUDE.md
- frontend/AGENTS.md
- fonts.d.ts
- novoclip_signals.py
- cn
- PROVENANCE.md
- iniciar_mac_linux.sh
- opus-worker.md
- Path
- test_integraciones.py
- optimize_clip
- CalendarView.tsx
- test_clip_editing.py
- Equipo de desarrollo IA de ClipForge
- hw_info
- sonnet-reviewer.md
- delete_job
- MockSwitcher.tsx
- _live_source
- _IgnoreWinReset
- label
- _no_cache_pages
- guia_ia.md

## God Nodes (most connected - your core abstractions)
1. `Code map` - 51 edges
2. `cn()` - 49 edges
3. `Options` - 46 edges
4. `NovoClip ✂️ — tu propia app de clipping` - 38 edges
5. `Api` - 37 edges
6. `process()` - 34 edges
7. `_render_clip_once()` - 33 edges
8. `optimize_clip()` - 32 edges
9. `process_live()` - 30 edges
10. `Button()` - 30 edges

## Surprising Connections (you probably didn't know these)
- `Start here (sesiÃ³n local nueva)` --references--> `yt_run()`  [INFERRED]
  docs/STATUS.md → pipeline.py
- `En la app` --references--> `gemini_key()`  [INFERRED]
  servidor_ia/LEEME.md → pipeline.py
- `IA incluida o clave propia (nuevo)` --references--> `gemini_key()`  [INFERRED]
  README.md → pipeline.py
- `hook()` --indirect_call--> `label()`  [INFERRED]
  pipeline.py → scripts/gen_map.py
- `test_rerender_inside_saved_piece_does_not_download()` --calls--> `rerender_clip()`  [EXTRACTED]
  tests/test_clip_editing.py → pipeline.py

## Import Cycles
- None detected.

## Communities (68 total, 18 thin omitted)

### Community 0 - "app.py"
Cohesion: 0.12
Nodes (13): _anunciar_version(), api_version(), classic(), clip_for_edit(), diagnostics(), gemini_models(), get_file(), get_integraciones() (+5 more)

### Community 1 - "pipeline.py"
Cohesion: 0.05
Nodes (37): analyze_framing(), apply_zoom(), _ass_color(), _avoid_box(), _blur_bg(), build_ass(), _cam_panel(), _clean_word() (+29 more)

### Community 2 - "ask_claude"
Cohesion: 0.07
Nodes (34): config(), settings(), ai_backend(), ai_mode(), _ai_note(), ai_source(), ai_sources_status(), anthropic_key() (+26 more)

### Community 3 - "Code map"
Cohesion: 0.04
Nodes (52): ./, .claude/, .claude/agents/, .claude/hooks/, .claude/skills/model-router/, .claude/skills/model-router/references/, .claude/skills/model-router/scripts/, .claude/skills/token-optimization/ (+44 more)

### Community 4 - "ClipEditor.tsx"
Cohesion: 0.13
Nodes (22): metadata, Page(), ClipEditor(), LAYOUTS, norm(), sec(), STYLE_LABEL, TOGGLE_DEFAULTS (+14 more)

### Community 5 - "HomeFlow.tsx"
Cohesion: 0.09
Nodes (26): Page(), AI_NAMES, DEFAULTS, fmtTime(), HomeFlow(), LAYOUT_OPTIONS, parseTime(), Settings (+18 more)

### Community 6 - "NovoClip ✂️ — tu propia app de clipping"
Cohesion: 0.04
Nodes (46): Actualizar en Windows, Ajuste automático según el equipo (nuevo), Archivos, 📷 Calidad de la webcam del streamer, 🎯 Clips con más sentido y notas más justas, Clips de directo editables, 🎯 Clips que terminan la idea, Consejos (+38 more)

### Community 7 - "process"
Cohesion: 0.12
Nodes (23): Cancelled, check_cancel(), describe_device(), download(), hook(), _ggml_model(), _is_bot_check(), low_res_warning() (+15 more)

### Community 8 - "Clip"
Cohesion: 0.24
Nodes (5): align_clip(), Clip, _cut_clip(), _keep_clip_source(), test_keep_clip_source_moves_file()

### Community 9 - "types.ts"
Cohesion: 0.09
Nodes (24): guard(), extras, realApi, request(), AiSource, ApiError, ClipEditData, ClipEdits (+16 more)

### Community 11 - "mock.ts"
Cohesion: 0.17
Nodes (14): config, SeedJob, Ev, extras, failIfModeError(), getMockMode(), K, latency() (+6 more)

### Community 12 - "create_job"
Cohesion: 0.19
Nodes (9): clip_optimize(), clip_rerender(), clip_revert(), _clip_task(), create_job(), create_preview(), _opts(), purge_expired() (+1 more)

### Community 13 - "Options"
Cohesion: 0.11
Nodes (20): _auto_keywords(), _best_hook(), complete_endings(), extend_to_sentence_end(), _line_energy(), _line_features(), _loudness_curve(), manual_clips() (+12 more)

### Community 14 - "integraciones.py"
Cohesion: 0.12
Nodes (11): _deepfilter_exe(), denoise_audio(), editly_spec(), kdenlive_xml(), refine_words(), status(), Integraciones opcionales, test_editly_spec_json() (+3 more)

### Community 15 - "ProjectDetail.tsx"
Cohesion: 0.13
Nodes (31): metadata, Page(), Inner(), Page(), metadata, Page(), Accounts(), RecentProjects() (+23 more)

### Community 16 - "Accounts.tsx"
Cohesion: 0.14
Nodes (20): NETWORKS, NetworkIcon(), FramingPreview(), clipText(), Net, NETS, svg, MAP (+12 more)

### Community 17 - "package.json"
Cohesion: 0.05
Nodes (50): dependencies, @fontsource/big-shoulders-display@^5.3.0, @fontsource-variable/bricolage-grotesque@^5.3.0, @fontsource-variable/figtree@^5.3.0, @fontsource-variable/manrope@^5.3.0, @heroui/react@^3.2.7, @heroui/styles@^3.2.7, @internationalized/date@^3.12.4 (+42 more)

### Community 20 - "pathlib"
Cohesion: 0.18
Nodes (8): cap(), current_section(), doc_map(), main(), milestone_id(), read(), render(), section()

### Community 21 - "extras.ts"
Cohesion: 0.18
Nodes (15): createExtras(), ExtrasCtx, K, load(), NET_LABEL, networkLabel(), seedAccounts(), seedTemplates() (+7 more)

### Community 22 - "test_reglas.py"
Cohesion: 0.08
Nodes (34): apply_glossary(), _hook_options(), load_rules(), pick(), run_tech(), _lines(), _norm(), read_glossary() (+26 more)

### Community 23 - "novoclip"
Cohesion: 0.22
Nodes (8): NOVOCLIP_WORKERS, build, environment, ports, restart, volumes, services, novoclip

### Community 24 - "compilerOptions"
Cohesion: 0.11
Nodes (18): compilerOptions, allowJs, esModuleInterop, incremental, isolatedModules, jsx, lib, module (+10 more)

### Community 25 - "server.py"
Cohesion: 0.18
Nodes (7): ai(), AIRequest, _db(), Img, _license(), license_status(), _used_today()

### Community 26 - "BrandKit.tsx"
Cohesion: 0.17
Nodes (21): metadata, Page(), blank(), BrandKit(), ColorField(), Group(), PreviewOf(), Soon() (+13 more)

### Community 27 - "AppShell.tsx"
Cohesion: 0.26
Nodes (8): metadata, RootLayout(), viewport, AppShell(), isActive(), NAV, LogoMark(), ToastProvider()

### Community 28 - "gen_map.py"
Cohesion: 0.16
Nodes (14): build_map(), clean(), _dash_summary(), Entry, _hash_summary(), list_files(), main(), markdown_sections() (+6 more)

### Community 29 - "json"
Cohesion: 0.24
Nodes (4): decide(), line_count(), main(), _manifest_summary()

### Community 30 - "work"
Cohesion: 0.23
Nodes (9): _cleanup_partial(), work(), work(), work(), _edit_gate(), _worker(), progress(), begin_job() (+1 more)

### Community 31 - "process_live"
Cohesion: 0.11
Nodes (16): main(), _clip_video_bytes(), _fmt_clock(), _frames_b64(), _kill_tree(), _live_keep_source(), process_live(), progress() (+8 more)

### Community 32 - "_job_dir"
Cohesion: 0.22
Nodes (9): _clip_by_index(), clip_delete(), clip_meta(), clip_project(), clip_subs(), _clip_subs(), get_zip(), _job_dir() (+1 more)

### Community 34 - "AGENTS.md"
Cohesion: 0.29
Nodes (5): Equipo de desarrollo, Mapa de documentos, Protocolo, Reglas de coste (siempre), Reglas de tokens y archivos

### Community 35 - "STATUS.md"
Cohesion: 0.40
Nodes (4): Notas de entorno, Preguntas abiertas para el dueÃ±o, Session log (newest first), Start here (sesiÃ³n local nueva)

### Community 37 - "NovoClip · frontend"
Cohesion: 0.40
Nodes (4): Cómo ejecutarlo, Datos simulados o reales, Estructura, NovoClip · frontend

### Community 38 - "mock-data.ts"
Cohesion: 0.17
Nodes (16): allJobs(), buildEvents(), ASSET_KEYS, assetFor(), CLIP_POOL, ClipSeed, extremeJobs(), makeClips() (+8 more)

### Community 40 - "CLAUDE.md"
Cohesion: 0.50
Nodes (3): Claude Code — equipo de cuatro roles, graphify, Orquestación inteligente (Opus · Sonnet · Haiku)

### Community 43 - "novoclip_signals.py"
Cohesion: 0.14
Nodes (7): audience_bonus(), overlap_ratio(), replay_intervals(), _valid_intervals(), AudienceBonusTests, OverlapRatioTests, ReplayIntervalsTests

### Community 44 - "cn"
Cohesion: 0.26
Nodes (16): ResultStep(), ResultThumb(), ClipCard(), clipText(), GRAV, isReview(), ReviewPanel(), TIPO (+8 more)

### Community 48 - "opus-worker.md"
Cohesion: 0.40
Nodes (4): Antes de planificar, Coordinación y cierre, Entregable de arquitectura, Principios específicos

### Community 51 - "Path"
Cohesion: 0.09
Nodes (18): _all_words(), _attach_replay_signals(), classify_video(), delete_clip(), _grab_jpeg(), _job_info(), _live_src(), load_clip_for_edit() (+10 more)

### Community 53 - "test_integraciones.py"
Cohesion: 0.18
Nodes (9): clip_words(), _lines(), subs_text(), _ts(), _no_pysubs2(), test_ass_fallback_wellformed(), test_clip_words_relative(), test_pysubs2_path_if_installed() (+1 more)

### Community 54 - "optimize_clip"
Cohesion: 0.14
Nodes (18): optimize_clip(), cut_text(), run_copy(), run_verify(), env(), roles(), set_review(), test_cli_model_error_falls_back_to_sonnet() (+10 more)

### Community 55 - "CalendarView.tsx"
Cohesion: 0.11
Nodes (43): metadata, Page(), NetworkChip(), CalendarView(), cap(), Cursor, dayLabel(), Dots() (+35 more)

### Community 56 - "test_clip_editing.py"
Cohesion: 0.16
Nodes (14): hook_of(), job(), mk_lines(), test_hook_cuts_at_question_and_prefers_strong_line(), test_hook_ignores_lines_after_25s(), test_hook_max_words_and_no_filler_edges(), test_hook_no_orphan_inverted_marks(), test_hook_single_word_not_empty_and_no_cta() (+6 more)

### Community 57 - "Equipo de desarrollo IA de ClipForge"
Cohesion: 0.29
Nodes (6): Equipo de desarrollo IA de ClipForge, Flujo recomendado, Política de modelos, Roles, Skills del proyecto, Skills externas opcionales para frontend

### Community 58 - "hw_info"
Cohesion: 0.18
Nodes (5): _add_nvidia_dll_dirs(), _encoder_test(), hw_info(), video_encoder(), _windows_gpus()

### Community 59 - "sonnet-reviewer.md"
Cohesion: 0.40
Nodes (4): Formato de salida, Revisión obligatoria, Riesgos específicos de vídeo, Riesgos específicos del frontend

### Community 60 - "delete_job"
Cohesion: 0.33
Nodes (3): cancel_job(), delete_job(), cancel_thread()

### Community 61 - "MockSwitcher.tsx"
Cohesion: 0.40
Nodes (5): MockSwitcher(), MODES, MockMode, USE_MOCK, writeString()

### Community 62 - "_live_source"
Cohesion: 0.09
Nodes (11): _cookie_methods(), _cookie_opts(), _cookie_opts_now(), fetch_captions(), _find_cookies_file(), _group_words(), is_live_url(), _live_source() (+3 more)

### Community 65 - "label"
Cohesion: 0.40
Nodes (3): fmt_tokens(), label(), size_label()

## Knowledge Gaps
- **18 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `gemini_key()` connect `ask_claude` to `pipeline.py`, `NovoClip ✂️ — tu propia app de clipping`?**
  _High betweenness centrality (0.037) - this node is a cross-community bridge._
- **Should `app.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12 - nodes in this community are weakly interconnected._
- **Why does `NovoClip ✂️ — tu propia app de clipping` connect `NovoClip ✂️ — tu propia app de clipping` to `integraciones.py`?**
  _High betweenness centrality (0.036) - this node is a cross-community bridge._
- **Should `pipeline.py` be split into smaller, more focused modules?**
  _Cohesion score 0.052403846153846155 - nodes in this community are weakly interconnected._
- **Why does `IA incluida o clave propia (nuevo)` connect `NovoClip ✂️ — tu propia app de clipping` to `ask_claude`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Should `ask_claude` be split into smaller, more focused modules?**
  _Cohesion score 0.0660377358490566 - nodes in this community are weakly interconnected._
- **Should `Code map` be split into smaller, more focused modules?**
  _Cohesion score 0.038461538461538464 - nodes in this community are weakly interconnected._