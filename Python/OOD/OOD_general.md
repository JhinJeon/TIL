# 요약

- 객체 지향 프로그래밍이란?
- 객체 지향 프로그래밍 기본
  - 인스턴스
  - 클래스
  - 메서드
- 객체지향의 핵심 개념
  - 추상화
  - 상속
  - 다형성
  - 캡슐화
- 에러와 예외

# 객체 지향 프로그래밍이란?

## 객체

- **정보(클래스변수, 인스턴스변수)와 행동(메서드)이 모인 독립된 단위**
- **속성과 행동으로 구성된 모든 것**
- 객체 =  변수(정보) + 함수
- 파이썬은 모든 것이 객체인 객체지향 프로그래밍
  - 파이썬의 모든 것에는 속성과 행동이 존재

## 객체지향 프로그래밍
- 객체 지향 프로그래밍(Object-Oriented Programming)은 컴퓨터 프로그램의 패러다임 중 하나
- 데이터와 기능(메서드)의 분리, 추상화된 구조(인터페이스)
  - 패러다임은 어떤 작업이나 행동을 하는 방식의 일종
- 프로그램을 명령어의 목록이 아닌 *객체들의 모임*으로 파악하는 관점
  - 각각의 객체는 메시지를 주고받고, 데이터를 처리할 수 있음
  - 프로그램을 여러 개의 독립된 객체들과 그 객체 간의 상호작용으로 파악하는 프로그래밍 방법
- 객체 간 서로 통신 및 상호작용하도록 프로그래밍하는 방법

> 예시
> - 콘서트
>   - 가수 객체
>       - 행동 : 노래 부르기
>   - 감독 객체
>   - 관객 객체
>       - 행동 : 관람하기

## 객체지향의 장단점

- 장점
  - 대규모 프로젝트에 적합
  - **프로그램의 유지보수가 쉬움**

- 단점
  - 느린 실행속도
    - 컴퓨터의 처리구조는 절차지향 프로그래밍과 유사
  - 설계 시 많은 노력과 시간 필요
    - 다양한 객체들 간 상호작용 구조를 만들어야 함

## 절차지향 프로그래밍과의 비교

- 객체지향 프로그래밍의 반대 개념
- 여러 함수들(파이프라인)을 거쳐서 프로그래밍 완성
- 특정 부분에 문제가 생겼을 때 부분변경하기 어려움
  
# 객체 지향 프로그래밍 기본

## 객체의 특징

- 타입(type) : 어떤 연산자와 조작이 가능한가
- 속성(attribute) : 어떤 상태 데이터를 가지고 있는가
- 조작법(method) : 어떤 행위(함수)가 가능한가
- Python의 객체와 클래스 : 객체(Object) = 속성(Attribute) + 기능(Method)

## 클래스

- 객체의 추상적인 타입(type)
- 클래스를 만든다 == 타입을 만든다 == 실제사례를 만든다 == 사용자 정의 타입의 일종
- 기본 클래스 == Python 내장 함수
- 클래스 선언의 목적 : 데이터(정보)와 메서드(함수)를 묶기 위함

## 클래스 변수

- 한 클래스의 모든 인스턴스가 공유하는 값
- 같은 클래스의 인스턴스들은 같은 값을 보유
- 클래스 선언 내부에서 정의

## 인스턴스

- **클래스로 만든(선언된) 객체**
- 특정 클래스/타입의 인스턴스~ 로 표현
  - 예) def solution(): 선언 후 a = solution(n)을 입력한 경우 a는 인스턴스

## 인스턴스 변수

- 각 인스턴스들이 가지고 있는 고유한 변수(속성)
- 생성자 메서드(\_\_init__)에서 self.로 정의

## 메서드

- 클래스 안에 있는 함수
- 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)


### 메서드의 종류

- 인스턴스 메서드
  - 인스턴스 변수 처리
  - 인스턴스 변수를 사용하거나 변수에 값을 설정하는 메서드
  - 클래스 내부에 정의되는 메서드의 기본
  - **메서드 호출 시 첫 번째 인자로 인스턴트 자신(self)이 전달됨**
    - 아무 인자를 입력하지 않아도 self 입력은 필수
- 클래스 메서드
  - 클래스 처리
- 정적 메서드
  - 인스턴스와 클래스를 제외한 나머지

### 매직 메서드(스페셜 메서드)

- 특수한 동작을 위해 만들어진 메서드
- 특정 상황에 자동으로 불리는 메서드
- Double Underscore(\__)로 표시
```python
class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def __del__(self):
        Doggy.num_of_dogs -= 1
```

## 인스턴스와 클래스 간의 이름 공간(namespace)

- 클래스를 정의하면 클래스에 해당하는 이름 공간 생성
- 인스턴스를 만들면 인스턴스 객체가 생성되고 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면 인스턴스-클래스 순으로 탐색

--- 

# 기본 문법

## 클래스의 정의
- 클래스의 앞 글자는 항상 대문자
```python
class MyClass:
    pass
```

## 인스턴스의 생성
```python
my_instance = MyClass()
```

## 생성자 메서드
```python
def __init__(self,instance):
  self.instance = instance
```

## 메서드 호출
```python
my_instance.my_method()
```

## 속성
```python
my_instance.my_attribute
```

## 객체 간 비교

- 동등함(equal)
  - == 로 비교
  - 변수가 참조하는 객체가 동등하면 True 반환
  - 실제로 동일한 대상을 가리키고 있다고 표시해 주는 것은 아님

- 동일함(identical)
  - is 로 비교
  - 두 변수가 동일한 객체를 가리키고 있으면 True

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b, a is b) # True False
print(a == c, a is c) # True True
```


## 인스턴스 변수

- 인스턴스가 개인적으로 가지고 있는 속성
- 각 인스턴스들의 고유한 변수
- 생성자 메서드(\__init__)에서 self.\<name>으로 정의
- 인스턴스가 생성된 이후 \<instance>.\<name>으로 접근 및 할당

## 클래스 변수

- 클래스 선언 내부에서 정의
- \<classname>.\<name>으로 접근 및 할당

## 클래스 변수 활용

- 사이트 방문자 수 세기 : 인스턴스 변수가 생성될 때마다 count가 늘어나도록 작성한 클래스
```python
class Person:
    count = 0
    # 인스턴스 변수 설정
    def __init__(self, name):
        self.name = name
        Person.count += 1

person1 = Person('')
person2 - Person('')
print(Person.count)
```

- 클래스 변수 변경 시 \<클래스>.\<클래스변수> 형식으로 변경

## 인스턴스 메서드

- self 매개 변수를 사용하여 인스턴스 조작

## 클래스 메서드

- cls 매개 변수를 사용하여 클래스 조작
```python
class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def __del__(self):
        Doggy.num_of_dogs -= 1

    @classmethod
    def get_status(cls):
        return f'Birth: {cls.birth_of_dogs}, Current: {cls.num_of_dogs}'

```

## 스태틱 메서드

- 클래스 변수나 인스턴스 변수를 사용하지 않는 경우
  - 객체 상태나 클래스 상태 수정 불가
- @staticmethod

# 객체지향의 핵심

## 추상화

- 복잡한 것(원리, 프로세스 등)을 숨기고, 필요한 것만 드러내기

## 상속

- 두 클래스 간 부모-자식 관계를 정립하는 것
- 클래스는 상속이 가능
  -  모든 Python Class는 object를 상속받음

```python
class ChildClass(ParentClass):
  pass
```

- ChildClass는 ParentClass에서 상속받는 관계
- 하위 클래스는 상위 클래스에서 정의된 속성, 메서드, 행동, 관계 및 제약 조건을 모두 상속받음
- 코드 재사용성 증가

관련 함수
- issubclass(class,classinfo)
  - class가 classinfo의 subclass(하위 클래스)면 True 반환
- super()
  - 자식 클래스에서 부모 클래스를 사용하고 싶은 경우 사용
  - super().\<부모 클래스>

다중 상속
- 두 개 이상의 클래스에서 상속받는 경우
- 상속받은 클래스들의 모든 요소 사용 가능
- 중복되는 메서드 등이 있으면 상속 순서에 따라 결정됨

다중 상속 방법 :
```python
class Childclass(ParentClass1, ParentClass2)
```

MRO(Method Resolution Order)

- 해당 인스턴스의 클래스가 어떤 부모 클래스를 갖고 있는지 확인하는 메서드
- 상속 관계가 있으면 인스턴스 -> 자식 클래스 -> 부모 클래스 순으로 확장

## 다형성

- polymorphism
- 동일한 메서드도 클래스에 따라 동작이 다를 수 있음

오버라이딩(Overriding)

- 상속받은 메서드를 재정의
- 부모 클래스에 존재하는 동일한 이름의 메서드로 덮어써서 구현
  - 부모 클래스의 메서드를 실행시키고 싶으면 super().\<부모 클래스 메서드> 사용


```python
# 부모 클래스
class Person:
  def __init__(self, name):
    self.name = name
  def talk(self):
    return f'저는 {self.name}입니다.'

# 부모 클래스의 메서드 실행
class Student(Person):
  def talk(self):
    super().talk()
    print('반갑습니다.')

# 부모 클래스의 메서드 덮어쓰기
class Professor(Person):
  def talk(self):
    return f'{self.name}이오.'
```

## 캡슐화

- 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 접근 차단
- 개인정보 보호 등에 활용
- 파이썬에서 언어적으로 존재하지는 않지만, 암묵적으로 존재

Public Member

- 언더바 없이 시작하는 메서드나 속성
- 어디서나 호출 가능
- 하위 클래스 override 허용
- 일반적으로 작성되는 메서드의 속성

Protected Member

- 언더바 1개로 시작하는 메서드나 속성
- 암묵적으로 부모 클래스 내부와 자식 클래스에서만 호출 가능
- 하위 클래스 override 허용

Private Member

- 언더바 2개로 시작하는 메서드나 속성
- 본 클래스 내부에서만 사용 가능
- 하위클래스 상속 및 호출 불가
- 외부 호출 불가
  - 위 두 가지 시도 시 오류 발생
  - 변수에 접근할 수 있는 메서드를 별도로 생성해야 함
    - getter : 변수의 값을 읽어오는 메서드
    - setter : 변수의 값을 설정하는 메서드

```python
class Person:
  def __init__(self, name, age, idnum):
    self.name = name  # Public Member
    self._age = age # Protected Member
    self.__idnum = idnum  # Private Member

  def get_age(self):
    return self._age

  def get_idnum(self):
    return self.__idnum
```

## 디버깅

- 잘못된 프로그램을 수정하는 행위
- 에러 메시지가 발생하는 경우 해당 위치를 찾아서 해결
- 그 밖에 로직 에러가 발생하는 경우:
  - 예상과 다른 결과가 출력되는 경우
    - 정상 동작하는 코드와 비교
    - 전체 코드 점검
    - 휴식
    - 누군가에게 설명하기

디버깅 팁

- print() 함수 활용
- 개발 환경(vsc, eclipse 등)에서 제공하는 기능 활용
  - breakpoint, 변수 조회 등
- 단순 컴파일은 python tutor 활용
- 다른 사람들에게 도움 요청

## 오류의 종류

### 문법 에러(SyntaxError)

- 문법 에러 발생 시 코드는 실행되지 않음
- 파일명이나 코드 줄 번호 일부에 ^ 표시로 어느 부분에 문제가 있는지 표시
  - 줄에서 에러가 감지된 위치의 가장 앞을 가리킴

문법 에러 예시:
- invalid syntax : 유효하지 않은 구문(형식)
- assign to literal : 잘못된 값 할당
- EOL(End of Line), EOF(End of File) : 괄호 닫기가 정확하게 되지 않았을 때

### 예외(ExceptionError)

- 실행 중 감지되는 에러
- 실행 중 예기치 못한 상황 발생 시 프로그램 실행 중단
- 에러는 여러 타입으로 나뉘고, 타입이 메시지의 일부로 출력됨
- 모든 내장 예외는 Exception Class를 상속받아 이루어짐
- 사용자 정의 예외를 만들어 관리 가능(try-except 구문 등)

예외 에러 예시:
- NameError : namespace 상에 정의된 이름이 없을 경우
- ZeroDivisionError : 어떤 수를 0으로 나누려 할 때 발생하는 에러
- TypeError: type이 불일치할 때 발생
  - 숫자를 넣어야 할 때 순수 문자(알파벳)을 넣는 경우
  - 숫자와 문자를 같이 사칙연산을 시도하는 경우
  - 요구하는 datatype과 입력한 datatype이 불일치하는 경우
  - 입력한 인자 수가 함수에서 요구하는 인자 수보다 많거나 적은 경우 등등...
- ValueError : datatype은 올바르지만 실행 결과를 반환할 수 없을 때
  - int(3.5), range(3).index(6) 등...
- IndexError : 유효하지 않은 인덱스 범위(값)를 탐색할 때
- KeyError : 딕셔너리에서 입력한 키 값을 찾을 수 없을 때
- ModuleNotFound : import 시도한 모듈을 찾을 수 없을 때
- IndentationError : 코드 문단 들여쓰기가 적절하게 되지 않았을 때

## 예외 처리

- try : 오류가 발생할 수 있는 코드 실행, 정상 실행 시 except 생략
- except : try 이하 코드 실행 시 오류가 발생했을 때 실행하는 구문
  - 오류 상황 발생 시 적절한 조치를 취할 수 있음
  - 여러 개의 except 구문 설정 가능(1개 이상 필요)
- else : try 이하 코드 실행 시 오류가 발생하지 않았을 때 실행하는 구문
- finally : 예외 상황(오류 발생)과 관계 없이 항상 실행하는 구문

```python
try:
  a = input()
  print(int(a))
except TypeError:
  print('숫자가 입력되지 않았습니다.')
except ValueError as err:
  print(f'{err}, 유효하지 않은 정수입니다.')
else:
  return f'{a}는 숫자입니다.'
```

- 예외 처리는 try와 if 중에서 상황에 맞게 사용
  - if 구문이 try보다 실행속도가 더 빠름