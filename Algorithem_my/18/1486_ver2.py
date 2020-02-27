import sys


def f(n, N, s):
    global m
    if n == N:
        if s >= B and m >= s - B:
            m = s - B
    elif s >= B and m >= s - B:
        m = s - B
    elif m < s - B:
        return
    else:
        v[n] = 1
        f(n+1, N, s+d[n])
        v[n] = 0
        f(n+1, N, s)
        # for i in range(N):
        #     if v[i] == 0:
        #         v[i] = 1
        #         f(i+1, s+d[i])


sys.stdin = open('1486_input.txt')
# 10
# 5 16
# 3 1 3 5 6
T = int(input())
# T = 2
for t in range(1, T+1):
    N, B = map(int, input().split())
    d = list(list(map(int, input().split())))
    v = [0]*N
    # print(d)
    m = 10000*N
    f(0, N, 0)
    print(f'#{t} {m}')
