# 작성자 이름, 메일 등록 (최초 1번만 실행)

git config --global user.name "github username"

git config --global user.email "github email"

# config 정보 출력

git config --global --list

# 일반 폴더 -> 로컬 저장소

git init

# 버전 상태 출력

git status

# 로컬 저장소와 원격 저장소를 연결

git remote add origin [Github repository URL]

# 연결된 원격 저장소 목록 조회
git remote -v

# 원격 저장소 연결 삭제
git remote rm origin

git remote remove origin