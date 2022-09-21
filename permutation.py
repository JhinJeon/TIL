p = [1, 2, 3, 4]


def permutation(n, k):  # 배열 p에서 k개 뽑기(n은 선택된 원소의 인덱스)
    if n == k:
        print(p)
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            permutation(n+1, k)
            p[n], p[i] = p[i], p[n]


permutation(0, 4)
