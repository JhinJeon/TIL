# 1231. 중위순회

import sys
sys.stdin = open('input.txt')
# def inorder(v):  # global을 사용하지 않고 리턴하기
#     if v:
#         L = inorder(ch1[v])
#         R = inorder(ch2[v])
#         return L + alp_list[v] + R
#     return ""

def inorder(v):                 # 중위순회 (LVR)
    global answer
    if v:
        inorder(ch1[v])         # 왼쪽 자식 (L)
        answer += alp_list[v]   # 현재 노드 (V)
        inorder(ch2[v])         # 오른쪽 자식 (R)


for tc in range(1, 11):
    N = int(input())
    alp_list = [""] * (N + 1)   # 각 노드의 번호를 인덱스로 갖는 알파벳 리스트
    ch1 = [0] * (N + 1)         # 자식1
    ch2 = [0] * (N + 1)         # 자식2
    answer = ""                 # 순회하면서 나오는 알파벳들을 모아놓는 변수

    for _ in range(N):
        arr = input().split()                   # 중간에 알파벳이 나오기 때문에 map(int, ...) 사용 불가
        idx, alp = int(arr[0]), arr[1]          # 공통적인 부분
        if len(arr) == 4:                       # 자식이 둘인 경우
            l, r = int(arr[2]), int(arr[3])     # int화
            ch1[idx] = l                        # 자식1에 왼쪽 자식 삽입
            ch2[idx] = r                        # 자식2에 오른쪽 자식 삽입

        elif len(arr) == 3:                     # 자식이 하나인 경우
            l = int(arr[2])                     # int화
            ch1[idx] = l                        # 자식1에 왼쪽 자식 삽입

        alp_list[idx] = alp                     # 알파벳 리스트에도 해당 노드의 알파벳 삽입

    inorder(1)                                  # root를 1로 하는 중위탐색 시작
    print(f"#{tc} {answer}")

		# print(f"#{tc} {inorder(1)}") # global을 사용하지 않고 리턴하기