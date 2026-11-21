@AGENTS.md

## Claude Code — equipo de cuatro roles

- Para trabajo no trivial, usa Opus como coordinador/arquitecto: entiende el objetivo, fija criterios de aceptación y divide el trabajo. En Desktop selecciona Opus para la sesión de coordinación; en terminal puedes iniciar con `claude --model opus`.
- Haiku (`haiku-worker`) investiga de forma acotada: encuentra símbolos, contratos, docs, logs y pruebas. No decide arquitectura ni hace cambios ambiguos.
- Sonnet (`sonnet-worker`) es el implementador predeterminado: backend Python/FastAPI, pipeline FFmpeg/Whisper/yt-dlp y frontend Next.js/React/TypeScript.
- Sonnet (`sonnet-reviewer`) revisa de forma independiente los cambios tras la implementación. No edita; informa hallazgos con archivo:línea. Sonnet implementa las correcciones.
- No invoques los cuatro agentes para cada tarea pequeña. Sigue `.claude/skills/model-router/SKILL.md` y `docs/AI_TEAM.md`.
- Carga `clipforge-media-pipeline` solo para ingesta, transcripción, clipping, timestamps, encuadre, audio, FFmpeg, GPU o directos. Carga `clipforge-frontend` solo para Next.js, React, TypeScript, editor o UI.
- Usa `token-optimization` para sesiones largas, auditorías y checkpoints. Prefiere `/clear` + `docs/STATUS.md` cuando el contexto anterior ya no sea útil.
- Para clasificar una tarea: `python3 .claude/skills/model-router/scripts/route.py "descripción" --files N`.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- When graphify-out/graph.json exists, run `graphify query "<question>"` before your first grep, search or source-file read for a codebase question, and include this rule in every subagent prompt that explores code. Read raw files only for lines the graph or an earlier read located.
- Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. Use `graphify section "<heading>"` for a scoped Markdown section.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
- A committed graphify-out/graph.json is rewritten whole on every build; do not flag its expected generated diff as churn.

## Orquestación inteligente (Opus · Sonnet · Haiku)

Objetivo: máxima calidad con el mínimo gasto. Decide por tarea, no por costumbre.

1. **Clasifica primero.** `python3 .claude/skills/model-router/scripts/route.py "tarea" --files N`. Tarea pequeña (1 archivo, causa clara) → hazla tú directamente como Sonnet, sin agentes.
2. **Haiku localiza, nunca decide.** Para encontrar código, contratos, logs o tests, usa `haiku-worker` con `graphify query` primero. Pide como máximo 15 líneas: `archivo:línea` + una frase. Lanza varias búsquedas independientes de Haiku en el mismo turno, en paralelo.
3. **Sonnet implementa.** Un `sonnet-worker` por unidad coherente. En paralelo solo si tocan archivos distintos. Dale: objetivo, archivos exactos, criterio de aceptación, qué NO tocar y el formato de respuesta (archivos tocados, test ejecutado, lo no verificado).
4. **Revisor solo cuando hay riesgo:** render FFmpeg, contratos de API, pipeline.py, cambios en varios módulos. Cambio trivial: sin revisor. `sonnet-reviewer` no edita; Sonnet corrige lo confirmado.
5. **Opus como advisor, en tres momentos:** antes de fijar un plan no trivial, cuando el mismo error aparece dos veces y antes de declarar terminado un trabajo grande. Pásale hechos, no archivos enteros. Si `--advisor` no está activo, usa `opus-worker` solo en esos tres momentos. Opus nunca escribe código rutinario.
6. **Escala a Opus de verdad** ante seguridad, riesgo de pérdida de datos, decisiones de arquitectura entre módulos o dos arreglos fallidos.
7. **Corta los bucles:** máximo 2 rondas de arreglo por hallazgo. Si no converge, para y reporta con evidencia en vez de seguir gastando.
8. **Verifica en escalera:** archivo tocado → prueba dirigida → un chequeo completo (`python -m pytest -q`, `python -m py_compile pipeline.py app.py integraciones.py`). Nunca digas que algo pasó si no lo ejecutaste; di qué no pudiste verificar.
9. **Resultados cortos:** los subagentes devuelven hallazgos, rutas y decisiones, no archivos completos. No releas lo que ya está en contexto.
10. **Cierre:** `graphify update .` tras cambiar código; actualiza `docs/STATUS.md` (≤ 40 líneas) en trabajos grandes.
