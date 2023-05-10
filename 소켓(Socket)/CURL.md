# CURL(컬) 정의

- Client URL의 약자
- 클라이언트에서 CLI나 소스코드로 웹 브라우저처럼 활동할 수 있게 해주는 유틸리티(기술)
- URL 기반으로 데이터를 서버(웹)로 전송할 수 있다.
- 오픈 소스로 다양한 통신 프로토콜들을 지원한다.

# CURL 설정

- 대부분의 리눅스 배포 환경에는 CURL 패키지가 기본 설치되어 있다.
    - 설치 여부를 확인하려면 'curl --help' 또는 'curl --manual'을 입력하면 된다.
- curl이 없는 경우 별도로 설치한다.

# CURL 실행

- curl {option} {URL} 순으로 입력한다.

```
curl example.com
```

- 프로토콜을 별도로 지정하지 않은 경우 CURL은 사용할 프로토콜을 자동으로 설정한다.(기본: HTTP)

## CURL 기본 option

- X : http method 를 get/post로 할건지 지정 지정없으면 디폴트는 get
- H : http 헤더값
- d : http body값 or 함께 전달할 파라미터 값
- G : 전송할 사이트 url 및 ip 주소
- I : 사이트의 Header 정보만 가져오기
- i : 사이트의 Header와 바디 정보를 함께 가져오기
- u : 사용자 정보