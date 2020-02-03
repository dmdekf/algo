# 완전히 열거한 뒤 풀어보기.
import sys

sys.stdin = open('input.txt')

T = int(input())
# N : 숫자개수, M :구간 d : 숫자리스트
for tc in range(1,T+1):
    N, M = map(int,input().split())
    d = list(map(int, input().split()))

    arr = []

    for i in range(N-M+1):
        arr.append(sum(d[i:i+M]))

    print('#{} {}'.format(tc, max(arr) - min(arr)))