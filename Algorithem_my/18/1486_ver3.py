import sys


def DFS(n, v):
    global m
    if n == N:
        if v >= B:
            m = min(m, v)
        return
    DFS(n+1, v + D[n])
    DFS(n+1, v)


sys.stdin = open('1486_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    D = list(map(int, input().split()))
    m = float('inf')
    # print(m)
    DFS(0, 0)
    print('#{} {}'.format(tc, m-B))
