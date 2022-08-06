# flexbox

- 메인 축(main axis): 아이템이 쌓이는 방향에 따라 결정됨
  - 가로로 쌓이면 가로가, 세로로 쌓이면 세로가 메인 축
- flex는 자식까지만 적용됨(자손은 적용되지 않음)

## wrap/nowrap
> 부모 클래스에 설정
- wrap : 블록의 크기 초과 시 다음 줄로 자동 줄바꿈
- nowrap : 블록의 크기가 초과하면 비율을 줄여서 한 줄에 들어갈 수 있게 조정

## justify

- 메인 축의 정렬 설정
- justify-content : 메인 축을 기준으로 flex item들을 어떻게 배치할지 설정
- 기본값은 flex-start

## align

- 교차 축(메인 축에 수직인 축)의 정렬 설정
- align-items : 교차 축을 기준으로 flex item들을 어떻게 배치할지 설정

## content와 items의 차이

- content : 정렬하려는 축이 여러개일 때
- item : 정렬하려는 축이 한 개일 때
  - 단, justify-items, justify-self는 flexbox에서 인식되지 않음

## flex 컨테이너의 자식 블록 스타일 설정

- style="flex-grow: x" : 남은 여백 중에 비율 x만큼 차지(기본값 0)

```html
<div class="container">
  <div class="item" style="flex-grow: 1;">1</div>
  <div class="item" style="flex-grow: 2;">2</div>
</div>
```

- 여백이 생기는 경우 1번 블록과 2번 블록이 늘어나서 1:2의 비율로 차지

- align-self : 개별 블록의 위치를 조절 가능

## HTML 페이지 배포하기

- netlify.com에 HTML 관련 파일들(html 문서, 스타일 css 등)을 압축해서 업로드
- Domain management - options에서 도메인명 변경 가능
- Django로 서버 제작해서 연동 가능