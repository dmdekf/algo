import sys

sys.stdin = open('input_5209.txt')


def f(row, result):
    global mini
    if row == N:
        if result and mini > result:
            mini = result
            return
    elif mini <= result:
        return
    for i in range(N):
        if not chk_row[i]:
            chk_row[i] = 1
            f(row+1, result+d[row][i])
            chk_row[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    d = []
    for _ in range(N):
        d.append(list(map(int, input().split())))
    chk_row = [0]*N
    mini = float('inf')
    cnt = 0
    f(0, 0)
    print(f'#{tc} {mini}')

# def f(row, result, idx):
#     global mini
#     if row == idx:
#         if result and mini > result:
#             mini = result
#             return
#     elif mini <= result:
#         return
#     for i in range(N):
#             if not chk_row[i]:
#                 chk_row[i] = 1
#                 f(row+1, result+d[row][i], idx)
#                 chk_row[i] = 0

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     d = []
#     for _ in range(N):
#         d.append(list(map(int, input().split())))
#     chk_row = [0]*N
#     mini = float('inf')
#     cnt = 0
#     f(0, 0, N)
#     print(f'#{tc} {mini}')
