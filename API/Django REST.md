🔔목차🔔


- [HTTP](#http)
  - [HTTP의 특징](#http의-특징)
- [Resource](#resource)
  - [웹에서의 리소스 식별](#웹에서의-리소스-식별)
- [통합 자원 식별자(URI)](#통합-자원-식별자uri)
  - [URL](#url)
    - [URL의 구조](#url의-구조)
  - [URN](#urn)
- [REST API](#rest-api)
- [WEB API](#web-api)
- [REST](#rest)
  - [REST 정리](#rest-정리)
- [JSON](#json)
- [vue](#vue)
- [serialization](#serialization)
  - [serializer 설치](#serializer-설치)
    - [ModelSerializer](#modelserializer)
    - [api_view decorator](#api_view-decorator)
- [Django REST Framework - N:1 관계](#django-rest-framework---n1-관계)
  - [get_list_or_404](#get_list_or_404)

# HTTP

- HyperText Transfer Protocol
- HTML 등의 문서(콘텐츠)를 가져올 수 있도록 하는 웹 상의 프로토콜(규약)
- 클라이언트-서버 프로토콜이라고도 한다.
- 클라이언트와 서버는 메시지의 요청(request)와 반응(response)으로 통신

## HTTP의 특징

- Stateless(무상태)
  - 동일한 연결에서 연속적으로 수행되는 두 요청 사이에 링크가 없다.
  - 쿠키와 세션을 이용해 연결 상태를 표현(보완)

# Resource

- HTTP 요청의 대상
  - GET : 리소스의 표현(조회) 요청
    - 데이터를 검색(READ)하는 경우에만 사용
  - POST : 데이터를 지정된 리소스에 제출
    - 서버 상태 변경
  - PUT : 요청한 주소의 리소스 수정(UPDATE)
  - DELETE : 저장된 리소스 삭제

## 웹에서의 리소스 식별

- 리소스는 문서, 사진, 기타 등 어떤 것도 될 수 있다.
- 각 리소스는 URI로 식별된다.

# 통합 자원 식별자(URI)

- 인터넷에서 하나의 리소스를 가리키는 문자열
- 대표적으로 URL(웹 사이트 주소) 등이 있다.

## URL

- 통합 자원 위치
- 웹에서 주어진 리소스의 주소
- 네트워크 상에 리소스가 어느 위치(리소스의 주소)에 있는지 알려주는 약속

### URL의 구조

1. 브라우저가 리소스를 요청하는 데 사용해야 하는 프로토콜(HTTP, HTTPS 등)
- URL의 첫 부분은 브라우저가 어떤 규약을 사용하는지 표시
2. 권한(Authority)
- ://로 구분
- 도메인과 포트 포함
  1. 도메인 이름
    - 요청 중인 웹 서버(어떤 웹 서버를 요청하는지) 표시
    - 직접 IP 주소를 입력하는 것도 가능하지만, 일반적으로 도메인 이름을 사용
  2. 포트
    - 웹 서버의 리소스에 접근하는 데 사용되는 기술적인 관문(Gate)
    - HTTP 표준 포트(HTTP-80, HTTPS-443)을 제외한 다른 포트는 생략 불가
    - Django의 기본 포트는 8000(80 + 00)
3. Path
- 웹 서버의 리소스 경로
- 초기에는 물리적인 위치를 표시했지만, 최근에는 *추상화된 형태*의 구조 표현
  - 서버 구성에 따라 경로 정의는 변경될 수 있다.

4. Parameter

- URL에서 ?로 파라미터가 시작됨을 표시
- 웹 서버에 제공하는 추가 데이터
- '&'로 구분되는 key-value 쌍 목록

5. Anchor

- URL에서 \#으로 구분
- 리소스의 다른 부분에 대한 앵커
- 앵커 부분은 서버에 전송되지 않음
- 브라우저가 서버에 요청을 전송하지 않고도 특정 북마크(지점)로 이동할 수 있도록 함

## URN

- 자원의 고유한 이름으로 식별

# REST API

- 애플리케이션과 프로그래밍으로 소통하는 방법
- 복잡한 기능을 쉽게 만들 수 있도록 프로그래밍 언어로 제공되는 구성

# WEB API

- 웹 서버 또는 웹 브라우저를 위한 API
- HTML, XML, JSON 등 다양한 데이터 타입 응답

# REST

- Representational State Transfer
- API 서버를 개발하기 위한 일종의 SW 설계 방법론
- 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법 서술

## REST 정리

- 정보의 자원 식별 : URL
- 정보의 자원 표현 : JSON
- 자원에 대한 행위 : HTTP Methods

# JSON

- JavaScript 표기법을 따른 단순 문자열
- key-value 형태의 구조를 가지고 있어서 컴퓨터 언어가 갖고 있는 자료구조로 쉽게 전환할 수 있다.
- 현재 API에서 가장 많이 사용하는 데이터 타입

# vue

- Front-end Framework
- Django는 model과 view(백엔드) 구성에 사용하고, template(프론트앤드)는 vue로 분리해서 구성할 예정

# serialization

- 데이터 구조나 객체 상태를 동일 혹은 다른 컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정
- 어떠한 언어나 환경에서도 나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정
- json이 가장 보편적으로 사용됨

## serializer 설치

- 개별 앱 폴더에 serializers.py 파일 생성


### ModelSerializer

- 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 생성할 수 있는 shortcut
- 필드 생성, 유효성 검사, 생성(create) 및 수정(update)의 간단한 기본 기능 구현

- many 옵션
  - 단일 객체 인스턴스 대신 QuerySet 데이터를 통째로 불러오려면 many=True 옵션을 설정해야 함

### api_view decorator

- DRF view 함수가 응답해야 하는 HTTP 메서드 목록
- GET 메서드만 허용되며 다른 메서드의 경우 405 Not Allowed 응답

```
from rest_framework.decorators import api_view

@api_view(['GET','POST','PUT'])
```

# Django REST Framework - N:1 관계

## get_list_or_404

```python
from django.shortcuts import get_list_or_404

articles = get_list_or_404(Article)
```