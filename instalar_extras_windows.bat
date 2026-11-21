@echo off
chcp 65001 >nul
echo Instalando extras opcionales de NovoClip, uno por uno...
python -m pip install pysubs2 && echo [OK] pysubs2 || echo [NO] pysubs2
python -m pip install stable-ts && echo [OK] stable-ts || echo [NO] stable-ts
python -m pip install deepfilternet && echo [OK] deepfilternet || echo [NO] deepfilternet: necesita Rust (https://rustup.rs). Sin el, la limpieza de audio usa el filtro de FFmpeg y funciona igual.
echo.
echo Listo. Lo que salga [NO] no es necesario. Reinicia NovoClip.
pause
