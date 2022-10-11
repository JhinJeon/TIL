🔔목차🔔

- [Static file(정적 파일)](#static-file정적-파일)
- [Media file](#media-file)
- [웹 서버와 정적 파일](#웹-서버와-정적-파일)
- [static files 구성](#static-files-구성)
  - [Django Template Tag](#django-template-tag)
- [static file 관련 핵심 설정(core settings)](#static-file-관련-핵심-설정core-settings)
- [MEDIA_ROOT](#media_root)
- [ImageField](#imagefield)
- [업로드한 이미지 출력](#업로드한-이미지-출력)


# Static file(정적 파일)

- 파일 자체가 고정되어 있고, 서비스 중에도 추가나 변경이 없는 파일
- 이미지, 자바스크립트, CSS 등 미리 준비된 파일
- Django는 staticfiles 앱으로 정적 파일과 관련된 기능 지원

# Media file

- static file의 일종
- 사용자가 웹에서 업로드하는(user-upload) 정적 파일
- 유저가 업로드한 모든 정적 파일

# 웹 서버와 정적 파일

- 웹 서버의 기본동작은 특정 위치에 있는 리소스를 요청(request) 받아서 
- 응답(HTTP response)을 처리하고 제공(serving)하는 것
- 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공하는 역할 수행

# static files 구성

1. INSTALL_APPS에 django.contrib.staticfiles가 포함되었는지 확인
2. settings.py에서 STATIC_URL 정의
3. 앱의 static 폴더에 정적 파일 위치하기
4. 탬플리셍서 static 태그를 사용하여 저장된 경로에 있는 정적 URL 생성

```html
{% load static %}

<img src="{% static 'sample_img.jpg' %}" alt="sample_imgs">
```

## Django Template Tag

1. load tag

- 특정 라이브러리, 패키지에 등록된 모든 템플릿 태그와 필터를 로그

```html
{% load %}
```

2. static tag

- static root('')에 저장된 정적 파일에 연결

```html
{% static '' %}
```

# static file 관련 핵심 설정(core settings)

1. STATIC_ROOT

- Django에서 사용하는 모든 정적 파일을 한 곳에 몰아넣는 경로
- collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
- **개발 과정에서 settings.py의 DEBUG값이 True인 경우 STATIC_ROOT 미적용**
  - 실제 배포 환경에서는 자세한 오류 메세지를 사용자에게 반환하지 않아야 함

2. STATICFILE_DIRS

- DEFAULT : empty( [] )
- app/static(기본 경로) 외에 추가 정적 파일 경로 목록을 정의하는 리스트
- 추가 파일 디렉토리에 대한 전체 경로를 문자열 형태로 작성

3. STATIC_URL

- DEFAULT : None
- STATIC_ROOT에 있는 정적 파일을 참조할 때 사용할 URL
- **실제 파일이나 디렉토리가 아니며, URL로만 존재**
- 비어 있지 않은 값으로 설정하려면 URL 문자열은 슬래시(/)로 끝나야 함

```python
# 작성 예시
STATIC_URL = '/static/'
```

# MEDIA_ROOT

- 사용자가 업로드한 미디어 파일을 저장할 디렉토리의 절대 경로
  - **DB에 저장되는 것은 파일이 아니라 파일 경로**
- 반드시 STATIC_ROOT와 다른 경로로 지정해야 함

# ImageField

- 이미지 업로드 기능을 제공할 때 사용
- 파라미터로 blank=True를 입력하면 사용자가 이미지를 첨부하지 않아도 작성이 가능하게 설정할 수 있음
  - 기본 값은 False, 이 경우 이미지를 업로드하지 않으면 콘텐츠를 게시할 수 없음
- null=True 입력 시 이미지를 업로드하지 않고 저장하는 경우 DB에 저장되는 값은 NULL
  - ImageField는 URL을 문자열 형태로 저장하므로, 빈 값을 저장할 때 null 대신 blank(빈 문자열)를 사용하는 것이 권장됨 

```python
class Article(modles.Model):
    image = models.ImageField(blank=True)
```

# 업로드한 이미지 출력

- html 코드에 {% if article.image %}를 입력하면 이미지 데이터가 있는 경우에만 데이터를 가져오도록 할 수 있다.