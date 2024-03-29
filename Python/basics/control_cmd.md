## 제어문

- 조건문과 반복문으로 구분 가능
- 파이썬은 기본적으로 위에서 아래로 차례로 명령 수행
- 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요함
- 순서도(flowchart)로 표현가능

## 조건문

### if 조건문

- 참/거짓을 가릴 수 있는 조건식과 함께 사용
- 조건이 True인 경우 이후 들여쓰기 되어 있는 코드 블록을 실행
- 그 외의 경우 else 이후 들여쓰기 되어 있는 코드를 실행
  - else의 경우 조건을 선택적으로 부여할 수 있음
- *복수의 조건식*을 사용할 경우 'elif' 사용

```python
a = 5
if a > 5:   # if의 조건을 충족하지 않음
    print('5 초과')
else:   # 이하 들여쓰기 된 코드 실행
    print('5 이하')
```
  
```python
# 조건문 실습 : 홀수/짝수 구분
num = int(input())
if num % 2 == 1:
    print('odd')
else:
    print('even')
```

### 중첩 조건문

- 조건문을 다른 조건문과 중첩하여 사용할 수 있음(들여쓰기 주의)

```python
hat = 'red'
clothes = 'blue'
if hat == 'red':
    if clothes == 'red':
        print('red')
    else:
        print('semi red')
else:
    print('not red')
```

### 조건 표현식

- 조건 표현식을 일반적으로 조건에 따라 값을 정할 때 사용
- **삼항 연산자**라고도 부른다
  - *왼참 if  조건 else 오거*
  
```python
value = num if num >= 0 else value = 0  # 숫자의 절대값 표시
```

- 위 조건 표현식은 아래 조건문과 동일한 작업 수행

```python
if num >= 0:
    value = num
else:
    value = 0
```

### 반복문

- while
  - 조건식이 참인 경우 들여쓰기 된 코드를 반복적으로 코드 실행 
  - 종료 조건에 해당하는 코드로 반복문을 종료시켜야 함
    - 종료 조건을 지정하지 않으면 **무한 반복될 수 있음**

- for
  - 반복 가능한 개체(iterable)를 모두 순회하면 종료됨
  - 별도의 종료 조건이 필요하지 않음  

  > **iterable** : 순회할 수 있는 자료형과 함수  
  > 예) string, list, dict, tuple, range, set, enumerate

<span style="color:# 808080">문자열 순회</span>
  ```python
  for chr in chrs:
    print(chr)
  ```

  ```python
  for idx in len(chrs):
    print(chrs[idx])
  ```

<span style="color:# 808080">딕셔너리 순회</span>
  ```python
  for key in dic:
    print(key)
  ```

<span style="color:# 808080">enumerate 순회</span>
- enumerate(리스트, start = )
- <u>start에 숫자를 넣으면</u> 몇 번째 인덱스부터 시작할지 설정 가능

## **List Comprehension**
  - 표현식과 제어문을 통해 특정 조건의 리스트를 간결하게 생성 가능

1. 기본형 : [code for 변수 in iterable]  
    ```python
    cubic_list= [number ** 3 for number in range(1,4)]
    ```
    ```python
    my_list = [i for i in range(5)]
    ```

2. 조건문 추가 : [code for 변수 in iterable if 조건식]

    ```python
    # 짝수만 넣기
    my_list = [i for i in range(11) if i % 2 == 0]
    ```

## Dictionary Comprehension
1. 기본형 : {key : value for 변수 in iterable}
    ```python
    cubic_dict = {number: number ** 3 for number in range(1,4)}
    ```
2. 조건문 추가 : 
  - 방법1) {(key 조건) : (value 조건) for key,value in my_dict.items()}
  - 방법2) {key : value for 변수 in iterable if 조건식}

    ```python
    original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

    even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
    print(even_dict)  # jack : 38, michael : 48
    ```

> 추가) 궁금한 사항에 대해 피드백 받은 내용
> 
> 방법 1과 방법 2는 구조적으로 다른 코드이다.
> 
> 다만 실질적으로 결과는 같다. 차이점이라면 방법 1은 조건식이 복잡할 때 쓰기 어렵고, 
> 방법 2는 코드 가독성이 떨어지는 문제가 있다.
> 
> 따라서 방법 2는 그냥 *'이렇게 작성할 수도 있다'* 정도만 알고 넘어가도 충분하다.

### 반복 제어

  - **break** : 반복문 즉시 종료(반복문 탈출)

    ```python
    a = 0
    while a < 5:
        if a == 2:
            break
        print(a)
        a += 1
      # return : 0,1,2
      ```

  - **continue** : continue 이후의 코드 블록을 수행하지 않고, 다음 블록(조건) 실행
    ```python
    while a < 5:
        if a == 3:
            continue
        print(a)
        a += 1
    # return : 0,1,2,4
    ```
  - for-else : 끝까지 반복문을 실행한 후 else문 실행
    - break를 통해 중간에 종료되는 경우 else 이하는 실행되지 않음
    - <u>for 구문이 잘 실행되는지 체크하는 용도</u>로도 사용됨
    - for와 else를 **동일한 여백만큼 들여쓰기** 하면 됨  

    ```python
    # 이하 코드는 '작업 끝'이 출력되지 않음
    for a in range(5):
        print(a)
        if a == 3:
            break
    else:
        print('작업 끝')
    ```

  - pass : 아무 동작 없음(문법적으로 필요한 경우에만 삽입)

### 복합 연산자

- 연산과 할당(저장)을 합쳐 놓은 것
- 반복문을 실행하면서 개수를 세는 경우 사용


### 파이썬의 범위(scope)

- global scope
  - 코드 어디에서도 참조할 수 있는 공간
  - global variable : global scope에 정의된 변수 
  
- local scope
  - 함수 내부에서 정의되고, 함수 내에서만 참조 가능
  - local variable : local scope에 정의된 변수

### 변수의 주기(lifecycle)

- built-in scope : 파이썬이 실행된 이후부터 영구히 유지
- global scope : 모듈이 호출된 시점 이후 또는 인터프리터가 끝날 때까지 유지
  - (global scope는 프로그램이 살아있는 한 유지됨)
- local scope : 함수가 호출될 때 생성되고, 종료될 때까지 유지
- 함수 내에서는 바깥 변수를 불러올 수는 있지만 그것을 수정할 수는 없음
---
- scope 순서 : LEGB
  - local-> enclosed-> global-> built-in 순서로 탐색

- global
  - 현재 코드 전체 블록에 적용
  - global에 나열된 이름은 같은 코드 블록에서 global 앞에 등장할 수 없음
  - global에 나열된 변수는 parameter, for 루프 대상, 클래스, 함수 등으로 정의되지 않아야 함

- nonlocal
  - global을 제외한 가장 가까운 scope의 변수들을 연결하도록 함
    - enclosed 변수 = local 변수
  - nonlocal에 나열된 이름은 enclosed에서 등장해야 함
  - nonlocal에 나열된 변수는 parameter, for 루프 대상, 클래스, 함수 등으로 정의되지 않아야 함

- map
  - 순회 가능한 모든 iterable에 function 적용

- filter
  - 순회 가능한 모든 iterable에 function을 적용하고, 그 중에서 True인 값만 반환

- zip(*iterables)
  - 복수의 iterable을 모아 튜플을 원소로 하는 zip object 반환
  ```python
  girls = ['Amy','Ashe']
  boy = ['Sam','Tom']
  pair = zip(girls,boys)
  print(list(pair))
  #  [('Amy','Sam'),('Ashe','Tom')]
  ```

### lambda 함수
- lambda 함수는 함수의 이름을 지정하지 않고 사용
- 간단한 함수나 자주 호출하지 않는 함수를 작성할 때 사용
```python
def solution(b, h):
    return b * h * 0.5
print(solution(5,6))
```

```python
# 위의 코드를 lambda 함수로 작성
solution = lambda b, h : 0.5 * b * h
print(solution(5, 6))
```

### 재귀 함수(recursive)

- 자기 자신을 호출하는 함수
- 무한한 호출을 목표로 하지 않음
- 알고리즘 구성에 유리
- 변수 사용을 줄이고 코드 가독성을 높일 수 있음
- 1개 이상의 종료 상황에 수렴하도록 작성
- 입력 값이 커질수록 연산이 오래 걸림
```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
```

```python
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```