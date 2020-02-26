def f(x, y, j):
    if j > int(chk[0]):
        return 1
    else:
        if d[x][y] == chk[j]:
            v[x][y] = 1
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # print(nx, ny, j)
                if nx >= 0 and ny >= 0 and nx < N and ny < N:
                    if v[nx][ny] == 0:
                        if f(nx, ny, j+1) == 1:
                            return 1
            return 0


sys.stdin = open(('9640_input.txt'))


T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T+1):
    chk = list(input().split())
    N = int(input())
    d = list(list(input().split()) for _ in range(N))
    v = list([0]*N for _ in range(N))

    c = []
    for i in range(N):
        for j in range(N):
            if d[i][j] == chk[1]:
                c.append((i, j))

    result = 0
    while c:
        x, y = c.pop()
        if f(x, y, 1) == 1:
            result = 1
            break

    print(f'#{tc} {result}')
