목차

- [Lifecycle Hooks](#lifecycle-hooks)
  - [create, mount](#create-mount)
  - [특징](#특징)
- [vuex-persistedstate(환경설정)](#vuex-persistedstate환경설정)
- [Vuex 사용처](#vuex-사용처)


# Lifecycle Hooks

- 각 Vue 인스턴스는 생성 및 소멸 과정 중 단계별 초기화 과정을 거친다.
  - 인스턴스가 생성되거나, 인스턴스가 DOM에 마운트되거나, 데이터가 변경되어 DOM을 업데이트 하는 등의 과정에서 초기화 과정을 거친다.

- 각 단계별로 트리거가 되어 특정 로직을 수행할 수 있는데, 이를 Lifecycle Hooks라고 한다.

## create, mount

- create는 상위 컴포넌트부터 하위 컴포넌트 순으로 진행되지만, mount는 하위 컴포넌트부터 상위 컴포넌트 순으로 진행된다.

## 특징

- 컴포넌트 별로 조회할 수 있다.
- 부착(mount) 여부가 부모-자식 관계에 따라 순서를 가지고 있지 않다.

# vuex-persistedstate(환경설정)

- 설치 : npm i vuex-persistedstate 입력
- 이후 index.js에 import createPersistedState from 'vuex-persistedstate' 입력
- export default new Vuex.Store 안에 plugins 추가

```js
import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
```
- createPersistedState 플러그인을 사용하면 dispatch, 로컬스트리지 저장 액션, mutation 등 복잡한 코드를 작성하지 않아도 된다.

# Vuex 사용처

- 작고 단순한 프로젝트에서는 사용하지 않는 것이 더 좋을 수 있다.
- 처음 배우기에는 복잡하고 알아야 할 것이 많지만, 큰 프로젝트를 효율적으로 관리할 수 있다.
- 프로그램 규모가 일정 수준 이상으로 커지는 경우 Vuex를 사용하면 된다.