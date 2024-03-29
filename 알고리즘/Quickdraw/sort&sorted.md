## sort()/sorted() 고급

리스트 안의 값이 iterable 형태(딕셔너리, 튜플, 리스트 등)일 때 값 안의 값을 기준으로 정렬하는 방법

1. lambda
```python
answer = sorted(
        movie_list, key=lambda movie_list: movie_list['vote_average'], reverse=True)
```
- key=에 특정 타입을 입력하기 어려운 경우(dict의 값들을 기준으로 정렬해야 할 때 등)에 사용

2. key = itemgetter(인덱스 번호) 또는 key = attrgetter(값)
```python
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
sorted(student_objects, key=attrgetter('grade', 'age'))
# 결과 : [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
```

- 주의 : 클래스 단위에서 사용 가능

3. multisort() : 여러 가지 기준으로 정렬할 때

```python
def multisort(xs, specs):
    for key, reverse in reversed(specs):
        xs.sort(key=attrgetter(key), reverse=reverse)
    return xs
```