import sys
from _collections import deque


def miro(q):
    while q:
        f = q.popleft()
        i = f[0]
        j = f[1]
        for r, c in rc:
            if 0 <= i+r < N and 0 <= j+c < N and d[i+r][j+c] != '1' and v[i+r][j+c] == 0:
                if d[i+r][j+c] == '3':
                    return v[i][j]
                else:
                    v[i+r][j+c] += v[i][j] + 1
                    q.append([i+r, j+c])

    return 0


sys.stdin = open('input_5105.txt')


T = int(input())
# T = 1
for tc in range(1, T+1):
    N = int(input())
    d = [list(input().strip()) for _ in range(N)]
    q = deque()
    v = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if d[i][j] == '2':
                q.append([i, j])
                # v[i][j] = 1
                break

    rc = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    print(f'#{tc} {miro(q)}')
