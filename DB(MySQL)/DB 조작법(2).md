# 새로운 컬럼 추가하기

- ALTER (테이블명) ADD (컬럼명) (데이터 타입)

```sql
-- 10자 이하의 문자열로 구성된 TEST_COLUMN 추가
ALTER TEST_TABLE ADD TEST_COLUMN VARCHAR(10)
```

## 새로운 컬럼을 추가하면서 데이터도 넣고 싶다면?

> [] 안의 내용은 선택 사항

- CASE WHEN (조건문) THEN (조건이 참일 때) ELSE(거짓일 때) END [AS 컬럼명]

```sql
CASE
WHEN (MID_EXAM + FINAL_EXAM) // 2 >= 70
THEN "PASS"
ELSE "FAIL"
END AS RESULT
```

- WHEN-THEN을 여러 줄에 걸쳐 써서 여러 조건을 주는 것도 가능하다.

```sql
CASE
WHEN (MID_EXAM + FINAL_EXAM) // 2 >= 90 THEN "A"
WHEN (MID_EXAM + FINAL_EXAM) // 2 >= 70 THEN "B"
WHEN (MID_EXAM + FINAL_EXAM) // 2 >= 60 THEN "C"
ELSE "F"
END AS RESULT
```

# 데이터를 날짜 형식으로 전환

- (연)-(월)-(일)로 바꾸고 싶을 때 : "%Y-%m-%d"
  - m과 d를 대문자로 쓰면 영문자로 표시된다(예: August 5th)

# 날짜 간 차이(기간) 구하기

- DATEDIFF((시작일), (말일))

```sql
DATEDIFF("2023-01-01", "2023-02-01")
```