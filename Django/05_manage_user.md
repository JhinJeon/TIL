# 인증 시스템(authentication)

🔔
[인증이란?](#인증이란)
[사용자 지정 모델 생성하기](#대체-모델-생성하기)
[쿠키](#쿠키)
[세션](#세션)
[자동 로그아웃](#쿠키의-수명)
[회원가입](#회원가입)

## 1. 인증이란?
- Authentication(인증)
  - 사용자가 자신이 누구인지 확인하는 체계
  - 신원 확인

- Authorization(권한, 허가)
  - 사용자에게 권한 부여
  - 인증된 사용자의 작업 수행 범위 결정

- 보통 Authentication과 Authorization을 합쳐서 Authentication System(인증 시스템)이라고 부른다.
- 관련 경로, 키워드, 변수명 등은 accounts로 저장하는 것을 권장

## 사용자 지정(custom user) 모델

- Django는 사용자 지정 모델 사용을 강력하게 권장(highly recommended)
- 사용자 지정 모델은 기본 모델과 동일하게 작동하며, 필요 시 맞춤 설정 가능

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```
- 사용자 지정 모델 대체 작업은 첫 migrate를 실행하기전에 마쳐야 함
  - migration이 실행된 후 시도하는 경우 기존의 테이블 간 관계를 망가뜨릴 수 있음
  - makemigrations -> custom usermodel -> migrate 순으로 실행
  
> Q : 만약 프로젝트 도중에 변경해야 하는 경우라면?
> 
> A : 데이터베이스를 초기화한 뒤 진행할 수 있다.
>
>  초기화 과정 : migrations 파일 삭제 -> db.sqlite3 삭제 -> migration 진행

## 대체 모델 생성하기

- AbstractUser를 상속받는 커스텀 사용자 클래스 생성

# 대체 모델 생성 코딩

2. settings.py에서 AUTH_USER_MODEL = 'accounts.user' 입력

```python
# settings.py
AUTH_USER_MODEL = 'accounts.user'
```

3. admin.py에 커스텀 사용자 모델 등록

# 2. 쿠키

## 쿠키

- 서버가 사용자 웹 브라우저에 전송하는 작은 데이터 조각
- 최초에 웹 브라우저가 쿠키를 로컬 컴퓨터에 저장한 후, 클라이언트가 동일 서버에 재요청 시 저장된 쿠키를 함께 전송
- 쿠키는 두 요청이 모두 동일한 브라우저에서 들어왔는지 판단할 때 사용
  

# 쿠키 사용 목적(응용)

1. 세션 관리
   - 로그인 상태 유지
   - 상태 정보 기억
   - 장바구니 기억
   - 공지 일정 기간 동안 다시 안 보기

2. 개인화
   - 사용자 선호 기억
   - 테마 설정

3. 트래킹
   - 사용자 행동 기록 및 분석
   - 맞춤형 광고, 상품, 서비스 등 표시

## 세션

- 사이트와 특정 브라우저 사이의 상태(state)를 유지시키는 방법
- 클라이언트가 서버에 접속하면 서버는 session id를 발급하고, 클라이언트는 이를 쿠키에 저장
  - 클라이언트가 다시 동일한 서버에 접속하면 요청과 쿠키를 함께 전달
- 쿠키에는 session id만 저장
- Django는 세션의 복잡한 매커니즘에 대한 부담을 완화해 줌

## 쿠키의 수명

- 세션 쿠키
  - 현재 세션이 종료되면 삭제됨
  - 브라우저 종료와 함께 세션 삭제

- 지속 쿠키(persistent cookies)
  - 만료 속성에서 지정한 날짜 또는 기간이 도래하면 세션 삭제

# 3. 웹 요청에 대한 인증

## 로그인

- 세션을 생성(create)하는 과정
- User를 생성하는 건 회원가입(등록)

## 인증 폼

## 로그인 구현

1. 로그인 진행 페이지 생성
2. views와 urls에 로그인 페이지 처리 코드 작성

## 로그아웃

- 로그아웃은 세션을 삭제하는 과정

```python
from django.contrib.auth import logout as auth_logout

def logout(requests):
    auth_logout(requests)
    return redirect('articles:index')
```

## 회원가입

- user를 생성하는 과정
- built-in form인 UserCreationForm 사용

### UserCreationForm

- username, password, Password2 필드로 구성

## 커스텀 폼

- django에서는 사용자 지정 모델을 직접 참조하는 것을 권장하지 않음

```python
# forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    model = get_user_model()

# views.py
from .forms import CustomUserCreationForm
```

## 회원탈퇴

```python
def delete(request):
    auth_logout(request.user)
    request.user.delete()
    return redirect('articles:index')
```

## 회원탈퇴 기능 구현 시 주의사항

- 회원탈퇴는 로그인 상태에서 진행할 수 있도록 해야 함
- 사용자 정보를 지워도 세션 정보(로그인 인증)는 없어지지 않음
- 회원탈퇴를 하면서 로그아웃을 같이 구현하려면 **로그아웃 후 회원탈퇴**
  - 반대로 하면 로그아웃 시도 시 입력할 개체가 없는 문제 발생