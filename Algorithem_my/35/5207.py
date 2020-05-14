import sys

sys.stdin = open('input_5207.txt')


def f(l, r, chk=False):
    global cnt
    m = (l+r)//2
    if N[m] == num:
        cnt += 1
        return True
    if N[m] > num and (not chk or chk == 'r'):
        return f(l, m-1, 'l')
    elif N[m] < num and (not chk or chk == 'l'):
        return f(m+1, r, 'r')


T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    N = list(map(int, input().split()))
    M = list(map(int, input().split()))
    N.sort()
    cnt = 0
    for num in M:
        f(0, A-1)
    print(f'#{tc} {cnt}')
