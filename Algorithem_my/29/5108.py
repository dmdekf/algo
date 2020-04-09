import sys

sys.stdin = open('input_5108.txt')


T = int(input())
# T = 1
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    d = list(input().split())

    for _ in range(M):
        index, data = map(int, input().split())
        d.insert(index, data)

    print(f'#{tc} {d[L]}')
