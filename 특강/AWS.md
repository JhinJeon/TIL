# AWS를 사용하는 이유

- 아마존 서버에 배포된 REST API서버와 통신하며 데이터 활용
- 통신 기기의 종류가 다양해지고(스마트폰, 컴퓨터, 자동차 등) 클라이언트 장비들의 성능이 상향됨에 따라 API 서버는 데이터만 전송
- 데이터를 받아서 변환하고 해석하는 기능은 클라이언트가 담당

# 클라우드 시스템

- 물리적인 자원을 가상화한 시스템
- CPU 및 시스템 리소스를 분할하는 방식
- 가상화 : 물리적인 리소스(저장소, CPU 등)를 분할하여 저장 및 처리하는 기술

# AWS 사용이 유리한 상황

- 초기 비용이 부담스러울 때
- 필요한 서버 인프라 자원이 불안정하고 가변적일 때
- 세계적으로 통용되는 서비스와 연동되어야 할 때

# 가상 리눅스 환경 사용

## PuTTy 사용

- putty.exe 다운로드 후 실행
- 호스트명에 AWS에서 생성한 인스턴스의 IP 주소 입력
- Auth > Configuration에서 인증 키 파일 업로드 후 실행

## 리눅스 명령어

> ### _이탤릭체_ 로 작성한 내용은 **사용자 임의로 수정 가능**

- cd ~ : 홈 디렉토리로 이동
- pwd : 현재 디렉토리(위치) 조회
- echo : 출력(python의 print)
- cat : 파일 정보 조회
- ifconfig : 현재 접속한 IP 주소 확인
- ifconfig > _ipinfo.txt_ : ipinfo.txt 파일에 ifconfig 정보 저장
- rpm -qa |grep _python_ : 현재 OS에 설치된 프로그램 정보들 중 python과 관련된 정보만 불러오기
- history _N_ : 최근 실행한 N개의 명령어 출력
- sudo yum install -y _httpd_ : httpd 설치
- systemctl status _httpd_ : httpd의 서비스 상태 확인
- sudo systemctl start _httpd_ : httpd 서비스 시작(활성화)
- ps -ef : 동작 중인 프로세스 확인
  - |grep httpd를 입력하여 http 관련 프로세스만 확인 가능

> ### Note: | grep ~
> - | grep는 일종의 필터 역할을 담당한다(grep 뒤에 입력하는 키워드를 기준으로 필터링)