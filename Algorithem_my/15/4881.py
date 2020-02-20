
def f(row, col):
    global m
    global s
    if s >= m:
        return
    if row == N:
        if m > s:
            m = s
        return
    for col in range(N):
        if not v[col]:
            v[col] = 1
            s += d[row][col]
            f(row+1, col)
            s -=d[row][col]
            v[col] = 0

import sys
sys.stdin = open('4881_input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    d = list(list(map(int,input().split())) for _ in range(N))
    v = [0] * N
    m = 10000000000000000000
    s = 0
    f(0,0)
    print(f'#{tc} {m}')