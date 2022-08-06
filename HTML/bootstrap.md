## Bootstrap

- 일반 HTML 문서 대비 마진이 거의 없음
- 자주 사용하는 클래스들을 모아둠

## Bootstrap 기본 원리

- 여백 조절(spacing)
  - {property}{sides}-{size}
    - property : margin 또는 padding 설정
    - sides : 어느 방향으로 여백을 낼지 결정
    - size : 여백 크기 결정
      - ex) mt-3(margin 위쪽 3), ms-5 (margin 시작 지점 5)
    - {size} 1단위당 0.25rem(4px)

## Bootstrap 사용

- Bootstrap 홈페이지 > Download > CDN via jsDelivr의 코드 복붙
- link 부분은 html의 헤드에, script 부분은 body의 마지막 부분에 붙여넣기
## 반응형 웹 페이지

- 화면의 크기에 따라 표시되는 콘텐츠를 설정할 수 있음
- 작을 때 안 보이거나 작아야 보이도록 설정도 가능
- 모바일 웹 화면에 사용 가능

## 모달 창

- 경고, 알림 등을 웹 페이지 위에 나타내는 창
- 모바일에서는 외부 배경을 터치해도 나갈 수 있지만, PC환경에서는 X를 눌러야 끌 수 있음

## Bootstraip grid system

- column 12개, grid breakpoints 6개로 구성됨