# LINE Notify
![HAKC)][hakc-shield]
![HACS][hacs-shield]
![Version v1.4][version-shield]

LINE Notify를 이용하여, Homeassistant의 notify를 합니다.<br>
네이버 스마트싱스 카페에 광역번개님이 올리신 글을 참고하여, Custom Components로 작성하였습니다.<br>
Notify이기때문에 따로 센서가 생성되거나 하지는 않습니다. 서비스에서 notify 관련 서비스를 확인하시면 됩니다.<br>
<br>

## Version history
| Version | Date        | 내용              |
| :-----: | :---------: | ----------------------- |
| v1.0.0  | 2020.09.23  | First version  |
| v1.0.1  | 2021.03.09  | manifest.json add version attribute.  |
| v1.0.2  | 2021.03.09  | Bug Fixed  |
| v1.0.3  | 2021.12.12  | Bug Fixed  |
| v1.1.0  | 2022.03.16  | 통합구성요소 추가 |

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

<br>

### 기본 설정값

|옵션|내용|
|--|--|
|platform| (필수) line_notify  |
|name| (옵션) line_notify |
|token| (필수) LINE Notify Token |

<br>

### 서비스 옵션
|옵션|내용|
|--|--|
|stickerId| (옵션) stickerPackageId와 항상 함께 사용  |
|stickerPackageId| (옵션) stickerId와 항상 함께 사용 |
|imageFile| (옵션) LINE으로 전송할 이미지파일 경로. 예)'/config/media/wyze_cam/image.png' |

<br>

## 참고사이트
[1] 네이버 Smartthings & Connected Home 카페 | 광역번개님의 HA에서 라인(LINE) 메신저 노티 받기 (<https://cafe.naver.com/stsmarthome/11415>)<br>
[2] LINE 스티커 리스트 (<https://developers.line.biz/media/messaging-api/sticker_list.pdf>)<br>


[version-shield]: https://img.shields.io/badge/version-v1.1.0-orange.svg
[hakc-shield]: https://img.shields.io/badge/HAKC-Enjoy-blue.svg
[hacs-shield]: https://img.shields.io/badge/HACS-Custom-red.svg
