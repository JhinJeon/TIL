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

