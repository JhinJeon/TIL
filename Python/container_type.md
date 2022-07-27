## 자료의 타입
1. None : 값이 없음을 나타내기 위해 사용, 함수에서 '없음'이라는 값을 반환하기 위해서도 사용
2. Boolean : 논리적으로 True/False를 나타내기 위해 사용

### 컨테이너

- 여러 개의 데이터 값을 담을 수 있는 객체
- 서로 다른 자료형을 저장할 수 있음
- 대표적으로 list
- 컨테이너는 순서가 있는(ordered) 데이터와 순서가 없는 데이터(unordered)가 있음

### 튜플(tuple)

- 소괄호 ( ) 로 표시
- 순서가 있는 컨테이너이지만 값 수정 불가능
- 인덱스 조회 가능
- 튜플은 마지막 항목에도 쉼표로 마무리하는 게 좋음(오류 X)
- print() 구문에 사용됨

### 셋(set)

- 수학의 집합과 동일
- 데이터의 중복을 허용하지 않음
- 순서가 없음(비시퀀스형 컨테이너) : 인덱스 사용 불가
- 가변 자료형 : 담고 있는 요소 수정 가능
- 빈 셋을 만들고 싶으면 set() 을 사용할 것
- 셋끼리 집합 연산 가능
    - & : 합집합
    - | : 교집합
    - '-' : 차집합
    - ^ : 대칭차집합(합집합 - 교집합)