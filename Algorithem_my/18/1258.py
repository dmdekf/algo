import sys


def f(i, j):
    global ex
    global ey
    if d[i+1][j] == 0 and d[i][j+1] == 0:
        d[i][j] = 0
        ex = i
        ey = j
        # print(fx, fy)
        return 1

    else:
        d[i][j] = 0
        # print(i, j)
        for n in range(2):
            nx = i+dx[n]
            ny = j+dy[n]
            if nx >= 0 and ny >= 0 and nx < N and ny < N and d[nx][ny] != 0:
                if f(nx, ny) == 1:
                    return True
        return False


sys.stdin = open('1258_input.txt')

T = int(input())
# T = 2

for tc in range(1, T+1):
    N = int(input())
    d = [list(map(int, input().split())) for _ in range(N)]
    # print(d)
    dx = [0, 1]
    dy = [1, 0]
    chk = []
    for i in range(N):
        for j in range(N):
            if d[i][j]:
                chk += [[i, j]]
    flag = len(chk)
    stop = 0
    result = []
    # print(chk)
    ex = 0
    ey = 0
    while stop != flag:
        i, j = chk[stop]
        # print(d[i][j])
        if d[i][j] and f(i, j):
            # print(i, j)
            # print(ex, ey)
            for x in range(ex-i+1):
                for y in range(ey-j+1):
                    # print(d[i+x][j:j+ey])
                    d[i+x][j+y] = 0
            result.append([ex-i+1, ey-j+1])
        stop += 1
        ex = 0
        ey = 0
    result = sorted(result, key=lambda x: (x[0]*x[1], x[0]))
    print(f'#{tc} {len(result)}', end='')
    for a, b in result:
        print(f' {a} {b}', end='')
    print()
