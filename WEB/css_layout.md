## CSS 레이아웃

### 레이아웃 기술 출시 순서

- Display
- position
- Float(CSS1)
- Flexbox
- Grid
- 기타 : 반응형 웹 디자인(2010), 미디어 쿼리(2012)
- 최신 버전이라고 항상 좋은 것은 아님(안정성)

## float

- 이미지가 텍스트 영역의 일부를 차지하고 싶게 만들 때 사용
- 현재는 많이 사용하지는 않음
- position으로도 구현 가능

## flexbox

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- display: flex;
- 블록 요소를 인라인처럼 보이게 설정
  - 내용물을 부모 요소의 크기만큼 차지하게 만들기 가능

## flexible box layout

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃
- 수직 정렬과 일정한 간격으로 정렬 구현을 쉽게 할 수 있음

- 축
  - main axis(메인 축)
  - cross axis(교차 축)
- 구성 요소
  - Flex Container(부모 요소)
  - Flex Item(자식 요소)

## Flex 속성

- 배치 설정
  - flex-direction
    - main axis의 방향 설정(열 방향, 열 역방향, 행 방향, 행 역방향)
  - flex-wrap
    - nowrap : 한 줄 안에 들어가도록 크기 조정(기본값)
    - -wrap: 크기 고정, 크기 초과 시 자동 줄바꿈
- 공간 나누기
  - justify-content(main axis 기준)
  - align-content(cross axis 기준)
- 역방향의 경우 HTML 태그 순서와 시각적으로 다름(눈으로 보이는 것과 코드 실행 순서가 다름)
- 크롬 개발자 도구에서 테스트 가능

# CSS 우선순위

- 동일한 우선순위라면 css 파일의 가장 아래쪽 항목이 우선순위 높음

1. \!important 붙은 속성
2. 인라인 스타일(html 파일에서 태그 안에 style=로 설정한 값)
3. id(\#)로 정의된 속성
4. 클래스, 태그(대괄호로 정의)
    - 클래스/태그 중에서는 더 많은 클래스/태그에 달린 css 값이 더 높은 우선순위를 가짐