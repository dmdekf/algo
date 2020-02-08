import sys

sys.stdin = open('input_8797.txt')


def rec(x):
    recd = [[0] * N for _ in range(N)]
    for j in range(N):
        for i in range(N):
            recd[j][N - i - 1] = d[i][j]
    return recd


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    d = [list(map(int, input().split())) for _ in range(N)]

    result = [0] * 4
    for j in range(4):
        for i in range(N // 2):
            result[j] += (sum(d[i][i:-i - 1]))
        d = rec(d)

    print('#{} {}'.format(tc, (max(result) - min(result))))