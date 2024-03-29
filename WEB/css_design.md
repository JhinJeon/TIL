## CSS

- Cascading Style Sheets
- 우선순위가 같으면 가장 나중에 선언된 스타일이 우선순위 높음
- 선택자, 결합자, display, position으로 구분

## CSS 원칙

- 모든 요소는 네모(박스모델)이다.
  - 박스 모델은 Margin-Border-Padding-Content로 구성된다.
  - 여백 크기 : margin {x}: a b c d
    - x에 들어가는 숫자만큼 a, b, c, d 개수 조절
- 요소들은 좌상단부터 우하단 방향으로 쌓인다.

## css 구문

- 선택자, 선언, 속성, 값으로 구성됨
  - 선택자를 통해 스타일을 지정할 HTML 요소 선택
  - 속성과 값을 정해서 어떤 스타일을 어떻게 변경할지 결정

## CSS 정의 방법
1. 인라인

- html 문서 내에 body를 구성하는 개별 구문에 css 선언

2. 내부참조

- head에 스타일 선언
- \<style>선택자\</style>
- 선택자에 해당하는 모든 요소에 적용

3. 외부참조

- 별도의 .css 파일 생성 후 연결
- head에서 \<link> 태그로 연결
- \<link:css> 입력하면 자동으로 스타일시트 기본 포맷 입력


## Css 선택자(selector)

- 기본 선택자
  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자

- 결합자(Combinatiors)
  - 자손 결합자, 자식 결합자
  - 일반 형제 결합자, 인접 형제 결합자

- 의사 클래스/요소(Pseudo Class)

## 개발자 도구의 선택자
- lorem : 의미 없는 텍스트로 구성된 문장 표시(문자열이 잘 출력되는지 확인하는 용도)

## Css 선택자

- 요소 선택자 : HTML 태그 직접 선택
- 클래스 선택자 : 마침표(.)로 시작하며, 해당 클래스가 적용된 항목 선택
- 아이디 선택자 : 
  - \# 문자로 시작하며 해당 아이디가 적용된 항목 선택
  - 일반적으로 하나의 문서에 1번만 사용
  - 여러 번 사용해도 동작하지만, 단일 ID 사용이 권장됨
- CSS 구문에서는 동일한 우선순위인 경우 가장 아래쪽에 있는 코드가 우선 적용

## 크기 단위

- 픽셀 : 고정 수치, 화면 크기에 따라 변하지 않음
- 비율(%) : 백분율 단위, 가변 레이아웃에서 사용
- em : (바로 위, 부모 요소에 대한) 상속 영향을 받음(상대적 사이즈)
- rem : (바로 위, 부모 요소에 대한) 상속 영향을 받지 않음, 최상위 요소 기준 배수의 단위
- viewpoint : 웹 페이지를 방문한 유저에게 바로 보이는 웹 페이지 영역
  - 디바이스의 viewpoint를 기준으로 상대적인 사이즈가 결정됨
  - vw, vh, vmin, vmax 등
- px는 브라우저 크기에 상관없이 일정, vw는 브라우저 크기에 따라 변경

## 결합자(Combinators)

- 자손 결합자 : 공백으로 설정, 이하의 모든 selector에게 적용
- 자식 결합자 : >로 설정, 바로 아래의 selector에게만 영향
- 일반 형제 결합자 : ~로 설정, 뒤에 있는 모든 selector들 선택
- 인접 형제 결합자 : +로 설정, 바로 뒤에 있는 selector 선택

## Box model

- margin : 테두리 가장 바깥쪽, 배경 설정 불가
  - margin 값은 시계 방향으로 설정 : 상 우 하 좌 순
- border : 테두리 영역
- padding : 테두리 내부 여백
- content : 페이지의 실제 내용(텍스트, 이미지 등)

## box-sizing

- 기본적으로 모든 요소의 box-sizing은 contents box
  - Padding을 제외한 순수 contents 영역만 box로 지정
- contents-box : 컨텐츠 영역의 너비만 계산
- border-box : contents와 외부 여백을 합한 영역의 너비 계산
- display에 따라 크기와 배치가 달라짐

## 인라인(inline)

- 인라인의 기본 넓이는 콘텐츠 영역만큼
- 인라인은 텍스트 취급

margin-right: auto; 오른쪽 자동 정렬
margin-left: auto; 왼쪽 자동 정렬

margin-right: auto;

margin-left: auto; 가운데 자동 정렬

## 추가 : 테두리(border) 만들 떄 유의사항

- border-style을 설정해야 함(기본값 none)
  - border-style을 설정하지 않으면 border-color, border-radius 등을 설정해도 테두리가 표시되지 않음

- 또는 border: solid를 입력해도 border-style이 solid로 입력된 것으로 간주됨