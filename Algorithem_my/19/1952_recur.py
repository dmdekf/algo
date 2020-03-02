import sys


def f(n, s, d, m, m3):
    global minV
    if n > 12:
        if minV > s:
            minV = s
        return
    elif s >= minV:
        return
    else:
        f(n+1, s+min(data[n]*d, m), d, m, m3)
        if data[n]:
            f(n+3, s+m3, d, m, m3)


sys.stdin = open('1952_input.txt')

T = int(input())
# T = 1
for tc in range(1, T+1):
    d, m, m3, y = map(int, input().split())
    data = [0] + list(map(int, input().split()))
    # print(d)
    minV = y
    f(1, 0, d, m, m3)
    print(f'#{tc} {minV}')
# for tc in range(1, T+1):
#     fare = list(map(int, input().split()))
#     d = list(map(int, input().split()))
#     # print(d)
#     dp = [0]*12
#     dp[0] = min(fare[0]*d[0], fare[1])
#     for i in range(1, 12):
#         dp[i] = min(dp[i-1]+d[i]*fare[0], dp[i-1]+fare[1])
#         if i >= 2:
#             dp[i] = min(dp[i-3]+fare[2], dp[i])
#     result = min(dp[11], fare[3])
#     print(f'#{tc} {result}')
