# Django 폼

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
