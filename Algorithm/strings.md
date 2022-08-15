# 문자열(string)

## 컴퓨터에서 문자표현

- 서로 정보 처리(코드 해석)를 다르게 한다는 문제가 발생
- 비트(bit)를 기준으로 인코딩 표준안 제정
- 아스키코드 : 인코딩 표준안의 일종
  - 아스키코드는 8진수(8비트)로 표현
- 유니코드 : 다국어 처리를 위한 인코딩 표준안
  - 기본값은 UTF-8(8비트)
- 다른 인코딩 방식으로 처리하려면 코드 맨 첫 줄에 인코딩 방식을 서술하면 됨

## 문자열의 처리

- 문자열은 시퀀스 자료형으로 분류됨
- container > sequence > immutable > iterable 순
- replace(), split(), ord(), chr(), isalpha() 등
- 문자열을 split()을 쓰지 않고 list()에 편입하면 개별 문자가 리스트의 원소가 됨

## 문자열 뒤집기

1. 반복문 사용

- 반복문 range를 거꾸로(n,-1,-1) 돌려서 새로운 문자열에 추가

```python
string = 'Hello Algorithm'
reversed_string = ''

for i in range(len(string) - 1, -1, -1):  # 맨 뒤에서부터 시작하여 처음까지
    reversed_string += string[i]

print(reversed_string)
```
  
1. reverse 사용

- 문자열을 리스트로 만든 후 (리스트명).reverse() 사용

```python
string = 'hello algorithm'
string_list = list(string)
string_list.reverse()
reversed_string = ''.join(string_list)
print(reversed_string)
```

3. 슬라이싱

- 문자열 인덱스를 지정할 때 [시작 지점, 끝 지점, step] 설정
- step = -1로 지정하면 반대 방향으로 읽음
- [::-1]은 시작 지점부터 끝 지점까지 반대 방향으로 읽어들임
- 가장 편하고 빠른 방법

```python
string = 'hello algorithm'
reversed_string = string[::-1]
```

## int() 함수 쓰지 않고 문자를 정수로 변환

```python
def atoi(number): # str 형태로 입력
  int_number = 0

  for char in number:
    int_number *= 10
    int_number += ord(char) - ord('0')
  
  return int_number
```

## str() 함수 쓰지 않고 정수를 문자 타입으로 변환

```python
def itoa(number):
    if number == 0:
        return '0'

    is_positive = True
    # 값이 음수인 경우 음수라는 정보를 기억하고 양수로 전환
    if number < 0:
        is_positive = False
        number = -number

    str_number = ''
    while number > 0:
        number, remainder = number // 10, number % 10  # divmod(number, 10)
        str_number = chr(ord('0') + remainder) + str_number

    if not is_positive:
        str_number = '-' + str_number

    return str_number

result = itoa(123)
print(type(result)) # type : str
print(result) # '123'
```

## 문자를 특정 값으로 대치

- 문자열.replace(원본 값, 대체할 값)
- 문자열은 수정 불가능한 자료형이므로, 새로운 변수로 정의해야 함
- word = word.replace()로 작성하면 수정한 값을 원래 변수에 저장 가능
