# 연습문제1 - 순회


# 트리 구조의 최상위 노드를 반환하는 함수 find_root
def find_root():
    for i in range(1, v+1):
        if par[i] == 0:  # 부모가 없으면 root
            return i


# 전위 순회하며 탐색한 값을 출력하는 함수 preorder
def preorder(n):    # 전위순회
    if n:
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])


v = int(input())        # v = 정점 개수이자 마지막 정점 번호
arr = list(map(int, input().split()))
e = len(arr) / 2        # e = 연결 관계의 개수

# ch1, ch2 = ch1은 왼쪽 자식, ch2는 오른쪽 자식
ch1 = [0] * (v + 1)
ch2 = [0] * (v + 1)

# par = 부모 노드
par = [0] * (v + 1)

for i in range(e):
    p, c = arr[i*2], arr[i*2+1]     # 연결 관계 정보 가져오기
    # 아직 연결 관계 대상에 대한 정보가 없는 경우 새로운 정보 추가
    if ch1[p] == 0:
        ch1[p] = c
    # 이미 정보가 기록된 경우 자식 노드 추가
    else:
        ch2[p] = c
    # 탐색한 노드의 부모 노드 정보 저장
    par[c] = p

# root = root 노드
root = find_root()


# root를 기준으로 전위 순회 결과 출력
preorder(root)
