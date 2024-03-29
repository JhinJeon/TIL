# CS(컴퓨터 사이언스)

## 함수 vs 메서드:

- 메서드 : 특정 자료형에서만 사용 가능한 명령어
- 함수 : 모든 자료형에서 사용 가능한 명령어

## sort() vs replace()

- **문자열(튜플)**은 immutable 자료형 : replace()하면 새로운 데이터를 반환함
  - 문자열을 +=로 붙이는 경우 원본 문자열을 수정하는 것이 아니라 붙은 새로운 문자열을 반환하는 원리
- 리스트는 mutable 자료형 : list.sort()하면 원본을 수정

## mutable vs immutable

- mutable은 수정 가능한 자료형
- immutable은 수정 불가능한 자료형, 수정을 시도하면 새로운 값으로 대치
  - [0] * 3 리스트를 만든 후 0번 인덱스만 수정이 가능한 이유 : 값이 immutable 자료형이기 때문

## 얕은 복사와 깊은 복사

- 할당 : 변수에 특정 값 설정
  - a = b
  - 변수에 mutable 값을 설정한 후 사본을 생성한 경우 원본을 수정할 때 사본도 수정됨

- 얕은 복사(슬라이싱)
  - 동일한 내용을 담은 다른 값을 별도의 변수에 설정
  - a = list(b) 또는 a = b[:]
  - 리스트 안에 리스트가 있는 경우 내부 리스트는 같은 메모리 주소에 저장됨
  - 이차원 리스트를 생성하는 경우 문제가 됨 : 내부 리스트의 값을 수정하면 원본도 수정됨

- 깊은 복사
  - 동일한 내용을 다른 메모리 주소에 저장
  - import copy 필요
  - a = copy.deepcopy(b)
