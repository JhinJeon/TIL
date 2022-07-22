# 작성자 이름, 메일 등록 (최초 1번만 실행)

git config --global user.name "github username"

git config --global user.email "github email"

# config 정보 출력

git config --global --list

# 일반 폴더 -> 로컬 저장소

git init

# 버전 상태 출력

git status

# Working Directory -> Staging Area

git add [Filename]

git add .  # 모든 파일 add

# Staging Area -> Commits

git commit -m "commit message"

# commits 목록 출력

git log

git log --oneline  # 한줄로 보기 옵션

git log -p  # 커밋마다 차이 보기 옵션

# 로컬 저장소와 원격 저장소를 연결

git remote add origin [Github repository URL]

# 연결된 원격 저장소 목록 조회
git remote -v

# 원격 저장소 연결 삭제
git remote rm origin

git remote remove origin

# 로컬 저장소의 commits을 원격 저장소에 반영

git push origin master

git push -u origin master  # -u 옵션을 했다면 이후 push할 때는 git push만으로도 가능