
import sys

sys.stdin = open('3752_input.txt')

# idea1
# def f(d):
#     r = {0}
#     for i in d:
#         for j in list(r):
#             r.add(i+j)
#     return len(r)
# T = int(input())
# idea 2
# dp = {0}
# for s in d:
#     temp = set()
#     for n in dp:
#         temp.add(s+n)
#     dp.update(temp)
# print(len(dp))
# idea 4
# for tc in range(1, T+1):
#     N = int(input())
#     d = list(map(int, input().split()))
#     s = sum(d)
#     nd = [1] + [0]*(s)
#     for n in d:
#         for i in range(s-n, -1, -1):
#             # if nd[i]:
#             #     nd[i+n] = 1
#             nd[i+n] = s[i+n] | s[i]
#     print(f'#{tc} {sum(nd)}')

# idea 5 dpstyle
# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     d = list(map(int, input().split()))
#     s = sum(d)
#     nd = [1] + [0]*(s)
#     for n in d:
#         for i in range(s, n-1, -1):
#             # if nd[i-n]:
#             #     nd[i] = 1
#             nd[i] = nd[i-n]

#     print(f'#{tc} {sum(nd)}')
# idea6(3 + 5)
# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     d = list(map(int, input().split()))
#     s = sum(d)
#     rd = [0]
#     nd = [1] + [0]*(s)
#     for i in d:
#         temp = rd[:]
#         for j in temp:
#             if not nd[i+j]:
#                 nd[i+j] = 1
#                 rd.append(i+j)

#     print(f'#{tc} {sum(nd)}')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    d = list(map(int, input().split()))
    s = sum(d)
    rd = {0}
    nd = [1] + [0]*(s)
    for i in d:
        for j in list(rd):
            if not nd[i+j]:
                nd[i+j] = 1
                rd.add(i+j)
    print(f'#{tc} {sum(nd)}')

# # idea bit

# T = int(input())
# for tc in range(1, T+1):
#     n = input()
#     data = map(int, input().split())
#     a = 1
#     for i in data:
#         a |= a << i
#     print('#%i' % tc, bin(a).count('1'))
