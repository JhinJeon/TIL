## 딕셔너리 관련 메서드

1. 딕셔너리의 모든 키 값 반환 : dic.keys()
2. 딕셔너리의 모든 값 반환 : dic.values()
3. 딕셔너리의 모든 키와 값 반환 : dic.items()

## Dictionary로 이루어진 List의 합 구하기
   
- 정답

```python
dict_list_sum(
    [
    {'name': 'kim', 'age': 12},
    {'name': 'lee', 'age': 4}
    ]
)  # => 16
```
     
```python
def dict_list_sum(infos):
    age_sum = 0
 
    for info in infos: # 딕셔너리의 key값을 받아서 계산
        age_sum += info['age']
 
    return age_sum
```

## 딕셔너리 연습 2


### .get()으로 없는 키를 찾을 때도 에러가 나지 않도록 설정

```python
my_dict = {'민트': '초코',
           '피자': '파인애플'}

print(my_dict.get('탕수육', '없는데요?'))
# 결과 : 없는데요?
```

### .update()로 딕셔너리 값 수정

- Type A

```python
my_dict = {'민트': '초코',
           '피자': '파인애플'}
my_dict.update(민트='만먹음', 피자='파인애플안넣어')
print(my_dict)
# 결과 : {'민트': '만먹음', '피자': '파인애플안넣어'}
```

- Type B

```python
my_dict = {'민트': '초코',
           '피자': '파인애플'}
my_dict.update({'민트': '만먹음', '피자': '파인애플안넣어'})
print(my_dict)
```