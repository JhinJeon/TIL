# 연습문제1 - 순회

# 간선은 부모 - 자식 순서로 표시
# 전위 순회(부모 노드를 가장 먼저 탐색)
# v = e + 1
# e = v - 1

def find_root():
    for i in range(1, V+1):
        if par[i] == 0:  # 부모가 없으면 root
            return i


def preorder(n):    # 전위순회
    if n:
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])


def inorder(n):     # 중위순회
    if n:
        inorder(ch1[n])
        print(n, end=' ')
        inorder(ch2[n])


def postorder(n):   # 후위순회
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end=' ')


def f(n):   # 순회한 정점 수를 반환하는 함수

    return


V = int(input())    # 정점 개수이자 마지막 정점 번호
arr = list(map(int, input().split()))
E = V - 1

ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)

par = [0] * (V + 1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p
root = find_root()

preorder(root)
print()
inorder(root)
print()
postorder(root)

# 세부 트리 순회 : 위 함수에 세부 트리의 루트 번호 입력
# 예) 3번 노드의 세부 트리 전위 순회 : preorder(3)
