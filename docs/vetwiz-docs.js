/* =============================================================
   호환용 shim — vetwiz-docs.js
   실제 스크립트는 /docs/shared/js/docs-common.js 로 이전되었습니다.
   기존/외부에서 이 파일을 직접 참조하는 경우를 위해 공통 스크립트를 로드합니다.
   신규 문서는 docs-common.js 를 직접 링크하세요. (docs/README.md 참고)
   ============================================================= */
(function () {
    var s = document.createElement("script");
    s.src = "/docs/shared/js/docs-common.js";
    s.defer = true;
    document.head.appendChild(s);
})();
