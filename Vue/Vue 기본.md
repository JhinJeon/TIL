
- [Vue intro](#vue-intro)
  - [Front-end Framework](#front-end-framework)
  - [Web App](#web-app)
- [SPA(Single Page Application)](#spasingle-page-application)
  - [SSR(Server Side Rendering)](#ssrserver-side-rendering)
  - [CSR(Client Side Rendering)](#csrclient-side-rendering)
    - [CSR의 장단점](#csr의-장단점)
  - [CSR vs SSR](#csr-vs-ssr)
- [Vue CDN](#vue-cdn)
- [Vue 함수](#vue-함수)
  - [입력값과 DOM 연계](#입력값과-dom-연계)
- [MVVM Pattern](#mvvm-pattern)
  - [View Model(Vue)](#view-modelvue)
  - [생성자 함수](#생성자-함수)
  - [el(element)](#elelement)
- [Basic Syntax](#basic-syntax)
  - [v-show vs v-if](#v-show-vs-v-if)
  - [v-for](#v-for)
    - [key 이름 설정](#key-이름-설정)
  - [v-on](#v-on)
- [Vue advanced](#vue-advanced)
  - [computed](#computed)
  - [watch](#watch)

# Vue intro

## Front-end Framework

- 사용자에게 표시할 화면을 설계

## Web App

- 웹 브라우저이서 실행되는 애플리케이션 소프트웨어
- 개발자 도구 \> 디바이스 모드
- 웹 페이지가 애플리케이션처럼 보이도록 UI/UX를 변경하는 기술

# SPA(Single Page Application)

- SPA는 서버에서 1장의 HTML만 전달받아 모든 요청에 대응할 수 있다.
  - 이 때 서버에서 받아오는 문서는 빈 HTML 문서
- CSR(Client Side Rendering) 방식으로 요청을 처리
- 요청 처리 과정에서 별도의 HTML 문서를 생성하지 않는다.

## SSR(Server Side Rendering)

- 서버가 사용자의 요청에 적합한 HTML 문서를 렌더링해서 보여주는 방식
- 매 요청마다 새로운 페이지를 받아야 할 수 있다.

## CSR(Client Side Rendering)

- 서버에서 빈 HTML 문서를 받아온 후, 각 요청에 대한 대응은 Javascript를 이용해 필요한 부분만 렌더링
- 필요한 페이지를 서버에 AJAX로 요청
- 서버는 화면을 그리기 위해 필요한 정보를 JSON 방식으로 전달
- JSON 형식 데이터를 Javascript로 처리하여 DOM 트리에 반영(렌더링)

### CSR의 장단점

1. 장점

- 모든 HTML 페이지를 서버로부터 받아서 표시하지 않아도 된다.(트래픽 감소, 응답 속도 향상)
- 각 요청이 끊기지 않고 계속 진행할 수 있다.(UX 향상)
- 백엔드와 프론트엔드 작업 영역을 명확히 분리할 수 있다(협업 용이)

2. 단점

- 첫 구동에 필요한 데이터가 많을 수록 오랜 시간이 걸린다.
- 모바일에 설치된 웹 애플리케이션을 실행하는 경우 잠깐의 로딩 시간이 필요하다.
- 서버는 텅 빈 HTML 파일만 제공하므로 검색엔진 최적화(SEO)에 불리하다.

## CSR vs SSR

- 내 서비스에 더 적합한 렌더링 방식을 사용해야 한다.
- SPA 서비스에서도 SSR을 지원하는 프레임워크가 발전하고 있다.
  - Vue의 Nuxt.js, React의 Next.js, Angular의 Universe 등

# Vue CDN

- Vue로 작업을 시작하려면 CDN을 가져와야 한다.

- Vue === JS Front-end Framework
  - Bootstrap에서 사용했던 CDN 방식
  - Vue 공식문서에 있는 script 태그 코드 복붙하기

> ## Note : 버전 주의
> 앞으로 실습할 Vue는 Vue2 버전으로 작업하므로, vue 공식문서에서 Docs > Vue 2 Docs를 참고해야 한다.

# Vue 함수

1. 생성자 함수 Vue()

- 작성법은 자바스크립트처럼 쓰면 된다(Vue는 일종의 자바스크립트 보조 장치)

```js
const app = new Vue({

})
```

## 입력값과 DOM 연계

- input 태그에 v-model 설정

```js
<body>
  <div id="app">
    <p id="name">name : {{ message }}</p>
    <input id="inputName" type="text" v-model="message">
  </div>
    <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    // CODE HERE
    const app = new Vue({
      el: '#app',
      data: {
        message: '',
      }
    })
  </script>
</body>
```

> ## Note : Vue3 vs Vue2
> - Vue3에서 새로운 기능 추가 등 개선사항이 있으나 안정성과 참고 자료 등은 Vue2로 배우는 것이 편하다.
> - Vue3로 전환되는 과정을 거칠 예정

# MVVM Pattern

- Model, View, Viewmodel
- Viewmodel은 이벤트가 발생하면 이를 인식하고(DOM Listeners) 처리하는 역할 담당
- View는 사용자에게 보이는 부분(DOM)
- Model은 실제 데이터(JSON)
  - Vue는 Viewmodel 담당

- Model과 View는 독립적이다(직접 연결되지 않음)

## View Model(Vue)

- View를 위한 모델
- View와 연결(Binding)되어 Action을 주고 받는다.
- Model이 변경되면 View Model과 바인딩된 View도 같이 변경된다.

## 생성자 함수

- 동일한 객체를 여러 개 만들고 싶을 때 사용
- 함수 이름은 대문자로 시작
- 생성자 함수를 사용할 때는 반드시 new 연산자를 사용해야 한다.

```js
function Member(name, age, sId) {
  this.name = name
  this.age = age
  this.sId = sId
}

const member3 = new Member('isaac', 21, 2022654321)
```

## el(element)

- View와 Model을 연결(Mount)하는 옵션
  - HTML에서 작성한 id 또는 class를 el:의 값으로 설정해서 연결 가능
- Vue instance와 연결되지 않은 DOM 외부는 Vue의 영향을 받지 않는다(Vue의 속성 및 메서드 사용 불가)

# Basic Syntax

- 렌더링 된 DOM을 기본 Vue instance의 data에 선언적으로 바인딩할 수 있는 HTML 기반 template syntax 사용
  - 렌더링 된 DOM : 브라우저에 의해 보기 좋게 그려질 HTML 코드
  - v-html = 'rawHTML'

> ## Note : v-html 사용 시 주의사항
> 사용자가 입력하거나 제공하는 콘텐츠에는 *절대* 사용하지 말 것 - XSS 공격에 취약하다.

## v-show vs v-if

1. v-show : Expensive initial load, cheap toggle
- v-show는 표현식 결과와 상관없이 렌더링되므로 초기 렌더링 비용은 높을 수 있다.
- 다만 display 속성 변경으로 표현 여부를 판단하므로 렌더링 후 toggle 비용은 적다.

2. v-if : Cheap initial load, expensive toggle
- v-if의 경우 표현식 결과가 false인 경우 렌더링 자체를 시도하지 않는다(초기 비용 낮음)
- 단, 표현식 값이 자주 변경되는 경우 다시 렌더링을 해야 하므로 toggle 비용이 증가할 수 있다.

> ### Note : 대체로 후자(v-if)를 사용하는 경우가 많을 것 

## v-for

- 태그 안에 입력된 값의 반복
- 파이썬의 for문처럼 순회 가능한 개체를 하나씩 반환
- v-for=(값, 키) in 순회할 객체 : key=키
  - key=에 들어가는 값은  v-for가 Vue 내부에서 다른 for문과 간섭하지 않도록 작동할 수 있도록 구분하기 위함

```html
<div v-for="(item, index) in myArr2" :key="`arry-${index}`">
  <p>{{ index }}번째 아이템</p>
  <p>{{ item.name }}</p>
</div>
```
```js
myArr2: [
  { id: 1, name: 'python', completed: true },
  { id: 2, name: 'django', completed: true },
  { id: 3, name: 'vue.js', completed: false },
],
```

### key 이름 설정

- v-for문에 입력하는 :key값은 vue가 각 순회 항목을 구별할 수 있도록 해 주는 고유한 값이다.
- v-for="()" 에 (값, 키)쌍을 입력한 경우 :key="값.키"로 설정하는 경우 개별 항목의 key가 인덱스 번호로 부여된다.

> ## Note : 키 이름 선정
> - :key=의 값으로 v-for에 입력한 '키'를 다시 사용하는 경우 변수명 충돌로 인한 오류가 발생할 수 있다.
> - 다만 객체에서는 key 값이 중복될 여지가 없으므로 '키' 변수명을 다시 사용해도 된다.

```html
<!-- 1. :key 값을 "값.키"의 형식으로 설정한 경우 -->
<div v-for="(value, key) in myObj" :key="value.key">
  <p>{{ key }} : {{ value }}</p>
</div>

<!-- 2. :key 값을 "키"로 설정한 경우(이하 myObj의 형태에 따라 사용 가능) -->
<div v-for="(value, key) in myObj" :key="value.key">
  <p>{{ key }} : {{ value }}</p>
</div>
```

```js
myObj: {
    name: 'harry',
    age: 27
},
```

## v-on

- method를 통한 data 조작도 가능
- 일반 함수를 호출할 때와 동일한 방식
- ':'(콜론)을 통해 전달받은 인자 확인
- 값으로 JS 표현식 작성
- 대기하고 있던 이벤트가 발생하면 할당된 표현식을 실행한다.
- '@'로 간소화 가능(v-on 대신 입력)

# Vue advanced

## computed

- vue instance가 가진 옵션 중 하나
- computed 객체에 정의한 함수를 페이지가 최초로 렌더링 될 때 호출하여 계산
  - 계산 결과가 변하기 전까지 함수를 재호출하지 않는 대신 계산된 값 반환

- 연산 결과를 저장하는 역할 수행 : 호출 횟수 절약 가능

```js
const app = new Vue({
  el: '#app',
  data: {
    number1: 100,
    number2: 100
  },
  computed: {
    add_computed: function () {
      console.log('computed 실행됨!')
      return this.number1 + this.number2
    }
  },
})
```

- computed는 this.number1 또는 this.number2에 변화가 있을 때에만 새로운 연산 수행

## watch

- 감시할 대상 설정
- 과거값을 보유하고 있다.
- 디버깅 할 때 유용

```js
const app = new Vue({
  el: '#app',
  data: {
    number: 0,
    name: '',
    myObj: { completed: true }
  },
  watch: {
    number: function (val, oldVal) {
      console.log(val, oldVal)
    },
  })
```