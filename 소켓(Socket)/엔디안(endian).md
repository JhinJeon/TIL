# 엔디안 구분

- 네트워크와 호스트(기기)가 데이터를 저장하는 방식이 상이한 경우가 있다.
- 데이터를 저장할 때 네트워크는 빅 엔디안 방식으로 저장하지만, 호스트는 리틀 엔디안 방식으로 저장한다
    - 물론 예외인 경우도 있다.

# 엔디안 타입(형식) 전환

- 소켓 프로그래밍에서 엔디안 타입이 다른 기기 간 통신하는 경우, 수신자 쪽에서 엔디안 타입을 교정할 필요가 있다.

## htons(), htonl()

- hton은 host to network의 약자로, 인자로 받은 **리틀 엔디안 값을 값을 빅 엔디안 형식으로 바꿔준다.**
- CPU가 빅 엔디안을 사용하는 경우 입력한 값을 그대로 반환한다.
- htons()는 unsigned short, htonl()은 unsigned long 타입으로 전환한다.

```c
// host에서는 데이터를 주로 리틀 엔디안 타입으로 취급한다.
u_short htons(u_short hostshort);
u_long htonl(u_long hostlong);
```

## ntohs(), ntohl()

- ntoh는 network to host의 약자로, 인자로 받은 **빅 엔디안 값을 리틀 엔디안 형식으로 바꿔준다.**
- CPU가 리틀 엔디안을 사용하는 경우 입력한 값을 그대로 반환한다.
- ntohs()는 unsigned short, ntohl()은 unsigned long 타입으로 전환한다.

```c
// network에서는 데이터를 주로 빅 엔디안 타입으로 취급한다.
u_short ntohs(u_short netshort);
u_long ntohl(u_long netlong);
```