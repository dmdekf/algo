import sys

sys.stdin = open('1861_input.txt')

T = int(input())
rc = [[0, 1], [1, 0], [-1, 0], [0, -1]]
for tc in range(1, T+1):
    N = int(input())
    d = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*(N**2+1)

    for i in range(N):
        for j in range(N):
            for r, c, in rc:
                if 0 <= i+r < N and 0 <= j+c < N and d[i][j] + 1 == d[i+r][j+c]:
                    v[d[i][j]] = 1
    M = 0
    cnt = 1

    for i in range(len(v)-1, -1, -1):
        if v[i]:
            c += 1
        else:
            if cnt <= c:
                cnt = c
                M = i+1
            c = 1

    print(f'#{tc} {M} {cnt}')
