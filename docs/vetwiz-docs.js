/* =============================================================
   호환용 shim — vetwiz-docs.js
   실제 스크립트는 /docs/shared/js/docs-common.js 로 이전되었습니다.
   기존/외부에서 이 파일을 직접 참조하는 경우를 위해 공통 스크립트를 로드합니다.
   신규 문서는 docs-common.js 를 직접 링크하세요. (docs/README.md 참고)
   ============================================================= */
(function () {
    // 이 파일 위치 기준 상대경로로 해석합니다(웹 서버·file:// 더블클릭 모두 동작).
    var self = document.currentScript && document.currentScript.src;
    var s = document.createElement("script");
    s.src = self ? new URL("shared/js/docs-common.js", self).href : "/docs/shared/js/docs-common.js";
    s.defer = true;
    document.head.appendChild(s);
})();
