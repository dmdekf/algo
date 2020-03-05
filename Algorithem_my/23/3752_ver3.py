
import sys

sys.stdin = open('3752_input.txt')


def f(idx, res):
    global cnt
    if idx == N:
        if dp[idx].get(res) == None:
            dp[idx][res] = 1
            cnt += 1
        return
    elif dp[idx].get(res):
        return

    f(idx+1, res+d[idx])
    f(idx+1, res)
    dp[idx][res] = 1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    d = list(map(int, input().split()))
    dp = [{} for _ in range(N+1)]
    cnt = 0
    f(0, 0)
    print(f'#{tc} {cnt}')
