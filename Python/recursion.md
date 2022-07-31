## 재귀함수

- 자기 자신을 호출하며 점점 더 깊게 들어가는 함수
- 재귀 깊이가 깊어질수록 범위가 작아짐
- 재귀탈출조건(base case)과 점화식으로 구성됨
  - base case를 설정하지 않으면 maxdepth error 발생
- 코드를 직관적이고 간결하게 표현할 수 있다
- 메모리 사용량과 처리 속도에서 불리하다

```python
def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(4)) # 결과 : 3
```

- 모든 재귀함수는 반복문(for)으로도 표현 가능

```python
def fibonacci(n):
  fibonacci_list = []
  for i in range(n):
    if i == 0 or i == 1:
      fibonacci_list.append(1)
    else:
      fibonacci_list.append(fibonacci_list[i-2]+fibonacci_list[i-1])
  return fibonacci_list[-1]
```

> 재귀함수의 작동 원리
>
> 함수를 호출할 때 def로 선언된 함수를 실행, 이 때 함수 안에 있는 함수는 선언된 함수를 참조하여 실행