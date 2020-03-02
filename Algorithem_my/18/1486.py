import sys


def f(n, s):
    global cnt
    cnt += 1
    global m
    if n == N:
        if m >= s - B > -1:
            m = s - B
    elif m >= s - B > -1:
        m = s - B
    elif m < s - B:
        return
    else:
        f(n+1, s+d[n])
        f(n+1, s)


sys.stdin = open('1486_input.txt')

T = int(input())

for t in range(1, T+1):
    N, B = map(int, input().split())
    d = list(list(map(int, input().split())))
    m = 10000*N
    cnt = 0
    f(0, 0)
    print(cnt)
    print(f'#{t} {m}')
