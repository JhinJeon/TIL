🔔목차🔔

- [용어 정의](#용어-정의)
  - [이름 공간(namespace)](#이름-공간namespace)
  - [모델](#모델)
  - [쿼리(query)](#쿼리query)
  - [매핑(mapping)](#매핑mapping)
  - [스키마(schema)](#스키마schema)
- [데이터 타입 설정](#데이터-타입-설정)
- [migration](#migration)
  - [ORM(Object-Relational-Mapping)](#ormobject-relational-mapping)
  - [ORM의 장단점](#orm의-장단점)
  - [Queryset](#queryset)
  - [DB 저장 시 주의사항](#db-저장-시-주의사항)
    - [.save()](#save)
    - [all()](#all)
    - [get()](#get)
    - [filter()](#filter)
    - [field lookup](#field-lookup)
- [CRUD](#crud)
  - [수정(update)](#수정update)
  - [삭제(delete)](#삭제delete)

# 용어 정의

## 이름 공간(namespace)

- 개체를 구분할 수 있는 범위

## 모델

- Django가 데이터를 구조화하고 조작하기 위한 추상적 계층
- 데이터베이스는 여러 테이블로 구성됨
    - 테이블 : 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
    - 필드 : 속성과 컬럼(column)으로 구성
    - 레코드 : 튜플과 행(row)으로 구성됨
    
- 테이블의 데이터는 레코드에 저장됨

## 쿼리(query)

-데이터를 조회하기 위한 명령어
- 쿼리를 날린다 == DB를 조작한다
    
## 매핑(mapping) 

-하나의 값을 다른 값으로 대응시키는 행위

## 스키마(schema)

- 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조(structure)


# 데이터 타입 설정

- 새로운 값을 입력받을 때 입력받는 데이터의 유형을 정의해야 한다.
- models 함수에 기본적으로 내장되어 있음
- Django의 model은 데이터 필드의 스키마를 구성하고, 데이터의 유효성을 검사한다.
  - 예1) CharField의 경우, 길이에 제한이 있는 문자열을 저장한다(길이 제한은 max_length= 인자로 설정)  
  - 예2) TextField의 경우 문자열 길이 제한을 두지 않으므로 기본적으로 데이터 유효성을 검증하지 않는다.

# migration

- 데이터베이스에 모델의 변경 사항을 반영하는 방법
- 모델의 변경사항과 데이터베이스를 동기화

> 마이그레이트 실행 명령어: python manage.py sqlmigrate (애플리케이션명) (마이그레이션 이름)
> ex) python manage.py sqlmigrate articles 0001
> 마이그레이션 생성(모델 버전 생성) 명령어: python manage.py makemigrations
> python manage.py makemigrations

> Note: 마이그레이션 시 주의사항
> - Django의 settings.py에 등록된 프로그램(모델)만 마이그레이션 대상으로 인식된다.
> - 모델과 스키마에 이상이 없음에도 마이그레이션이 진행되지 않는다면 settings.py의 INSTALLED_APPS를 확인해 보자.

## ORM(Object-Relational-Mapping)

- 객체 지향 매핑
- DB를 연동할 때 호환되지 않는 데이터를 자동으로 변환하는 프로그래밍 기법
- 모델(설계도)와 view를 오가는 과정
- Django는 자체 내장 ORM 사용
- SQL을 사용하지 않고 데이터를 조작할 수 있게 만드는 매개체

## ORM의 장단점

장점 : SQL을 몰라도 DB 조작 가능, **높은 생산성**

단점 : 대용량의 DB를 세밀하게 조작하기 어려움

## Queryset

- DB에서 전달 받은 객체 목록(데이터 모음)
- 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용 가능
- Django ORM을 통해 만들어진 자료형 
- 필터, 정렬 등 수행 가능
- 단, 단일 객체를 반환할 때는 쿼리셋이 아니라 모델 인스턴스로 반환

## DB 저장 시 주의사항

- 업로드 시각은 UTC를 기준으로 기록됨 : 한국 시간으로 표시하려면 별도로 번역 과정 필요

### .save()

- DB에 데이터가 저장되기 전까지 입력된 데이터의 id는 None

### all()

- QuerySet return
- 전체 데이터 조회
- 반복 가능 개체(for, if 등으로 응용 가능)

### get()

- 단일 데이터 조회
- 조회할 값이 단 하나인 경우에만 사용해야 함(값을 찾을 수 없는 경우에도 오류)
- 고유성(uniqueness)을 보장하는 조회에서 주로 사용

### filter()

- 지정된 조회 매개 변수와 일치하는 객체를 포함한 새 Queryset 반환
- 필터 결과가 하나여도 단일 쿼리셋으로 반환

### field lookup

- 찾고자 하는 레코드의 조건 설정
- 필터(filter, exclude, get 등)의 인자로 사용


# CRUD

- 소프트웨어가 가지는 기본적인 기능 4가지(Create, Read, Update, Delete)를 묶어서 일컫는 말
## 수정(update)

- **수정 전에 먼저 수정할 대상을 조회해서 가져와야 함**
- 대상 조회 후 새로운 값 입력(최초 입력과 동일한 방법)
- 업데이트 시각 확인(생성 시각은 불변)

## 삭제(delete)

- 삭제할 대상 선택 후 delete()로 삭제
- 중간의 데이터를 삭제하는 경우 새로 추가되는 데이터는 맨 마지막 데이터의 뒤에 추가됨
- 삭제된 데이터의 경로는 재사용하지 않음