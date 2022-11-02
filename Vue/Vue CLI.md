🔔목차🔔

- [Vue CLI](#vue-cli)
  - [Node.js](#nodejs)
- [환경설정](#환경설정)
  - [Babel](#babel)
  - [Webpack](#webpack)
  - [Module](#module)
  - [Bundler](#bundler)
  - [src 폴더](#src-폴더)
- [SFC](#sfc)
  - [Component](#component)
  - [SFC(Single File Component)의 필요성](#sfcsingle-file-component의-필요성)
  - [component 등록하기](#component-등록하기)
  - [component 재사용하기](#component-재사용하기)
- [Pass Props & Emit Events](#pass-props--emit-events)
  - [Data in components](#data-in-components)
  - [Pass Props](#pass-props)
  - [Emit Events](#emit-events)
  - [pass props/ emit event 컨벤션](#pass-props-emit-event-컨벤션)

# Vue CLI

## Node.js

- 자바스크립트는 브라우저를 조작하는 유일한 언어이나, 브라우저 밖에서는 구동할 수 없는 문제가 있었다.
- Node.js를 이용하면 브라우저가 아닌 환경에서도 자바스크립트를 구동할 수 있다
- Node.js는 자바스크립트를 구동할 수 있는 런타임 환경
  - 여러 OS 환경에서 실행 가능

# 환경설정

1. 전역 구역(global, windows의 바탕 화면)에 node.js 설치

- 바탕 화면에 git bash창 실행 -> npm install -g @vue/cli 입력

2. 프로젝트 생성

- 전역 구역의 하위 구역에서 실행
- vscode로 open한 후 CLI에 vue create vue-cli 입력
- 리소스 불러오기가 완료되면 화살표 키로 vue 버전 선택 가능

3. 새로운 서버 파일 만들기

- cd vue-cli/ 입력
- 구성 파일은 자동으로 생성됨
  - 파일 용량이 상당히 크므로(133MB) github에 업로드하지 않는 것을 권장

> ## Note. 환경 설정 파일 버전 관리
> - 환경 설정 파일은 업로드하지 않고(.gitignore에 추가), 해당 환경을 구성하는 정보만 업로드(requirements.txt 등)

4. 서버 구동

- npm run serve 입력
- 로컬 주소와 네트워크 주소 제공(네트워크 주소는 보안 정책에 따라 제공되지 않을 수 있음) 

## Babel

- Javascript 컴파일러
- 자바스크립트의 ES6+ 코드를 구버전 코드로 번역(변환)해 주는 코드
  - 파편화된 다양한 버전의 코드들이 존재하므로 이를 표준화하기 위한 수단
- vue-cli의 babel.config.js가 Babel에 해당된다.

## Webpack

- 모듈 간 의존성 문제를 해결하기 위한 도구
- 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프 빌드

## Module

- 애플리케이션 파일을 분리하여 관리하는 방법
- 단일 클래스 또는 특정한 목적을 가진 복수의 함수로 구성된 라이브러리로 구성
- 모듈 수가 증가하면서 모듈 간 의존성(연결성)이 증가하며 문제 해결이 어려워지는 현상이 발생한다.
  - 이를 해결하기 위해 Webpack 사용

## Bundler

- Bundling : 모든 의존성 문제를 해결해 주는 작업
- Webpack은 Bundler의 일종
- Bundling된 결과물은 실행할 때 개별 모듈의 실행 순서에 영향을 받지 않는다.
- vue cli는 Babel, Webpack의 초기 설정이 자동으로 되어 있다.

## src 폴더

- src/assets : 정적 파일을 저장하는 디렉토리
- src/components : 하위 컴포넌트들이 위치한다.
- src/App.vue : 최상위 컴포넌트, public/index.html과 연결되어 있다.
- **src/main.js** : webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point
  - public/index.html과 src/App.vue를 연결하는 작업이 이루어지는 곳이다.
  - Vue 전역에서 활용할 모델을 등록하는 파일

# SFC

## Component

- UI를 독립적이고 재사용 가능한 조각들로 나눈 것
  - 컴포넌트는 기능별로 분화한 코드 조각이다.

- 재사용성을 고려하여 범용적으로 사용 가능한 소프트웨어 구성 요소
- 일반적으로 하나의 app은 중첩된 컴포넌트들의 tree 형태로 구성한다.

## SFC(Single File Component)의 필요성

- 한 컴포넌트는 한 가지 기능만 수행해야 한다.
- Vue instance를 기능 단위로 작성하는 것이 핵심

## component 등록하기

1. 불러오기

- app.vue 파일에 import {컴포넌트명} from {파일 주소} 입력
  - 파일 주소는 간략하게 입력 가능(상대 주소를 @로 표시, .vue 확장자명 생략)

2. 등록하기

- export default 객체를 구성하는 component 객체에 새로 추가할 컴포넌트 이름을 추가한다.
- 맨 마지막 항목이여도 쉼표로 마무리한다(확장성 고려, 프로그램에 지장 없음)

3. 보여주기

- template 태그에 {컴포넌트명} 태그를 입력한다.

- 주의 : 등록한 컴포넌트를 표시하지 않으면 Vue CIL는 에러 메시지를 표시한다.

(app.vue 파일)

```html
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <!-- 3. 보여주기 -->
    <MyComponent />
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
// 1. 불러오기
import MyComponent from "./components/MyComponent.vue";
// import MyComponent from "@/components/MyComponent"  <= 간소화된 입력 방식

export default {
  name: "App",
  components: {
    HelloWorld,
    // 2. 등록하기
    MyComponent,
  },
};
</script>
```

> ## Note : SPA(Single Page Application) 방식의 특징 - 실시간 문서 렌더링 변경
> - 프론트엔드 서버에 변경 사항이 있어도 새로고침 등 별도의 요청 없이 페이지에 변화를 줄 수 있다.
> vue는 SPA 방식을 사용한다. 

## component 재사용하기

- template 태그 안에 {컴포넌트명} 태그를 여러 개 입력하면 된다.

# Pass Props & Emit Events

- Pass Props : 부모 객체에서 자식 객체로 데이터 전달
- Emit Events : 자식 객체에서 부모 객체로 데이터 전달

## Data in components

- 컴포넌트의 부모-자식 관계만 데이터를 주고받도록 설계하자!
- 데이터의 흐름 파악이 용이하고, 유지 보수가 편리해진다.

## Pass Props

- 요소의 속성(property)을 사용하여 데이터 전달
- Props : 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
- 하위(자식) 컴포넌트는 props 옵션을 설정하여 수신하는 props를 명시적으로 선언해야 한다.(상위 컴포넌트가 무엇인지) 
- v-bind:로 묶여 있는 "" 안의 구문은 javascript의 구문으로 볼 수 있다.
- 하위 컴포넌트에서 prop를 변경하려고 시도하면 안 된다(콘솔 경고 발생).

> ## Note : data must be a function
> - export default의 data에서 정보를 설정할 때 return{}으로 감싸야 한다.
> - 그렇지 않은 경우 error가 발생함(서버 실행 불가, 다른 컴포넌트에 의도하지 않은 영향 등)

```js
import MyComponentItem from "@/components/MyComponentItem";

export default {
  name: "MyComponent",
  components: {
    // 2. 등록하기
    MyComponentItem,
  },
  // vue-cli에서 data는 함수가 return하는 객체여야 한다.
  data: function () {
    return {
      dynamicProps: "이건 동적인 데이터!",
    };
  },
};
```

## Emit Events

- 원칙적으로 자식 컴포넌트에서 부모 컴포넌트로 데이터를 옮길 수는 없다.
- 다만 자식 컴포넌트가 부모 컴포넌트에게 데이터 변동 정보(이벤트)가 있음을 전달받음으로서 간접적으로 데이터 전송 효과를 볼 수 있다.
- emit 이벤트를 작성할 때 this.$emit(이벤트 이름, 이벤트 내용)으로 작성하기
  - export default에 methods: {}를 추가하여 그 안에 작성
  - emit 앞에 $를 붙이는 이유는 함수 내에서 이름이 emit인 변수명과 충돌할 가능성을 방지하기 위함
  - 이벤트를 받는 대상은 HTML: 중간에 '-'가 있는 변수명으로 작성
  - 첫 번째 인자는 텍스트, 두 번째 인자는 보낼 데이터

```js
// MyComponentItem.vue
export default {
  name: "MyComponentItem",
  // 받을 때는 변수명을 camelCase로 선언
  // type은 앞글자 대문자
  props: {
    staticProps: String,
    dynamicProps: String,
  },
  methods: {
    childToParent: function () {
    // give-me-ma-money : 상위 컴포넌트로 전송할 내용
      this.$emit("give-me-ma-money");
    },
  },
};

// MyComponent.vue
<template>
  <div class="border">
    <h1>싸피 이거는 내가 만든 새로운 컴포넌트다!</h1>
    <!-- MyComponentItem에 문자열 데이터 보내기 -->
    <!-- static-props는 하위 컴포넌트로만(하향) 데이터 이동 가능 -->
    <MyComponentItem
      static-props="MyComponent에서 보낸 데이터"
      :dynamic-props="dynamicProps"
      @give-me-ma-money="parentGetEvent"
    />

    <!-- v-bind 적용 가능 : 앞에 ':'이 있으면 v-bind가 생략된 것 -->
    <!-- v-bind를 이용하면 동적인 데이터 전송 가능 -->
    <!-- 아래의 url은 DNS 이름이 'url'인 URL 주소로 이동 -->
    <a href="url"></a>
    <!-- 아래의 url은 자바스크립트를 쓸 수 있는 공간 -->
    <a :href="url"></a>
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from "@/components/MyComponentItem";

export default {
  name: "MyComponent",
  components: {
    // 2. 등록하기
    MyComponentItem,
  },
  // vue-cli에서 data는 함수가 return하는 객체여야 한다.
  data: function () {
    return {
      dynamicProps: "이건 동적인 데이터!",
    };
  },
  methods: {
    parentGetEvent: function () {
      console.log("용돈 없어!!");
    },
  },
};
</script>
```

## pass props/ emit event 컨벤션

- HTML 요소에서 사용할 때는 kebab-case
- Javascript에서 사용할 때는 camelCase
- 현재 코드를 작성하는 구역별로 나누는 것이 아니라 **데이터를 전달하는 대상**에 맞추어야 한다.

1. props
   
- 상위(컴포넌트) => 하위(컴포넌트) 흐름을 HTML 요소로 내려주므로 kebab-case
- 하위에서 받을 때는 Javascript에서 받으므로 camelCase

2. emit

- HTML 요소가 이벤트 발생을 청취해야 할 때는 kebab-case
- 메서드, 변수명 등은 Javascript에서 사용하므로 camelCase