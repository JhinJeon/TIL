# AIoT 트렌드

- 클라우드 컴퓨팅이 등장하면서 디바이스 자체의 성능보다는 데이터 저장 및 처리 능력이 더 중요해졌다.
- 산업용 장비는 비용절감, 관리최적화의 측면에서 엣지 디바이스 선호
- 엣지 디바이스는 데이터 통합(공유)이 어려운 문제가 있다.
- 하이브리드 디바이스 : 중요한 정보는 메인 디바이스에서 공유, 그 밖의 정보는 엣지 디바이스에서 관리
- 음성 데이터는 민감도와 정확도는 높지만, 음성인식과 자연어 처리는 어렵다.
- 엣지 디바이스 시장은 침체 분위기(2023.05 기준)
- AIoT의 최종 목표는 의사결정의 자동화
- B2C 시장은 성장이 정체되고 있지만, B2B 시장(공장, 기업체 등)에서는 생산성 향상을 위해 적극적으로 도입하려고 시도한다.


# API(Application Programming Interface)

- 아마존, 네이버, ChatGPT 등 다양한 플랫폼 서비스(기업)들이 API를 지원한다.

# AIoT와 IoT의 차이점

- IoT는 임베디드 관련 네트워크 통신체계 구축이 필요했다(데이터 처리 등은 메인 서버에서 처리하므로).
- AIoT 장비는 데이터 처리와 분석을 디바이스 자체에서 처리하므로, 디바이스의 요구 사항과 원가가 증가한다.
  
# 사물인터넷 기술

- **IoT 제품은 인터넷에 연결되어 있어야 한다.**(인터넷에 연결되어 있지 않다면 단순 사물통신)
- IoT 기술의 필수요소는 **서버**이다(데이터를 수집해서 전달하는 역할).

- 수집 : 정보 수집용 장치(센서)
- 연결 : 통신 프로토콜(전력소모, 범위, 보안성 등 고려)
- 처리 : 별도의 서버에서 데이터 처리 및 관리
- 제공 : IoT를 서비스로서 제공(상품화)

# API를 이용한 시각화

# TensorFlow, Teachable Machine, Chat GPT등을 모아서 단일 시각화 환경 생성

# 디바이스 구매 사이트

- 엣지 디바이스를 구매하려는 경우 해외 사이트를 이용하는 것도 좋음
- 주로 소량 주문, 시제품 제작, 제품 기획 등을 진행할 때 이용하면 좋다.

## 국내 사이트

- 엘레파츠
- 엔티렉스(디바이스마트)
- 아이씨뱅큐
- IC114

## 해외 사이트

- dfrobot(중국)
- sparkfun(미국)
- adafruit(미국)
- seeedstudio(미국)

# Maixpy 사용

## 이미지 식별용 박스 그리기

- draw_rectangle() 함수 사용

```py
import sensor, image, lcd

# Initialize the LCD screen
lcd.init()

# Initialize the camera
sensor.reset()
sensor.set_hmirror(0)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

# Capture images from the camera and display them on the LCD screen
while True:
    # img = 카메라 센서 스냅샷
    img = sensor.snapshot()
    
    # 바운드 박스(식별용) 그리기
    # 왼쪽부터 x시작점, y시작점, 너비, 높이, 선 색상, 선 두께, 채우기 여부
    img.draw_rectangle(20, 100, 100, 80, color=(0, 255, 0), thickness = 2, fill=False)
    
    # 선 그리기
    # 왼쪽부터 x시작점, y시작점, x종료점, y종료점, 선 색상, 선 두께
    img.draw_line(20, 20, 300, 20, color = (255, 255, 0), thickness = 3)

    # 원 그리기
    # 왼쪽부터 x시작점, y시작점, 직경, 테두리 색상, 선 두께
    img.draw_circle(200, 100, 50, color=(0, 0, 255), thickness = 3)

    # LCD 화면에 표시
    lcd.display(img)
```

## 색상 인식

- 인식하려는 색상 별 RGB값 기준이 필요하다.
- 영상처리 분야는 HSV와 Lab값 사용

## QR코드 인식

- find_qrcoes() 함수 사용

```py
# while 위쪽 부분은 위 코드와 동일
while True:
    img = sensor.snapshot()

    # QR코드 찾아주는 함수
    res = img.find_qrcodes()
    print(res)

    # 주소값은 5번째 항목
    if res:
        res = res[0]
        address = res.payload()
        img.draw_string(2, 2, address, color = (255, 255, 255), scale = 2)
        lcd.display(img)
        utime.sleep(3)

    lcd.display(img)
```

## 원형 인식

- 신호등 등을 인식할 때 원 모양을 인식하여 구별하는 방식으로 구현한다.

# 작성한 소스코드 파일 내용을 부트 파일에 저장

- 부트 파일에 저장하면 전원이 꺼져도 부팅할 때 자동으로 실행된다(비휘발성 메모리에 저장).
- 부트 파일에 저장하지 않으면 전원이 꺼질 때 데이터나 프로그램이 소실된다(휘발성 메모리).
- boot.py에 저장하려면 Tools 탭 > Save open script to board(boot.py) 선택

# MNIST(Modified National Institute of Standards and Technology database)

- 손글씨 이미지로 구성된 대형 데이터베이스
- MNIST 데이터를 기반으로 AI 모델을 학습시킬 수 있다.
- 패션 MNIST 등 다양한 바리에이션이 있다.

# Teachable Machine

- MBileNet 아키텍쳐 기반 kmodel
- Mbilenet은 yolo보다 경량화한 형태의 모델로, Google Teachable Machine과 유사하다.
- 고성능, 높은 정확성보다는 저전력, 임베디드 환경에 적합

## 모델 학습 설정

- 배치 크기 : 학습 샘플들을 그룹화하여 그룹 별 학습, 그룹 별 샘플 수는 배치 크기에 입력한 값에 비례
- 에포크 : 전체 데이터 세트의 학습 반복 횟수, 에포크가 클수록 성능이 높아지는 경향이 있다.

# 시리얼 통신 사용(PuTTY)

- 외부 세션이나 장치에 연결하는 데 사용
- PuTTY 실행 > 세션 > 연결 타입 Serial 체크, Serial Line에 COM4(컴퓨터에 연결된 포트), 통신 속도 115200 입력 후 연결

# 분류(판단) 모델 만들기

- AIoT의 목적은 **자동화 프로세스 구현**
- AI 모델이 분류한 결과를 바탕으로 다른 디바이스나 사람과 상호작용해야 한다(서비스의 영역).
  - 기계장치 조작, 모니터, 알림 등

- 통신하는 기기마다 프로토콜이 다르다.(OSI 7 계층의 차이)
- 미들웨어 개발 : 네트워크 프로토콜 호환성과 데이터의 전처리 필요성 증가
- 엣지디바이스와 IoT 장비/머신/웹/서버/게이트웨이 등을 연결할 수 있는 플랫폼 서비스들이 등장하는 추세(MS, AWS, 삼성 Automation Studio 등)

# Node-RED

- IoT 장비의 데이터를 별도의 장비나 호환성 통합 작업 없이 표시 및 시각화할 수 있는 프로그램(시각화 도구는 아님)
- 사용자에게 디자인 및 테마 커스터마이징 기능(대시보드 시각화) 지원
- 웹 시각화 자체는 FineReport 등 다른 플랫폼을 이용하는 게 더 좋음

## Node-RED 특징

- 브라우저 기반 개발 가능(블록 코딩)
- Node.js 기반의 빌드 작업
  - Node.js 클라우드, 가상화, API 구현 시 주로 사용된다.(전세계 약 80% 이상)

## 설치 및 환경설정

1. Node.js 설치

- 홈페이지 접속 > LTS 버전 다운로드
- 구버전을 다운로드하려면 다운로드 탭에서 조회

2. Node-RED 설치

- cmd에서 'npm install -g --unsafe-perm node-red' 입력

## Node-RED 서버 접속

- cmd에서 'node-red' 입력 후 로컬 주소로 접속

## 기본 사용법

- 디버그 메세지 : 터미널에 디버깅 메시지가 뜨는 것과 동일한 역할

## 프로젝트 내보내기/불러오기

- Node-RED에서는 모든 프로젝트는 JSON 파일로 관리한다.
- JSON은 빅 데이터 영역에서 가장 많이 사용되는 데이터 포맷이다.

## 코딩하기

### 1. 단순 문자열 출력

- 텍스트를 출력하려면 메시지 payload에 넣어서 return하면 된다.

```js
// 자바스크립트 코드로 작성
const date = new Date();

// 메시지 페이로드에 넣어서 반환
msg.payload = msg.payload + date;
return msg;
```

### 2. 대시보드로 데이터 표현하기

```js
const ran = Math.floor(Math.random() * 100);

// 무작위 숫자(1~100 사이)를 payload에 전송
msg.payload = ran;
return msg;
```

- 시각화 : '로컬 주소/ui/' 로 접속하며, 기본적으로 'cannot GET' 오류가 뜬다.
  - 팔렛트에서 node-red dashboard를 설치한 후 다시 접속하면 전용 UI가 뜬다.

```js

```

- Dashboard의 탭 노드를 추가한 다음 그룹 노드를 추가해야 한다.

## 웹캠 노드

- Node-Red의 ui-webcam 노드를 이용하면 관제 모니터 등을 구현할 수 있다.

## Teachable Machine과 연동하기

- 팔렛트에서 teachable machine과 image-tools 설치

#### 주의사항

- 하위 그룹이나 구성 요소의 크기는 상위 그룹의 크기보다 작거나 같아야 한다.
- 새로운 그룹을 추가할 때는 ***의 노드타입 추가 옵션 선택하기(그렇지 않으면 기존 그룹/탭 설정을 덮어쓴다).
- Node-RED에 Teachable Machine 노드를 설치할 때 적절한 버전으로 설치하기(최신 버전인 경우 버그나 호환성 등 문제)

# 마이크로파이썬 사용? - 개인적으로 조사해 보기