import sys

sys.stdin = open('1861_input.txt')


def dp(i, j):
    cnt = 1
    flag = True
    while flag:
        flag = False
        v[d[i][j]] = 1
        for x, y in rc:
            if 0 <= i+x < N and 0 <= j+y < N and d[i][j]+1 == d[i+x][j+y]:
                i += x
                j += y
                if dpp[d[i][j]]:
                    cnt += dpp[d[i][j]]
                    return cnt
                cnt += 1
                flag = True
                break
    return cnt


T = int(input())

for tc in range(1, T+1):
    rc = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    N = int(input())
    n = N**2
    d = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * (n+1)
    dpp = [0] * (n+1)
    c = 0

    for i in range(N):
        for j in range(N):
            if not v[d[i][j]] and c <= n-d[i][j]:
                cnt = dp(i, j)
                dpp[d[i][j]] = cnt
                if c == cnt:
                    if r > d[i][j]:
                        r = d[i][j]
                elif cnt > c:
                    c = cnt
                    r = d[i][j]
    print(f'#{tc} {r} {c}')
