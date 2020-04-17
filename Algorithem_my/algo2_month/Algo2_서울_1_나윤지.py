def f(i, j, n, k):
    global M
    global s
    if n*k > M:
        s = k
        M = n*s
    for r, c in rc:
        if 0 <= i+r < N and 0 <= j+c < N:
            if v[i+r][j+c]==0 and d[i+r][j+c]==n:
                v[i + r][j + c] =1
                k+=1
                f(i+r, j+c,n,k)
    return

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    d = [list(map(int, input().split())) for _ in range(N)]
    v=list([0]*N for _ in range(N))
    rc = [(1, 0), (0, -1), (0, 1), (-1, 0),(-1,-1),(1,1),(-1,1),(1,-1)]
    M = float('-inf')
    s = 1
    for i in range(N):
        for j in range(N):
            if d[i][j] and v[i][j]==0:
                v[i][j] = 1
                f(i,j,d[i][j],1)

    print('#{} {} {}'.format(tc, M, s))
