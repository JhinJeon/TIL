# 함수에서 return하는 값 포맷 바꾸기

## 개요

어제 실습을 진행하다가 애를 먹은 사항이 있었는데, 바로 딕셔너리 값 목록을 리스트 형태로 출력하는 과제였다.

딕셔너리에서 값(value)만 따로 뽑고 싶으면 <u>(딕셔너리명).values()</u>를 하면 되지만, 문제는 반환되는 값의 형식(format)이었다.

문제에서는 리스트 형태로 출력하라고 했는데, 내가 작성한 코드의 반환값은 dict_values라는 형태로 출력됐다.

일단 어제는 이중 리스트로 작성해서 해결하긴 했지만, '딕셔너리로 할 수는 없을까?' 라는 의문이 들었다.

---

## 문제 제기

```python
단어를 입력하면 그에 해당하는 숫자를 반환하는 함수
def num_to_char(month_char):
    month_dict = {
        'January' : 1,
        'February' : 2,
        'March' : 3,
        'April' : 4,
        'May' : 5,
        'June' : 6,
        'July' : 7,
        'August' : 8,
        'September' : 9, 
        'October' : 10, 
        'November' : 11, 
        'December' : 12
    }
    return month_dict.values(month_char)
```
위 함수를 실행하면 다음 값이 반환된다:
```python
dict_values([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
```

## 궁금했던 점

- 딕셔너리에서 값(values)들만 반환하고 싶을 때 .values() 함수를 쓰는데, 이 때 반환되는 형식이 예쁘지가 않았다.
- 그래서 리스트나 숫자열 형태로 반환 및 출력할 수는 없는지 찾아보았다.
- 구글링한 결과 다음과 같은 정보를 얻을 수 있었다.

### 1. 리스트로 출력하기
```python
def num_to_char(month_char):
    # (중략)
    return list(month_dict.values())
# 결과 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

- 함수 값을 return 할 때 .values()를 하나의 리스트로 만들면, 이중 리스트가 되지 않고 dict_values()만 깔끔하게 사라지는 걸 볼 수 있었다.

### 2. 숫자열 형태로 출력하기 : return한 값을 print()할 때

```python
def num_to_char(month_char):
    # (중략)
    return list(month_dict.values())
    

print(*num_to_char())
# 결과 : 1 2 3 4 5 6 7 8 9 10 11 12
```

- num_to_char()함수가 리스트 값을 반환하므로, print할 값 앞에 **Asterisk**( * )를 붙이면 해결할 수 있었다.

---

## 그렇다면 함수에서 값을 반환할 때 (리스트를 언패킹해서) 숫자열 형태로 반환할 수는 없을까?

- 혹시 이건 되지 않을까? 하고 아래와 같이 코드를 작성해 봤다.

```python
def num_to_char(month_char):
    # (중략))
    return *[(month_dict.values())]
```

그런데 막상 쓰고 나니까 왜 안 되는지 알 것 같았다.  

### 왜 안되는 거임?

- 파이썬 함수는 기본적으로 하나의 값만 반환한다. 다만 예외적으로 두 개 이상의 값을 쉼표(,)로 구분하면 튜플의 형태로 반환한다.
- 이 때 리스트를 언패킹해버리면 함수의 답이 리스트의 값 개수만큼 되어 버려서, 쉼표 없이 두 개 이상의 값을 반환하라는 코드가 되어 버린다.
- 그래서 위와 같이 코드를 작성해 보면 list()를 쓰든, []를 쓰든 문법적으로 어긋난다고 표시를 해 준다.

---

## 요약 및 결론

- dict.values()로 값만 반환하면 기본적으로 리스트 형태로 반환해 주는데, 사용자 함수(def~) 안에 집어넣으니까 dict_values()라는 형식으로 출력되는 것이 힘들었다.
- 딕셔너리의 값을 반환하는 함수를 만들 때 dict_values()라는 형태로 반환된다.
- 이를 리스트의 형태로 출력되게 만들고 싶으면 return하는 값을 list(), [ ] 중 하나로 감싸면 된다.
- 다만 리스트를 언패킹한 숫자열을 반환할 수는 없다. 언패킹한 형태로 출력하고 싶으면 return받은 값을 print할 때 언패킹을 해 줘야 한다.
- 그냥 딕셔너리 대신 이중 리스트 쓰자.

## 참고한 사이트

https://stackoverflow.com/questions/16228248/how-can-i-get-list-of-values-from-dict

https://yeomss.tistory.com/160

---

# 딕셔너리 조작

> 실험 대상 리스트 :

```python

month_dict_list = [
        {'January': 1},
        {'February': 2},
        {'March': 3},
        {'April': 4},
        {'May': 5},
        {'June': 6},
        {'July': 7},
        {'August': 8},
        {'September': 9},
        {'October': 10},
        {'November': 11},
        {'December': 12}
]
```

> 실험 대상 딕셔너리 :

```python
month_dict = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12
    }
```

# 새로운 딕셔너리 만들기

### Type A

```python
# 딕셔너리 리스트에서 key: value가 일대 일 대응을 이루는 단일 딕셔너리로 전환
def create_dict(old_dict_list):
    new_dict = {}   # 새로 만들 딕셔너리
    for old_dict in old_dict_list:  # 기존 딕셔너리 리스트에서 개별 딕셔너리 반환
        for key, value in old_dict.items(): # 개별 딕셔너리에서 key와 value를 추출
            new_dict[key] = value   # 새로 만들 딕셔너리에 key: value 추가
    return new_dict # 새로 만든 딕셔너리 반환
```

### Type B

```python
# 큰 딕셔너리에서 딕셔너리 리스트로 전환
def create_dict_list(old_dict):
    new_dict_list = []  # 새로 만들 딕셔너리 리스트
    for key, value in old_dict.items(): # 기존 딕셔너리에서 key와 value 반환
        new_dict_list.append({key : value}) # 새로운 딕셔너리 리스트에 들어갈 딕셔너리의 key와 value 설정
    return new_dict_list    # 완성된 딕셔너리 리스트 반환
```

### Type C

```python
# 단일 딕셔너리에 (키 튜플) : (값 튜플)로 이어지도록 만들기
def create_big_dict(old_dict):
    dict_keys = []  # 새 딕셔너리에 추가할 키 튜플
    dict_values = []    # 새 딕셔너리에 추가할 값 튜플
    for key, value in old_dict.items():
        dict_keys.append(key)   # 기존 딕셔너리의 키만 별도로 저장
        dict_values.append(values)  # 기존 딕셔너리의 값만 별도로 저장
    new_dict = {tuple(dict_keys) : tuple(dict_values)}  # 튜플로 저장하기 위해 각 리스트를 tuple() 처리
    return new_dict
```

## 각 월 별로 날짜가 며칠 있는지 표시해 주기

```python
def day_and_month(old_month_dict_list):
    days = [1] * 12  # 각 월 별로 날짜를 나타내기 위한 days 리스트(임시로 값을 모두 1로 설정)
    # 각 월 별로 며칠이 들어가는지 설정
    days[0] = [i for i in range(1, 32)]
    days[1] = [i for i in range(1, 29)]  # 윤년인 경우 무시
    days[2] = [i for i in range(1, 32)]
    days[3] = [i for i in range(1, 31)]
    days[4] = [i for i in range(1, 32)]
    days[5] = [i for i in range(1, 31)]
    days[6] = [i for i in range(1, 32)]
    days[7] = [i for i in range(1, 32)]
    days[8] = [i for i in range(1, 31)]
    days[9] = [i for i in range(1, 32)]
    days[10] = [i for i in range(1, 31)]
    days[11] = [i for i in range(1, 32)]

    months = []     # 딕셔너리에서 key값을 받아서 저장하기 위한 리스트
    for month in old_month_dict_list:
        for key in month.keys():    # month를 얻기 위해 key값 반환
            months.append(key)  # 딕셔너리의 key만 저장

    day_month_dict_list = []  # 새로 만들 딕셔너리 리스트
    for i in range(len(months)):  # 리스트에 각 월별로 {month:day} 딕셔너리 추가
        day_month_dict_list.append({months[i]: days[i]})
    return day_month_dict_list  # 결과 반환
```

# 마지막 문자가 숫자인지 확인하는 방법

## 1. 리스트 만들기

```python
def check_str(chrs):
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if chrs.get('id')[-1] in num_list:  # 마지막 문자가 숫자(0~9)인지 확인
        return True
    else:
        return False
```

## 2. isdigit() 활용

```python
def check_str(user_data):
    if chrs.get('id')[-1].isdigit():    # 숫자형으로 변환 가능한 경우 True 반환
        return True # 모든 문자열이 숫자인 경우 True 반환
    else:
        return False
```

## 응용 : 문자열 중에 숫자가 하나 이상 있는지 확인하는 함수

```python
def check_validation(id_input): # 유효한 id인지(id에 숫자가 1개 이상 들어가 있는지) 확인하는 함수
    for digit in id_input:  # id를 구성하는 문자열에서 문자를 하나씩 반환
        if digit.isdigit(): # 만약 숫자가 발견되는 경우 즉시 유효성 통과(True)
            return True
            break
    else:   # 숫자가 전혀 발견되지 않으면 무효(False)
        return False
```

## 추가 : isdecimal(), isdigit(), isnumeric()

- 공통 : 숫자로 변환 가능한 문자열인지 확인해 주는 함수

- isdecimal(chr) : chr가 int()로 변환 가능한지 확인

- isdigit(chr): chr가 숫자처럼 생겼는지 확인 (지수 및 특수기호 포함)
> isdigit()에서 True가 반환되는 경우 : ⑦, 2² 등

- isnumeric(chr) : chr가 숫자값을 표현하는지 확인(제곱근, 분수 특수문자 등)