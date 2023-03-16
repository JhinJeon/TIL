# Python 환경설정

1. python mysqlclient 설치

- 설치하려면 visual studio Build Tools가 있어야 한다(별도 설치).
  - visual studio 설치 페이지에서 build tools 검색 > 빌드 도구 설치
  - 워크로드 > C++를 사용한 데스크톱 개발 체크

```
pip install mysqlclient
```

1. (DB가 없는 경우) DB 생성

```
mysql> create database django_insta character set utf8mb4 collate utf8mb4_general_ci;
Query OK, 1 row affected (0.01 sec)

mysql> use django_insta
mysql> show tables;
Empty set (0.01 sec)
```

1. settings.py에 DATABASES={}에 테이블 정보 입력

```py
# settings.py
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_insta',   # mysql에서 생성한 DB 이름
        'USER': 'root',           # mysql에서 DB 접속에 사용하는 사용자 정보
        'PASSWORD': 'password',
        'HOST': 'localhost',      # 접속 포트(로컬: 127.0.0.1)
        'PORT': '3306',           # 포트 번호(기본: 3306)
    }
}
```

4. 마이그레이션 실행(python manage.py migrate)

> ## 마이그레이션이란?
>
> - 마이그레이션은 시스템 간 데이터나 SW가 이동하는 작업 또는 과정이다.
> - 데이터 마이그레이션이 이루어지면 데이터가 기존의 시스템에서 새로운 시스템으로 이동하며, 대체된다.

- ORM(Python의 클래스와 객체를 바탕으로 SQL식 DB로 바꿔주는 언어)이 자동으로 MySQL DB와 Django model를 호환되게 해준다.

5. 설정 확인

- django에서 python manage.py inspectdb로 확인할 수 있다.
- db가 성공적으로 연동된 경우 테이블 정보가 표시된다.
