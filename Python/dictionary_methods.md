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

## get(dic_key, if_no_key)

- 딕셔너리의 키에 입력된 값을 가져올 때 사용
- 딕셔너리 안에 입력한 dic_key값이 없으면 if_no_key에 입력한 값을 표시
    - if_no_key의 기본값은 None
- **keyerror로 인한 인터럽트**를 <u>방지</u>할 수 있는 방법