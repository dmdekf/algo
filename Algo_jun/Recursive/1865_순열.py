import sys

sys.stdin = open('1865_input.txt')


def f(n, s):
    global M
    if s <= M:
        return 0
    if n == N:
        if M < s:
            M = s
            return 0
    for i in range(N):
        if u[i] == 0:
            u[i] = 1
            if d[n][i]:
                f(n+1, s*(d[n][i]/100))
            u[i] = 0


T = int(input())
# T = 2
for tc in range(1, T+1):
    N = int(input())
    u = [0]*N
    d = [list(map(int, input().split())) for _ in range(N)]
    M = float('-inf')
    f(0, 1)
    # M *= 100
    # print('#{} {}'.format(tc, "%0.6f" % M))
    print('#{} {:.6f}'.format(tc, M*100))
