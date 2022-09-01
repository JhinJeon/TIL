# 기본 설정 보충


## settings.py의 TEMPLATES 설정

-'DIRS'에 설정하는 경로는 어느 폴더에서 html 파일을 찾을지 설정

```python
# 프로젝트 디렉토리의 settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # 기본(최상위) 디렉토리의 templates 폴더
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
## 프로젝트에 include 선언 + 개별 앱에 앱 이름 선언하기 : 확장성을 고려한 프로그래밍

```python
# 프로젝트의 urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),

# 개별 앱의 urls.py
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
]
```

models.py : 클래스 선언

CharField(max_length=) = 제목 등을 저장하는 필드, 글자 수 제한 필수
TextField() = 본문 등의 데이터를 저장하는 필드

### DB에 새로운 데이터 입력(create)

- views.py에 DB의 어떤 위치에 어떤 정보를 보내는지 입력해야 함
- 클래스를 불러와서 인스턴스를 선언할 때 : 클래스 안에 키워드 인자를 입력해서 정의하기도 가능
```python
# 개별 앱의 views.py
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article()     # Article(title=title, content=content)도 가능
    article.title = title
    article.content = content

    return render(request, 'articles/create.html')

# 개별 앱의 models.py
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

## 게시(create) 이후 다음 화면으로 넘어가도록 설정

- action="{% url '(html 파일 경로)' %}" method="GET"
``` python
# 게시글 작성 페이지 new.html
{% extends 'base.html' %}

{% block content %}
<form action="{% url 'articles:create.html' %}" method="GET">
  <h1>NEW</h1>
  <form action='#' method='GET'
  <label for = "title">Title: </label>
  <input type="text" id="title" name="title">
  <br>
  <label for="content">Content: </label>
  <textarea name="content" id="content"></textarea>
  <input type="submit">
</form>
{% endblock content %}
```

## read(조회)

```python
{% extends 'base.html' %}

{% block content %}
  <h1>Article</h1>
  <a href="{% url "articles:new" %}">NEW</a>    # href의 값은 urls.py에 정의한 이름 사용
    # articles 디렉토리의 url.py 파일의 new 변수에 있는 값 참조
  {% for article in articles %}
    <hr>
    <p>글 번호 : {{ article.pk }}</p>
    <p>글 제목 : {{ article.title }} </p>
    <p>글 내용 : {{ article.content }}</p>
  {% endfor %}
{% endblock content %}
```

## redirect

- 새로운 게시글을 작성한 후 게시판 화면으로 돌아가게 하고 싶을 때
- redirect는 기존의 설정된 요청에 새로운 요청을 덮어서 전송

```python
from django.shortcuts import render, redirect
from .models import Article

# views.py 일부

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()

    # return render(request, 'articles/create.html')
    # render로 완료 화면을 생략하려 하면 경로가 제대로 바뀌지 않으면서 빈 껍데기만 불러오는 문제 발생
    return redirect('articles:index')  # 완료 화면을 생략하려면 redirect 사용
```

## DB에 변화를 줄 떄

GET : 데이터 조회
- Get도 데이터 요청 기능 수행 가능, 전송 시 URL 뒤에 '/?정보' 추가(URL에 드러남)
POST : 데이터를 생성, 수정, 삭제, 변경할 때
- POST로 요청하는 경우 Querystring을 통해 전송됨
- URL에 DB의 구조를 html의 body에 감출 수 있음
- csrf token 필요(보안 토큰)

```python
# new.html파일
{% block content %}
  <h1>NEW</h1>
  <form action="{% url "articles:create" %}" method="POST">
  {% csrf_token %}  # csrf 토큰
  <label for = "title">Title: </label>
  <input type="text" id="title" name="title">
  <br>
  <label for="content">Content: </label>
  <textarea name="content" id="content"></textarea>
  <input type="submit">
</form>
{% endblock content %}
```

## 상세 페이지 보기(개별 반응형 웹 페이지)

- <> 안에 반응형 변수 넣기

```python
# 개별 앱의 urls.py
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
]

# 개별 앱의 views.py
```

- 메인 화면에서 세부 정보 화면으로 넘어가는 링크 : 세부 화면을 찾는 기준을 적어줘야 함

```python
# index.html
{% extends 'base.html' %}

{% block content %}
  <h1>Article</h1>
  <a href="{% url "articles:new" %}">NEW</a>
  {% for article in articles %}
    <hr>
    <p>글 번호 : {{ article.pk }}</p>
    <p>글 제목 : {{ article.title }} </p>
    <p>글 내용 : {{ article.content }}</p>
# articles 디렉토리의 detail 함수 실행 - 키 번호가 pk에 해당하는 값을 article로 불러오기
    <a href="{% url "articles:detail" article.pk %}">DETAILS</a>
  {% endfor %}
{% endblock content %}
```

## 게시물 게시 후 바로 세부 사항으로 이동하게 만들기

```python
# views.py
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()

    # return render(request, 'articles/create.html')
    # render로 완료 화면을 생략하려 하면 경로가 제대로 바뀌지 않으면서 빈 껍데기만 불러오는 문제 발생
    return redirect('articles:detail', article.pk)  # 완료 화면을 생략하려면 redirect 사용
```

## 게시물 삭제하기

- urls.py에 새로운 패턴 생성
- 패턴 생성 시 삭제할 대상도 설정해줘야 함

```python
# 개별 앱 urls.py
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]

# 개별 앱 views.py
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```

- 게시물 삭제는 POST 요청으로 진행 
  - POST 요청은 form 태그, csrf 토큰을 사용해야 함
    
```python
# 개별 앱 detail.html(삭제 버튼 추가)
{% block content %}
<h1>DETAIL</h1>
<h3>{{ article.pk }}번째 글</h3>
<hr>
<p>제목 : {{ article.title }}</p>
<p>내용 : {{ article.content }}</p>
<p>작성시간 : {{ article.created_at }}</p>
<p>수정시간 : {{ article.updated_at }}</p>
<hr>
<a href="{% url "articles:index" %}">INDEX</a>
<form action="{% url 'articles:delete' article.pk %}" method="POST">
  {% csrf_token %}
  <input type='submit' value='DELETE'>
</form>
{% endblock content %}
```

## 게시물 변경(수정)

- edit과 update 추가
- edit은 새로운 정보 작성용, update는 edit으로 작성한 정보 반영용

```python
# 개별 앱 urls.py
from django.urls import path
from . import views

# update는 함수만 생성
app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update', views.update, name='update'),
]


# 개별 앱 views.py
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect("articles:detail", article.pk)


# 개별 앱 edit.html(수정한 정보 전송용)
{% extends 'base.html' %}

{% block content %}
 <h1>EDIT</h1>
 <form action="{% url "articles:update" article.pk %}" method="POST">
  {% csrf_token %}
  <label for = "title">Title: </label>
  <input type="text" id="title" name="title" value="{{ article.title }}">
  <br>
  <label for="content">Content: </label>
  <textarea name="content" id="content">{{ article.content }}</textarea>
  <input type="submit">
</form>
{% endblock content %}

```
- edit.html에서 작성한 정보를 서버에 전송 - update 인스턴스를 호출하여 정보 처리 - 수정된 내용 반영

## 기본 관리자 페이지(Admin site)

- 서버 관리자가 활용하는 페이지
- 모델 class를 admin.py에 등록하고 관리
- 레코드 생성 여부 확인에 용이, 직접 레코드 삽입 가능

### 관리자의 모델 관리

- 데이터베이스 직접 편집 가능
- GUI 기반의 관리자용 페이지 제공

```python
# 개별 앱의 admin.py
from django.contrib import admin
from .models import Article

# Register your models here.

admin.site.register(Article)
```