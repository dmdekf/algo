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
        f(n+1, N, s+d[n])
        f(n+1, N, s)


sys.stdin = open('1486_input.txt')

T = int(input())

for t in range(1, T+1):
    N, B = map(int, input().split())
    d = list(list(map(int, input().split())))
    m = 10000*N
    f(0, N, 0)
    print(f'#{t} {m}')
