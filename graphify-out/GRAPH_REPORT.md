# Graph Report - novoclip-v2  (2026-11-23)

## Corpus Check
- 100 files · ~91,294 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 14 file(s) not represented in the graph (top: .bat 7, (none) 5, .example 1)

## Summary
- 1268 nodes · 3044 edges · 69 communities (49 shown, 20 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 44 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `40f6ed4c`
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
- Options
- optimize_clip
- types.ts
- Api
- mock.ts
- create_job
- Options
- integraciones.py
- ProjectDetail.tsx
- Button
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
- _sp_run
- _job_dir
- TwitchChat
- AGENTS.md
- STATUS.md
- _QuietLog
- NovoClip · frontend
- mock-data.ts
- test_codex.py
- CLAUDE.md
- frontend/AGENTS.md
- fonts.d.ts
- novoclip_signals.py
- cn
- PROVENANCE.md
- iniciar_mac_linux.sh
- opus-worker.md
- Path
- _clip_task
- optimize_clip
- CalendarView.tsx
- test_clip_editing.py
- Equipo de desarrollo IA de ClipForge
- Servidor de IA de NovoClip (IA incluida)
- sonnet-reviewer.md
- subprocess
- MockSwitcher.tsx
- _live_source
- _IgnoreWinReset
- test_descargar.py
- _no_cache_pages
- test_broll.py
- guia_ia.md

## God Nodes (most connected - your core abstractions)
1. `Code map` - 51 edges
2. `Options` - 49 edges
3. `cn()` - 49 edges
4. `NovoClip ✂️ — tu propia app de clipping` - 40 edges
5. `Api` - 38 edges
6. `_render_clip_once()` - 34 edges
7. `process()` - 34 edges
8. `optimize_clip()` - 32 edges
9. `process_live()` - 30 edges
10. `Button()` - 30 edges

## Surprising Connections (you probably didn't know these)
- `Start here (sesiÃ³n local nueva)` --references--> `yt_run()`  [INFERRED]
  docs/STATUS.md → pipeline.py
- `En la app` --references--> `gemini_key()`  [INFERRED]
  servidor_ia/LEEME.md → pipeline.py
- `hook()` --indirect_call--> `label()`  [INFERRED]
  pipeline.py → scripts/gen_map.py
- `IA incluida o clave propia (nuevo)` --references--> `gemini_key()`  [INFERRED]
  README.md → pipeline.py
- `test_rerender_inside_saved_piece_does_not_download()` --calls--> `rerender_clip()`  [EXTRACTED]
  tests/test_clip_editing.py → pipeline.py

## Import Cycles
- None detected.

## Communities (69 total, 20 thin omitted)

### Community 0 - "app.py"
Cohesion: 0.12
Nodes (12): _anunciar_version(), api_version(), classic(), diagnostics(), gemini_models(), get_file(), get_integraciones(), get_job() (+4 more)

### Community 1 - "pipeline.py"
Cohesion: 0.06
Nodes (31): analyze_framing(), apply_zoom(), _ass_color(), _blur_bg(), build_ass(), _cam_panel(), _clean_word(), _cluster_people() (+23 more)

### Community 2 - "ask_claude"
Cohesion: 0.06
Nodes (38): config(), ai_backend(), ai_mode(), _ai_note(), ai_source(), ai_sources_status(), anthropic_key(), ask_claude() (+30 more)

### Community 3 - "Code map"
Cohesion: 0.04
Nodes (52): ./, .claude/, .claude/agents/, .claude/hooks/, .claude/skills/model-router/, .claude/skills/model-router/references/, .claude/skills/model-router/scripts/, .claude/skills/token-optimization/ (+44 more)

### Community 4 - "ClipEditor.tsx"
Cohesion: 0.10
Nodes (25): metadata, Page(), ClipEditor(), LAYOUTS, norm(), sec(), STYLE_LABEL, TOGGLE_DEFAULTS (+17 more)

### Community 5 - "HomeFlow.tsx"
Cohesion: 0.11
Nodes (22): Page(), AI_NAMES, DEFAULTS, fmtTime(), HomeFlow(), LAYOUT_OPTIONS, parseTime(), ResultStep() (+14 more)

### Community 6 - "NovoClip ✂️ — tu propia app de clipping"
Cohesion: 0.04
Nodes (47): Actualizar en Windows, Ajuste automático según el equipo (nuevo), Archivos, 📷 Calidad de la webcam del streamer, 🎯 Clips con más sentido y notas más justas, Clips de directo editables, 🎯 Clips que terminan la idea, Codex (ChatGPT) como IA (+39 more)

### Community 7 - "Options"
Cohesion: 0.10
Nodes (26): main(), Cancelled, check_cancel(), describe_device(), download(), hook(), download_plain(), _ggml_model() (+18 more)

### Community 8 - "optimize_clip"
Cohesion: 0.11
Nodes (16): fetch_captions(), _group_words(), _job_info(), _live_src(), load_clip_for_edit(), _local_video(), norm_provider(), optimize_clip() (+8 more)

### Community 9 - "types.ts"
Cohesion: 0.09
Nodes (23): guard(), extras, realApi, request(), AiSource, ApiError, ClipEditData, ClipEdits (+15 more)

### Community 11 - "mock.ts"
Cohesion: 0.15
Nodes (20): allJobs(), buildEvents(), config, extremeJobs(), makeClips(), makeResult(), NOW(), seedJobs() (+12 more)

### Community 12 - "create_job"
Cohesion: 0.15
Nodes (9): clip_rerender(), create_job(), create_preview(), delete_job(), descargar(), _opts(), purge_expired(), _purge_loop() (+1 more)

### Community 13 - "Options"
Cohesion: 0.11
Nodes (17): _auto_keywords(), _best_hook(), complete_endings(), extend_to_sentence_end(), _line_energy(), _line_features(), _loudness_curve(), manual_clips() (+9 more)

### Community 14 - "integraciones.py"
Cohesion: 0.09
Nodes (20): clip_words(), _deepfilter_exe(), denoise_audio(), editly_spec(), kdenlive_xml(), _lines(), refine_words(), status() (+12 more)

### Community 15 - "ProjectDetail.tsx"
Cohesion: 0.13
Nodes (33): metadata, Page(), Inner(), Page(), metadata, Page(), Accounts(), NETWORKS (+25 more)

### Community 16 - "Button"
Cohesion: 0.15
Nodes (18): PostDialog(), ScheduleDialog(), FramingPreview(), ResultThumb(), clipText(), Net, NETS, PublishDialog() (+10 more)

### Community 17 - "package.json"
Cohesion: 0.05
Nodes (50): dependencies, @fontsource/big-shoulders-display@^5.3.0, @fontsource-variable/bricolage-grotesque@^5.3.0, @fontsource-variable/figtree@^5.3.0, @fontsource-variable/manrope@^5.3.0, @heroui/react@^3.2.7, @heroui/styles@^3.2.7, @internationalized/date@^3.12.4 (+42 more)

### Community 20 - "pathlib"
Cohesion: 0.18
Nodes (8): cap(), current_section(), doc_map(), main(), milestone_id(), read(), render(), section()

### Community 21 - "extras.ts"
Cohesion: 0.16
Nodes (18): createExtras(), ExtrasCtx, K, load(), NET_LABEL, networkLabel(), seedAccounts(), seedPosts() (+10 more)

### Community 22 - "test_reglas.py"
Cohesion: 0.08
Nodes (33): apply_glossary(), _hook_options(), load_rules(), pick(), _lines(), _norm(), read_glossary(), read_guide() (+25 more)

### Community 23 - "novoclip"
Cohesion: 0.22
Nodes (8): NOVOCLIP_WORKERS, build, environment, ports, restart, volumes, services, novoclip

### Community 24 - "compilerOptions"
Cohesion: 0.11
Nodes (18): compilerOptions, allowJs, esModuleInterop, incremental, isolatedModules, jsx, lib, module (+10 more)

### Community 25 - "server.py"
Cohesion: 0.18
Nodes (8): ai(), AIRequest, _db(), Img, _license(), license_status(), _used_today(), R

### Community 26 - "BrandKit.tsx"
Cohesion: 0.16
Nodes (23): metadata, Page(), blank(), BrandKit(), ColorField(), Group(), PreviewOf(), Soon() (+15 more)

### Community 27 - "AppShell.tsx"
Cohesion: 0.26
Nodes (8): metadata, RootLayout(), viewport, AppShell(), isActive(), NAV, LogoMark(), ToastProvider()

### Community 28 - "gen_map.py"
Cohesion: 0.12
Nodes (17): build_map(), clean(), _dash_summary(), Entry, fmt_tokens(), _hash_summary(), list_files(), main() (+9 more)

### Community 29 - "json"
Cohesion: 0.24
Nodes (4): decide(), line_count(), main(), _manifest_summary()

### Community 30 - "work"
Cohesion: 0.23
Nodes (9): _cleanup_partial(), work(), work(), work(), _edit_gate(), _worker(), progress(), begin_job() (+1 more)

### Community 31 - "_sp_run"
Cohesion: 0.08
Nodes (18): _add_nvidia_dll_dirs(), _clip_video_bytes(), _encoder_test(), _fmt_clock(), _frames_b64(), hw_info(), _kill_tree(), _live_keep_source() (+10 more)

### Community 32 - "_job_dir"
Cohesion: 0.20
Nodes (10): _clip_by_index(), clip_delete(), clip_for_edit(), clip_meta(), clip_project(), clip_subs(), _clip_subs(), get_zip() (+2 more)

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
Cohesion: 0.18
Nodes (10): ASSET_KEYS, assetFor(), CLIP_POOL, ClipSeed, SeedJob, StoredJob, ClipResult, Job (+2 more)

### Community 39 - "test_codex.py"
Cohesion: 0.27
Nodes (4): _fake(), test_codex_reintenta_sin_imagenes(), test_codex_responde_y_se_elige(), test_codex_sin_sesion_da_mensaje_claro()

### Community 40 - "CLAUDE.md"
Cohesion: 0.50
Nodes (3): Claude Code — equipo de cuatro roles, graphify, Orquestación inteligente (Opus · Sonnet · Haiku)

### Community 43 - "novoclip_signals.py"
Cohesion: 0.13
Nodes (7): audience_bonus(), overlap_ratio(), replay_intervals(), _valid_intervals(), AudienceBonusTests, OverlapRatioTests, ReplayIntervalsTests

### Community 44 - "cn"
Cohesion: 0.16
Nodes (18): HOME_STEPS, Stepper(), ClipCard(), clipText(), GRAV, isReview(), ReviewPanel(), TIPO (+10 more)

### Community 48 - "opus-worker.md"
Cohesion: 0.40
Nodes (4): Antes de planificar, Coordinación y cierre, Entregable de arquitectura, Principios específicos

### Community 51 - "Path"
Cohesion: 0.07
Nodes (25): align_clip(), _all_words(), _attach_replay_signals(), _avoid_box(), classify_video(), Clip, _cut_clip(), delete_clip() (+17 more)

### Community 53 - "_clip_task"
Cohesion: 0.20
Nodes (6): cancel_job(), clip_optimize(), clip_revert(), _clip_task(), settings(), cancel_thread()

### Community 54 - "optimize_clip"
Cohesion: 0.18
Nodes (13): env(), roles(), set_review(), test_gemini_backend_ignores_roles_and_skips_verify(), test_happy_path_order_and_one_call_each(), test_invalid_cut_keeps_original_and_does_not_call_opus_for_it(), test_invalid_cut_twice_says_so_in_notes(), test_no_technical_problems_skips_sonnet() (+5 more)

### Community 55 - "CalendarView.tsx"
Cohesion: 0.12
Nodes (38): metadata, Page(), NetworkChip(), CalendarView(), cap(), Cursor, dayLabel(), Dots() (+30 more)

### Community 56 - "test_clip_editing.py"
Cohesion: 0.16
Nodes (14): hook_of(), job(), mk_lines(), test_hook_cuts_at_question_and_prefers_strong_line(), test_hook_ignores_lines_after_25s(), test_hook_max_words_and_no_filler_edges(), test_hook_no_orphan_inverted_marks(), test_hook_single_word_not_empty_and_no_cta() (+6 more)

### Community 57 - "Equipo de desarrollo IA de ClipForge"
Cohesion: 0.29
Nodes (6): Equipo de desarrollo IA de ClipForge, Flujo recomendado, Política de modelos, Roles, Skills del proyecto, Skills externas opcionales para frontend

### Community 58 - "Servidor de IA de NovoClip (IA incluida)"
Cohesion: 0.40
Nodes (4): Arrancarlo, En la app, Licencias, Servidor de IA de NovoClip (IA incluida)

### Community 59 - "sonnet-reviewer.md"
Cohesion: 0.40
Nodes (4): Formato de salida, Revisión obligatoria, Riesgos específicos de vídeo, Riesgos específicos del frontend

### Community 61 - "MockSwitcher.tsx"
Cohesion: 0.40
Nodes (5): MockSwitcher(), MODES, MockMode, USE_MOCK, writeString()

### Community 62 - "_live_source"
Cohesion: 0.13
Nodes (7): _cookie_methods(), _cookie_opts(), _cookie_opts_now(), _find_cookies_file(), _live_source(), platform_of(), _tiktok_live_api()

## Knowledge Gaps
- **20 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `gemini_key()` connect `ask_claude` to `pipeline.py`, `Servidor de IA de NovoClip (IA incluida)`?**
  _High betweenness centrality (0.037) - this node is a cross-community bridge._
- **Should `app.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11692307692307692 - nodes in this community are weakly interconnected._
- **Why does `NovoClip ✂️ — tu propia app de clipping` connect `NovoClip ✂️ — tu propia app de clipping` to `ask_claude`, `integraciones.py`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Should `pipeline.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05723905723905724 - nodes in this community are weakly interconnected._
- **Why does `IA incluida o clave propia (nuevo)` connect `ask_claude` to `NovoClip ✂️ — tu propia app de clipping`?**
  _High betweenness centrality (0.028) - this node is a cross-community bridge._
- **Should `ask_claude` be split into smaller, more focused modules?**
  _Cohesion score 0.05786090005844535 - nodes in this community are weakly interconnected._
- **Should `Code map` be split into smaller, more focused modules?**
  _Cohesion score 0.038461538461538464 - nodes in this community are weakly interconnected._