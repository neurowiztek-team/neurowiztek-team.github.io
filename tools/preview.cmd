@echo off
rem Local preview: the site uses root-absolute links (/docs/..., /assets/...),
rem so pages do not work when double-clicked (file://). Serve the repo root instead.
cd /d "%~dp0.."
start "" http://localhost:8000/
python -m http.server 8000
