🔔목차🔔

- [반복과 재귀](#반복과-재귀)
- [완전검색](#완전검색)
  - [고지식한 방법(Brute-Force)](#고지식한-방법brute-force)
  - [순열](#순열)
    - [재귀 호출을 이용한 순열 생성](#재귀-호출을-이용한-순열-생성)
    - [순열을 직접 구현하는 방법](#순열을-직접-구현하는-방법)
- [탐욕 알고리즘(그리디)](#탐욕-알고리즘그리디)


# 반복과 재귀

- 반복과 재귀는 유사한 작업 수행 가능
  - 반복은 주어진 작업이 해결될 때까지 지속 수행
  - 재귀는 주어진 해를 구하기 위해 동일하면서 더 작은 해를 이용하는 방법(큰 문제를 작게 쪼개서 처리)

- 일반적으로 재귀 알고리즘은 반복 알고리즘보다 더 많은 리소스를 요구함(특히 입력값이 커질수록)

# 완전검색

## 고지식한 방법(Brute-Force)

- 자료의 처음 부붙부터 끝 부분까지 순차적으로 탐색
- 대부분의 문제에 적용 가능
- 알고리즘 설계가 빠르지만 처리 속도가 느릴 수 있음
- 문제에 포함된 자료(인스턴스)의 크기가 작은 경우 유용함
- 완전 검색으로 답을 도출한 후, 다른 알고리즘을 사용하여 시간 및 메모리 사용량을 단축하는 게 좋음

## 순열

- 순서화된 요소들의 집합에서 최적의 방법을 찾을 때 사용
- n개의 요소들에 대해서 n!개의 경우의 수 도출

### 재귀 호출을 이용한 순열 생성

```python
array = []
p = [1,2,3,4]

def permutation(n, k): # 배열 p에서 k개 뽑기(n은 선택된 원소의 수)
    if n == k:
        print(p)
    else:
        for i in range(n,k):
            p[n], p[i] = p[i], p[n]
            permutation(n+1,k)
            p[n], p[i] = p[i], p[n]

```

### 순열을 직접 구현하는 방법

1. 앞쪽부터 인덱스를 차례대로 바꾸기(순서만 바꾸는 문제에 유용)
2. 값 사용 여부를 판단하는 used 리스트를 별도로 만들기

# 탐욕 알고리즘(그리디)