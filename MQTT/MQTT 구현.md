# MQTT 구현(실행) 순서

1. 브로커 IP 확인
2. 구독자(Subscriber) 클라이언트 실행 및 브로커에 구독 요청
3. 브로커 대기 상태 돌입
4. 발행자(Publisher) 클라이언트 실행 및 브로커에 배포
5. 브로커에서 클라이언트로 메시지 전달
- 구독자 클라이언트가 OFF 상태이면 메시지가 증발한다.

# MQTT 구현 코드

1. 구독자 클라이언트 작성

```c
#include <stdio.h>
#include <stdlib.h>
#include <mosquitto.h>

void on_message(struct mosquitto *mosq, void *userdata, const struct mosquitto_message *message)
{
    printf("Received message on topic '%s': %s\n", message->topic, (char*)message->payload);
}

int main(int argc, char** argv)
{
    struct mosquitto *mosq = NULL;

    // argument가 3개가 아닌 경우 에러 처리
    if (argc != 3)
    {
        printf("illegal arguments.\n");
        exit(0);
    }

    mosquitto_lib_init();
    
    mosq = mosquitto_new(argv[1], true, NULL);

    mosquitto_message_callback_set(mosq, on_message);
    // localhost에 연결
    mosquitto_connect(mosq, "localhost", 1883, 60);

    mosquitto_subscribe(mosq, NULL, argv[2], 0);

    mosquitto_loop_forever(mosq, -1, 1);

    mosquitto_destroy(mosq);

    mosquitto_lib_cleanup();
    
    return 0;
}
```