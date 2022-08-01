## 딕셔너리 키와 값을 맞바꿀 때

- Python에서 일반적으로 딕셔너리의 키와 값을 맞바꾸려면 다음과 같이 하면 된다.

```python
old_dict = {1: 10, 2: 20, 3: 30, 4: 30} # 기존 딕셔너리
new_dict = {} # 키와 값이 맞바뀐 새 딕셔너리

# items()로 key에는 키, value에는 값을 반환
for key, value in old_dict.items(): 
  # 새 딕셔너리의 키는 기존 딕셔너리의 값, 새 딕셔너리의 값은 기존 딕셔너리의 키
  new_dict[value] = key 
print(new_dict)
# 결과 : {10: [1], 20: [2], 30: [4]}
```

- 다만 앞서 작성한 코드의 경우 딕셔너리의 키와 값을 맞바꿀 때 값(value) 중에 동일한 것이 있으면 기존의 key 값은 새로운 딕셔너리에 한 개밖에 저장되지 않는 문제가 있었다.
- 구글링 한 결과 다음과 같은 코드를 발견할 수 있었다:

```python
old_dict = {1: 10, 2: 20, 3: 30, 4: 30} # 기존 딕셔너리
new_dict = {} # 키와 값이 맞바뀐 새 딕셔너리
for key, value in my_dict.items():
  # 새 딕셔너리의 키가 될 값에 중복이 있는 경우
  if value in new_dict:
    # 딕셔너리의 값을 업데이트하는 대신 기존 값에 추가
    new_dict[value].append(key)
  # 그렇지 않은 경우 위의 코드처럼 진행
  else:
    new_dict[value]=[key]
print(new_dict)
# 결과 : {10: [1], 20: [2], 30: [3,4]}
```

- 이렇게 하면 원본 딕셔너리에 동일한 값이 있어서 스왑 시 원본 딕셔너리의 키가 한 가지밖에 저장되지 않는 불상사를 해결할 수 있다.

- 출처 : (https://www.geeksforgeeks.org/python-program-to-swap-keys-and-values-in-dictionary/)