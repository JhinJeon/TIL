## homework & Workshop 어려웠던 부분

### 1. 가변 인자 리스트

- 가변 인자 입력 시 쉼표 단위로 입력받아도 알아서 잘 처리해 준다.
  (개떡같이 입력해도 찰떡같이 처리함)
- 단일 인자에 다수를 입력했을 때 패킹되는 형태는 **튜플**

```python
def my_avg(*n):
    if len(n) == 1:
        return n
    else:
        return(sum(n)/len(n))


print(my_avg(77, 83, 95, 80, 70))
```

## 2. List의 합 구하기

- sum을 안 쓰고 리스트 합계 구하는 방법

```python
def list_sum(list_sample, answer=0):
    for i in list_sample:
        answer += int(i)
    return answer


print(list_sum([1, 2, 3, 4, 5]))
```

## 3. Dictionary로 이루어진 List의 합 구하기

- sum을 안 쓰고 리스트의 딕셔너리 값 합계 구하는 방법

```python
def dict_list_sum(dict_sample, answer=0):
    for dic in dict_sample:
        for key, value in dic.items():
            if type(value) == int:
                answer += int(value)
    return answer
```

## 4. 2차원 List의 전체 합 구하기

- sum 안 쓰고 2차원 리스트의 합계 구하기

```python
def all_list_sum(sample_list, answer=0):
    for i in sample_list:
        if type(i) == list:
            for k in range(len(i)):
              answer += int(i[k])
        else:
            answer += int(i)    
    return answer
```
## 기본 인자값

- 함수를 선언할 때 Argumnet에 기본 값을 설정해 줄 수 있음

```python
print(greeting())
print(greeting('철수'))
```

- 단 기본 Argument 다음에 기본 Argument가 없는 인자는 사용 불가

```python
# 아래 코드를 실행하면 에러 발생
def greeting(name='peter', age):
  return f'{name}은 {age}살입니다.'
```

## 변수가 리스트로 주어졌을 때

```python
numbers = [1, 1, 3, 3, 0, 1, 1]
result = []

for idx, num in enumerate(numbers):
  # 맨 처음 등장한 문자이거나 마지막 문자와 다른 경우 새로운 문자로 추가
    if idx == 0 or result[-1] != num: 
        result.append(num)

print(result)
```