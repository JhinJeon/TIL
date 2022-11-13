목차
- [UX & UI](#ux--ui)
  - [UX](#ux)
  - [UI](#ui)
    - [좋은 UI를 설계하려면](#좋은-ui를-설계하려면)
- [Prototyping](#prototyping)
  - [Figma를 사용하는 이유](#figma를-사용하는-이유)
- [프로젝트를 시작하기 전에 해야 할 것](#프로젝트를-시작하기-전에-해야-할-것)
- [협업 시](#협업-시)
- [라우팅(Routing)](#라우팅routing)
  - [Routing ins SPA / CSR](#routing-ins-spa--csr)
  - [라우팅이 필요한 이유](#라우팅이-필요한-이유)
- [Vue Router](#vue-router)
  - [Vue Router 시작하기(코드 작성)](#vue-router-시작하기코드-작성)
  - [history mode](#history-mode)
- [router-link](#router-link)
- [router-view](#router-view)
- [src/views 폴더](#srcviews-폴더)
- [v-bind 적용](#v-bind-적용)
  - [프로그래밍 방식 네비게이션](#프로그래밍-방식-네비게이션)
- [Dynamic Route Matching](#dynamic-route-matching)
  - [lazy-loading](#lazy-loading)
- [Navigation Guard](#navigation-guard)
  - [Navigation Guard의 종류](#navigation-guard의-종류)
  - [Global Before Guard(전역 가드)](#global-before-guard전역-가드)
  - [beforeEnter() -라우터 가드](#beforeenter--라우터-가드)
    - [params 변화 감지](#params-변화-감지)
- [404 Not Found](#404-not-found)


# UX & UI

## UX

- 데이터를 기반으로 유저를 조사하고 분석하여 개발자, 디자이너가 이해할 수 있게 소통
- 유저의 느낌, 태도, 행동을 디자인한다.
- 좋은 UX를 위해서는 사람들의 마음과 생각을 정리해서 우리 제품에 녹여내고, 다양한 설계와 조사가 필요하다.
  - 설문조사, 데이터 설계 및 정제, 시나리오 구상, 프로토타입 설계 등
- 학문적인 정의 : 유저가 겪는 모든 경험(컴퓨터와 무관한 부분까지 포함)

## UI

- 유저에게 표시되는 화면을 디자인
- UX를 고려한 디자인 반영
- 기능 개선 및 추가가 필요한 경우 Front-end 개발자와 가장 많이 소통한다.
- 학문적인 정의 : 비시각적인 부분(소리 등)까지 포함한 디자인

### 좋은 UI를 설계하려면

- 심미성보다 편의성, 편리성을 고려해야 한다.
- UI 디자인에 있어 가장 중요한 것은 **협업**

# Prototyping

- 애플리케이션의 프로토타입(완성되기 전 버전)을 제작하는 것
- 한 번에 완성 버전이 나올 수 없으므로 중간 중간 현재 상태를 체크해야 한다.
- Protyping Tool은 대표적으로 *Figma*가 있다.

## Figma를 사용하는 이유

- 웹 기반 시스템 : 리소스 소모가 적고, 작업 내역이 웹에 저장된다.
- **실시간으로 협업**할 수 있는 기능 제공
- 직관적이고 다양한 디자인 툴 제공
- 사용자들이 제작한 다양한 플러그인(VSCode의 확장프로그램 등)이 존재한다.
- 대부분의 기능을 **무료로 사용할 수 있다**.
- 높은 성능을 보이지는 않지만 원활한 협업을 통해 디자인에 집중할 수 있는 툴이다.

# 프로젝트를 시작하기 전에 해야 할 것

- 개발부터 시작하지 말고 (개발 시간만큼)<u>충분한 기획</u>을 거칠 것
- 우리가 완성하고자 하는 대략적인 모습을 그려보는 과정이 필요하다(프로토타이핑).
- 개발 과정에서 기획 단계에서 구상한 화면이나 API 등을 확인할 수 있다.
- 설계와 기획이 끝난 후 개발을 시작해야 체계적인 진행이 가능하다.

# 협업 시

- 협업은 프로젝트와 팀이 성공하기 위한 토대
- 효과적인 협업을 위한 다양한 방법과 도구를 찾고, 사용법을 학습하며 여러 프로젝트를 경험하는 과정이 필요하다.

# 라우팅(Routing)

- 네트워크에서 경로를 선택하는 프로세스
- 웹 서비스의 라우팅은 유저가 방문한 URL에 대해 적절한 결과를 응답하는 것
- 서버가 모든 라우팅을 통제한다(render, redirect 등).

## Routing ins SPA / CSR

- 서버는 하나의 html 파일만을 제공한다.
- 그 밖의 동작은 HTML 문서 상에서 JavaScript 코드를 통해 구현된다.
  - axios 등 AJAX 요청을 보낼 수 있는 수단을 이용해 데이터를 가져오고 처리한다.
- 즉 하나의 URL만 처리할 수 있다.

## 라우팅이 필요한 이유

- 라우팅이 있어야 사용자가 URL을 통한 페이지의 변화를 감지할 수 있다.
- (라우팅이 없으면) 페이지가 무엇을 렌더링하는지 알 수 없고, 새로고침 및 링크 공유 시 메인 페이지를 반환한다.
- 라우팅이 없으면 **브라우저의 뒤로 가기 기능을 사용할 수 없다.**

# Vue Router

- Vue에서 제공하는 공식 라우터
- SPA(Single Page Application) 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공한다.
- 라우트(routes)에 컴포넌트를 매핑한 후, 어떤 URL에서 렌더링할지 알려준다.
  - SPA를 MPA(Multiple Page Application)처럼 URL을 이동하며 사용할 수 있다.
  - 실제로 URL을 이동하는 것이 아니라 표시하는 컴포넌트에 변화를 주는 것(여러 페이지가 이동하는 것처럼 느끼게 한다.)
  - SPA의 단점 중 하나인 "URL이 변경되지 않는다"를 해결한다.

## Vue Router 시작하기(코드 작성)

- CLI에 vue add router 입력

> ## Note : 기존 프로젝트에 router를 추가하는 경우
> - 기존 프로젝트 진행 중에 router를 추가하면 App.vue를 덮어쓰므로 라우터가 필요한 경우 파일을 백업해 두어야 한다.

- 이후 뜨는 질문창에 y 입력(history mode 사용 여부 포함)

## history mode

- 브라우저의 history API를 활용한 방식
  - 새로고침 없이 URL 이동 기록을 남길 수 있다.
  - 우리에게 익숙한 URL 구조로 사용 가능하다.

- history mode 미사용 시 '#'로 표시된다.

# router-link

- a 태그와 비슷하게 url로 이동하는 역할
- routes 폴더에 등록된 컴포넌트와 매핑된다.
- 목표 경로는 'to='로 설정
- HTML에서는 a 태그로 렌더링되지만, 필요에 따라 바뀔 수 있다.

```html
<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
    <router-view/>
  </div>
</template>
```

# router-view

- 주어진 URL에 일치하는 컴포넌트를 렌더링 해 주는 컴포넌트
- 실제 컴포넌트가 DOM에 부착되어 보이는 자리
- router-view는 Django의 {block } tag와 유사한 기능 수행
- App.vue는 base.html의 역할

# src/views 폴더

- router-view에 들어갈 컴포넌트 작성
- 컴포넌트를 components 폴더와 views 폴더에 나누어 작성해야 한다.
  - 한 페이지를 구성하는 하위 컴포넌트(라우팅에 연결되지 않은 vue)는 components 폴더 안에 작성
  - URL 입력 시 표시하는 컴포넌트(라우터에 연결된 vue)는 views 폴더 안에 작성

# v-bind 적용

- 동적인 웹 사이트 주소명을 구현하려면 v-bind를 구현해야 한다.
- v-bind의 축약자인 ':'을 to 앞에 붙이기

```html
<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'home' }">Home</router-link> |
      <router-link :to="{ name: 'about' }">About</router-link>
    </nav>
    <router-view />
  </div>
</template>
```

## 프로그래밍 방식 네비게이션

- 다른 URL로 이동할 때 this.$router.push 사용
- history stack에 기록이 남기 때문에 뒤로 가기 버튼을 이용해 이전 URL로 돌아갈 수 있다.

- 위(router-link 태그)가 선언 방식, 아래(button 태그)가 프로그래밍 방식

```vue
<template>
  <div class="about">
    <h1>This is an about page</h1>
    <router-link :to="{ name: 'home' }">홈으로!</router-link>
    <br />
    <button @click="toHome">홈으로!</button>
  </div>
</template>

<script>
export default {
  name: "AboutView",
  methods: {
    toHome() {
      this.$router.push({ name: "home" });
    },
  },
};
</script>
```

# Dynamic Route Matching

- URL의 특정 값을 변수처럼 사용할 수 있다.

## lazy-loading

- 잘 사용하지 않는(또는 당장 사용하지 않는) 컴포넌트는 처음부터 불러올 필요는 없다.
- 특정 라우트에 방문할 때 필요한 컴포넌트를 별도로 불러오는 방식
- 최초 불러오는 시간(initialize)이 빨라지는 효과가 있다.

# Navigation Guard

- Vue router를 통해 특정 URL에 접근할 때 다른 URL로 리다이렉트하거나 접근 자체를 막는 수단
- 사용자 인증 정보가 없는 경우 등 접근을 차단해야 하는 경우 유용하다.

## Navigation Guard의 종류

- 전역 가드 : 애플리케이션 전역에서 동작
- 라우터 가드 : 특정 URL에서 동작
- 컴포넌트 가드 : 라우터 컴포넌트에서 정의

## Global Before Guard(전역 가드)

- **다른 URL로 이동할 때** 항상 실행
- router/index.js에서 router.beforeEach()를 이용해 설정
- 콜백 함수는 to, from, next 인자를 받는다.
  - to : 이동할 URL의 정보
  - from : 현재 URL의 정보
  - next : 지정한 URL로 이동하기 위해 호출하는 함수
    - 반드시 한 번만 호출되어야 하며, 기본적으로 to에 작성한 URL로 이동한다.

```js
// index.js 맨 아래쪽
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// beforeEach() 함수 추가
router.beforeEach((to, from, next) => {
  console.log('to', to)
  console.log('from', from)
  console.log('next', next)
  next()  // next() 함수를 호출하지 않으면 화면이 넘어가지 않는다.
})

export default router
```

> ## Note : 전역 가드 작동 원리
> - 기본적으로 기본 페이지(to)로 이동하지만 이동이 불가능한 경우 대체 페이지(조건문으로 표시된 페이지)로 이동

## beforeEnter() -라우터 가드

- route에 진입 시 실행됨
- 콜백 함수는 to, from, next를 인자로 받는다.
- 라우터를 등록한 위치에 추가
- 단, 다른 경로에서 탐색할 때만 실행된다.

### params 변화 감지

- url 값이 변화하지 않는 이유 : 컴포넌트가 재사용되었기 때문
- 기존 컴포넌트를 지우고 새로운 컴포넌트를 만드는 대신 재사용하는 것이 효율적이다.
- beforeRouteUpdate()를 이용해 처리

# 404 Not Found

- 형식은 유효하지만 특정 리소스를 찾을 수 없는 경우
  - 예를 들어 1번 게시물을 요청했는데 1번 게시물이 삭제된 경우