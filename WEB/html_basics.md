## HTML 복습

- html은 자식과 부모로 구성된 DOM Tree 구조를 가짐
- 브라우저는 html 문서를 바탕으로 DOM Tree 생성

## head

- 문서에는 직접적으로 나타나지 않음
- 데이터를 설명하는 데이터
- 인코딩 방식 설정 : charset="인코딩 방식"
- 다만 title의 경우 입력한 값이 브라우저의 탭에 표시됨

## body

- 사용자가 직접 볼 수 있는 부분

## 요소(element)

- 태그(tag)와 내용(content)로 구성됨
- 여는 태그와 닫는 태그로 요소를 감싸기
  - \<태그>요소\<\/태그>


## 개발자 도구

- 브라우저에서 F12 누르기

## anchor tag

- 다른 웹 페이지와 연결
- \<a href="연결할 웹 페이지 URL">\</a>
- href : 하이퍼링크 레퍼런스, 어느 링크를 참조하는지 표시

## class

- 부가적인 기능 제공

## div

- 가상의 레이아웃 설정(공간 분리)
- 별도의 기능 없음(non-semantic)
- 줄 전체를 블록으로 점유

## span

-별도의 기능 없음(non-semantic)

# HTML 문서 구조화

인라인과 블록은 요소를 구성하는 내용들

## 인라인

- 인라인은 글자처럼 취급
- 자신이 보유한 내용만큼의 크기만 차지
- strong, span, a 등...

## 블록 요소

- 한 줄 모두를 차지
- div 등

## 시맨틱 태그

- 문서 영역에 의미를 부여
- header, section, footer 설정
- 웹 페이지 접근성 개선

## form

- 정보를 서버에 제출하기 위해 사용하는 태그
- form의 기본 속성
  - action : form을 처리할 서버의 URL
  - method : form을 제출할 때 사용할 HTTP 메서드(get 또는 post)

## input

- 서버로 넘기는 값을 입력받는 폼
- type : 정보를 입력받는 형태(text, checkbox, submit 등)
- label : 어떤 정보를 입력해야 하는지 알려주는 부연 설명(레이블)
  - \<label for="input_name">레이블\</label>
- id : label에 입력한 for=와 동일한 이름을 사용해야 함
  - \<input id="input_name">
  - 동일한 이름을 사용하지 않으면 label과 input이 적절하게 매치되지 않을 수 있음
  - checkbox 형태의 input인 경우 레이블을 클릭해도 체크박스를 설정/해제할 수 있음



### 선택자

- 스타일을 지정하는 구문
- 속성, 값으로 선언
```
h1 {
  color: blue;  #선언
  font-size: 15px;  #속성: 값;
}
```
- 속성: 값은 세미콜론(;)을 기준으로 여러 개 정할 수 있음
- 요소 선택자 : html 문서 내의 특정 태그를 선택
- 클래스 선택자 : 사용자가 원하는 요소만 선택
  - 선택자를 선언할 때 .클래스명 으로 설정한 후 적용하고 싶은 요소에 해당 class="아이디명" 입력
- id 선택자 : 고유하게 식별하고 싶은 요소인 경우
  - #아이디명으로 선택자를 설정한 후 적용하고 싶은 요소에 id="아이디명" 입력

### 결합자

- 일반 형제 결합자
  - \~로 표시
  - selectorA와 병렬적인(같은 깊이에 있는) 요소들 중 뒤에 있는 모든 요소에 적용
  
- 인접 형제 결합자
  - \+로 표시
  - selectorA와 병렬적인(같은 깊이에 있는) 요소들 중 바로 뒤에 있는 요소에만 적용

- 자식 형제 결합자
  - \>로 표시
  - selectorA 바로 하위에 있는 selectorB 요소들만 포함

- 자손 결합자
  - 공백으로 표시
  - selectorA 하위의 모든 selectorB 요소(하위의 하위도 포함)
  - 예) div 태그 하위의 p 태그에만 스타일을 적용하고 싶을 때

### display

- block
  - 줄 바꿈이 일어나는 요소
  - 화면 전체를 차지
  - div 태그로 설정

- inline
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - 내용 너비만큼 가로폭 차지
  - 상하 여백은 line-height로 지정
  - **너비, 높이, margin-top, margin-bottom 지정 불가**
  - span 태그로 설정

- 스타일 설정할 때 div 안에 display: inline-block; 설정 시 블록을 인라인처럼 표시할 수 있음(프로그램 내부에서는 블록으로 취급)
  - 이렇게 설정하면 **인라인처럼 보이는 요소에 너비, 높이, margin-top, margin-bottom 지정 가능**

### position

- 문서 상에서 요소의 위치를 지정
- 공간이 없을 경우 다음 블록으로 줄 바꿈
- 모든 요소의 기본 position은 static
  - static(normal) : box모델에서 좌상단-우하단으로 표시되는 normal flow
- 상대 기준으로 위치 설정
  - absolute
  -  static의 위치가 변경될 위치에서 top, left만큼 이동한 것으로 간주, 요소의 차지 공간은 없음
  -  부모 클래스 중에서 static이 아닌 요소를 기준
    - top : static에서 아래로 이동
    - left : static에서 오른쪽으로 이동
    - 이하의 블록들은 위쪽으로 자동 정렬
    - 주의 : 부모 요소가 position: relative인지 확인할 것
  - relative: static의 위치가 변경될 위치에서 top, left만큼 이동한 것으로 간주, 요소의 차지 공간은 static과 동일
    - top : static에서 아래로 이동
    - left : static에서 오른쪽으로 이동
  - fixed:


## 기타

- html 관련 정보는 뒤에 mdn을 붙이면 공신력 있는 정보 검색 가능
- snippet : ! + tab 입력 시 html 기본 포맷이 등장
- marque 태그 : 이미지가 자동으로 이동하게 만드는 태그(권장하지 않음)