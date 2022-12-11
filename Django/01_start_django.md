🔔목차🔔

- [Django 시작하기](#django-시작하기)
  - [Framework 이해하기](#framework-이해하기)
  - [클라이언트 - 서버 구조](#클라이언트---서버-구조)
  - [동적 웹 페이지](#동적-웹-페이지)
  - [디자인 패턴](#디자인-패턴)
  - [Django의 장점](#django의-장점)
  - [Django의 디자인 패턴 :  MTV 패턴](#django의-디자인-패턴---mtv-패턴)
- [Django 환경 설정](#django-환경-설정)
  - [가상환경 설정](#가상환경-설정)
  - [Django 환경 설정 명령어](#django-환경-설정-명령어)
  - [프로젝트 생성](#프로젝트-생성)
  - [개별 앱 생성](#개별-앱-생성)
  - [Django 서버 실행](#django-서버-실행)
  - [Django Template Language(DTL)](#django-template-languagedtl)
  - [메인 페이지 설정하기](#메인-페이지-설정하기)
  - [throw](#throw)
  - [catch](#catch)
- [서버에 보내는 요청 메서드(method)](#서버에-보내는-요청-메서드method)
  - [get](#get)
  - [post](#post)
  - [put](#put)
  - [delete](#delete)
- [Django URLs](#django-urls)
  - [Variable routing](#variable-routing)

# Django 시작하기

## Framework 이해하기

- 기존에 개발된 웹 서비스 코드를 재사용하기
- 자주 사용되는 코드들을 개발에 활용할 수 있도록 미리 모아둔 것
- 소프트웨어의 생산성과 품질을 높임

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

## Django의 장점

- Flask 대비 자유도는 낮은 대신 유용한 기능들이 많음
- 검증된 웹 프레임워크 : 안정적으로 사용 가능
  
## Django의 디자인 패턴 :  MTV 패턴

- MTV 패턴 : MVC 디자인 패턴에서 변형된 형태
  - MVC : Model - View - Controller, 하나의 프로그램을 세 가지 역할로 구분한 개발 방법론
    - model = 원본 데이터
    - view = 표시 형식
    - controller = 연결 방식
  - MTV : Model - Template - View
  - MVC의 view, controller는 MTV의 template, view
- 위 패턴은 HTTP 구조 내에서 작동

# Django 환경 설정
  
## 가상환경 설정
- 가상환경 만들기
  -  python -m venv (가상환경 이름)
  - 가상환경 이름은 주로 venv로 설정함
- 가상환경 활성화
  - source (가상환경 이름)/Scripts/activate
  - 가상환경이 활성화된 동안 cmd에 (venv)가 표시됨

- 가상환경 비활성화 : # deactivate

## Django 환경 설정 명령어
- Django 설치
  - pip install django==(버전명)
  - ==버전명은 생략 가능(생략 시 최신 버전 설치)

- 가상 환경 패키지 목록 조회
  - $ pip list

- 환경설정 백업
  - pip freeze > requirements.txt

- 백업한 목록 설치하기
  - pip install -r requirements.txt

## 프로젝트 생성
- django-admin startproject firstproject .

## 개별 앱 생성
- python manage.py startapp (appname)

- 이후 프로젝트 폴더의 settings.py의 INSTALLED_APPS 리스트에 추가
  - 사용자 지정 애플리케이션을 리스트에 추가할 때 맨 앞 부분에 추가하는 것을 권장
  - 반드시 애플리케이션 생성 후 등록해야 함

## Django 서버 실행

- python manage.py runserver
- 코드 실행 후 출력되는 URL로 접속 가능


## Django Template Language(DTL)

- Django 템플릿에서 사용하는 built-in template system
- 조건, 반복, 변수, 치환, 필터 등의 기능 제공
  - 필터 설정 : {{context 원본|필터 조건}}

## 메인 페이지 설정하기

- 프로젝트 > settings.py의 TEMPLATES의 'DIRS' : []에 __BASE_DIR / 'templates',__ 입력

```html
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates',],
        'APP_DIRS': True,
...중략
```

## throw

- 클라이언트가 서버에 데이터 정보를 전송하는 형식
- throw의 form은 action과 method로 구성됨
  - action = 서버의 어느 위치에 데이터를 보낼지
  - method = 어떤 방식으로 데이터를 전송할지
  - type = 전송하는 데이터의 유형
  - name = 서버에서 전송받은 데이터를 어떤 변수명으로 취급할지 설정
  - type="submit" = 제출 버튼

## catch

- throw에서 전송한 데이터를 받는 형식
- get에서 return하는 값을 출력할 수 있음

# 서버에 보내는 요청 메서드(method)

## get

- throw에서 받은 데이터를 처리하는 방식
- request.GET.get((받은 데이터의 변수명))으로 표시

## post

- 백엔드 서버에 데이터를 전송할 때 사용
- 풀 스택 프로세스를 Django 내부에서 처리하는 경우 기본적으로 CSRF 토큰 인증을 요구한다.

## put

- DB에 저장된 데이터를 수정할 때 사용
- POST로도 구현할 수 있지만 PUT으로 구현하는 것이 더 깔끔하다.
  - POST로 구현하려 하는 경우 수정된 데이터가 기존 데이터에 덮어쓰지 않고 새로 추가되는 오류가 발생할 수 있음
- **수정할 데이터**와 **수정할 내용**을 지정해 주어야 한다.

## delete

- POST로 삭제 요청을 보낼 수도 있지만, DELETE 요청으로 보내는 것도 가능하다.
- **삭제할 데이터**를 지정해 주어야 한다.


# Django URLs

- 웹 애플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작함
- Django는 URL 끝에 /(Trailing slash)가 없으면 자동으로 붙여주는 게 기본 설정
  - 웹 프로그래밍 단계에서 경로의 맨 끝이여도 Trailing slash를 붙여주는 게 좋다.

## Variable routing

- 템플릿의 많은 부분이 중복되고 일부만 변경되는 상황인 경우 기본 템플릿을 최대한 재사용하는 게 좋음
- 매 사용자마다 정적인 html 파일을 만드는 것보다 사용자의 요청에 따라 URL을 변경할 수 있도록 동적으로 설계하는 것이 좋음
- urls.py에서 path() 선언 후 views에 show 함수 정의