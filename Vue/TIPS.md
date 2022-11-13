# params로 받은 정보를 쓸 때

- 배울 때는 $router.params.(파라미터 이름)으로 정보를 받았다.
- 하지만 공식 문서에 따르면 router/index.js에서 props:true 설정하면 개별 vue 파일에서 상위 컴포넌트 props 받는 것처럼 사용할 수 있다.

## Optional Chaining

- '?'를 입력하여 사용
- ?. 앞의 평가 대상이 undefined나 null인 경우 에러 대신 undefined 반환

```js
<div>
  <h1>Detail</h1>
  <p>글 번호: {{ article?.id }}</p>
  <p>글 제목: {{ article?.title }}</p>
  <p>글 내용: {{ article?.content }}</p>
  <p>작성 시간: {{ article?.createdAt }}</p>
</div>
```