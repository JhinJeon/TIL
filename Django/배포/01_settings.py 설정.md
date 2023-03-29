# 환경 변수 설정

- Django SECRET_KEY와 같은 기밀 정보들은 배포 환경에 노출되면 안 된다.
- 따라서 별도의 환경 변수로 저장하여 관리해야 한다.

# django-environ 사용

1. 라이브러리 설치

```
pip install django-environ
```

2. .env 파일 만들기

- 파일 위치는 django-environ이 자동으로 인식한다.

3. .env에 사용할 환경 변수 입력

- SECRET_KEY, DB 비밀번호 등의 정보를 저장하면 된다.

4. settings.py 설정

- .env에 저장한 값을 불러오려면 os.environ.get('.env에 선언한 변수명') 으로 불러온다.

```py
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
```

5. .gitignore에 .env 추가

- .env가 git에 커밋된다면 별도의 환경변수로 관리하는 의미가 없다.
- .gitignore에 .env를 입력하면 환경 변수 파일의 위치를 자동으로 찾아준다.

# 주의사항

- 배포 환경에서는 .env 파일이 자동으로 업로드되지 않으므로, 환경 변수를 별도로 설정해 주어야 한다.
