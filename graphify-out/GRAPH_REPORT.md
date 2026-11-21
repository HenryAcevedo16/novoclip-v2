# Graph Report - clipforge  (2026-11-21)

## Corpus Check
- 96 files · ~87,722 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 14 file(s) not represented in the graph (top: .bat 7, (none) 5, .example 1)

## Summary
- 1220 nodes · 2953 edges · 64 communities (45 shown, 19 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 41 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `835751ad`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- app.py
- pipeline.py
- ask_claude
- Code map
- Settings.tsx
- HomeFlow.tsx
- NovoClip ✂️ — tu propia app de clipping
- Options
- Path
- types.ts
- Api
- mock.ts
- create_job
- select_heuristic
- integraciones.py
- ProjectDetail.tsx
- ClipEditor.tsx
- package.json
- _job_age_ref
- start.py
- extras.ts
- test_reglas.py
- novoclip
- compilerOptions
- server.py
- BrandKit.tsx
- layout.tsx
- gen_map.py
- guard_read.py
- work
- process_live
- _job_dir
- TwitchChat
- AGENTS.md
- Status
- _QuietLog
- NovoClip · frontend
- mock-data.ts
- json
- CLAUDE.md
- frontend/AGENTS.md
- fonts.d.ts
- novoclip_signals.py
- cn
- PROVENANCE.md
- iniciar_mac_linux.sh
- opus-worker.md
- optimize_clip
- Cancelled
- optimize_clip
- time.ts
- test_clip_editing.py
- Equipo de desarrollo IA de ClipForge
- sonnet-reviewer.md
- Servidor de IA de NovoClip (IA incluida)
- is_live_url
- _IgnoreWinReset
- guia_ia.md

## God Nodes (most connected - your core abstractions)
1. `Code map` - 51 edges
2. `cn()` - 49 edges
3. `Options` - 45 edges
4. `NovoClip ✂️ — tu propia app de clipping` - 38 edges
5. `Api` - 37 edges
6. `process()` - 34 edges
7. `_render_clip_once()` - 32 edges
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
- `Integraciones opcionales` --references--> `refine_words()`  [INFERRED]
  README.md → integraciones.py
- `hook()` --indirect_call--> `label()`  [INFERRED]
  pipeline.py → scripts/gen_map.py

## Import Cycles
- None detected.

## Communities (64 total, 19 thin omitted)

### Community 0 - "app.py"
Cohesion: 0.12
Nodes (15): _anunciar_version(), api_version(), classic(), _clip_by_index(), clip_for_edit(), clip_project(), clip_subs(), _clip_subs() (+7 more)

### Community 1 - "pipeline.py"
Cohesion: 0.05
Nodes (33): analyze_framing(), apply_zoom(), _ass_color(), _attach_replay_signals(), _avoid_box(), _blur_bg(), build_ass(), _cam_panel() (+25 more)

### Community 2 - "ask_claude"
Cohesion: 0.07
Nodes (33): config(), settings(), ai_backend(), ai_mode(), _ai_note(), ai_source(), ai_sources_status(), anthropic_key() (+25 more)

### Community 3 - "Code map"
Cohesion: 0.04
Nodes (52): ./, .claude/, .claude/agents/, .claude/hooks/, .claude/skills/model-router/, .claude/skills/model-router/references/, .claude/skills/model-router/scripts/, .claude/skills/token-optimization/ (+44 more)

### Community 4 - "Settings.tsx"
Cohesion: 0.18
Nodes (14): metadata, Page(), ClipEditor(), norm(), sec(), AI_LABEL, AI_SUB, DIAG_ICON (+6 more)

### Community 5 - "HomeFlow.tsx"
Cohesion: 0.09
Nodes (26): Page(), AI_NAMES, DEFAULTS, fmtTime(), HomeFlow(), LAYOUT_OPTIONS, parseTime(), Settings (+18 more)

### Community 6 - "NovoClip ✂️ — tu propia app de clipping"
Cohesion: 0.04
Nodes (46): Actualizar en Windows, Ajuste automático según el equipo (nuevo), Archivos, 📷 Calidad de la webcam del streamer, 🎯 Clips con más sentido y notas más justas, Clips de directo editables, 🎯 Clips que terminan la idea, Consejos (+38 more)

### Community 7 - "Options"
Cohesion: 0.09
Nodes (26): align_clip(), _cookie_methods(), _cookie_opts(), _cookie_opts_now(), describe_device(), download(), hook(), fetch_captions() (+18 more)

### Community 8 - "Path"
Cohesion: 0.08
Nodes (22): _all_words(), classify_video(), Clip, _clip_video_bytes(), _cut_clip(), _filter_path(), _frames_b64(), _grab_jpeg() (+14 more)

### Community 9 - "types.ts"
Cohesion: 0.09
Nodes (23): guard(), extras, realApi, request(), AiSource, ApiError, ClipEditData, ClipEdits (+15 more)

### Community 11 - "mock.ts"
Cohesion: 0.17
Nodes (14): config, SeedJob, Ev, extras, failIfModeError(), getMockMode(), K, latency() (+6 more)

### Community 12 - "create_job"
Cohesion: 0.13
Nodes (12): cancel_job(), clip_optimize(), clip_rerender(), clip_revert(), _clip_task(), create_job(), create_preview(), delete_job() (+4 more)

### Community 13 - "select_heuristic"
Cohesion: 0.11
Nodes (16): _auto_keywords(), _best_hook(), complete_endings(), extend_to_sentence_end(), _line_energy(), _line_features(), manual_clips(), _norm() (+8 more)

### Community 14 - "integraciones.py"
Cohesion: 0.09
Nodes (20): clip_words(), _deepfilter_exe(), denoise_audio(), editly_spec(), kdenlive_xml(), _lines(), refine_words(), status() (+12 more)

### Community 15 - "ProjectDetail.tsx"
Cohesion: 0.13
Nodes (32): metadata, Page(), Inner(), Page(), metadata, Page(), Accounts(), RecentProjects() (+24 more)

### Community 16 - "ClipEditor.tsx"
Cohesion: 0.11
Nodes (25): NETWORKS, NetworkIcon(), FramingPreview(), LAYOUTS, STYLE_LABEL, TOGGLE_DEFAULTS, TOGGLE_LABELS, Tool (+17 more)

### Community 17 - "package.json"
Cohesion: 0.05
Nodes (50): dependencies, @fontsource/big-shoulders-display@^5.3.0, @fontsource-variable/bricolage-grotesque@^5.3.0, @fontsource-variable/figtree@^5.3.0, @fontsource-variable/manrope@^5.3.0, @heroui/react@^3.2.7, @heroui/styles@^3.2.7, @internationalized/date@^3.12.4 (+42 more)

### Community 19 - "_job_age_ref"
Cohesion: 0.25
Nodes (4): get_job(), _job_age_ref(), _job_from_disk(), list_projects()

### Community 20 - "start.py"
Cohesion: 0.23
Nodes (8): cap(), current_section(), doc_map(), main(), milestone_id(), read(), render(), section()

### Community 21 - "extras.ts"
Cohesion: 0.17
Nodes (16): blank(), createExtras(), ExtrasCtx, K, load(), NET_LABEL, networkLabel(), seedAccounts() (+8 more)

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
Nodes (7): ai(), AIRequest, _db(), Img, _license(), license_status(), _used_today()

### Community 26 - "BrandKit.tsx"
Cohesion: 0.14
Nodes (24): metadata, Page(), BrandKit(), ColorField(), Group(), PreviewOf(), Soon(), ClipPreview() (+16 more)

### Community 27 - "layout.tsx"
Cohesion: 0.18
Nodes (12): metadata, RootLayout(), viewport, AppShell(), isActive(), NAV, LogoMark(), MockSwitcher() (+4 more)

### Community 28 - "gen_map.py"
Cohesion: 0.12
Nodes (17): build_map(), clean(), _dash_summary(), Entry, fmt_tokens(), _hash_summary(), list_files(), main() (+9 more)

### Community 29 - "guard_read.py"
Cohesion: 0.20
Nodes (4): decide(), line_count(), main(), main()

### Community 30 - "work"
Cohesion: 0.23
Nodes (9): _cleanup_partial(), work(), work(), work(), _edit_gate(), _worker(), progress(), begin_job() (+1 more)

### Community 31 - "process_live"
Cohesion: 0.08
Nodes (20): _add_nvidia_dll_dirs(), check_cancel(), _encoder_test(), _fmt_clock(), _ggml_model(), hw_info(), _kill_tree(), _live_source() (+12 more)

### Community 32 - "_job_dir"
Cohesion: 0.24
Nodes (5): clip_delete(), clip_meta(), _job_dir(), _no_cache_pages(), _refresh_result()

### Community 34 - "AGENTS.md"
Cohesion: 0.29
Nodes (5): Equipo de desarrollo, Mapa de documentos, Protocolo, Reglas de coste (siempre), Reglas de tokens y archivos

### Community 35 - "Status"
Cohesion: 0.40
Nodes (4): Notas de entorno, Preguntas abiertas para el dueÃ±o, Session log (newest first), Start here (sesiÃ³n local nueva)

### Community 37 - "NovoClip · frontend"
Cohesion: 0.40
Nodes (4): Cómo ejecutarlo, Datos simulados o reales, Estructura, NovoClip · frontend

### Community 38 - "mock-data.ts"
Cohesion: 0.17
Nodes (16): allJobs(), buildEvents(), ASSET_KEYS, assetFor(), CLIP_POOL, ClipSeed, extremeJobs(), makeClips() (+8 more)

### Community 43 - "novoclip_signals.py"
Cohesion: 0.13
Nodes (7): audience_bonus(), overlap_ratio(), replay_intervals(), _valid_intervals(), AudienceBonusTests, OverlapRatioTests, ReplayIntervalsTests

### Community 44 - "cn"
Cohesion: 0.24
Nodes (17): ScheduleDialog(), ResultStep(), ResultThumb(), ClipCard(), clipText(), GRAV, isReview(), ReviewPanel() (+9 more)

### Community 48 - "opus-worker.md"
Cohesion: 0.40
Nodes (4): Antes de planificar, Coordinación y cierre, Entregable de arquitectura, Principios específicos

### Community 51 - "optimize_clip"
Cohesion: 0.12
Nodes (15): _group_words(), _job_info(), _live_src(), load_clip_for_edit(), _local_video(), norm_provider(), optimize_clip(), cut_text() (+7 more)

### Community 54 - "optimize_clip"
Cohesion: 0.18
Nodes (13): env(), roles(), set_review(), test_gemini_backend_ignores_roles_and_skips_verify(), test_happy_path_order_and_one_call_each(), test_invalid_cut_keeps_original_and_does_not_call_opus_for_it(), test_invalid_cut_twice_says_so_in_notes(), test_no_technical_problems_skips_sonnet() (+5 more)

### Community 55 - "time.ts"
Cohesion: 0.12
Nodes (42): metadata, Page(), NetworkChip(), CalendarView(), cap(), Cursor, dayLabel(), Dots() (+34 more)

### Community 56 - "test_clip_editing.py"
Cohesion: 0.16
Nodes (14): hook_of(), job(), mk_lines(), test_hook_cuts_at_question_and_prefers_strong_line(), test_hook_ignores_lines_after_25s(), test_hook_max_words_and_no_filler_edges(), test_hook_no_orphan_inverted_marks(), test_hook_single_word_not_empty_and_no_cta() (+6 more)

### Community 57 - "Equipo de desarrollo IA de ClipForge"
Cohesion: 0.29
Nodes (6): Equipo de desarrollo IA de ClipForge, Flujo recomendado, Política de modelos, Roles, Skills del proyecto, Skills externas opcionales para frontend

### Community 59 - "sonnet-reviewer.md"
Cohesion: 0.40
Nodes (4): Formato de salida, Revisión obligatoria, Riesgos específicos de vídeo, Riesgos específicos del frontend

### Community 61 - "Servidor de IA de NovoClip (IA incluida)"
Cohesion: 0.40
Nodes (4): Arrancarlo, En la app, Licencias, Servidor de IA de NovoClip (IA incluida)

## Knowledge Gaps
- **19 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `NovoClip ✂️ — tu propia app de clipping` connect `NovoClip ✂️ — tu propia app de clipping` to `integraciones.py`?**
  _High betweenness centrality (0.064) - this node is a cross-community bridge._
- **Should `app.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11904761904761904 - nodes in this community are weakly interconnected._
- **Why does `gemini_key()` connect `ask_claude` to `pipeline.py`, `Servidor de IA de NovoClip (IA incluida)`, `NovoClip ✂️ — tu propia app de clipping`?**
  _High betweenness centrality (0.056) - this node is a cross-community bridge._
- **Should `pipeline.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05202661826981246 - nodes in this community are weakly interconnected._
- **Why does `IA incluida o clave propia (nuevo)` connect `NovoClip ✂️ — tu propia app de clipping` to `ask_claude`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Should `ask_claude` be split into smaller, more focused modules?**
  _Cohesion score 0.06787330316742081 - nodes in this community are weakly interconnected._
- **Should `Code map` be split into smaller, more focused modules?**
  _Cohesion score 0.038461538461538464 - nodes in this community are weakly interconnected._