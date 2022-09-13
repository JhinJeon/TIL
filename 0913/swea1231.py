# SWEA 1231 - 중위순회

import sys
sys.stdin = open('input.txt')
# 트리 구조의 최상위 노드를 반환하는 함수 find_root


def find_root():
    for i in range(1, v + 1):
        if par[i] == 0:    # 부모가 없으면 root
            return i


# 중위 순회하며 탐색한  값을 출력하는 함수 inorder
def inorder(n):
    global answer
    if n:                                  # n이 0이 아닌 경우(자식이 있는 경우)
        inorder(ch1[n])
        answer += word[n]                  # answer에 순회에서 탐색하는 단어를 하나씩 조합
        inorder(ch2[n])


for tc in range(1, 11):
    v = int(input())                       # v = 정점 개수이자 마지막 정점 번호
    answer = ""                            # answer = 출력할 단어

    word = [0] * (v + 1)                   # 노드 번호(인덱스)에 값(문자) 저장
    ch1 = [0] * (v + 1)                    # 왼쪽 자식
    ch2 = [0] * (v + 1)                    # 오른쪽 자식
    par = [0] * (v + 1)                    # 부모 노드
    
    for i in range(v):
        input_info = list(input().split())  # 입력받는 값을 임시 리스트에 저장
        idx = int(input_info[0])
        word[idx] = input_info[1]           # 노드 번호에 지정된 값 정보 저장

        # 자식 노드가 1개 이상 있는 경우 왼쪽 자식에 저장
        if len(input_info) > 2:    
            left_child = int(input_info[2])
            ch1[idx] = left_child

            # 자식 노드가 2개인 경우 오른쪽 자식에도 저장
            if len(input_info) == 4:
                right_child = int(input_info[3])
                ch2[idx] = right_child

    # root = root 노드 번호
    root = find_root()

    # root를 기준으로 중위 순회 결과 출력
    inorder(root)
    print(f'#{tc} {answer}')
