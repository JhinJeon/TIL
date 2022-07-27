 ## 이차원 배열 응용

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