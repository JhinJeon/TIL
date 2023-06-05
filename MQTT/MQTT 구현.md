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