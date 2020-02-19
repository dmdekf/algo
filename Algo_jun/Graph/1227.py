def dfs(i, j):
    s = []
    v = [[0] * 100 for _ in range(100)]
    s.append((i, j))
    v[i][j] = 1
    while s:
        i, j = s.pop()
        if maze[i][j] == '3':
            return 1
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if maze[nx][ny] != '1' and v[nx][ny] == 0:
                s.append((nx, ny))
                v[nx][ny] = 1
    return 0

T = 10
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1, T + 1):
    n = input()
    maze = list(list(input()) for _ in range(100))

    si, sj = 1, 1
    print(f'#{tc} {dfs(si,sj)}')