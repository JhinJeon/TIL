목차

- [Vue with DRF](#vue-with-drf)
  - [서버-클라이언트 통신 방법](#서버-클라이언트-통신-방법)
  - [CORS(Cross-Origin Resource Sharing)](#corscross-origin-resource-sharing)
  - [교차 출처 리소스 공유](#교차-출처-리소스-공유)
  - [CORS 설정하기](#cors-설정하기)
- [권한 부여 및 허가](#권한-부여-및-허가)
    - [(추가) HTTP 에러에 따른 의미](#추가-http-에러에-따른-의미)
  - [인증 방식](#인증-방식)
  - [인증 사용 방법(TokenAuthentication)](#인증-사용-방법tokenauthentication)
  - [Dj-rest-auth](#dj-rest-auth)


# Vue with DRF

## 서버-클라이언트 통신 방법

## CORS(Cross-Origin Resource Sharing)

- URL 주소를 정상적으로 입력하여 HTTP 200 OK를 반환받음에도 오류가 발생할 수 있다.
- 브라우저는 보안 상 이유로 동일 출처 정책(SOP)에 의해 다른 출처의 리소스와 상호작용하는 것을 제한한다.
  - Django 서버는 8080 포트, Vue 서버는 8000 포트를 사용하므로 서로 다른 출처의 리소스와 상호작용하는 것이 된다.

> ## Note: 동일 출처 정책(Same-Origin Policy)
> - 잠재적으로 다른 출처(origin, 프로토콜+호스트+포트의 조합)의 리소스들은 서버에 위협이 될 수 있기 때문에, 출처 자체를 제한하여 공격받을 가능성을 줄인다.
> - 모든 브라우저는 기본적으로 동일 출처 정책을 사용한다.

## 교차 출처 리소스 공유

- 추가 HTTP 헤더를 사용하여, 특정 출처에서 실행 중인 웹 애플리케이션이 다른 출처의 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제
- 어떤 출처에서 자신의 콘텐츠를 불러갈 수 있는지 서버에 지정하는 방법
- 리소스가 자신의 출처와 다를 때 교차 출처 HTTP 요청을 실행하여, 브라우저에 다른 출처에 접근해도 된다는 사실을 알려야 한다.
  - 위 정책을 교차 출처 리소스 정책(CORS policy)라고 한다.

## CORS 설정하기

- HTTP Response Header를 이용해 통제 가능
- Access-Control-Allow-Origin : 단일 출처를 지정하여 브라우저가 해당 출처에 접근을 허용하도록 설정
- django-cors-headers 공식 문서 참조
  - INSTALLED_APPS와 MIDDLEWARE에 코드 추가
  - 이후 CORS_ALLOWED_ORIGINS에 추가할 출처 추가
    - 리스트 대신 True를 입력하면 모든 출처로부터의 접근 허용

> python -m pip install django-cors-headers 설치 필요

```python
# settings.py
INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]

MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
]

# vue(8000번 포트)로부터의 교차 출처(접근)을 허용
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8080',
]

```

# 권한 부여 및 허가

- 사용자에게 특정 리소스 또는 기능에 대한 액세스 권한을 부여하는 과정 또를 절차
- 보안 환경에서 권한을 부여하려면 <u>항상 먼저 인증되어야 한다.</u>
- 인증이 되었어도 모든 권한을 부여받는 것은 아님

### (추가) HTTP 에러에 따른 의미

- 403 Forbidden : 식별되지 않은 사용자
- 401 Error : 권한 없는 사용자(식별된 사용자이지만 접근 권한이 없는 경우)

## 인증 방식

- 토큰 인증 : 매우 간단하고, 다양한 외부 패키지를 지원한다

## 인증 사용 방법(TokenAuthentication)

> Django REST API 공식문서 참고

```python
# settings.py
INSTALLED_APPS = [
    ...,
    "rest_framework.authtoken",
    ...,
]

```

- 토큰 생성 시 Django에서 각 사용자에게 토큰을 발급하며, 토큰을 이용해 사용자 인증 및 권한 확인 프로세스 진행
- 사용자는 발급받은 토큰을 headers에 담아 요청과 함께 전송
  - 단, Token문자열을 합께 삽입해야 하며, 'Token' 문자열과 토큰 값 사이를 공백으로 구분해야 한다.

## Dj-rest-auth

- 회원가입, 인증(SNS 인증 포함), 비밀번호 재설정, 사용자 정보 검색, 회원정보 수정 등을 위한 REST API end point 지원

> 주의 : django-rest-auth는 더 이상 업데이트를 지원하지 않으므로, dj-rest-auth를 사용해야 한다.