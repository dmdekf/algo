import sys


def f(n, num, op1, op2, op3, op4):
    global maxi
    global mini
    # global num
    if n == N:
        if num > maxi:
            maxi = num
        if num < mini:
            mini = num
        return
    if op1:
        f(n+1, num+d[n], op1-1, op2, op3, op4)
    if op2:
        f(n+1, num-d[n], op1, op2-1, op3, op4)
    if op3:
        f(n+1, num*d[n], op1, op2, op3-1, op4)
    if op4:
        f(n+1, int(num/d[n])+1, op1, op2, op3, op4-1)


sys.stdin = open('4008_input.txt')

T = int(input())
# T = 2

for tc in range(1, T+1):
    N = int(input())
    op1, op2, op3, op4 = map(int, input().split())
    d = list(map(int, input().split()))
    maxi = float('-inf')
    mini = float('inf')
    f(1, d[0], op1, op2, op3, op4)
    print(f'#{tc} {maxi - mini}')

# def f(n, k, r, op1, op2, op3, op4):
#     global minV, maxV
#     if n==k:
#         if maxV<r:
#             maxV = r
#         if minV>r:
#             minV = r
#     else:
#         if op1>0:
#             f(n+1, k, r+card[n], op1-1, op2, op3, op4)
#         if op2>0:
#             f(n+1, k, r-card[n], op1, op2-1, op3, op4)
#         if op3>0:
#             f(n+1, k, r*card[n], op1, op2, op3-1, op4)
#         if op4>0:
#             f(n + 1, k, int(r/card[n]), op1, op2, op3, op4 - 1)

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     op1, op2, op3, op4 = map(int, input().split())
#     card = list(map(int, input().split()))
#     minV = 10000000000
#     maxV = -10000000000
#     f(1, N, card[0], op1, op2, op3, op4)
#     print('#{} {}'.format(tc, maxV-minV))
