import sys
sys.stdin = open('input_1249.txt')

# 다익스트라, 플로이드 => 최단경로 구현이 쉽다.


def dfs(x, y, temp):
    s = []
    s.append((x, y, temp))
    while s:
        i, j, t = s.pop(0)
        v[i][j] = t
        for r, c in rc:
            nx = i+r
            ny = j+c
            if 0 <= nx < N and 0 <= ny < N and v[nx][ny] > t+d[nx][ny]:
                v[nx][ny] = t+d[nx][ny]
                s.append((nx, ny, v[nx][ny]))
    return v[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = [[]*N for _ in range(N)]
    for i in range(N):
        d[i] = list(map(int, input()))
    rc = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    v = [[float('inf')]*N for _ in range(N)]
    minV = float('inf')

    print(f'#{tc} {dfs(0, 0, 0)}')
