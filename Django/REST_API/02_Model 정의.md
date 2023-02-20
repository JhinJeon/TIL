# 모델 생성하기

- 개별 앱 디렉토리의 models.py에 DB 역할을 하는 모델을 정의한다.
- 각 모델에 들어가는 데이터의 형식을 정의할 수 있다.

```python
# models.py
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

# ModelSerializer 만들기

- 모델에 DB 형식으로 저장된 값을 JSON 형식으로 변환한다.
- class Meta에 JSON으로 변환할 모델 본체(소스)와 필드를 입력한다.

  - fields:에 '\_\_all\_\_'을 입력하면 해당 모델의 모든 필드를 참조한다.

- serializer를 정의할 때 별도의 필드를 정의해서 JSON 파일에 포함시킬 수 있다.

```python
# 앱 디렉토리의 serializers.py
from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):

    # Article 모델의 일부 필드 데이터만 가져오기
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class CommentSerializer(serializers.ModelSerializer):

    # Comment 모델의 모든 필드 데이터를 가져오기(article 필드는 읽기 전용 설정)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    # 댓글 정보를 가져온 후 Article 모델의 필드 정보들과 함께 보내기
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

```
