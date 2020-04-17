import sys

sys.stdin = open('input.txt')


def f(i, j):
    for r, c in rc:
        if 0 <= i+r < 10 and 0 <= j+c < 10:
            if not v[i+r][j+c] and d[i+r][j+c]:
                v[i + r][j + c] = 1
                f(i+r, j+c)
    return 1


T = int(input())
for tc in range(1, T+1):
    d = [list(map(int, input().split())) for _ in range(10)]
    v = list([0]*10 for _ in range(10))
    rc = [(1, 0), (0, -1), (0, 1), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    M = 0
    for i in range(10):
        for j in range(10):
            if d[i][j] and v[i][j] == 0:
                v[i][j] = 1
                M += f(i, j)
    print('#{} {}'.format(tc, M))
