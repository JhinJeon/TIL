# 쉘 스크립트(Shell Script)

- 리눅스에서 Unix 커맨드 등을 나열해서 실행할 수 있는 스크립트
- 명령 실행 조건, 시기, 읽기 여부, 로그 파일 작성 등이 가능하다.

# 쉘 스크립트 파일 생성

- 확장자명을 .sh로 한 파일을 생성한다.

# 쉘 스크립트 실행

- 다음 커맨드 중 하나를 입력하면 쉘 스크립트를 실행할 수 있다.

```linux
chmod 755 <filename>.sh
sh <filename>.sh
bash <filename>.sh
```

# 쉘 스크립트 소스 코드 작성

## 주석 처리

- '#'를 입력하면 주석 처리가 가능하다.

```sh
#파이썬처럼 앞에 '#'를 붙이면 주석 처리가 가능하다.
echo "Hello World!"
```

## 기본 입출력

- echo로 출력, read로 입력 기능을 수행한다.

```sh
read NAME
# 앞에 포매팅 문자($)를 붙이면 변수의 값을 불러올 수 있다.
echo "Hello, $NAME!"
```

- bash에서는 -e플래그로 특수 텍스트를 이스케이프할 수 있다.(개행문자 등)

```sh
# !/bin/bash
echo -e "Hello\n$NAME!"
```

## 변수 선언

- 변수의 이름은 영문자, 숫자, 언더바를 사용하여 작성한다.
- 값을 전달할 때는 '='의 앞뒤에 **공백이 없어야 한다.**
- 변수에 접근할 때는 변수명 앞에 '$'를 넣거나, $를 붙인 상태로 변수를 중괄호{ }로 감싼다.
- 변수의 값이 덮어쓰기되는 현상을 방지하려면 readonly를 붙여서 선언한다.
- 변수를 unset으로 삭제할 수 있다. 다만 readonly 변수는 삭제가 불가능하다.

```sh
# '=' 앞뒤로 공백이 있으면 안 된다.
var="변수1"
VaR_2="변수2"
echo "VaR_2=$VaR_2"

# 변수 접근 시 ${변수명}의 형태도 가능하다.
VaR_2="변수가 변경되었다."
echo ${VaR_2}

# readonly 변수는 변경할 수 없다.
# 따라서 아래 코드는 실행 시 오류가 발생한다.
readonly var
var="readonly var를 바꿔보자"
```

## 지역 변수, 전역 변수, 환경 변수

- 변수 선언 시 기본적으로 전역 변수(global variable)로 설정된다.
    - 전역 변수는 스크립트 내에서 지역 구분 없이 사용 가능하지만, 스크립트 외부에서 참조할 수 없다.
- 단 함수 안에서만 지역 변수를 사용할 수 있는데, 이 경우에는 변수 앞에 local을 붙여야 한다.
- 변수명 앞에 export를 붙이면 환경변수로 설정되어 자식 스크립트에서 사용 가능하다.

```sh
# 전역 변수 지정
string="hello world"
echo ${string}

# 지역 변수 테스트 함수
string_test() {
    # 전역 변수와 동일하게 사용함. 만약 local 뺀다면 전역 변수에 덮어씌어지게 됨
    local string="local"
    echo ${string}
}
# 지역 변수 테스트 함수 호출
string_test
# 지역 변수 테스트 함수에서 동일한 변수 명을 사용했지만 값이 변경되지 않음
echo ${string}

# 환경 변수 선언
export hello_world="hello world..."
# 자식 스크립트 호출은 스크립트 경로을 쓰면된다.
/home/export_test.sh

#환경 변수를 테스트하기 위해 export_test.sh 파일을 만들고 선언한 변수를 확인해본다.
echo ${hello_world}
```

## 특별한 변수

- $0 : 스크립트명
- $1 ~ $9 : 인수(첫 번째 인수는 $1, 두 번째 인수는 $2... 로 접근)
- $# : 스크립트에 전달된 인수의 수
- $* : 모든 인수를 모아 하나로 처리
- $@ : 모든 인수를 각각 처리
- $? : 직전에 실행한 커맨드의 종료 값 **(0=성공, 1=실패)**
- $$ : 이 쉘 스크립트의 프로세스 ID
- $! : 마지막으로 실행한 백그라운드 프로세스 ID

## 특수문자 입력

- 특수 문자 자체를 문자열로서 사용하려면 '\'를 앞에 붙여서 쓴다.

# 함수 선언

- 함수 작성 시 '함수명() { 내용 }' 형태로 작성한다.
- 함수 앞에 function을 생략해도 된다.
- 생성한 함수를 실행할 때 인자는 공백 단위로 구분하여 입력한다.

```sh
# 앞에 function을 붙이지 않아도 함수로 인식한다.
string_test() {
    echo "string test"
}

function string_test2() {
    echo "string test 2"
    echo "input : ${@}"
}
string_test

# 함수에 인자값을 전달할 때는 공백으로 구분하여 입력
string_test2 "hello" "world"
```

# while, until

- while은 조건문이 true인 한 계속 실행된다(조건식이 false가 되면 종료).
- until은 조건문이 false인 한 계속 실행된다(조건식이 true가 되면 종료).

```sh
# 수행 조건이 true 일때 실행됨 (실행 횟수 지정이 필요하지 않은 반복문 필요 시 좋음)
count=0
while [ ${count} -le 5 ]; do
    echo ${count}
    count=$(( ${count}+1 ))
done

# 수행 조건이 false 일때 실행됨 (실행 횟수 지정이 필요하지 않은 반복문 필요 시 좋음)
count2=10
until [ ${count2} -le 5 ]; do
    echo ${count2}
    count2=$(( ${count2}-1 ))
done
```

# 조건문 작성

## if, elif, else

- Python과 유사하게 elif를 사용한다.
- 조건문 작성 시 **실행 문장이 없으면 오류가 발생한다.**

## case

- '|' 기호로 다중 조건(or)을 입력받을 수 있다.
- 조건문의 마무리는 ';;'로 표시한다.

```sh
# case문 테스트를 위한 반복문
for string in "HELLO" "WORLD" "hello" "world" "s" "start" "end" "etc"; do

    # case문 시작
    case ${string} in
        hello|HELLO)
            echo "${string}: hello 일때"
            ;;
        wo*)
            echo "${string}: wo로 시작하는 단어 일때"
            ;;
        s|start)
            echo "${string}: s 혹은 start 일때"
            ;;
        e|end)
            echo "${string}: e 혹은 end 일때"
            ;;
        *)
            echo "${string}: 기타"
            ;;
    esac
    # //case문 끝

done
```