## 함수로 값을 반환받을 때 주의해야 할 점

```python
import json

def dec_movies(movies):
    movie_dict = []  # 영화 id, 제목 저장 이중 리스트
    film_list = []  # 영화 제목 리스트
    revenue_list = []   # 수익 리스트
    budget_list = []    # 예산 리스트
    answer = 0
    for movie in movies:
        id = movie.get('id')
        title = movie.get('title')
        movie_dict.append({id: title})
        film_json = open(f'data/movies/{id}.json', encoding='utf-8')
        film_dict = json.load(film_json)
        revenue_list.append(film_dict.get('revenue'))
        budget_list.append(film_dict.get('budget'))
    profit = 0
    for m in range(len(budget_list)):
        true_revenue = revenue_list[m] - budget_list[m]
        if answer < true_revenue:
            answer = true_revenue
            profit = m
    for val in movie_dict[profit].values():
        return val
```
## 궁금했던 사항
- 위 코드에서 그냥 movie_dict[profit].values()를 반환하면 dic_values() 형식으로 반환되는데 for 구문에 iterable로 넣으면 그런 거 없이 출력되는 이유가 뭘까?

## 의문 해결
- 형식의 문제이기 때문에 type() 함수로 반환되는 값의 형식을 체크해보기로 했다.
- 내가 원하는 출력 형태는 정수 또는 리스트이므로, 이하 이런 형태로 표시해 줄 수 있는 map() 함수와 타입을 비교해보기로 했다.

 아래 solution 시리즈 함수들은 .values()가 어떤 특징을 가지고 있는지 비교하기 위해 만들어 본 함수이다.

```python
sample_dict = {'A': 1, 'B': 2, 'C': 3}


def solution1(dictionary):
    return type(dictionary.values())

def solution2(dictionary):
    return type(map(int, dictionary.values()))

def solution3(dictionary):
    return list(dictionary.values())

print(solution1(sample_dict))   #dit_values
print(solution2(sample_dict))   #map object
print(solution3(sample_dict))   # [1,2,3]

```


 위 코드를 실행하면서 의문이 들었던 게 .values() 메서드가 리스트 형태로 값을 반환한다면 왜 3번 함수는 반환값이 이중 리스트로 나오지 않느냐는 것이었다.

 이에 대해서 구글링 하던 중 다음과 같은 글을 발견할 수 있었다.

> The view object values doesn't itself return a list of sales item values but it returns **a view of all values** of the dictionary.

## a view of all values??

구글에서 찾아 보니까 Python이 Python2 -> Python3으로 넘어가면서 생긴 변화라고 한다.

Python2에서는 .values() 메서드로 반환받은 값의 타입은 리스트인데, 이 때 이 값을 **본래 딕셔너리와 다른 메모리 주소에 저장**했다고 한다. 

그래서 딕셔너리의 값을 수정하는 경우 .values()로 반환받은 값은 수정되지 않는 현상이 있었다.

그런데 딕셔너리는 수정 가능(mutable)한 자료형이기 때문에, 원본 딕셔너리가 수정되었음에도 .values()로 조회하는 결과에 변화가 없는 현상은 파이썬 이용자에게 혼동을 줄 여지가 있었다.

그래서 Python3에서 .values()의 타입을 dict_values()로 바꾸면서, 딕셔너리 원본의 값이 바뀌었을 때 .values()로 값을 조회했을 때도 값이 바로 수정되도록 변경되었다. 

그리고 이 점을 구현하기 위해 view object라는 것을 추가했다고 한다.


## 정리

- 처음에는 왜 dict_values()라는 별도의 자료형을 만들었나 했는데, 나름 기존 사용자 편의를 위해 변경된 사항이라고 하니 어느 정도 납득되는 부분이 있다.
- 함수에서 값을 return할 때 dict_values()가 거추장스럽게 붙어 나오는 것을 떼고 싶다면 map(), for 반복문 등을 사용하여 자료형을 약간 수정해야 한다.
## 참고 자료

<https://www.programiz.com/python-programming/methods/dictionary/values>
<https://bluese05.tistory.com/67>
<https://johnlekberg.com/blog/2020-09-19-dict-view.html>