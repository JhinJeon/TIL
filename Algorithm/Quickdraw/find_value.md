## 리스트 안에서 특정 값을 찾는 방법

1. for 구문 활용
```python
#홀수의 개수 세기
num = [1,2,3,4,5,6,7,8,9]
odd = 0
for num in odd:
    if num % 2 == 1:
        odd += 1
```

2. .count 활용
```python
k = 3
grade = [1,2,2,2,3,3,3,3,3,3,4,4,4,5]
if k in grade:
    grade.count(k)
```

- 주의 : 리스트 안에 값이 없으면 에러가 발생하므로, if 등을 활용해 리스트를 미리 확인할 필요가 있음