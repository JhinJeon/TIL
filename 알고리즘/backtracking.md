# 계산기

- 문자열로 된 계산식이 주어질 때, 스택을 사용하여 계산식의 값을 계산할 수 있다.

## step1 : 중위 표기법에서 후위 표기법으로 전환

1. 입력 받은 중위 표기식에서 토큰을 읽는다
  - 토큰 : 연산자와 피연산자를 구분하는 최소 단위
2. 토큰이 피연산자이면 토큰을 출력한다.
3. 토큰이 연산자일 때(괄호 포함), 

## 중위 표기법으로 표현하는 수식

1. 기호와 숫자를 하나씩 스택에 저장
2. 토큰(스택에 저장된 값) 하나 가져오기
3. top 변경(스택에 쌓여 있는 마지막 값)

## 백트래킹

- 해를 찾는 도중에 막히면(해가 아니면) 되돌아가서 다시 해를 찾는 기법
- 최적화 문제와 결정(decision) 문제 해결 가능
  - 결론이 '답이 없다' 또는 '최적의 답은 n이다' 일 때
- 조건을 만족하는 해의 존재 여부를 yes/no로 답하는 문제
  - 미로 찾기, n-Queen, Map coloring, 부분집합의 해 구하기 등에 사용


## 백트래킹 구현 원리

- 함수 정의
  - 함수 변수는 기본적으로 (값, 개수)가 포함됨
  - 뽑고 싶은 개수만큼 뽑은 경우 결과 반환
  - 뽑고 싶은 개수만큼 뽑지 않은 경우 별도의 작업(부분집합, 순열 위치교체 등) 후 재귀호출

## 백트래킹 vs 깊이우선탐색(DFS)

- 백트래킹은 불필요한 경로를 조기에 차단, DFS는 모든 경우의 수 고려
- 백트래킹은 탐색하는 경우의 수를 감소시키지만 최악의 경우(지수함수 시간을 요구하는 경우)에는 처리하기 어려움

## 백트래킹 실습 : 부분집합 구하기

1. for 구문을 여러 개 사용해서 확인하기

```python
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)
```

2. powerset을 구하는 백트래킹 알고리즘

```python
def backtrack(a, k, input):
    global MAXCANDIDATES    # MAXCANDIDATES = 원본 집합의 원소 개수
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k)  # 답인 경우 원하는 작업 실행

    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)
```

- 백트캐링의 기본적인 접근은 부분집합 구하기와 유사함
  - 0/1로 False/True 구분