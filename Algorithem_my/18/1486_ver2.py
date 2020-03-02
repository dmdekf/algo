import sys

sys.stdin = open('1486_input.txt')


def f(n, s):
    global m
    if n == N:
        if s >= B:
            m = min(m, s)
        return
    f(n+1, s+d[n])
    f(n+1, s)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    d = list(list(map(int, input().split())))
    m = float('inf')
    f(0, 0)
    print(f'#{tc} {m - B}')
