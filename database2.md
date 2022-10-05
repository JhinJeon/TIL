🔔목차🔔

- [외래 키(Foreign Key)](#외래-키foreign-key)
  - [참조 무결성](#참조-무결성)
- [관계](#관계)
  - [RDB에서의 관계](#rdb에서의-관계)
- [Comment(댓글)](#comment댓글)
- [Django Relationship fields](#django-relationship-fields)
  - [Comment 모델 정의](#comment-모델-정의)
  - [Django 관계 필드에서 외래 키의 필수 인자](#django-관계-필드에서-외래-키의-필수-인자)
    - [\(참고) 데이터 무결성](#참고-데이터-무결성)
  - [역참조](#역참조)
- [댓글 기능 구현하기](#댓글-기능-구현하기)
  - [댓글 개수 출력하기](#댓글-개수-출력하기)
  - [댓글이 없을 때 대체 콘텐츠 출력하기](#댓글이-없을-때-대체-콘텐츠-출력하기)

# 외래 키(Foreign Key)

- 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
- 참조되는 테이블의 기본 키를 가리킴
- 각 행에서 서로 다른 테이블 간의 관계를 만드는 데 사용
- 참조하는 테이블 행 1개의 값은 참조되는 측 테이블의 행 값에 대응
- 참조하는 테이블 행 여러개가 참조되는 테이블의 동일한 행 참조 가능

## 참조 무결성

- 데이터베이스 관계 모델에서 관련된 2개의 테이블 간 일관성
- 외래 키가 선언된 테이블의 외래 키 속성(열)의 값은 그 테이블의 부모가 되는 테이블의 기본 키 값으로 존재해야 함
  - 없는 값을 외래 키로 사용할 수 없음

# 관계

- 테이블 간 상호작용을 기반으로 설정되는 여러 테이블 간 논리적 연결

## RDB에서의 관계

- 1:1 : 한 테이블의 단일 레코드가 다른 테이블의 레코드 한 개와 관련된 경우
- N:1 : 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우
- N:N : 한 테이블의 0개 이상 레코드가 다른 테이블의 0개 이상 레코드와 관련된 경우, 양쪽 모두에서 N:1 관계를 가짐

# Comment(댓글)

- Comment 모델과 Article 모델 간 관계 설정
- 0개 이상의 댓글은 1개의 게시글에 작성될 수 있음

# Django Relationship fields

## Comment 모델 정의

```python
class Comment(models.Model):
    article = models.Foreignkey(Article, on_delete=models.CASCADE)  # Article : 댓글을 달 게시물 모델
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):      # 조회 시 content의 내용 표시
        return self.content
```

## Django 관계 필드에서 외래 키의 필수 인자

1. 참조하는 model class
2. on_delete 옵션 : 외래 키 참조 객체가 사라졌을 때 외래 키를 보유한 객체를 어떻게 처리할지 결정
   - CASCADE : 부모 객체(게시글)이 삭제되었을 때 이를 참조하는 객체(댓글)도 삭제
   - PROTECT, SET_NULL, SET_DEFAULT 등도 사용 가능

### \(참고) 데이터 무결성

- 데이터의 정확성과 일관성을 유지하고 보증하는 것
- 무결성 제한의 유형(원칙)
    1. 참조 무결성 : 참조하려는 객체가 존재해야 함
    2. 개체 무결성 : 참조하려는 개체는 고유해야 함
    3. 범위 무결성 : 참조 범위는 유효해야 함

## 역참조

- 나를 참조하는 테이블(나를 외래 키로 지정한 테이블)을 참조(접근)하는 것
- N:1 관계에서 외래 키를 보유하지 않은 1이 N을 참조하는 경우

# 댓글 기능 구현하기

## 댓글 개수 출력하기

1. length 사용

```
{{ article.comment_set.all|length }}
```

2. count() 사용

```
{{ article.comment_set.count }}
```

## 댓글이 없을 때 대체 콘텐츠 출력하기

{% if comments%} 이후의 {% for ~ %}와 {% endfor %} 사이에 {% empty %} 삽입
- 불러온 댓글 정보가 없는 경우 {% empty %}와 {% endfor %} 사이의 정보 출력