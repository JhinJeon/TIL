 ## map(function,iterable)

- 모든 iterable 값에 적용 가능
- iterable에 문자열을 넣을 경우 문자 인덱스 단위로(철자 단위로) 나눔
- 문자열 또는 숫자열에 공백이 있는 경우 iterable.split()으로 공백 제거

- 사용자 지정 함수에도 사용 가능
```python
def minus_two(x):
  return x- 2
print(list(map(minus_two,[5,6]))) # 결과 : [3, 4]
```
 
 ## 이차원 배열에 응용

```python
matrix = [
   [1,2,3,4],
   [5,6,7,8,],
   [9,10,11,12]
]

print(max(map(max,matrix)))    # max 대신 sum, min 등도 가능
```

- 위의 방식으로도 쓸 수 있지만 아래 방식으로 써야 가독성이 좋음
    - 위 코드는 map()의 원리를 이해하는 용도로 받아들일 것

```python
matrix = [
    [1,2,3,4],
    [5,6,7,8,],
    [9,10,11,12]
]
max_value = -1000000
for i in range(3):
    for j in range(4):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
print(max_value)
```