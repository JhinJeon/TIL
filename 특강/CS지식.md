# CS 지식이 필요한 이유

- 고급 개발 지식 및 업무의 근간은 기본 CS 지식으로 연결된다.
- 효율적인 자료구조 선정 및 알고리즘 구현에 필요
- 컴퓨터 시스템에 대한 이해
- 코드 작성자(coder)에서 개발자로 성장하기 위해 필요
- 기업 목적에 따른 기본 CS 지식이 필요하다.
- 프로그램을 '어떻게 만드느냐'가 걸린 문제 - 건축의 건축도면과 비슷
- 다른 개발자들과 소통하기 위해 필요하다.

# 소프트웨어 개발 생명주기(라이프사이클)

- 정의 단계 : 타당성 분석 - 계발 계획 수립 - 목표 설정
- 개발 단계 : 설계 - 개발 - 테스트
- 유지보수 단계 : 유지보수 - 폐기(새로운 서비스로 대체)

# 소프트웨어 개발 프로세스

- 정의
  - 좁은 의미 : 사용자의 요구 사항을 SW로 구현하기 위한 절차와 과정
  - 넓은 의미 : 사용자의 목적을 이루기 위한 기획, 프로젝트 관리 등을 포함한 절차, 과정, 방법

1. 계획
2. 요구분석
3. 설계
4. 구현
5. 테스트
6. 반영
7. 유지보수

## 예) 소프트웨어의 위기에 대해 설명

- (답변 예시) 2000년대 싸이월드의 몰락 : 서비스에 대한 수요 예측과 사용자의 요구 사항을 제대로 반영하지 못해서 발생한 문제이다.\

# 소프트웨어 프로세스 모델

1. 폭포수 모델

- 개발 프로세스를 순차적으로 진행(위의 1번~7번 순으로)
- 피드백 사항이 있으면 이전 단계로 되돌아간다.

2. 프로토타입 모델

- 빠르게 설계하여 프로토타입을 제작한 후 평가
- 평가에 문제가 있으면 수정 요구 사항 반영
- 평가에 문제가 없으면 최종 제품 출시

3. 나선형 모델

- 계획 및 요구분석 -> 위험분석 -> 개발 -> 사용자 평가 -> 계획 및 요구분석 과정을 나선형으로 반복
- 

4. 통합프로세스 모델

- 계획 ~ 유지보수 과정이 명확하게 구분되지 않고 연속적으로 이어지는 모형
- 매 단계별로 구분되지 않으며, 모든 개발자들이 동일한 과정에 속하지 않을 수 있다.

5. 애자일 프로세스 모델

- 고객의 요구에 신속하게 대응하고 실시간으로 주어지는 문제를 해결하는 모형
- 실행 가능한 프로그램을 중시하고, 정해진 계획과 형식에 얽매이지 않으며 고객과의 협력 중시

# 소프트웨어 공학이 필요한 이유?

- 소프트웨어 공학이 있어야 소프트웨어의 개발, 운영, 유지보수 등의 과정이 효율적이고 체계적으로 진행될 수 있다.
- SSAFY 1학기 프로젝트를 진행할 떄 구현할 웹 사이트의 작동 구조를 프론트엔드, 백엔드 별로 구분해서 만들었는데, 팀원과 협업 및 소통할 때 도움이 되었고 내가 지금 어떤 기능을 구현해야 하는지, 어떤 문제를 해결해야 하는지 빠르게 알 수 있었다.

# 아키텍처 모델

- 데이터 중심형 모델 : 주요 데이터를 중앙 저장소에서 관리, 데이터 처리 과정에서 오류가 적지만 병목 현상이 발생할 가능성이 있다.
- 클라이언트-서버 모델 : 데이터 처리 기능을 서버와 클라이언트로 분리하여 사용
- 레이어링 모델 : 기능을 몇 개의 계층으로 나누어 분리
- MVC(Model-View-Controller) 모델 : 같은 모델의 서브시스템에 대하여 여러 뷰 서브시스템을 필요로 하는 시스템에 적합

# 컴퓨터 프로그래밍

- 어떤 목표를 이루기 위해 컴퓨터에 제시하는 기획
- 프로그래밍 언어를 이용해 코드를 작성한다.

## 컴퓨터 언어

- 저급 언어 : 컴퓨터가 이해할 수 있는 언어, 기계어
  - 비트 단위의 이진수로 표현

- 고급 언어 : 인간이 이해하기 쉬운 언어, 기계어로 변역하는 과정(컴파일)이 필요.
  - Java, C++, Python 등이 고급 언어에 해당

# 객체 지향

- 객체 : 현실의 객체를 필드와 메서드로 모델링한 것
  - 객체는 지칭 가능한 모든 대상
  - 소프트웨어 객체는 상태를 필드로, 동작을 메서드로 정의한다.

## 절차지향 프로그래밍과 비교

- 절차지향 프로그래밍은 일련의 동작을 순서에 맞추어 실행하며, 명령어의 순서와 흐름을 중시한다.
- 객체지향 프로그래밍은 필드(데이터)와 메서드(코드)를 하나로 묶어 표현하며, 프로그램의 변경이 자유롭다(수정 시 전체 절차를 건드릴 필요가 없기 때문).

## 객체지향 프로그래밍의 주요 개념

- 캡슐화 : 필드와 메서드를 하나의 캡슐처럼 만들어 외부에서 알 수 없게 한다.
- 상속 : 상위 객체를 상속받은 하위 객체는 상위 객체의 필드와 메서드를 사용한다.
- 다형성 : 대입되는 객체에 따라서 메서드가 다르게 동작하도록 한다.

# 데이터베이스

- 객체 지향 데이터베이스 : 객체지향 프로그래밍 기반으로 데이터를 추가하는 DB
- 객체 관계 데이터베이스 : 데이터베이스 관계를 기준으로 데이터를 추가하는 DB

## 분산 데이터베이스

- 데이터베이스를 여러 위치에 분산하여 관리하는 구조
- 신뢰성과 가용성 증대, 효율성과 확장성에 강점이 있다.
- 비용이 많이 든다.

# No SQL

- 기존 관계 데이터베이스를 대체할 새로운 대안의 필요성 : 비정형 데이터를 관리할 방법이 필요하다.
- 필요에 따라 다른 특성을 제공하는 데이터베이스를 사용하는 것이 좋다.

## No SQL의 장점

- 대규모의 데이터를 유연하게 처리할 수 있다.
- 설계가 단순하고, 데이터 확장에 유리하다.

# 임베디드 시스템

# 운영체제 아키텍처

# 커널의 정의

## 모놀리식 커널

## 마이크로커널

## 폰 노이만 아키텍쳐


## 커널 포팅


## 디바이스 드라이버 포팅

# OSI 7 레이어 

# TCP/IP 주소

- 물리 주소 : 인터넷을 구성하는 주소, 링크 또는 통신망에서 정의된 노드의 주소(모뎀, 네트워크 카드)
- 인터넷 주소 : 기존 물리 주소와 별개로 각 호스트를 식별하는 유일한 주소
- 포트 주소 : 수신자의 컴퓨터까지 전송하려면 물리 주소에 IP 주소가 추가로 필요(IP 주소)

## IP 주소의 구성

- IP 주소는 네트워크 주소와 호스트 주소로 구성된다.
- IP 주소를 효율적으로 배정하기 위해 클래스를 정의한다.
- 클래스 A~E까지 존재하며, E등급으로 갈수록 네트워크 주소 자리가 늘어나고, 호스트 주소 자릿수가 줄어든다.

# 라우팅

- 정적 라우팅 : 네트워크 통신 경로가 불변함. 단순하지만 혼잡성이 높다.
- 동적 라우팅 : 네트워크 경로가 상황에 따라 최적화됨. 효율적이지만 복잡하고 성능이 떨어진다.

# HTTP 프로토콜

- 클라이언트가 서버에 데이터를 요청하면, 서버에서 클라이언트에 데이터를 응답하는 방식으로 통신
- GET, POST, PUT, DELETE 등의 요청 메서드가 존재한다.
- 응답 코드에 따른 구분
  - 200대 : 정상
  - 300대 : 리다이렉션
  - 400대 : 클라이언트 오류
  - 500대 : 서버 오류

# 네트워크 관점에서 동작 설명하기

- 브라우저에 URL을 입력하면, 웹 브라우저는 실제 IP 주소를 DNS에서 조회한다.
- 이후 실제 IP 주소를 이용해 서버의 80포트를 통해 웹 서버에 데이터를 요청한다.
- 웹 서버는 브라우저를 위한 별도의 포트에 소켓을 개설하고, 그 소켓은 웹 브라우저에 연결된다.
- 웹 서버에서 웹 브라우저에 데이터를 응답한다.

# IPv4 vs IPv6

- IPv4는 4자리(32비트) 단위로 구성되며, 확장성과 용량 측면에서 한계가 있다.
- IPv6는 IPv4를 보완하기 위해 등장한 IP 주소 체계로, 6자리(128비트) 단위로 구성된다.

# 서비스 거부 공격(DoS)

- 서버에 과도한 요청을 보내거나 저장하는 정보를 과다하게 만들어서 서비스를 셧다운 시키는 공격 방법

## 분산 서비스 거부 공격(DDos)

- 다수의 개별 컴퓨터를 동원하여 서비스 거부 공격을 진행하는 공격 방법

# 세션 하이재킹

- 두 시스템의 연결이 활성화된 상태(세션)를 가로채는 행위
- 인증 위조, 신원 도용, 데이터 유출 등에 악용될 수 있다. 

# SSL

- 방대한 인터넷 상거래의 안전을 위해 사용되는 프로토콜
- https 프로토콜을 사용한다.
- SSL 세션은 비용이 소모되며, 공개 키 연산이 필요하다.
- 암호화, 무결성, 인증 등을 포함한다.
- 간단한 규격이지만 IPSec보다 보안성이 떨어진다.

# IPSec?