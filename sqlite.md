🔔목차🔔
- [데이터베이스](#데이터베이스)
  - [데이터베이스 관리](#데이터베이스-관리)
  - [데이터베이스 정의](#데이터베이스-정의)
- [관계형 데이터베이스(RDB)](#관계형-데이터베이스rdb)
  - [RDB 정의](#rdb-정의)
  - [RDB 장점](#rdb-장점)
  - [스키마(schema)](#스키마schema)
  - [테이블(Table)](#테이블table)
  - [기본 키(Primary Key)](#기본-키primary-key)
  - [관계형 데이터베이스 관리 시스템(RDBMS)](#관계형-데이터베이스-관리-시스템rdbms)
- [SQLite](#sqlite)
  - [SQL Syntax](#sql-syntax)
  - [Statement(문)과 Clause(절)](#statement문과-clause절)
- [DDL](#ddl)
  - [CREATE](#create)
- [SQL Data Type](#sql-data-type)
  - [데이터 타입 결정](#데이터-타입-결정)
  - [SQLite Datatypes 특징](#sqlite-datatypes-특징)
- [데이터 무결성](#데이터-무결성)
  - [Constraints 종류](#constraints-종류)
  - [rowid의 특징](#rowid의-특징)
- [ALTER TABLE](#alter-table)
  - [ALTER statement 사용예시](#alter-statement-사용예시)
  - [DROP TABLE](#drop-table)
- [DML](#dml)
  - [CML으로 실행하기](#cml으로-실행하기)
    - [DB 열기](#db-열기)
    - [CSV데이터를 SQLite 테이블로 가져오기](#csv데이터를-sqlite-테이블로-가져오기)
  - [ORDER BY](#order-by)
  - [Filtering Data](#filtering-data)
    - [SELECT DISTINCT](#select-distinct)

# 데이터베이스

## 데이터베이스 관리

- 데이터 관리/저장/탐색 성능을 보완하고, 구조적으로 정리하기 위해 사용
- 보안성과 확장성 증가
- 다양한 기능 제공
- CRUD(생성, 조회, 수정, 삭제) 작업이 데이터베이스 관리의 기본

## 데이터베이스 정의

- 체계화된 데이터의 모임
- 여러 사람이 공유하고 사용할 목적으로 관리되는 정보의 집합
- DBMS(데이터베이스 관리 시스템) 프로그램을 이용해 데이터베이스 조작

# 관계형 데이터베이스(RDB)

## RDB 정의

- 데이터를 테이블, 행, 열 등으로 나누어 구조화하는 방식
- 자료를 여러 테이블로 나누어 관리하고, 테이블 간 관계를 설정해 여러 데이터를 쉽게 조작할 수 있음

## RDB 장점

- 데이터를 직관적으로 표현 가능
- 대량의 데이터도 효율적으로 관리 가능
- 관련 데이터 접근성 용이
 
## 스키마(schema)

- 테이블의 구조
- 자료 구조, 표현방법, 관계 등 전반적인 명세를 기술한 것

## 테이블(Table)

- 필드(column)와 레코드(row)를 사용해 조직된 데이터 요소들의 집합
- 관계(relation)라고도 부름

## 기본 키(Primary Key)

- 각 레코드의 고유 값
- 각 데이터를 구분할 수 있도록 하는 고유 값(unique)
- 한 데이터베이스 내에서 다른 항목들과 절대로 중복될 수 없음

## 관계형 데이터베이스 관리 시스템(RDBMS)

- 관계형 데이터베이스를 만들고 업데이트하는 데 사용하는 프로그램

# SQLite

- 응용 프로그램에 파일 형식으로 넣어 사용하는 비교적 가벼운 DB
- 대부분의 운영 체제에서 지원, 높은 호환성 보유
- 오픈소스 프로젝트이므로 자유롭게 사용 가능
- 대규모 동시 작업 처리에 부적합
- 다른 RDBMS에서 지원하는 SQL 기능을 지원하지 않을 수 있음
- 유연한 학습 환경 제공, Django Framework의 기본 DB

## SQL Syntax

- 모든 SQL 구문은 SELECT, INSERT, UPDATE 등의 키워드로 시작하고, 하나의 구문은 세미콜론(;)으로 구분됨
- SQL 키워드는 대소문자를 구분하지 않음
  - 다만 테이블/필드 등의 고유 이름과 구분하기 위해 대문자로 작성하는 것이 권장됨

```
SELECT column_name FROM table_name;
```

## Statement(문)과 Clause(절)

- Statement
  - 독립적으로 실행 가능한 완전한 코드 조각
  - statement는 clause로 구성됨

- clause
  - statement의 하위 단위

```
SELECT column_name FROM table_name;
```

- SELECT column_name, FROM table_name이라는 두 개의 clause가 모여 하나의 SELECT statement를 구성함

# DDL

- 데이터를 조작하기 위한 틀(테이블)을 정의하는 언어
- **CREATE(생성), ALTER(수정), DROP(삭제)**

## CREATE

- CREATE TABLE 테이블명([스키마](#스키마schema))
  - SQL은 들여쓰기를 엄격히 지킬 필요는 없음

```
CREATE TABLE tale_name(
    column1 data_type constraints,
    column2 data_type constraints,
    column3 data_type constraints
)
```

- column 값에 *공백을 허용하지 않게* 하려면?

```
CREATE TABLE contacts(
    name TEXT NOT NULL
    age INTEGER NOT NULL
    email TEXT NOT NULL
)
```

# SQL Data Type

1. NULL

- NULL value
- 정보가 없거나 알 수 없는 경우

2. INTEGER

- 정수
- 크기에 따라 0, 1, 2, 3, 4, 6, 8바이트 등 가변 크기를 가짐

3. REAL

- 실수
- 8바이트 부동 소수점을 사용하는 십진수값이 있는 실수

4. TEXT

- 문자 데이터(python의 string)

5. BLOB(Binary Large Object)

- 입력된 그대로 저장된 데이터 덩어리(타입 없음)
- 멀티미디어 파일
  - 예) 이미지 데이터 등

추가) SQL은 별도의 Boolean 타입을 지원하지 않으므로, 대신 정수형으로 변환하여 저장(0, 1)

6. 날짜 데이터 저장하기

- SQLite는 날짜 형식을 별도로 지원하지 않음
- 대신 built-in 'Date And Time Functions'로 TEXT, REAL, INTEGER 형태 등으로 저장할 수 있음

참고) Binary Data

- 데이터 저장 및 처리를 목적으로 0/1의 이진 형식으로 인코딩 된 파일
- 컴퓨터의 모든 데이터는 기본적으로 Binary data이며, 필요에 따라 텍스트 타입으로 변환하여 사용

## 데이터 타입 결정

- 따옴표, 소수, 지수 표시 등이 없으면 INTEGER
- 따옴표(작은 따옴표, 큰 따옴표 모두)로 묶인 경우 TEXT
- 값에 따옴표나 소수점, 지수가 없으면 REAL
- 따옴표 없이 NULL이면 NULL

## SQLite Datatypes 특징

- 다른 SQL 데이터베이스 엔진은 정적이고 엄격한 타입(static, rigid typing)을 사용
  - 컬럼에 저장된 데이터 타입 설정을 따름
- SQLite는 동적 타입 시스템(dynamic type system) 사용
  - 컬럼에 저장된 값에 따라 데이터 타입이 결정됨

# 데이터 무결성

- DB 내 데이터들의 정확성과 일관성을 보장하기 위한 수단
  - 무결성: 정확성과 일관성

## Constraints 종류

- **이하 제약 사항은 중첩 사용 가능**

1. NOT NULL

- 공백을 허용하지 않음
- 기본적으로 NULL(공백)을 허용함

2. UNIQUE

- 컬럼의 모든 값이 구별되거나 고유한 값을 가지도록 함

1. [PRIMARY KEY](#기본-키primary-key)

- 테이블 행의 고유성을 식별하는 데 사용하는 컬럼
- 각 테이블에는 하나의 기본 키만 있음
- 암시적으로 NOT NULL 제약조건이 포함됨

4. AUTOINCREMENT

- 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하지 못하도록 방지
- INTEGER PRIMARY KEY 이후에 작성하면 해당 rowid를 재사용하지 못하게 할 수 있음

```
CREATE TABLE table_name(
    id INTEGER PRIMARY KEY AUTOINCREMENT
)
```

- Django에서 테이블 생성 시 id 컬럼에 기본적으로 적용되는 제약조건

## rowid의 특징

- 테이블을 생성할 때마다 rowid라는 암시적 자동 증가 컬럼이 자동으로 생성됨
  - 게시글 번호 1번, 2번, 3번... 등이 자동으로 생성되는 이유

- 테이블 행을 고유하게 식별하는 64비트 부호 있는 정수 값
- 테이블에 새 행을 삽입할 때마다 정수 값을 자동으로 할당
  - 값은 1부터 시작
  - 데이터 삽입 시 rowid나 INTEGER PRIMARY KEY에 명시적으로 값이 지정되지 않은 경우, SQLite는 테이블에서 가장 큰 rowid보다 1 큰 수(다음 값)를 rowid로 선정함
  - INTEGER PRIMARY KEY 키워드를 가진 컬럼을 직접 만들면 이 컬럼은 rowid의 별칭(alias)가 됨
    - 이 경우 컬럼 이름과 rowid 이름으로 rowid에 접근 가능

- 데이터가 최대치에 도달한 경우 새 행을 삽입하려 하면 사용되지 않는 정수를 찾아서 사용
  - 일부 행 삭제 후 새 행을 삽입하면 삭제된 행의 rowid 재사용 시도
  - 만약 새로운 정수를 찾을 수 없으면 SQLITE_FULL 에러 반환

# [ALTER TABLE](#ddl)

- 기존 테이블의 구조 변경(수정)
- SQL의 ALTER TABLE이 지원하는 기능:
  - 테이블명 수정
  - 컬럼명 수정
  - 테이블에 새 컬럼 추가
  - 컬럼 삭제

## ALTER statement 사용예시

1. 테이블 이름 변경
2. 테이블 내 컬럼명 변경
3. 새 컬럼 추가(컬럼 스키마도 같이 설정 가능)
   - 새 컬럼에 입력되는 기본값은 NULL
   - DEFAULT를 이용해 컬럼을 생성하면서 기본 값 입력 가능
4. 컬럼 삭제
   - 삭제가 불가능한 경우:
   1. 컬럼이 다른 부분에서 참조되는 경우
   2. 기본 키인 경우
   3. UNIQUE 제약조건이 있는 경우

```
ALTER TABLE table_name RENAME TO new_table_name
ALTER TABLE table_name RENAME COLUMN column_name TO new_column_name
ALTER TABLE table_name ADD COLUMN the_new_column_name NOT NULL DEFAULT 'no data'
ALTER TABLE table_name DROP COLUMN the_new_column_name
```

## [DROP TABLE](#ddl)

- 테이블 삭제
  - 한 번에 하나의 테이블만 삭제 가능
  - 실행 취소 및 복구 불가
- DROP Table (테이블명)

```
DROP TABLE table_name
```

# DML

- INSERT, SELECT, UPDATE, DELETE 기능 수행
- 내가 원하는 데이터를 필터링해서 가져오기(SELECT)

## CML으로 실행하기

- 커멘드 라인에 sqlite3 입력
  
### DB 열기

- .open mydb.sqlite3(파일명)


### CSV데이터를 SQLite 테이블로 가져오기

- DML.sql 파일 생성 후 테이블 가져오기

## ORDER BY

- FROM clause 뒤에 작성
- 하나 이상의 컬럼을 기준으로 오름차순/내림차순 정렬
    - ASC(기본값) : 오름차순
    - DESC : 내림차순
- ORDER BY 기준은 여러 개를 입력할 수 있음
- NULL이 정렬 대상인 경우 가장 작은 값으로 간주하고 정렬됨

- 이름, 나이 데이터만 조회한 후 나이가 많은 순서로 정렬하여 표시
```
SELECT first_name, age FROM users ORDER BY age DESC; 
```

- 나이가 적은 순서대로, 나이가 같은 경우 balance(계좌 잔고)가 많은 순서대로 정렬
```
SELECT first_name, age, balance FROM users ORDER BY age ASC, balance DESC;
```

## Filtering Data

- 데이터에 필터링 조건을 설정하여 특정 데이터만 선택하거나, 중복을 제거하는 등의 용도로 사용 가능

### SELECT DISTINCT

- 조회 결과에서 중복 값 제거
- 지역, 품종 등의 종류 수를 조회할 때 유용

- 지역 값 중 중복되는 값을 제거한 후 오름차순(가나다순)으로 정렬
```
SELECT DISTINCT country from users ORDER BY country;
```