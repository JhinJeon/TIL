## 스도쿠 무결성 검증 코드

### 이차원 배열에서 선택한 범위 안의 값들을 계산하는 알고리즘

-스도쿠 보드에 기입된 숫자가 규칙에 맞게 작성되었는지 확인하려면 세 가지를 확인해야 한다:

1. 열(가로)에 있는 숫자들이 1부터 9까지 빠짐없이 있는가?
2. 행(세로)에 있는 숫자들이 1부터 9까지 빠짐없이 있는가?
3. 9 * 9 보드를 3 * 3 구역 9개로 나눴을 때, 각 구역마다 1부터 9까지 빠짐없이 있는가?

- 이 중에서 1번과 2번은 문제가 없었는데 3번의 경우 인덱스 범위 조정에 어려움이 있었다.

- 구글링을 해 보니 아래처럼 for 문을 4중으로 활용하여 인덱스 범위를 조절하는 코드가 나왔다.

```python
n = 5
m = 3
graph = [n * [0] for _ in range(n)]
total_max = 0
for column in range(n-m+1):
    for row in range(n-m+1):
        total = 0
        for column_idx in range(column,column+m):
            for row_idx in range(row,row+m):
                total += graph[column_idx][row_idx]
        if total > total_max:
            total_max = total
print(total_max)
```

코드 리뷰

- 큰 사각형 안에서 작은 사각형 범위 안의 값을 계산할 때 인덱스 범위가 벗어나거나 그래프 전체를 포괄하지 못하는 불상사가 발생하지 않아야 한다.
  
- 또한 이차원 리스트 안에 있던 값들을 저장해야 할 떄는, for 구문의 줄 위치를 잘 봐서 잘못된 값이 나오지 않도록 주의해야 한다.

관련 문제 :

<https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE&problemTitle=2001&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1> 
