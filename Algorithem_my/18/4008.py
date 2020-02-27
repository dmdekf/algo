import sys


def f(n, k, s):
    global max
    global min
    if n == k:
        if s > max:
            s = max
        elif s < min:
            s = min
    # if s < max and s > min
    else:
        if cal[n]:
            cla[n][1] -= 1
            f(n+1, k, s+d[n])
        f(n+1, k, s)


sys.stdin = open('4008_input.txt')

T = int(input())
T = 2

for tc in range(1, T+1):
    N = int(input())
    cd = list(map(int, input().split()))
    cal = [
        ['+', 0],
        ['-', 0],
        ['*', 0],
        ['/', 0],
    ]
    # print(cd)
    for i in range(N-1):
        cal[i][1] = cd[i]
    # print(cal)
    d = list(map(int, input().split()))

    max = -10000000000
    min = 10000000000
