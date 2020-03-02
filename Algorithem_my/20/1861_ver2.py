import sys

sys.stdin = open('1861_input.txt')


# def dp(i, j):
#     cnt = 1
#     flag = True
#     while flag:
#         flag = False
#         v[d[i][j]] = 1
#         for x, y in rc:
#             if 0 <= i+x < N and 0 <= i+y < N and d[i][j]+1 == d[i+x][j+y]:
#                 i += x
#                 j += y
#                 if dpp[d[i][j]]:
#                     cnt += dpp[d[i][j]]
#                     return cnt
#                 cnt += 1
#                 flag = True
#                 return cnt
#                 break
#     return cnt


# T = int(input())
# rc = [[0, 1], [1, 0], [-1, 0], [0, -1]]
# for tc in range(1, T+1):
#     N = int(input())
#     n = N**2
#     d = [list(map(int, input().split())) for _ in range(N)]
#     v = list([0] for _ in range(n+1))
#     dpp = [0] * (n+1)
#     c = 0

#     for i in range(N):
#         for j in range(N):
#             if not v[d[i][j]] and c <= n-d[i][j]:
#                 cnt = dp(i, j)
#                 dpp[d[i][j]] = cnt
#                 if c == cnt:
#                     if r > d[i][j]:
#                         r = d[i][j]
#                 elif cnt > c:
#                     c = cnt
#                     r = d[i][j]
#     print(f'#{tc} {r} {c}')


def dp(i, j):
    cnt = 1
    flag = True
    while flag:
        flag = False
        visited[board[i][j]] = True
        for dx, dy in idx:
            if 0 <= i+dx < N and 0 <= j+dy < N and board[i][j]+1 == board[i+dx][j+dy]:
                i += dx
                j += dy
                if cache[board[i][j]]:
                    cnt += cache[board[i][j]]
                    return cnt
                cnt += 1
                flag = True
                break
    return cnt


T = int(input())
for t in range(T):
    N = int(input())
    n = N**2
    board = [list(map(int, input().split())) for _ in range(N)]
    idx = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited = [False] * (n+1)
    cache = [0] * (n+1)
    res = 0
    for i in range(N):
        for j in range(N):
            if not visited[board[i][j]] and res <= n - board[i][j]:
                cnt = dp(i, j)
                cache[board[i][j]] = cnt
                if res == cnt:
                    if board[i][j] < l:
                        l = board[i][j]
                elif cnt > res:
                    res = cnt
                    l = board[i][j]
    print('#{} {} {}'.format(t+1, l, res))
