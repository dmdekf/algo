# def f(n, k):
#     global minV
#     global cnt
#     cnt += 1
#     if n == k:
#         s =0
#         for i in range(k):
#             s += arr[i][p[i]]
#         if minV > s:
#             minV = s
#     else:
#         for i in range(k):
#             if u[i]==0:
#                 u[i] = 1
#                 p[n] = i
#                 f(n+1, k)
#                 u[i] = 0
def f(n, k, s):
    global minV
    global cnt
    cnt+=1
    if n == k:
        if minV > s:
            minV = s
    elif minV <=s:
        return
    else:
        for i in range(k):
            if u[i]==0:
                u[i] = 1
                f(n+1, k, s+arr[n][i])
                u[i] = 0

import sys
sys.stdin = open('4881_input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    print(arr)
    p = [0] * N
    u = [0] * N
    minV = 10*N
    cnt = 0
    # f(0,N)
    f(0, N, 0)
    print(minV, cnt)