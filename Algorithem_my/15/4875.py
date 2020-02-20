def dfs(si, sj):
    if maze[si][sj] == '3':
        return 1
    else:
        maze[si][sj] = '1'
        for k in range(4):
            nx = si + dx[k]
            ny = sj + dy[k]
            if maze[nx][ny] != '1':
                if dfs(nx, ny) ==1:
                    return 1
        return 0

# def dfs(si, sj):
#     s = []
#     v = [[0]*(N+2) for _ in range(N+2)]
#     s.append((si,sj))
#     v[si][sj] = 1
#     while s:
#         si, sj = s.pop()
#         if maze[si][sj] == '3':
#             return 1
#
#         else:
#             for k in range(4):
#                 nx = si + dx[k]
#                 ny = sj + dy[k]
#                 if maze[nx][ny] !='1' and v[nx][ny] == 0:
#                     s.append((nx,ny))
#                     v[nx][ny] = 1
#     return 0
import sys
sys.stdin = open('1226_input.txt')

T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())

    maze = list(['1']*(N+2) for _ in range(N+2))
    d = list(list(input()) for _ in range(N))
    # print(maze)
    for i in range(0, N):
        for j in range(0, N):
            maze[i+1][j+1] = d[i][j]
    # print(maze)
    si, sj = -1, -1
    for i in range(N+1):
        for j in range(N+1):
            if maze[i][j] == '2':
                si = i
                sj = j
                break
    if sj ==-1:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {dfs(si, sj)}')