import sys

sys.stdin = open('1861_input.txt')


def f(x, y, s, c):
    global M
    global cnt
    if cnt < c:
        cnt = c
        M = s
    if cnt == c:
        M = min(M, s)
    v[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if d[nx][ny] == d[x][y] + 1:
            v[nx][ny] = 1
            f(nx, ny, s, c+1)
        v[nx][ny] = 0
    return


T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1, T+1):
    N = int(input())
    d = [list(map(int, input().split())) for _ in range(N)]
    v = list([0]*N for _ in range(N))
    M = float('inf')
    cnt = float('-inf')
    for i in range(N):
        for j in range(N):
            if cnt <= N**2 - d[i][j]:
                f(i, j, d[i][j], 1)
    print(f'#{tc} {M} {cnt}')
