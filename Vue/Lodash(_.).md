#  Lodash 라이브러리

- built-in 객체를 작성하지 않아도 연산을 수행하는 함수를 제공하는 라이브러리
- _.(언더스코어 함수)로 작성

> ## Note
> - underscore 등 '_'를 사용하는 다른 라이브러리랑 혼동하지 않도록 주의
> - 정확한 정보는 Lodash 공식 문서를 참조할 것

# 사용 예시

> ### Note
> - '[ ]' 안에 입력한 내용은 선택 인자

1. sample

- _.sample(추출 대상, [추출 개수])
- 추출 대상 목록에서 [추출 개수]만큼의 원소를 무작위로 선정
- 추출 개수를 지정하지 않으면 1개의 숫자만 반환

```js
const sampleArray = _.sample([1,2,3,4,5],3)
// sampleArray = 1, 2, 3, 4, 5 중에서 3개의 원소를 무작위로 추출
```

2. sampleSize

- _.sampleSize(추출 대상, 추출 개수)
- sample과 유사하지만, 

# CLI 환경에서 Lodash 사용하기

- script 태그를 붙여넣는 대신 CLI에 npm install lodash를 입력해서 설치
- 이후 lodash를 사용하려는 컴포넌트에 import _ from 'lodash' 입력