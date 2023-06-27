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

# ChatGPT 코드

- 클라이언트

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "MQTTClient.h"

#define ADDRESS     "tcp://mqtt.example.com:1883"
#define CLIENTID    "ExamplePublisher"
#define TOPIC       "my/topic"
#define QOS         1
#define TIMEOUT     10000L

int main(int argc, char* argv[])
{
    MQTTClient client;
    MQTTClient_connectOptions conn_opts = MQTTClient_connectOptions_initializer;
    MQTTClient_message pubmsg = MQTTClient_message_initializer;
    MQTTClient_deliveryToken token;
    int rc;

    MQTTClient_create(&client, ADDRESS, CLIENTID, MQTTCLIENT_PERSISTENCE_NONE, NULL);
    conn_opts.keepAliveInterval = 20;
    conn_opts.cleansession = 1;

    if ((rc = MQTTClient_connect(client, &conn_opts)) != MQTTCLIENT_SUCCESS) {
        printf("Failed to connect, return code %d\n", rc);
        exit(EXIT_FAILURE);
    }

    pubmsg.payload = "Hello, MQTT!";
    pubmsg.payloadlen = (int)strlen(pubmsg.payload);
    pubmsg.qos = QOS;
    pubmsg.retained = 0;
    
    MQTTClient_publishMessage(client, TOPIC, &pubmsg, &token);
    printf("Waiting for publication of %s on topic %s for client with ClientID: %s\n",
        pubmsg.payload, TOPIC, CLIENTID);

    rc = MQTTClient_waitForCompletion(client, token, TIMEOUT);
    printf("Message with delivery token %d delivered\n", token);

    MQTTClient_disconnect(client, 10000);
    MQTTClient_destroy(&client);
    return rc;
}
```

- 서버

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "MQTTClient.h"

#define ADDRESS     "tcp://mqtt.example.com:1883"
#define CLIENTID    "ExampleSubscriber"
#define TOPIC       "my/topic"
#define QOS         1
#define TIMEOUT     10000L

volatile MQTTClient_deliveryToken deliveredtoken;

void delivered(void *context, MQTTClient_deliveryToken dt)
{
    printf("Message with token value %d delivery confirmed\n", dt);
    deliveredtoken = dt;
}

int msgarrvd(void *context, char *topicName, int topicLen, MQTTClient_message *message)
{
    char* payloadptr;
    printf("Received message on topic: %s\n", topicName);
    payloadptr = message->payload;
    printf("Message: %.*s\n", message->payloadlen, payloadptr);
    MQTTClient_freeMessage(&message);
    MQTTClient_free(topicName);
    return 1;
}

void connlost(void *context, char *cause)
{
    printf("Connection lost\n");
    printf("Cause: %s\n", cause);
}

int main(int argc, char* argv[])
{
    MQTTClient client;
    MQTTClient_connectOptions conn_opts = MQTTClient_connectOptions_initializer;
    int rc;

    MQTTClient_create(&client, ADDRESS, CLIENTID, MQTTCLIENT_PERSISTENCE_NONE, NULL);
    conn_opts.keepAliveInterval = 20;
    conn_opts.cleansession = 1;

    MQTTClient_setCallbacks(client, NULL, connlost, msgarrvd, delivered);

    if ((rc = MQTTClient_connect(client, &conn_opts)) != MQTTCLIENT_SUCCESS) {
        printf("Failed to connect, return code %d\n", rc);
        exit(EXIT_FAILURE);
    }

    MQTTClient_subscribe(client, TOPIC, QOS);

    printf("Subscribed to topic: %s\n", TOPIC);

    while (1) {
        usleep(1000000L); // Sleep for 1 second
    }

    MQTTClient_disconnect(client, 10000);
    MQTTClient_destroy(&client);
    return rc;
}
```

# Paho MQTT 구현

1. MQTTClient_create

- MQTT 클라이언트 인스턴스를 생성한다.
- 파라미터는 [클라이언트 핸들, 브로커(서버) URI, 클라이언트 ID, persistence type, persistence context] 순으로 입력한다.
- 정수형 값을 반환한다.(성공 시 MQTTCLIENT_SUCCESS, 실패 시 에러 코드)

2. MQTTClient_connect

- MQTT 브로커와 연결한다.
- 파라미터는 [클라이언트 인스턴스 핸들, MQTTClient_connectOptions 구조체의 메모리 주소] 순으로 입력한다.
- 반환 값은 위와 동일하다.

3. MQTTClient_publish

- 메시지를 주제(topic)에 공개(publish)한다.
- 파라미터는 **[클라이언트 인스턴스 핸들, topic 이름(파일 경로로 표시), 메시지 payload 길이, QoS(0/1/2), Retained flag(0/1), delivery 토큰 메모리 주소]** 순으로 입력한다.
- 반환 값은 위와 동일하다.

4. MQTTClient_subscribe

- publish된 topic을 구독(subscribe)한다.
- 파라미터는 **[클라이언트 인스턴스 핸들, 구독하려는 topic filter, QoS(0/1/2)]** 순으로 입력한다.
- 반환 값은 위와 같다.

5. MQTTClient_setCallbacks

- 메시지 접수(reception), 연결 끊김, 메시지 도착, 메시지 전달 확인 등의 과정을 수행할 때 콜백 함수를 설정할 수 있다.
- 파라미터는 [클라이언트 인스턴스 핸들, User-defined context, 연결 끊김 콜백 함수 메모리 주소, 메시지 도착 시 콜백 함수 메모리 주소, 메시지 전송 완료 콜백 함수 메모리 주소] 순으로 입력한다.
- 함수 자체는 아무런 값을 반환하지 않는다.

6. MQTTClient_disconnect

- MQTT 브로커와의 연결을 끊는다.
- 파라미터는 [클라이언트 인스턴스 핸들, 타임아웃] 순으로 입력한다.
- 정수형 값을 반환한다(성공 시 MQTTCLIENT_SUCCESS, 실패 시 에러 코드)

# Paho MQTT 샘플 코드 추가(C)

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "MQTTClient.h"

#define ADDRESS     "tcp://mqtt.example.com:1883"
#define CLIENTID    "ExampleClient"
#define TOPIC       "my/topic"
#define QOS         1   // 0 = 전송 검증 안 함, 1 = 기본 전송(수신확인이 될 때까지 전송 반복), 2 = 정확한 전송(핸드쉐이킹)
#define TIMEOUT     10000L

volatile MQTTClient_deliveryToken deliveredtoken;

// Callback function for connection lost
void connectionLost(void *context, char *cause)
{
    printf("\nConnection lost\n");
    printf("Cause: %s\n", cause);
}

// Callback function for message arrival
int messageArrived(void *context, char *topicName, int topicLen, MQTTClient_message *message)
{
    printf("\nReceived message on topic: %s\n", topicName);
    printf("Message: %.*s\n", message->payloadlen, (char *)message->payload);

    MQTTClient_freeMessage(&message);
    MQTTClient_free(topicName);
    return 1;
}

// Callback function for message delivery completion
void deliveryComplete(void *context, MQTTClient_deliveryToken token)
{
    printf("Message delivery completed\n");
    deliveredtoken = token;
}

int main(int argc, char* argv[])
{
    MQTTClient client;
    MQTTClient_connectOptions conn_opts = MQTTClient_connectOptions_initializer;
    int rc;

    MQTTClient_create(&client, ADDRESS, CLIENTID, MQTTCLIENT_PERSISTENCE_NONE, NULL);
    conn_opts.keepAliveInterval = 20;
    conn_opts.cleansession = 1;

    // 콜백 함수 등록
    MQTTClient_setCallbacks(client, NULL, connectionLost, messageArrived, deliveryComplete);

    if ((rc = MQTTClient_connect(client, &conn_opts)) != MQTTCLIENT_SUCCESS) {
        printf("Failed to connect, return code: %d\n", rc);
        exit(EXIT_FAILURE);
    }

    // TOPIC 구독
    MQTTClient_subscribe(client, TOPIC, QOS);

    printf("Subscribed to topic: %s\n", TOPIC);

    // MQTTClient_message_initializer 구조체 포맷의 pubmsg 변수(인스턴스) 생성
    MQTTClient_message pubmsg = MQTTClient_message_initializer;
    pubmsg.payload = "Hello, MQTT!";
    pubmsg.payloadlen = (int)strlen(pubmsg.payload);
    pubmsg.qos = QOS;
    pubmsg.retained = 0;

    MQTTClient_deliveryToken token;
    MQTTClient_publishMessage(client, TOPIC, &pubmsg, &token);
    printf("Publishing message: %s\n", pubmsg.payload);

    rc = MQTTClient_waitForCompletion(client, token, TIMEOUT);
    printf("Message delivery result: %d\n", rc);

    printf("Press Enter to exit...\n");
    getchar();

    MQTTClient_disconnect(client, TIMEOUT);
    MQTTClient_destroy(&client);
    return 0;
}
```

# 트러블슈팅(문제가 발생했을 때)

1. connect 단계에서 -15 오류가 뜨는 경우

- conn_opts.username에 문자열 변수를 입력하는 경우, 배열의 크기(size)를 여유롭게 해야 한다.(size - strlen 시 2 이상 남도록)
    - \0 포함 2자리 이상 남겨야 한다.