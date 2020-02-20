def dfs(i, j):
    if maze[i][j] =='3':
        return 1
    else:
        maze[i][j] = '1'
        for k in range(4): #상하좌우 체크
            nx = i + dx[k]
            ny = j + dy[k]
            if maze[nx][ny] != '1': #벽이 아닌 칸이 있으면
                if dfs(nx, ny) == 1: #이동, 목적지를 찾은 경우 중단
                    return 1
        return 0

def dfs2(i, j):
    s = []
    v = [[0]*16 for _ in range(16)]
    s.append((i,j)) #시작점
    v[i][j] = 1
    while s:
        i, j = s.pop()
        if maze[i][j] == '3':
            return 1
        for k in range(4):
            nx = i+dx[k]
            ny = j + dy[k]
            if maze[nx][ny]!= '1' and v[nx][ny] == 0: # 벽이 아니고 방문안 한 칸이 있으면
                s.append((nx, ny))
                v[nx][ny] = 1
    return 0


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
T = 10
for tc in range(1, T+1):
    n = input()
    maze = list(list(input()) for _ in range(16))
    si, sj = -1, -1
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                si, sj = i, j
                break
        if si != -1:
            break
    # print(si,sj)
    # print(f'#{tc} {dfs(si, sj)}')
    print(f'#{tc} {dfs2(si, sj)}')
    # print(maze)
