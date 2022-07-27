## 스택(특정 항목의 연속된 개수) 세기
  관련 문제 : <https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq&categoryId=AV5PuPq6AaQDFAUq&categoryType=CODE&problemTitle=1979&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&>

## 문제되는 사항

- 문제를 해결하는 과정에서 에러는 발생하지 않는데 결과값이 전혀 다른 값으로 출력되는 문제가 있었다.
- 처음에는 주어진 단어 길이보다 같거나 길면 경우의 수를 세는 방식으로 구현했는데, 그 경우 빈 칸의 길이가 단어보다 긴 경우 조건에 해당한다고 처리해버리는 문제점이 있었다.
- 이차원 배열에서 특정 값이 연속되는 것을 구해야 할 때(퍼즐 문제 등) 정확하게 주어진 길이만큼 연속되는 경우를 도출하는 것이 어려웠다.
  
## 해결 방안(코드)

```python
k = 3
graph = [0,1,1,1,1,0,1,1,1,0]
streakmax = []
for x in graph:
    streak = 0
    if x == 1:
        streak += 1
    else:
        streakmax.append(streak)
        streak = 0
    if k in streakmax:
        print(streakmax.count(3))
    else:
        print(0)
```
## 위 코드를 작성하면서 배운 것:

- .count()를 써서 특정 값을 찾을 때 리스트 안에 그 값이 없으면 0(False)를 반환하는 게 아니라 에러가 발생한다. 그래서 위 코드처럼 if문을 활용하는 등의 방식으로 에러가 발생하지 않도록 해야 한다.