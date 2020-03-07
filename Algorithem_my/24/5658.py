

import sys

sys.stdin = open('5658_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    d = list(input())
    w = N//4
    num = set()
    for _ in range(w):
        for i in range(0, N, w):
            temp = ''.join(d[i:i+w])
            num.add(int(temp, 16))
        d.insert(0, d.pop())

    print(f'#{tc} {sorted(num)[len(num)-K]}')
