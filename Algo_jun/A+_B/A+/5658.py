

import sys

sys.stdin = open('5658_input.txt')

T = int(input())
# ver1 str
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     d = input()
#     w = N//4
#     num = set()

#     # 회전 후 첫 구역
#     for i in range(w):
#         # 구역 번호
#         for j in range(4):
#             s = ''
#             # 구역 내부 원소 번호
#             for p in range(w):
#                 s += d[(i+j*w+p) % N]
#             num.add(int(s, 16))
# ver2 add
for tc in range(1, T+1):
    N, K = map(int, input().split())
    d = input()
    w = N//4
    num = set()
    d += d[:w]
    for i in range(w):
        for j in range(4):
            num.add(int(d[(i+j*w):(i+j*w)+w], 16))

    print(f'#{tc} {sorted(list(num),reverse=True)[K-1]}')
