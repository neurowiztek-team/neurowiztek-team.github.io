# VetWiz EEG 사용설명서 — 촬영 필요 이미지 메모

`docs/products/vetwiz-eeg/manual.html`에서 아직 **실제 이미지가 확정되지 않은** 자리 목록입니다.
각 자리에는 문서 본문에 눈에 보이는 **“새로 캡처 필요” 안내 박스**와, 소스에 삽입용 **HTML 주석(`<!-- 📸 촬영 필요 … -->`)**을 넣어 두었습니다.

> ⚠️ **반드시 현재 VetWiz EEG 앱(package `com.neurowiztek.vetwizeeg`) 화면·리소스만 사용하세요.**
> SignalWiz Mobile 앱 화면·아이콘·기기 사진을 대신 넣지 마세요. **앱 화면·기기 사진 모두 VetWiz EEG 기준으로 직접 준비**해야 합니다.

## 배경(왜 다시 찍어야 하나)

- 이전 버전 문서에서 앱 스크린샷 6종을 `VetWiz-EEG/docs/exhibition`·`docs/screenshots`의 기존 캡처로 채웠으나,
  **현재 빌드 기준으로 새로 촬영하기 위해 모두 제거**했습니다(요청 사항).
- 기기 본체 사진은 SignalWiz Mobile 설명서 자산을 재사용했던 것이라 제거했습니다.
- **현재 문서에 확정 반영된 이미지는 앱 아이콘 `00_app_icon.png`(VetWiz EEG 스토어 아이콘) 하나뿐**입니다.

---

## 필요한 이미지 목록 (모두 실제 VetWiz EEG 기준)

| 파일명(권장) | 화면 | 진입 방법 | 담아야 할 것(실제 UI 문구) |
|---|---|---|---|
| `00_device_body.png` | **기기 본체(하드웨어) 사진** | VetWiz EEG 기기 본체 전면을 직접 촬영 | 전면의 **CH.1~CH.8·REF·GND 커넥터, 전원 버튼, 블루투스·충전 표시**. (앱 화면 아님) |
| `01_bluetooth_connection.png` | 블루투스 | [블루투스] 탭 | 상단 **“연결됨”**, **등록된 기기** 목록에서 기기 연결됨. **하단 탭에 `분석`·`설정` 포함**(= VetWiz EEG 확인 포인트) |
| `02_channel_setup.png` | 측정 채널 설정 | [채널 설정] 탭 | CH1~CH8 **사용/미사용** 카드, **“선택된 채널: …”**, **[설정 완료]** |
| `03_impedance.png` | 임피던스 | [임피던스] 탭 | CH1~CH8 값(**kΩ**)과 **좋음/높음/매우 높음** 상태 |
| `04_eeg_monitor.png` | 신호 모니터 | [모니터] 탭 | 상단 **시간 설정**·**[녹화 시작]**, **“Time Window: 5 s”**, 채널별 파형·µV Y축 |
| `05_analysis_spectrum.png` | 분석 — 파워스펙트럼 | [분석] 탭 → 파일 로드 | **[녹화 CSV 불러오기]**, 파일 정보 카드(녹화 시간·250 SPS·0–50 Hz·채널 수), 채널 선택, **파워스펙트럼** 그래프. 상단 **“데이터 경로: VetWiz EEG”** 확인 |
| `06_analysis_scalp_map.jpg` | 분석 — EEG Scalp Map | [분석] 탭 → Scalp Map | **“EEG Scalp Map · 상대 대역 파워”**, 대역 **Delta/Theta/Alpha/Beta/Gamma**, 강아지 두피 분포·0~100% 색상 막대 |
| `07_app_intro.png` | 앱 인트로/시작 화면 | 앱 최초 실행 직후 약 2.4초 | 태그라인 **“기억이 생명이다”** |
| `08_subject_input.png` | 피검체 정보 입력 다이얼로그 | [모니터] → **[녹화 시작]** | 제목 **“피검체 정보 입력”**, 필드 **동물 이름/ID·견종(드롭다운)·메모**, **[측정 시작]**/**[이름 없이 시작]** |
| `09_recording.png` | 녹화 진행 중 | 측정 시작 후 모니터 | **[녹화 중지]**, 상태 **‘녹화 중’**, 상태표시줄 **“데이터 기록 중”** 알림 |
| `10_record_library.png` (선택) | 녹화 라이브러리 | [분석] → **[녹화 CSV 불러오기]** | 파일 목록(동물 이름·견종), 검색창 **‘이름으로 검색’**, **삭제/공유** |
| `11_report.png` | 분석 보고서(PDF) | [분석] → **[분석 보고서 출력]** → PDF | qEEG 리포트 1페이지(종합 요약) 또는 PDF 뷰어 |
| `12_settings.png` (선택) | 설정 | [설정] 탭 | 하드웨어 설정·화면 모드·데이터 경로 등. **현재 코드 경로는 `Download/VetWiz EEG`** (구버전 캡처의 “SignalWiz EEG”/“Signalwiz mobile” 표기 금지) |

파일명 규칙: **영문 소문자 · 숫자 접두어 · 공백/한글 없음**. 저장 위치: 이 폴더(`assets/images/vetwiz-eeg/manual/`).

> ✅ **VetWiz EEG vs SignalWiz 구분 포인트:** 하단 탭에 **`분석`·`설정`이 있으면 VetWiz EEG**, 없으면(블루투스·채널설정·임피던스·모니터 4탭) SignalWiz입니다.
> 화면 제목이 “블루투스”면 VetWiz EEG, “Bluetooth 기기”면 SignalWiz입니다.

---

## 문서에 넣는 방법

각 자리의 안내 박스/HTML 주석을 아래 형태로 교체하세요.

```html
<figure class="doc-figure">
  <img class="app-shot" src="/assets/images/vetwiz-eeg/manual/01_bluetooth_connection.png"
       alt="VetWiz EEG 앱 블루투스 화면 — 상단 ‘연결됨’, 등록된 기기 목록">
  <figcaption>[블루투스] 화면 — 기기 연결 완료(연결됨) 상태</figcaption>
</figure>
```

분석 화면처럼 2장을 나란히 둘 때는 `<div class="shot-grid"> …figure×2… </div>`로 감쌉니다.

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
