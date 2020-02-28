import sys


def f(n, num):
    global maxi
    global mini
    # global num
    if n == N:
        if num > maxi:
            maxi = num
        if num < mini:
            mini = num
        return
    for i in range(4):
        if calc[i]:
            calc[i] -= 1
            if i == 0:
                newnum = num + d[n]
            elif i == 1:
                newnum = num - d[n]
            elif i == 2:
                newnum = num * d[n]
            else:
                if num // d[n] < 0 and num % d[n]:
                    newnum = (num // d[n]) + 1
                else:
                    newnum = num // d[n]
            f(n+1, newnum)
            calc[i] += 1


sys.stdin = open('4008_input.txt')

T = int(input())
# T = 2

for tc in range(1, T+1):
    N = int(input())
    calc = list(map(int, input().split()))
    d = list(map(int, input().split()))
    maxi = float('-inf')
    mini = float('inf')
    f(1, d[0])
    print(f'#{tc} {maxi - mini}')
