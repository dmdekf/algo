from collections import deque
import sys
sys.stdin = open('input_1249.txt')
# 다익스트라, 플로이드 => 최단경로 구현이 쉽다.


def dfs(x, y, temp):
    s = deque()
    s.append((x, y, temp))
    while s:
        i, j, t = s.popleft()
        v[i][j] = t
        for r, c in rc:
            nx = i+r
            ny = j+c
            if 0 <= nx < N and 0 <= ny < N and v[nx][ny] > t+d[nx][ny]:
                v[nx][ny] = t+d[nx][ny]
                s.append((nx, ny, v[nx][ny]))
    return v[N-1][N-1]


def bfs(r, c):
    maxV = (2 * N - 3) * 9
    v = [[maxV]*N for _ in range(N)]
    q = deque([[r, c]])
    v[r][c] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N:
                nValue = v[r][c]+f[nr][nc]
                if nValue < min(v[nr][nc], v[N-1][N-1]):
                    v[nr][nc] = nValue
                    if (r, c) != (N-1, N-1):
                        q.append([nr, nc])
    return v[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = [[]*N for _ in range(N)]
    for i in range(N):
        d[i] = list(map(int, input()))
    rc = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    v = [[10000]*N for _ in range(N)]

    print(f'#{tc} {dfs(0, 0, 0)}')
