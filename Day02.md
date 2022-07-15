# Git 활용 심화

## 1. README

- 파일 명을 README.md로 설정하면 저장소 메인 화면에 README 항목이 출력됨
---
## 2. .gitignore

- 파일 명 앞에 .을 붙이면 숨김 파일 처리(.gitignore)
- .gitignore에 파일명을 적어서 저장하면 해당 파일은 버전관리가 되지 않음
- 중요한 정보(AWS의 인증 키 등)를 관리할 때 사용

### `유의사항 : .gitignore 파일을 먼저 생성한 후 파일 이름을 적어서 저장해야 정상적으로 버전 관리가 무시됨`
---
### .gitignore 할 파일이 많을 때:
- [링크](https://www.toptal.com/developers/gitignore/) 참고
---
## 3. Clone

- Clone : 원격 저장소 내용을 로컬 저장소에 다운로드
### Git Clone의 기능
1. 폴더 생성
2. git init
3. git remote add
4. 버전 및 파일 생성

##### `나는 add&push만 하면 됨`

---
## 4. Pull

- Pull : 연결된 저장소에 변경 사항을 업데이트
- git push (원격 저장소) (로컬 저장소)
- 원격 저장소에 새로운 내용이 업데이트 된 경우, 다른 저장소에서 업데이트 내역을 pull 할 수 있음

### Git Pull의 비정상적인 흐름?

- 먼저 다른 저장소에서 변경 내역을 불러온 후(pull), 내가 변경한 내용을 push해야 함
- pull을 하지 않고 push를 하는 경우 branch가 갈려서 에러가 발생할 수 있음
- 이 때는 원격 저장소에서 pull을 먼저 해볼 것 : 변경 사항 두 가지 중에 하나를 선택하거나, 둘 다 선택할 수 있음
    - 위 과정은 버전을 새로 만드는 것으로 간주됨 : 제 3의 변경사항도 지정 가능

## 5. Push & Pull 과정에서 문제가 생겼을 경우

- 여러 가지 버전들을 합쳐야 함(merge)
- 이후 merge된 내용들을 push

## 6. Github에서 저장소 불러오기

- 불러오고 싶은 장소에 우클릭 -> Git Bash here
- 이후 터미널 명령 창에 git clone (저장소 링크) 입력
`이미 git을 실행한 상태여서 별도로 git init을 수행할 필요 없음`

## 7. Merge

- 공유되지 않은 두 변경 사항 간 충돌(conflict)이 발생하는 경우 이를 merge할 필요가 있음
- merge는 새로운 버전으로 간주됨

## 번외1. Github Pages

- 나만의 페이지 만들기
- html 코드 기반 프로그램

## 번외2. Github Profiles

- 내 Github 저장소 메인 화면에 랜딩 페이지(프로필) 표시 가능
- 내 이름과 동일한 저장소를 만들면 자동으로 프로파일 등록