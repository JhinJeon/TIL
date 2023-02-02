# 도커를 사용하는 이유

- 기기별로 실행 환경이 달라서, 다른 기기로 옮겼을 때 실행에 지장이 생기는 경우가 있다.
- 환경 설정 과정에서 생기는 오류와 시행착오를 최소화하기 위해 도커를 사용한다.

# 도커 활성화

```
docker build
```

# 빌드한 도커 이미지 확인

- 파일명, 생성 시간 등 정보 확인 가능

```
docker images
```

# 빌드한 도커 파일 컨테이너화

- p, a/d, name, rm 등 다양한 옵션 적용 가능

```
docker run
```

```
docker ps
```

- 컨테이너 중지

```
docker stop (컨테이너 ID)
```

- 컨테이너 삭제

```
docker rmi (컨테이너 혹은 이미지 ID)
```

# MySQL 설치

1. EC2 서버 업데이트 진행

```
sudo apt update
```

2. MySQL 설치

```
sudo apt install mysql-server
```

3. root 계정 접속

```
sudo mysql -u root -p
```

4. MySQL로 db 변경

```
use mysql;
```

5. 계정 생성

```
CREATE USER '아이디'@'호스트' identified with mysql-native_password by '비밀번호';
```

6. 계정 권한 부여

```
GRANT ALL PRIVILEGES ON [DB스키마]
```

7. 변경 사항 적용

```
FLUSH PRIVILEGES;
```

8. 외부 접속 허용

```
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
```

bind-address의 값을 0.0.0.0으로 수정

9. MySQL 재실행

```
sudo service mysql restart
```

# 도커 허브 가입 및 저장소 생성

# 로컬 환경에서 docker 파일 작성(docker desktop 실행)

# CIL에서 도커 로그인

```
docker login
```

# 도커 허브에 파일 push

- 이미지의 이름과 태그명을 [도커허브 계정명]/[저장소명]:[태그명]으로 해야 한다.

```
docker build -t jdznawa/DJRepository:django-deploy-latest
```

# 프론트엔드 배포 빌드

```
npm run build
```

- 이후 생성된 디렉토리(폴더) 확인

> ## Vue의 경우 빌드 결과 디렉토리 이름이 this가 되는 경우가 있다.

## Nginx 구성 파일 작성

### Nginx란?

- 동시접속 처리에 특화된 웹 서버 프로그램
- 가벼우면서 높은 성능을 자랑한다.
- 정적 파일 처리, 리버스 프록시, 로드 밸런싱 등을 담당한다.

## EC2에 Nginx 설치

- sudo apt-get install nginx

## 설치 확인

- sudo nginx -v

## Nginx 중지

- sudo systemctl stop nginx

## 설정 파일 작성

### conf 파일 생성

- sudo vim [파일명].conf

```
sudo vim test_deploy.conf
```

이후 insert mode에 진입한 후(단축키 i) 도메인 주소를 배포하려는 서버 주소에 맞게 수정
server에는 server_name 작성

## 파일 연동 및 테스트

- OK가 뜨면 성공

```
sudo ln -s /etc/nginx/sites-available/test_deploy.conf /etc/
```

sudo nginx -t

- 이후 Nginx 재시작(변경 사항 저장용)

- sudo systemctl restart nginx

## 도커에서 이미지 Pull 받기

- sudo docker pull [docker hub 계정명]/[저장소명]:[태그명]
- 도커에서 받은 이미지를 컨테이너에서 실행하면 배포 완료

# 컨테이너 실행

- sudo docker run --rm -d -p [포트번호]:[포트번호] --name [원하는 이름] [이미지 ID]

```
sudo docker run --rm -d -p 8080:8080 --name django-container 8acd4a0f76dd
sudo docker run --rm -d -p 8080:8080 --name react-container 8a45fd76dd

```
