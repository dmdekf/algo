
import sys

sys.stdin = open('input_5097.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    d = list(map(int, input().split()))
    print(f'#{tc} {d[M%N]}')
