# this 심화

- javascript의 객체(object)의 형식은 key : value
- this는 내가 있는 위치에서의 특정 개체를 가리킨다.
- 전역 변수로 사용되는 경우 전역 환경(window)을 가리킨다.
- 함수에서 호출되는 경우:
  - 함수로서 호출되는 경우 : window를 가리킨다.
  - method로서 호출되는 경우 : '.' 앞 객체를 가리킨다.

```js
obj.method  // obj의 this는 obj를 가리킨다.
obj['method']  // obj.method와 동일한 결과 
```

- bind를 통한 명시 : bind(*변수*)에서 명시한 *변수*를 가리킨다.
- 화살표 함수 : 상위의 this(상위 스코프)를 가리킨다.

# 시간 지연 두기

- setTimeout(함수, 지연 시간)
- 지연 시간 단위는 ms(1000 = 1초)

# callback 함수(다른 코드에 인수로서 넘겨주는 함수)
- callback 함수의 this는 전역 객체(함수 호출과 동일한 취급)
- addEventListener에서 콜백 함수 안의 this는 이벤트가 발생하는 html 요소
  - this는 자동으로 .addEventListener 앞에 있는 객체를 가리킨다.
  - 화살표 함수를 사용하는 경우 
- 콜백 함수를 제어하는 함수에서 this를 명시적으로 지정 가능한 것도 있다.