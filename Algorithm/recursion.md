## 팩토리얼

```python
def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n-1)
```

## 피보나치수열

```python
def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
```

## 파스칼의 삼각형(작성중)

```python
def pascal(n):
  if n == 1 or n == 2:
    return str(1) * n
  else:
    last_line = []

```