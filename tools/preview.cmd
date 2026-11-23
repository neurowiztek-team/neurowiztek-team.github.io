@echo off
rem Local preview server. Pages also open by double-click (relative links);
rem use this to preview exactly as GitHub Pages serves the site (incl. 404.html).
cd /d "%~dp0.."
start "" http://localhost:8000/
python -m http.server 8000
