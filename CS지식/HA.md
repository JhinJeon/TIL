# HA(High Availability)의 정의

- 고가용성
- 서버, 네트워크, 프로그램 등 정보 시스템이 오랜 기간동안 지속적으로 정상 운영이 가능한 성질
- 시스템 오류(이슈) 발생 시 **얼마나 빠른 시간에 복구 가능한지**에 대한 척도

# HA 관련 용어

- Active: Client로부터 요청을 받아서 처리하는 서버
- Standby: 예측한 이벤트(장애 등)가 발생했을 때 Active 대신 요청을 처리하는 서버
- Master: 하나의 역할을 수행하는 데 동작의 주체가 되는 역할 수행(쓰기, 수정, 삭제)
- Slave: Master의 지시에 따라 종속적인 역할을 수행(읽기)
- Backup: 특정 서버의 역할을 대체하기 위해 준비된 서버

## Cache 서버의 이중화 구성

- 캐시 서버 다운 발생 시 대체 가능한 미러링 서버 구성
- Active / Standby 와 Master / Backup 구성
- Auto Failable을 구현하면 한 쪽 서버가 다운될 때 자동으로 다른 쪽 서버로 스왑해 준다.

# 로드 밸런서

- nginx에서 제공
- 부하 분산을 위해 사용
- 다수의 Active 서버로 구성된다(Actvie / Active).
- 장애 발생 대응에도 사용한다.
