1. 블록(구역)의 정 가운데에 두고 싶은 경우

- mx-auto

```html
<div class="mx-auto bg-info" style="width: 200px;">Centered element</div>
```

2. 블록 내에서 콘텐츠를 계단식으로 나누어서 배치하고 싶은 경우

- b-col, b-row 사용
  - b-col은 태그 내의 콘텐츠들을 세로 방향으로 정렬한다.
  - b-row는 태그 내의 콘텐츠들을 가로 방향으로 정렬한다.
  - b-col 태그 내에 b-row태그를 넣을 수 있고, 그 반대도 가능하다.

3. 커스텀 색상 코드를 구하고 싶은 경우

- color picker를 사용하자.
- 원하는 색상을 고른 후 #(숫자+문자 6자리 조합) 코드를 복붙하면 된다.
- [https://www.quackit.com/css/css_color_codes.cfm]

4. router에서 store의 정보를 불러오고 싶을 때

- 1. import store from "../store/index.js"로 store의 정보를 가져온다.
- 2. store.(객체명).(인스턴스명)으로 원하는 인스턴스를 불러온다.

주의 : 위 방법은 router 전역 환경에서는 사용이 불가능한 것 같다. 맨 땅에 하지말고 beforeEnter나 beforeEach 안에서 불러와서 정의해야 한다.

```js
router.beforeEach((to, from, next) => {
  const isLoggedIn = store.getters.isLogin
  // console.log(to)
  // console.log(from)
  console.log(isLoggedIn)
  const authPages = ['RecommendView', 'DetailView', 'BookView', 'InitialLogin', 'HomeView',]
  const isAuthRequired = authPages.includes(to.name)
  if (isAuthRequired && !isLoggedIn) {
    next({ name: 'loginView' })
  } else {
    next()
  }
})
```