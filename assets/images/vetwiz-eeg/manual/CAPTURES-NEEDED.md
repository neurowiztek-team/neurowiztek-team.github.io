# VetWiz EEG 사용설명서 — 추가 촬영 필요 화면 메모

`docs/products/vetwiz-eeg/manual.html`에 아직 **실제 화면 캡처가 들어가지 못한** 부분 목록입니다.
adb에 기기가 연결되지 않아(그리고 저장소에도 해당 화면 캡처가 없어) 코드·문자열 기준 텍스트로만 서술해 둔 상태입니다.

> ⚠️ **반드시 실제 VetWiz EEG 앱(package `com.neurowiztek.vetwizeeg`) 화면만 사용하세요.**
> SignalWiz Mobile 앱 화면·아이콘을 대신 넣지 마세요. (기기 본체 사진은 브랜드 중립이라 공용 재사용 가능하지만, **앱 화면은 반드시 VetWiz EEG 것**이어야 합니다.)

기존에 채워진 실제 캡처(참고): `01_bluetooth_connection` · `02_channel_setup` · `03_impedance` · `04_eeg_monitor` · `05_analysis_spectrum` · `06_analysis_scalp_map`, 아이콘 `00_app_icon`, 기기 본체 `00_device_body`.

---

## 아직 필요한 캡처 (실제 VetWiz EEG 앱 화면)

| 파일명(권장) | 화면 | 앱에서 진입하는 방법 | 캡처에 반드시 보여야 할 것(실제 UI 문구) |
|---|---|---|---|
| `07_app_intro.png` | 앱 인트로/시작 화면 | 앱 최초 실행 직후 약 2.4초 | 태그라인 **“기억이 생명이다”**, VetWiz EEG 아이덴티티 |
| `08_subject_input.png` | 피검체 정보 입력 다이얼로그 | [모니터] → **[녹화 시작]** 을 누르면 표시 | 제목 **“피검체 정보 입력”**, 필드 **동물 이름/ID · 견종(드롭다운) · 메모**, 버튼 **[측정 시작]** / **[이름 없이 시작]** |
| `09_recording.png` | 녹화 진행 중 화면 | 피검체 입력 후 측정 시작 → 모니터에서 녹화 중 | **[녹화 중지]** 버튼, 상태 **‘녹화 중’**, 상단 상태표시줄 **“데이터 기록 중”** 알림 |
| `10_record_library.png` (선택) | 녹화 라이브러리(기록 목록) | [분석] → **[녹화 CSV 불러오기]** | 파일 목록(동물 이름·견종·메모), 검색창 **‘이름으로 검색’**, **삭제/공유** 동작 |
| `11_report.png` | 분석 보고서(PDF) | [분석]에서 파일 로드 → **[분석 보고서 출력]** → PDF 미리보기 | qEEG 리포트 1페이지(종합 요약) 또는 PDF 뷰어 화면 |
| `12_settings.png` (선택) | 설정 화면 | [설정] 탭 | 하드웨어 설정·화면 모드·데이터 경로 등. **⚠️ 최신 빌드로 재촬영** — 기존 저장소 캡처(`05_settings_1/2`)에는 구버전 표기 **“SignalWiz EEG” / “Download/Signalwiz mobile”**가 남아 있어 사용 금지. 현재 코드 기준 경로는 **`Download/VetWiz EEG`**. |

파일명 규칙: **영문 소문자 · 숫자 접두어 · 공백/한글 없음**. 저장 위치: 이 폴더(`assets/images/vetwiz-eeg/manual/`).

---

## 문서에 넣는 위치

각 캡처가 들어갈 자리에는 `manual.html`에 **HTML 주석(`<!-- 📸 촬영 필요 ... -->`)**으로 표시해 두었습니다.
캡처를 준비하면 해당 주석 자리에 아래 형태로 교체하세요.

```html
<figure class="doc-figure">
  <img class="app-shot" src="/assets/images/vetwiz-eeg/manual/08_subject_input.png"
       alt="VetWiz EEG 앱의 피검체 정보 입력 화면 — 동물 이름/ID·견종·메모 입력">
  <figcaption>[모니터] → [녹화 시작] 시 표시되는 피검체 정보 입력</figcaption>
</figure>
```

여러 장을 나란히 배치할 때는 `<div class="shot-grid"> … </div>`로 감쌉니다(분석 섹션 참고).

---

## 촬영 원칙 (요약)

- 실제 VetWiz EEG 앱만 사용, **SignalWiz 앱 캡처 금지**.
- 디버그 UI·개발자 옵션·터치 포인터 숨김.
- 알림창·개인정보 노출 금지, 상태바의 불필요한 개인정보는 크롭.
- 화면 비율 유지(늘이거나 찌그러뜨리지 않기), 동일 화면 중복 금지.
- 설명에 필요한 부분이 잘 보이도록 적절히 크롭(내용 자체 임의 조작 금지).

## adb 캡처 방법 (기기 연결 후)

```bash
adb devices                                   # 대상 기기 확인
adb shell screencap -p /sdcard/vetwiz_screen.png
adb pull /sdcard/vetwiz_screen.png .
adb shell rm /sdcard/vetwiz_screen.png
```
