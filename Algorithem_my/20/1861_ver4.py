import sys

sys.stdin = open('1861_input.txt')


def f(x, y, s, c):
    if v[d[x][y]]:
        return 1
    v[d[x][y]] = 1
    v[s] = c
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < N and 0 <= ny < N and d[nx][ny] == d[x][y] + 1:
            if f(nx, ny, s, c+1) == 1:
                return c + v[d[nx][ny]]
            f(nx, ny, s, c+1)
    return v[s]


T = int(input())
# T = 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1, T+1):
    N = int(input())
    d = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*(N**2+1)
    cnt = float('-inf')
    for i in range(N):
        for j in range(N):
            if not v[d[i][j]] and cnt <= N**2 - d[i][j]:
                v[d[i][j]] = f(i, j, d[i][j], 1)
                if cnt == v[d[i][j]]:
                    if M > d[i][j]:
                        M = d[i][j]
                elif cnt < v[d[i][j]]:
                    cnt = v[d[i][j]]
                    M = d[i][j]

    print(f'#{tc} {M} {cnt}')
