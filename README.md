# LINE Notify
![HAKC)][hakc-shield]
![HACS][hacs-shield]
![Version v1.4][version-shield]

LINE Notify를 이용하여, Homeassistant의 notify를 합니다.<br>
<br>

## Version history
| Version | Date        | 내용              |
| :-----: | :---------: | ----------------------- |
| v1.0.0  | 2020.09.23  | First version  |

<br>

## Installation
### Manual
- HA 설치 경로 아래 custom_components 에 파일을 넣어줍니다.<br>
  `<config directory>/custom_components/line_notify/__init__.py`<br>
  `<config directory>/custom_components/line_notify/manifest.json`<br>
  `<config directory>/custom_components/line_notify/notify.py`<br>
- configuration.yaml 파일에 설정을 추가합니다.<br>
- Home-Assistant 를 재시작합니다<br>
### HACS
- HACS > Integretions > 우측상단 메뉴 > Custom repositories 선택
- 'https://github.com/miumida/line_notify' 주소 입력, Category에 'integration' 선택 후, 저장
- HACS > Integretions 메뉴 선택 후, line_notify 검색하여 설치

<br>

## Usage
### configuration
- HA 설정에 line_notify를 추가합니다.<br>
```yaml
notify:
  - platform: line_notify
    name: line_notify
    token: 'your token'
```
<br><br>

### 기본 설정값

|옵션|내용|
|--|--|
|platform| (필수) line_notify  |
|name| (옵션) line_notify |
|token| (필수) LINE Notify Token |
<br>

## 참고사이트
[1] LINE 스티커 리스트 (<https://devdocs.line.me/files/sticker_list.pdf>)<br>


[version-shield]: https://img.shields.io/badge/version-v1.0.0-orange.svg
[hakc-shield]: https://img.shields.io/badge/HAKC-Enjoy-blue.svg
[hacs-shield]: https://img.shields.io/badge/HACS-Custom-red.svg
