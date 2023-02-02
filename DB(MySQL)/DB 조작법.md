# 와일드 카드(Wild Card)

- 데이터 검색 필터로 사용

- \* : 표시한 부분에 아무 문자가 와도 됨(길이 제한 X)
  - MySQL에서는 '*' 대신 '%'를 사용한다.
- \_ : 표시한 부분에 아무 문자가 와도 됨(개수만큼 길이 제한)

# SQL - ORM 변형

- CREATE = create
- ORDER BY = order_by
- SELECT * = all()
- DELETE = remove()
- SELECT a = get('a')

# 조회하려는 데이터 형식을 바꿔서 표시하기

## 날짜 형식으로 바꾸려는 경우

1. DATE_FORMAT(필드명, 변경 형식)

- yyyy-mm-dd 형식으로 바꾸려는 경우

```sql
SELECT DATE_FORMAT(PUBLISHED_DATE, '%y-%m-%d')
```

2. TO_CHAR(필드명, 변경 형식)

- 이 방법은 날짜 정보를 문자열 타입으로 변환해야 할 때 유용하다.

```sql
SELECT TO_CHAR(PUBLISHED_DATE, 'yyyy-mm-dd')
```

> ## Note: 열 이름 변경 주의
> - 위 방식을 이용하는 경우 열 이름이 PUBLISHED_DATE에서 DATE_FORMAT(PUBLISHED_DATE, '%y-%m-%d')로 자동 변경된다.
> - 기존의 열 이름을 사용하려면 뒤에 'AS PUBLISHED_DATE'를 붙여야 한다.