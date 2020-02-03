import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    d = list(map(int,input().split())) 

    max_value = d[0]
    min_value = d[0]
    for i in range(1, n):
        if max_value < d[i]:
            max_value = d[i]
        if min_value > d[i]:
            min_value = d[i]
    print('#{} {}'.format(tc, max_value - min_value))