## Framework 이해하기

- 기존에 개발된 웹 서비스 코드를 재사용하기
- 자주 사용되는 코드들을 개발에 활용할 수 있도록 미리 모아둔 것
- 소프트웨어의 생산성과 품질을 높임

## Django의 장점

- Flask 대비 자유도는 낮은 대신 유용한 기능들이 많음
- 검증된 웹 프레임워크 : 안정적으로 사용 가능

## 클라이언트 - 서버 구조

- 클라이언트가 서버에 요청을 보내고, 서버는 클라이언트에 응답하는 구조
- 클라이언트는 웹 사이트에 연결된 장치(크롬 브라우저)
- 서버는 클라이언트에 html 문자 형태의 데이터를 전송

## 동적 웹 페이지

- Dynamic Web Page
- 사용자마다 보이는 정보를 다르게 설정할 수 있음
- 같은 웹 사이트 주소여도 화면을 다르게 표시 가능

## 디자인 패턴

- 자주 사용하는 구조를 일반화한 것
- 특정 문맥에서 자주 발생하는 구조적 문제 해결
- 복잡한 커뮤니케이션이 간단해짐

## Django의 디자인 패턴 :  MTV 패턴

- MTV 패턴 : MVC 디자인 패턴에서 변형된 형태
  - MVC : Model - View - Controller, 하나의 프로그램을 세 가지 역할로 구분한 개발 방법론
    - model = 원본 데이터, view = 표시 형식, controller = 연결 방식
  - MTV : Model - Template - View
  - MVC의 view, controller는 MTV의 template, view

## MTV 디자인 패턴

- model : 데이터 관련 로직을 관리(데이터 구조 정의, 데이터베이스 기록 관리)
- template : 레이아웃과 화면 처리, UI 구조 관리
- view : model과 template 관련 로직을 처리해서 응답 반환, 클라이언트 요청에 대해 처리를 분기하는 역할

## Django 환경 설정

- SSAFY 8기 공식 문서 참조
- 가상환경 만들기 : $ python -m venv (가상환경 이름)
  - 가상환경 이름은 주로 venv로 설정함
  
- 가상환경 활성화 : source (가상환경 이름)/Scripts/activate
  - 가상환경이 활성화된 동안 cmd에 (venv)가 표시됨
- 가상환경 비활성화 : # deactivate

- Django 설치하기 : $ pip install django==(버전명)
- 가상 환경 패키지 목록 조회 : $ pip list

## requirements.txt 생성(환경설정 백업)

- pip freeze > requirements.txt

## 백업한 목록 설치하기

- pip install -r requirements.txt

## Django 프로젝트 생성

- django-admin startproject firstproject .

## Django 서버 실행

- python manage.py runserver
- 코드 실행 후 출력되는 URL로 접속 가능

## Django 애플리케이션 생성

- python manage.py startapp articles
- 이후 프로젝트 폴더의 settings.py의 INSTALLED_APPS 리스트에 추가
  - 사용자 지정 애플리케이션을 리스트에 추가할 때 맨 앞 부분에 추가하는 것을 권장
  - 반드시 애플리케이션 생성 후 등록해야 함