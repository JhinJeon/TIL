# Django 폼

요약
- [폼 적용 코드](#폼-적용-코드)
- [인증 시스템](#인증-시스템authentication)
- [데코레이터](#데코레이터decorator)
<hr>

- 사용자가 요청하는 데이터를 검증하는 수단
- Django 서버에 들어오는 요청들 중 비정상적이거나 악의적인 요청을 방지해야 함
- Django 폼은 유효성 검증 프로세스를 쉽고 빠르게 구현할 수 있도록 함

## Django 폼의 처리 영역

- 렌더링을 위한 데이터 준비 및 재구성
- 데이터에 대한 HTML forms 생성
- 클라이언트로부터 수신한 데이터 처리

## forms 클래스 선언

```python
# 개별 앱 디렉토리 내부에 forms.py 생성
from django import forms


class ArticleForm(forms, Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```

- form은 model field와 달리 TextField가 없음

## views.py 내에 new 함수에 새로운 코드 추가

```python
from .forms import ArticleForm

def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

```html
# new.html
# form 뒤에 .as_p를 붙이면 개별 항목마다 줄바꿈 제공

{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    {% comment %} <label for="title">Title: </label>
    <input type="text" name="title" id="title"><br>
    <label for="content">Content: </label>
    <textarea name="content" id="content"></textarea> <br> {% endcomment %}
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">뒤로가기</a>
{% endblock content %}
```

- 텍스트 입력 필드 만들기 : forms.py에서 CharField를 정의할 때 widget=forms.TextField 입력

```html
# forms.py의 클래스 항목

content = forms.CharField(widget=forms.Textarea)
```

## 메타데이터

- 데이터를 표현하기 위한 데이터
    - 사진 데이터의 촬영 시각, 사용 렌즈, 촬영 위치 등은 사진의 메타데이터
    
## 폼 적용 코드

```python
# views.py 파일
def create(request):
    form = ArticleForm(request.POST)    # update의 경우 instance=article 추가
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    # return redirect('articles:new')
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

## form과 modelform

- modelform과 form은 각자의 역할이 다른 것
    - form은 DB와 무관한 데이터를 받아서 처리할 때(로그인, 인증 등)
    - modelform은 DB와 유관한(저장할) 데이터를 받아서 처리할 때(글쓰기, 기록 등)
  
## 데코레이터(decorator)

- 기존에 작성한 함수를 수정하지 않고 새로운 기능을 추가해 주는 함수
- Django 자체적으로 내장 데코레이터 함수 지원
- 데코레이터를 사용하면 악의적인 접근을 차단하고 웹 서비스가 개발자가 의도한 방식대로 동작하도록 유도할 수 있음

### require_safe()

- require_get도 있지만 Django에서는 require_safe() 사용 권장

```python
@require_safe
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
```

## 인증 시스템(authentication)

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