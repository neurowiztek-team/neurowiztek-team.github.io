#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Neurowiztek 문서 링크·이미지·리디렉션 검사기 (표준 라이브러리만 사용)

- 모든 .html의 내부 href/src 대상이 실제 파일로 존재하는지 확인
- 루트 절대경로(/...), 상대경로, <base href> 를 모두 해석
- 리디렉션 스텁(meta refresh)의 타깃 존재 여부 및 순환 여부 확인
- 외부 URL(http/https/mailto/tel/data)과 순수 앵커(#...)는 제외

사용법:  python tools/check_docs.py
성공 시 종료코드 0, 문제 발견 시 1.
"""
import os
import re
import sys
from urllib.parse import urldefrag, urlsplit, unquote

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ATTR_RE = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
BASE_RE = re.compile(r"""<base\s[^>]*href\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
REFRESH_RE = re.compile(
    r"""<meta\s+http-equiv\s*=\s*["']refresh["']\s+content\s*=\s*["'][^"']*url=([^"']+)["']""",
    re.IGNORECASE,
)

EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:")


def is_external(url):
    u = url.strip().lower()
    return u.startswith(EXTERNAL_PREFIXES) or u.startswith("//")


def find_html_files():
    out = []
    for base, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in (".git", "_archive", "node_modules")]
        for f in files:
            if f.lower().endswith(".html"):
                out.append(os.path.join(base, f))
    return sorted(out)


def resolve(url, html_path, base_href):
    """참조 URL을 저장소 내 실제 파일 경로로 해석. 외부/앵커면 None."""
    url = url.strip()
    if not url or url.startswith("#") or is_external(url):
        return None
    path = urldefrag(url)[0]
    path = urlsplit(path).path  # drop any query
    if not path:
        return None
    path = unquote(path)
    if path.startswith("/"):
        rel = path.lstrip("/")
        return os.path.normpath(os.path.join(REPO_ROOT, rel))
    # 상대경로: <base href>가 있으면 그 기준, 없으면 파일 디렉터리 기준
    if base_href and base_href.startswith("/"):
        rel = os.path.join(base_href.lstrip("/"), path)
        return os.path.normpath(os.path.join(REPO_ROOT, rel))
    return os.path.normpath(os.path.join(os.path.dirname(html_path), path))


def get_refresh_target(html_path):
    with open(html_path, encoding="utf-8", errors="replace") as fh:
        m = REFRESH_RE.search(fh.read())
    return m.group(1).strip() if m else None


def rel(p):
    return os.path.relpath(p, REPO_ROOT).replace(os.sep, "/")


def main():
    html_files = find_html_files()
    broken = []       # (source, url, resolved)
    checked_refs = 0

    for hf in html_files:
        with open(hf, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        bm = BASE_RE.search(text)
        base_href = bm.group(1) if bm else None
        for url in ATTR_RE.findall(text):
            target = resolve(url, hf, base_href)
            if target is None:
                continue
            checked_refs += 1
            if not os.path.exists(target):
                broken.append((rel(hf), url, rel(target)))

    # 리디렉션 순환/타깃 검사
    redirects = {}  # src_html_abs -> target_abs (or None)
    cycle_errors = []
    for hf in html_files:
        tgt_url = get_refresh_target(hf)
        if not tgt_url:
            continue
        target = resolve(tgt_url, hf, None)
        redirects[os.path.normpath(hf)] = target
        if target is not None and not os.path.exists(target):
            broken.append((rel(hf), "[redirect] " + tgt_url, rel(target)))

    for start, target in redirects.items():
        seen = [start]
        cur = target
        while cur is not None and os.path.normpath(cur) in redirects:
            cur = os.path.normpath(cur)
            if cur in seen:
                cycle_errors.append(" -> ".join(rel(p) for p in seen + [cur]))
                break
            seen.append(cur)
            cur = redirects[cur]

    print("검사한 HTML 파일 수 : %d" % len(html_files))
    print("검사한 내부 참조 수 : %d" % checked_refs)
    print("리디렉션 스텁 수    : %d" % len(redirects))

    ok = True
    if broken:
        ok = False
        print("\n[깨진 내부 참조 %d건]" % len(broken))
        for src, url, target in broken:
            print("  %s\n    -> %s  (없음: %s)" % (src, url, target))
    else:
        print("\n[내부 참조] 깨진 링크·이미지 없음 ✔")

    if cycle_errors:
        ok = False
        print("\n[순환 리디렉션 %d건]" % len(cycle_errors))
        for c in cycle_errors:
            print("  " + c)
    else:
        print("[리디렉션] 순환 없음 ✔")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
