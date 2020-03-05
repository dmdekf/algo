import sys

sys.stdin = open('1865_input.txt')


def f(n, k, s):
    global maxV
    global u
    global w
    global P
    if(n == k):
        if(maxV < s*100):
            maxV = s*100
    elif(maxV >= s*100):
        return
    else:
        for i in range(k):
            if(u[i] == 0):
                u[i] = 1    # i번 사람이 n번 일을 맡음
                f(n+1, k, s*P[i][n]/100)  # n번 까지의 성공확률을 구하고, n+1 정하러 감
                u[i] = 0    # 다른 일을 맡도록 함


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for i in range(N)]
    u = [0]*N
    w = [0]*N
    maxV = 0
    f(0, N, 1)
    print('#{} {:.6f}'.format(tc, maxV))

# def f(n, s):
#     global M
#     if s <= M:
#         return 0
#     if n == N:
#         if M < s:
#             M = s
#             return 0
#     for i in range(N):
#         if u[i] == 0:
#             u[i] = 1
#             if d[n][i]:
#                 f(n+1, s*(d[n][i]/100))
#             u[i] = 0


# T = int(input())
# # T = 2
# for tc in range(1, T+1):
#     N = int(input())
#     u = [0]*N
#     d = [list(map(int, input().split())) for _ in range(N)]
#     M = float('-inf')
#     f(0, 1)
#     # M *= 100
#     # print('#{} {}'.format(tc, "%0.6f" % M))
#     print('#{} {:.6f}'.format(tc, M*100))
