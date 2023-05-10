# UDP 코드

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys.socket.h>

#define BUF_SIZE 1024

void error_handling(char *message);

// 실행파일명, 포트번호 입력받는 프로그램 코드
int main(int argc, char *argv[])
{
    int serv_sock, clnt_sock;   // 서버 소켓, 클라이언트 소켓 파일 디스크립터
    char message[BUF_SIZE];     // 전송할 메시지 내용
    int str_len // 문자열 길이

    struct sockaddr_in serv_adr, clnt_adr;  // 서버와 클라이언트 주소를 저장하는 구조체
    socklen_t clnt_adr_sz;

    // 입력값이 2개가 아닌 경우
    if (argc != 2)
    {
        printf("Usage : %s <port>\n", argv[0]);
        exit(EXIT_FAILURE);
    }
}
```

## UDP 소켓 계속 열어두기(지속 통신이 필요한 경우)

- UDP 소켓을 대상으로 connect 함수를 호출하면 된다.

```c
struct adr;
sock = socket(PF_INET, SOCK_DGRAM, 0);
memset(&adr, 0, sizeof(adr));
adr.sin_family = AF_INET;
adr.sin_addr.s_addr = ...   // IP 주소
adr.sin_port = ...  // 포트 번호
connect(sock, (struct sockaddr*)&adr, sizeof(adr));
```