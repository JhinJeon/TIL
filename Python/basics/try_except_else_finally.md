## try, except, finally, else

- try : try: 이하 코드를 실행(if-else처럼 작성)
- except : try 이하 코드를 실행했을 때 오류가 발생하면 실행하는 코드
- else : try 이하 코드를 성공적으로 실행했을 때 실행하는 코드
- finally : try/except 결과와 상관없이 항상 실행하는 코드

```python
def print_program(a):
  try:
    a = int(a)
  except:
    print('잘못된 입력입니다.')
  else:
    print(f'입력하신 숫자는 {a}입니다.')
  finally:
    print('프로그램을 종료합니다.')
```

- Case 1

```python
print(print_program(5))
```

> 결과 :
> 입력하신 숫자는 5입니다.
> 프로그램을 종료합니다.

- Case 2

```python
print(print_program('A'))
```

> 결과 :
> 잘못된 입력입니다.
> 프로그램을 종료합니다.