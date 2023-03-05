# Python 환경설정

1. python mysqlclient 설치

- 설치하려면 visual studio Build Tools가 있어야 한다(별도 설치).
  - visual studio 설치 페이지에서 build tools 검색 > 빌드 도구 설치

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
# my_settings.py
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',    [1]
        'NAME': 'django_insta',                  [2]
        'USER': 'root',                          [3]
        'PASSWORD': 'password',                  [4]
        'HOST': 'localhost',                     [5]
        'PORT': '3306',                          [6]
    }
}
```

```py
# settings.py
import my_settings.py

DATABASES = my_settings.DATABASES
```

4. 마이그레이션 실행(python manage.py migrate)

> ## 마이그레이션이란?
> - 마이그레이션은 시스템 간 데이터나 SW가 이동하는 작업 또는 과정이다.
> - 데이터 마이그레이션이 이루어지면 데이터가 기존의 시스템에서 새로운 시스템으로 이동하며, 대체된다.