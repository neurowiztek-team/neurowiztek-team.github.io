# Neurowiztek 제품 문서 (docs/)

이 디렉터리는 GitHub Pages(`https://neurowiztek-team.github.io/`)로 배포되는 제품 문서 모음입니다.
사이트는 저장소 루트에서 서빙되므로 모든 내부 참조는 **루트 절대경로**(`/docs/...`, `/images/...`, `/assets/...`)를 사용합니다.
덕분에 문서를 하위 디렉터리로 옮겨도 CSS·JS·이미지 참조가 깨지지 않습니다.

---

## 디렉터리 구조

```text
docs/
├─ products/                     제품별 활성 문서(정식 canonical 위치)
│  ├─ measurewiz/
│  │  ├─ quick-guide.html        ① 간편 안내
│  │  ├─ manual.html             ② 상세 사용설명서
│  │  └─ stress-guide.html       ③ 스트레스 패러다임(활용 가이드)
│  ├─ signalwiz/
│  │  ├─ quick-guide.html        ① 간편 안내
│  │  └─ manual.html             ② 상세 사용설명서
│  ├─ vetwiz-ecg/
│  │  ├─ quick-guide.html        ① 간편 안내
│  │  ├─ manual.html             ② 상세 사용설명서(앱 사용법 12~20장 통합)
│  │  └─ app-guide.html          (구 앱 사용법 → manual.html#app-install 리디렉션 스텁)
│  └─ vetwiz-eeg/
│     ├─ quick-guide.html        ① 간편 안내(앱 화면 캡처 준비 중)
│     └─ manual.html             ② 상세 사용설명서
│
├─ shared/                       공통 문서 디자인 시스템
│  ├─ css/
│  │  ├─ docs-base.css           토큰·리셋·타이포·접근성·제품별 강조색
│  │  ├─ docs-components.css     헤더/목차/히어로/알림/단계/카드/표/버튼/푸터…
│  │  └─ docs-print.css          A4 인쇄·PDF(페이지 나눔 제어)
│  └─ js/
│     └─ docs-common.js          모바일 메뉴·목차 접힘·스크롤 스파이·맨 위로
│
├─ 법적 고지(공통 시스템 적용 · 현재 위치 유지 — 아래 "법적 고지 문서" 참고)
│  ├─ personalpolicy.html            회사 공통 개인정보 처리방침(홈페이지)
│  ├─ vetwiz_personalpolicy.html     VetWiz(ECG) 앱 개인정보 처리방침
│  ├─ vetwiz_eeg_personalpolicy.html VetWiz EEG 앱 개인정보처리방침
│  └─ vetwiz_account_deletion.html   VetWiz 계정·데이터 삭제 안내
│
├─ 레거시 CSS(레거시 페이지 전용, 유지)
│  ├─ style.css / mobile.css     레거시 문서
│  └─ manual.css                 SignalWiz 레거시 문서
│
├─ vetwiz-docs.css / vetwiz-docs.js   호환용 shim(공통 시스템으로 이전)
│
└─ 기존 URL 호환용 리디렉션 스텁(*.html, 아래 URL 대응표 참고)
```

### 문서 종류 표준: 3단 체계(Tier)

모든 제품은 아래 3단 체계로 문서를 제공합니다. ①·②는 공통 필수, ③은 제품 특화(선택).

| Tier | 파일명(공통) | 성격 | 필수 |
|---|---|---|---|
| ① 간편 안내 | `quick-guide.html` | 1페이지 핵심 순서(전원→연결→측정→저장) | ✅ |
| ② 상세 사용설명서 | `manual.html` | 사양·설치·전 기능·문제 해결·고객지원 | ✅ |
| ③ 활용 가이드 | `<주제>-guide.html` | 제품 특화 심화(예: `stress-guide`) | ⬜ |

- 모든 제품 헤더 내비게이션은 `간편 안내 · 상세 사용설명서 · (활용 가이드)` 순으로 통일합니다.
- 각 문서 푸터에는 해당 앱의 개인정보 처리방침 등 법적 고지 링크(`.doc-footer__legal`)를 둡니다.

---

## 기존 URL ↔ 새 canonical URL 대응표

| 기존 공개 URL | 새 canonical URL |
|---|---|
| `/docs/measurewiz.html` | `/docs/products/measurewiz/manual.html` |
| `/docs/measurewiz_stress.html` | `/docs/products/measurewiz/stress-guide.html` |
| `/docs/signalwiz_detailed_manual.html` | `/docs/products/signalwiz/manual.html` |
| `/docs/signalwiz_quick.html` | `/docs/products/signalwiz/quick-guide.html` |
| `/docs/vetwiz_ecg.html` | `/docs/products/vetwiz-ecg/manual.html` |
| `/docs/vetwiz_ecg_app_usage.html` | `/docs/products/vetwiz-ecg/manual.html#app-install` |
| `/docs/products/vetwiz-ecg/app-guide.html` | `/docs/products/vetwiz-ecg/manual.html#app-install` |
| `/docs/signalwiz_mobile.html` | `/docs/products/signalwiz/quick-guide.html` |
| `/docs/app_usage.html` | `/docs/products/vetwiz-ecg/manual.html#app-install` |
| `/docs/vetwiz_quick_guide.html` | `/docs/products/vetwiz-ecg/manual.html#quick-start` |

기존 URL은 **삭제하지 않습니다.** 각 경로에는 리디렉션 스텁이 있으며 다음을 포함합니다.

- `<meta http-equiv="refresh">` — 즉시 이동
- `<link rel="canonical">` — 검색엔진용 정식 주소
- 사용자가 직접 누를 수 있는 링크(자동 이동 실패 대비)
- `<meta name="robots" content="noindex">` — 스텁이 색인되지 않도록

리디렉션은 **한 번만** 이동하며(스텁 → canonical), 순환하지 않습니다.

---

## 파일 명명 규칙

- 새 문서 파일명은 **영문 소문자 + kebab-case**: `quick-guide.html`, `manual.html`, `stress-guide.html`
- 제품 디렉터리: `products/<product-slug>/` (예: `measurewiz`, `signalwiz`, `vetwiz-ecg`, `vetwiz-eeg`)
- 문서 유형 표준 이름
  - ① 간편 안내 → `quick-guide.html`
  - ② 상세 사용설명서 → `manual.html`
  - ③ 활용 가이드 → `<주제>-guide.html` (예: `stress-guide.html`)

### 문서 수정 시 함께 갱신할 것

- **최종 수정일**: 제품 문서 푸터의 `최종 수정일: YYYY-MM-DD`를 의미 있는 내용 변경 때 갱신합니다(수동).
- **sitemap.xml**: 새 문서 추가/삭제 시 `<url>` 항목과 `<lastmod>`를 갱신합니다.
- **OG 메타**: 새 문서에는 `og:title/description/url/image` + `twitter:card`를 추가합니다(제품 로고를 절대 URL로).
- 커밋 전 `python tools/check_docs.py` 실행(또는 PR에서 CI가 자동 검사).

---

## 공통 디자인 시스템 사용법

새 제품 문서의 `<head>`와 `<body>`:

```html
<head>
  ...
  <link rel="stylesheet" href="/docs/shared/css/docs-base.css">
  <link rel="stylesheet" href="/docs/shared/css/docs-components.css">
  <link rel="stylesheet" href="/docs/shared/css/docs-print.css">
</head>
<body class="docs-page product-vetwiz-ecg document-manual">
  ...
  <script src="/docs/shared/js/docs-common.js" defer></script>
</body>
```

- `product-*` : 제품별 강조색(accent). `document-*` : 문서 유형(선택, 향후 유형별 미세조정용).
- 표준 컴포넌트 클래스: `.doc-header` `.doc-nav` `.doc-layout` `.doc-toc` `.doc-hero`
  `.doc-section` `.notice(--info/--warning/--danger/--tip)` `ol.steps` `.quickstart-grid`
  `.card-grid` `.table-wrapper` `.spec-table` `.app-shot` `.shot-grid` `.btn(--primary/--outline)`
  `.doc-pager` `.doc-footer` `.to-top`
- JavaScript가 꺼져 있어도 본문·목차 링크는 정상 동작합니다(점진적 향상).

### 제품별 강조색(accent) 추가 방법

`docs/shared/css/docs-base.css`의 "제품별 강조색" 영역에 블록 하나만 추가합니다.
모든 컴포넌트는 `var(--color-primary)` 계열을 참조하므로 이 세 변수만 바꾸면 전체 색이 일괄 적용됩니다.

```css
.product-vetwiz-eeg {
    --color-primary: #7a3cf0;
    --color-primary-dark: #5220a8;
    --color-primary-soft: rgba(122, 60, 240, 0.1);
}
```

### 호환용 shim

`docs/vetwiz-docs.css`, `docs/vetwiz-docs.js`는 기존/외부 참조 호환을 위해 유지되며,
각각 공통 CSS 3종과 `docs-common.js`를 로드합니다. **신규 문서는 shim을 쓰지 말고** 위의 공통 파일을 직접 링크하세요.

---

## 새 제품 문서 추가 절차

1. `docs/products/<product-slug>/` 디렉터리를 만든다.
2. `quick-guide.html`(①) / `manual.html`(②) / `<주제>-guide.html`(③) 중 필요한 문서를 만든다.
3. 위 "공통 디자인 시스템 사용법"의 head/body 골격을 사용한다.
4. 필요하면 `docs-base.css`에 `product-*` 강조색 블록을 추가한다.
5. `index.html`(제품 소개)과 관련 문서에서 새 문서로 링크한다.
6. 이전 URL이 있었다면 그 경로에 리디렉션 스텁을 남긴다.
7. 아래 "검증"을 수행한 뒤 커밋한다.

---

## 이미지 경로 운영 원칙

- 현재 이미지는 `/images/...`(다수)와 `/assets/images/...`(SignalWiz)로 **혼재**되어 있습니다.
- 이번 정리에서는 참조 안정성을 위해 **이미지를 이동하지 않았습니다.**
- 모든 이미지는 루트 절대경로로 참조합니다. 한 문서 안에서는 표기 방식을 일관되게 유지하세요.
- 향후 `assets/images/`로 통합하려면 (1) 파일 이동 → (2) 참조 일괄 수정 → (3) 링크 검증 순으로 진행합니다. 별도 검토 커밋 권장.

---

## 법적 고지 문서 관리 원칙

- `personalpolicy.html`(회사 공통 개인정보 처리방침), `vetwiz_personalpolicy.html`,
  `vetwiz_eeg_personalpolicy.html`, `vetwiz_account_deletion.html`은 **현재 위치(`/docs/*.html`)를 유지**합니다.
- 이유: 이 URL들은 앱스토어·Play 콘솔 등에 **등록된 법적 문서 주소**일 수 있어, 리디렉션·이동 자체가 위험합니다. URL 안정성을 최우선으로 둡니다.
- 이 문서들은 공통 디자인 시스템(껍데기)만 적용했고 **법적 문구는 원문 그대로 보존**했습니다. 조항 내용을 임의로 수정하지 마세요.
- 문서 종류(3단 체계)에는 포함하지 않는 **별도 카테고리(법적 고지)**입니다. 각 제품 문서 푸터에서 링크로 연결합니다.
- 앱별 방침 매핑: VetWiz-ECG → `vetwiz_personalpolicy.html` + `vetwiz_account_deletion.html`,
  VetWiz EEG → `vetwiz_eeg_personalpolicy.html`, SignalWiz·MeasureWiz → (앱 전용 방침 없음) 회사 공통 `personalpolicy.html`.
- 향후 `policies/` 또는 `legal/`로 이관하려면 위험도를 검토한 뒤 스텁과 함께 별도 커밋으로 진행합니다.

---

## 레거시 리디렉션 파일을 삭제하면 안 되는 이유

- 앱스토어·QR 코드·외부 사이트·검색 결과가 **기존 URL을 직접 가리킬 수 있습니다.**
- 스텁을 지우면 그 링크들이 404가 됩니다. 스텁은 사용자·크롤러를 정식 문서로 안전하게 넘겨줍니다.
- `_archive/`로 옮긴 파일도 되돌리지 않습니다(아카이브는 미사용 리소스 보관용).

---

## 검증 방법

로컬 서버에서 확인합니다(외부 패키지 불필요):

```bash
python -m http.server 8000
# http://localhost:8000/index.html
# http://localhost:8000/docs/products/vetwiz-ecg/manual.html
```

### 링크·이미지 검증

저장소에 재사용 가능한 검사 스크립트를 두었습니다(표준 라이브러리만 사용):

```bash
python tools/check_docs.py
```

- 모든 로컬 HTML의 내부 링크(`href`)·이미지(`src`) 대상이 실제로 존재하는지
- 리디렉션 스텁의 타깃이 존재하는지, 순환하지 않는지
- 외부 URL(`http(s)://`)은 검사 대상에서 제외

### 화면 검증(수동)

브라우저 개발자도구에서 폭 **1440 / 768 / 360px**로 확인:

- 본문 가로 스크롤 없음, 표·이미지가 화면을 넘지 않음
- 목차·모바일 메뉴 정상, 제품 색상이 달라도 레이아웃은 동일

### 인쇄 검증(수동)

각 문서에서 브라우저 인쇄 미리보기(또는 PDF 저장):

- 표·이미지·단계 카드가 페이지 경계에서 잘리지 않음
- 제목이 페이지 끝에 홀로 남지 않음, 빈 페이지 없음
- 표 머리글이 다음 페이지에서 반복됨

---

## 남아 있는 개선 과제

- **VetWiz EEG 앱 화면 캡처:** `products/vetwiz-eeg/`의 상세 사용설명서·간편 안내는 앱 화면 자리를 "촬영 필요" 안내로 비워 두었습니다. 현재 VetWiz EEG 빌드에서 실제 화면을 캡처해 교체해야 합니다(지침: `assets/images/vetwiz-eeg/manual/CAPTURES-NEEDED.md`). VetWiz EEG 기기 본체 사진도 필요.
- ~~VetWiz EEG 방침 저장 경로 확인~~ **(해결)** `vetwiz_eeg_personalpolicy.html`의 분석 리포트 저장 위치를 회사 확인에 따라 `Download/VetWiz EEG/report`로 수정했습니다. (SignalWiz mobile 앱에는 분석 리포트 기능이 없음)
- **SignalWiz·MeasureWiz 앱 방침(선택):** 두 앱이 배포·데이터 수집 중이라면 앱 전용 개인정보 처리방침 신설을 검토합니다. 현재는 회사 공통 방침을 링크.
- **이미지 디렉터리 통합:** `images/` ↔ `assets/images/` 혼재 해소.
- **법적 고지 문서 이관(선택):** 위험도 검토 후 `legal/`로 이동.
