/* =============================================================
   VetWiz ECG 문서 공통 스크립트 (vetwiz-docs.js)
   - 보조 기능만 담당(모바일 메뉴, 목차 접힘, 스크롤 스파이, 맨 위로)
   - JavaScript가 없어도 본문/링크/목차는 정상 동작(점진적 향상)
   ============================================================= */
(function () {
    "use strict";

    /* ── 모바일 메뉴(햄버거) ─────────────────────────────── */
    var toggle = document.querySelector(".doc-menu-toggle");
    var nav = document.getElementById("doc-nav");
    if (toggle && nav) {
        toggle.addEventListener("click", function () {
            var open = nav.classList.toggle("is-open");
            toggle.setAttribute("aria-expanded", open ? "true" : "false");
        });
        // 메뉴 링크 클릭 시 닫기
        nav.addEventListener("click", function (e) {
            if (e.target.closest("a")) {
                nav.classList.remove("is-open");
                toggle.setAttribute("aria-expanded", "false");
            }
        });
    }

    /* ── 모바일에서 목차 접기 ────────────────────────────── */
    var tocDetails = document.querySelector(".doc-toc__details");
    if (tocDetails && window.matchMedia) {
        var mq = window.matchMedia("(max-width: 1023px)");
        var applyToc = function (matches) {
            // 모바일이면 접고, 데스크톱이면 펼침
            tocDetails.open = !matches;
        };
        applyToc(mq.matches);
        if (mq.addEventListener) {
            mq.addEventListener("change", function (e) { applyToc(e.matches); });
        } else if (mq.addListener) {
            mq.addListener(function (e) { applyToc(e.matches); });
        }
    }

    /* ── 스크롤 스파이(현재 섹션 목차 강조) ──────────────── */
    var tocLinks = Array.prototype.slice.call(
        document.querySelectorAll(".doc-toc a[href^='#']")
    );
    if (tocLinks.length && "IntersectionObserver" in window) {
        var linkById = {};
        var targets = [];
        tocLinks.forEach(function (a) {
            var id = a.getAttribute("href").slice(1);
            var el = document.getElementById(id);
            if (el) {
                linkById[id] = a;
                targets.push(el);
            }
        });

        var setActive = function (id) {
            tocLinks.forEach(function (a) { a.classList.remove("is-active"); });
            if (linkById[id]) linkById[id].classList.add("is-active");
        };

        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    setActive(entry.target.id);
                }
            });
        }, { rootMargin: "-45% 0px -50% 0px", threshold: 0 });

        targets.forEach(function (el) { observer.observe(el); });
    }

    /* ── 맨 위로 버튼 ────────────────────────────────────── */
    var toTop = document.querySelector(".to-top");
    if (toTop) {
        var onScroll = function () {
            if (window.pageYOffset > 400) {
                toTop.classList.add("is-visible");
            } else {
                toTop.classList.remove("is-visible");
            }
        };
        window.addEventListener("scroll", onScroll, { passive: true });
        onScroll();
        toTop.addEventListener("click", function () {
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    }
})();
