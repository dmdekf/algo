import sys

sys.stdin = open('input_5208.txt')


# def f(idx, temp, s, rs):
#     global cnt
#     if s > N-1:
#         if cnt > temp:
#             cnt = temp
#             return
#         else:
#             return
#     elif s+rs < N:
#         return
#     else:
#         f(idx+1, temp, s, rs-M[idx])
#         f(idx+1, temp+1, s+M[idx], rs-M[idx])


# T = int(input())

# for tc in range(1, T+1):
#     d = list(map(int, input().split()))
#     N = d[0]
#     M = [d[i] for i in (range(1, N))]
#     cnt = N-1
#     f(0, 0, M[0], sum(M))
#     print(f'#{tc} {cnt}')

def f(idx, temp, s, rs):
    global cnt
    global fnt
    fnt += 1
    if cnt <= temp:
        return
    if idx+s >= d[0]:
        if cnt > temp:
            cnt = temp
        return
    if s+idx+rs < d[0]:
        return
    for i in d[idx+1:idx+s+1]:
        idx += 1
        s = i
        f(idx, temp+1, s, rs-(s))


T = int(input())

for tc in range(1, T+1):
    d = list(map(int, input().split()))
    cnt = float('inf')
    fnt = 1
    f(1, 0, d[1], sum(d[1:]))
    print(f'#{tc} {cnt} {fnt}')

# def backtrack(idx, x, cnt):
#     global res
#     global fnt
#     fnt += 1
#     if cnt >= res:
#         return
#     if idx + x >= info[0]:
#         if res > cnt:
#             res = cnt
#         return
#     for i in info[idx+1:idx+x+1]:
#         idx += 1
#         x = i
#         backtrack(idx, x, cnt+1)


# T = int(input())
# for t in range(T):
#     info = list(map(int, input().split()))
#     res = 10000000
#     fnt = 0
#     backtrack(1, info[1], 0)

#     print(f'#{t+1} {res} {fnt}')
