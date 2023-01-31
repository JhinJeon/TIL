# React 작업 시 CSS 스타일 충돌하는 현상

- 기본적으로 글로벌 네임스페이스(global namespace)를 사용하므로, 상위 컴포넌트에 적용한 CSS 스타일이 하위 컴포넌트에 \<style> 태그로 적용된다.
- 이 문제를 해결하려면 css-module을 사용해야 한다.

# CSS Module 이용하기

1. css 확장자명을 .css에서 .module.css로 수정
2. css 모듈을 불러올 자바스크립트 컴포넌트에서 import styles from "css 모듈 파일 주소" 입력
3. className={styles.css변수명} 입력

```css
/* LastSeason.module.css */
.miniBlock {
  background-color: #1d1e22;
  margin: 10px;
  padding: 5px;
  border: solid 0.5px white;
}
```

```js
// LastSeason.js
import styles from "./LastSeason.module.css";

<Row className={styles.miniBlock}>
```
