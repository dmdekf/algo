import sys
sys.stdin = open('input_1249.txt')


def f(x, y, temp):
    global minV
    if minV < temp:
        return 1
    if (x == N-1) and (y == N-1):
        if minV > temp:
            minV = temp
        return
    for r, c in rc:
        if 0 <= x+r < N and 0 <= y+c < N and v[x+r][y+c] > temp+d[x][y]:
            nx = x+r
            ny = y+c
            v[nx][ny] = temp+d[x][y]
            if f(nx, ny, temp+d[x][y]) == 1:
                return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = [[]*N for _ in range(N)]
    for i in range(N):
        d[i] = list(map(int, input()))
    rc = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    v = [[float('inf')]*N for _ in range(N)]
    g = [N-1, N-1]
    minV = float('inf')
    v[0][0] = 0
    f(0, 0, 0)
    print(f'#{tc} {minV}')
