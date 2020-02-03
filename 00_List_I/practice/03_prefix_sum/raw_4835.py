# 완전히 열거한 뒤 풀어보기.
import sys

sys.stdin = open('input.txt')

T = int(input())
# N : 숫자개수, M :구간 d : 숫자리스트
for tc in range(1,T+1):
    N, M = map(int,input().split())
    d = list(map(int, input().split()))

    max_value = 0
    #minvalue는 임의의 큰 값으로 잡는 것이 좋다.
    min_value = 1000000

    for i in range(N-M+1):
        s = 0
        for j in range(i, i+M):
            s += d[j]
        if max_value < s:
            max_value = s 
        if min_value > s:
            min_value = s

    print('#{} {}'.format(tc, max_value - min_value))

