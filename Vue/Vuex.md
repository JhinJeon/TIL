목차

- [상태 관리(State Management)](#상태-관리state-management)
  - [Pass Props & Emit Event](#pass-props--emit-event)
  - [중앙 저장소(Centralized Store)](#중앙-저장소centralized-store)
- [Vuex 구성(환경설정)](#vuex-구성환경설정)
  - [Mutations](#mutations)
  - [Getters](#getters)
  - [Action](#action)
- [코드 작성(실습)](#코드-작성실습)

# 상태 관리(State Management)

- 현재 상태(State)에 대한 정보를 관리하는 시스템
- 각 컴포넌트는 독립적이므로 각각의 상태를 가진다.
- 하지만 하나의 App을 구성하는 컴포넌트들은 같은 상태(데이터)를 유지할 필요가 있으므로, 상태 관리가 필요하다.

## Pass Props & Emit Event

- Prop & Emit을 통해 각 컴포넌트의 상태를 동일하게 유지하고, 데이터의 흐름을 직관적으로 파악할 수 있다.
- 하지만 prop, emit은 한 단계씩 움직이므로, 컴포넌트 중첩이 깊어질수록 데이터 전달 구현이 어렵다.

## 중앙 저장소(Centralized Store)

- 중앙 저장소에 데이터를 모아서 상태 관리를 일괄적으로 진행
- **컴포넌트 계층에 상관없이** 중앙 저장소에 접근하여 데이터를 얻거나 변화를 줄 수 있다.
- 중앙 저장소 데이터가 변경되면 각각의 컴포넌트는 데이터의 변화에 반응한다(변경된 데이터 반영).
- 대규모의 중첩이 깊은 컴포넌트로 구성된 앱을 관리하기에 용이한 방식이다.

# Vuex 구성(환경설정)

- vue-cli 생성 이후 터미널에 vue add vuex 입력
- src/store 폴더가 중앙 저장소
- 데이터는 store/index.js의 state에 저장된다.(중앙 저장소는 데이터를 상태로 저장/관리하기 때문)

## Mutations

- state를 변경하는 method
- (실제로) state를 변경하는 유일한 방법이다.
- vue 인스턴스의 methods에 해당하지만 Mutations에서 호출되는 핸들러 함수는 반드시 동기적이어야 한다.
- context 객체를 인자로 받으며, 이 객체를 통해 모든 요소와 메서드에 접근할 수 있다.
  - 즉 state를 직접 변경하는 코드는 Mutation으로만 구성되어야 한다.

- component에서 dispatch() 메서드에 의해 호출된다.

## Getters

- state를 활용하여 계산된 새로운 변수 값
- getters에서 계산된 값은 **state(원본)에 영향을 미치지 않는다**.
- 첫 번째 인자로 state, 두 번째 인자로 getter(다른 getter의 계산 결과를 이용하는 경우)로 받는다.
- computed처럼 연산 결과가 캐싱 되며, 연산 변수가 변하기 전까지 유지된다.

## Action

- state 변경 이외의 모든 로직 진행
- 비동기 작업이 포함될 수 있다(외부 API와 통신 등).

# 코드 작성(실습)

- 객체 메서드의 축약형을 사용한다.

```js
// before
const obj1 = {
    addValue: function(value) {
        return value
    },

// after : 함수 정의 function()이 생략된다.
const obj2 = {
    addValue(value) {
        return value
    },
}
}
```