# IPC 개요

- IPC(Inter-Process Communication)는 프로세스 간 데이터를 주고받는 행위, 경로, 방법 등을 뜻한다.
- 개별 프로세스는 독립적으로 존재하며, 일반적으로 프로세스 간 데이터 교류는 일어나지 않는다.
- 따라서 프로세스 간 통신을 구현하려면 별도의 통신 시스템 구현이 필요하다.

# IPC 구현 방식

- 파이프 : 단방향으로 데이터를 전송하는 파이프라인을 이중으로 구현
- 메시지 큐(Message Queue) : 프로세스 사이에 일종의 중개 프로그램을 구현하여 전송 담당
- 공유 메모리 : 커널 차원에서 공유 영역(메모리)를 할당하고, 프로세스가 해당 영역에 접근하여 공유
- 소켓(Socket) : 각 프로세스에 소켓을 생성하여 내부 통신 구현

# 소켓 기반의 IPC 구현

- 소켓 코드 작성 시 \<sys/types.h>, \<sys/socket.h> 헤더를 include 해야 한다.

```c
#include <sys/types.h>
#include <sys/socket.h>
```

## 소켓 구조체 생성

- sockaddr = (소켓 주소 정보를 담는) 기본 구조체
- sockaddr_in = 소켓 구조체의 주소 체계(sa_family)가 IPv4(AF_INET)인 경우 사용
- sockaddr_in6 = 주소 체계가 IPv6(AF_INET6)인 경우
- sockaddr_un = 단일 시스템 내에서 서로 다른 프로세스 사이의 통신에 사용할 소켓 주소를 지정할 때(AF_UNIX, AF_LOCAL) 사용


# 소스 코드

```c

```