## 함수

- 함수의 특징 : 분해와 추상
  - 분해(Decomposition)
    - 기능 단위로 쪼개서 재사용하기 편함
    - 간결하고 이해가 쉬움
  - 추상(Abstraction)
    - 프로그램 원리를 잘 몰라도 직관적으로 사용할 수 있음
    - 재사용성, 가독성, 생산성 향상
  - 미니프로그램, 프로그램이 갖는 저장과 처리 모두 갖고 있다.

- 함수의 종류
  - 내장(Built-in) 함수 : 파이썬 기본 함수
  - 외장 함수 : _import_ 명령어를 사용하여 외부에서 불러오는 함수
  - 사용자 정의 함수 : 사용자가 직접 작성하는 함수

> 많이 쓰이는 외장 함수는 내장 함수로 탑재되기도 함

- 함수의 정의
  - 특정한 기능을 하는 코드의 조각(묶음)

- 함수의 기본 구조
  - 선언, 호출(define & call)
  - 입력(input)
  - 문서화(docstring)
  - 범위(scope)
  - 결과(output)
  
  ```python
  def function_name(parameter):
    # function body
    return 'output'

## 함수의 결과값(Output)
- void function
  - 명시적인 return 값이 없는 경우, None(다른곳에서는 void라고함)을 반환하고 종료 : 반환값이 없는 함수 = None, void
  - ex) print <- 정확히 말하면 return None이 생략되어 있는 것. 그래서 void 함수를 print하게되면 None을 반환함
- value returning fuction
  - 함수 실행 후, return문을 통해 값 반환
  - return을 하게되면(return을 만나는 순간, 아래는 실행 안됨), 값 반환 후 함수 바로 종료
- return vs print
  - print를 사용하면 호출될 때마다 값이 출력됨(주로 테스트를 위해 사용), 반환X = 결과가 없다
  - 데이터 처리를 위해서는 return 사용
  - REPL(Read-Eval-Print Loop) 환경(jupyter notebook)에서는 작성된 코드 리턴값을 보여주므로 같은 걸로 착각할 수 있다.
- 두 개 이상의 값 반환
  - return은 한 개만 반환함
  - return x - y, x * y -> 이런식으로 튜플로 묶어서 반환하는 방법이 있다.

## 함수의 입력 : Parameter vs Argument

- Parameter : 함수를 정의(선언)할 때 함수 내부에서 사용되는 변수
- Argument : 함수를 호출할 때 넣어주는 값

```python
def solution(parameter):
    return 'answer'

solution('argument')
```

## Keyword Arguments

- 특정 argument를 parameter의 이름으로 위치 지정 가능
- 기본 값은 positional argument(위치에 따라 이동)
- *일단 keyword argument를 선언하면* 이후의 argument는 keyword를 선언해야 함

```python
def add(x,y)
    return x
add(a, b)   # positional argument
add(x=a, y=b)   # keyword argument
add(a, y=b) # a는 자동으로 positional argument로 인식됨
add(x=a,b)  # Error 발생(뒤에서부터 지정해야 함)
```

## Default Arguments

- 기본 값을 지정하여 함수 호출 시 argument를 받지 않게 할 수 있음
- 이 경우 정해진 개수보다 더 적은 argument로도 실행 가능

```python
def add(x,y=0)
    return x + y
add(2)
```

## Asterisk(애스터리스크 : 언패킹 연산자)

- 가변 인자
  - 여러 개의 positional argument를 필수 parameter로 받아들임
  - Arguments 입력 시 시퀀스를 언패킹하는 연산자
- 패킹 : 여러 개의 데이터를 묶어서 변수에 할당하는 것
- 언패킹 : 시퀀스 속의 요소들을 여러 변수에 나눠서 할당하는 것
- 언패킹 시 변수의 개수와 할당하려는 요소의 개수는 동일해야 함
    - **변수의 왼쪽에 '*'를 붙이면 남은 변수들을 그 변수에 할당 가능**
  - 가변 인자는 반드시 입력받아야 하는 값은 아님

    ```python
    numbers = (1,2,3,4,5,6)
    a, b, *rest = numbers
    c,*odds, d = numbers
    print(rest) # [3,4,5,6]
    print(odds) # [2,3,4,5]
    ```

    ```python
    def dice_roll(*dice1):
    if len(dice1) > 1:
        return sum(dice1)
    else:
        return dice1
    print(dice_roll(1,3,6)) # 10
    ```

- 가변 키워드 인자

  - 몇 개의 인자를 받을 지 알 수 없는 함수를 정의할 때 유용
  - 딕셔너리로 처리됨
  - parameter 앞에 **를 붙여서 표현

    ```python
    def owl(**dict_owl):
      for idx, val in dict_owl.items():
          print(idx, ':', val)

    owl(hey= '부엉', pour_sauce= '안돼') # 결과 == hey : 부엉 // sauce : 안돼
    ```

    ```python
    def owl(**dict_owl):
      for idx, val in dict_owl.items():
          print(idx, ':', val)
    
    joke_dict = {'hey': '부엉', 'pour_sauce': '부엉'}

    owl(**joke_dict)  # 결과 == hey : 부엉 // sauce : 부엉
    ```

> 가변 인자와 가변 키워드 인자는 함께 사용 가능

## lambda

- 익명 함수
- 간단한 함수를 표현할 때 사용

```python
minus_two = list(map(lambda x: x-2,[5,6]))
print(minus_two)  # 결과 : [3, 4]
```