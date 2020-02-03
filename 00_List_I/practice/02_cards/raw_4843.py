from collections import Counter
import sys

sys.stdin = open('input.txt')
# 카드의 특징. 정수, 0-9까지의 한정된 숫자.


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    d = list(input())
    
    c = [0]*10

    for i in d:
        c[int(i)] += 1
    
    max_idx = 0
    max_value = c[0]
    
    for i in range(1,10):
        if max_value <= c[i]:
            max_value = c[i]
            max_idx = i
    print('#{} {} {}'.format(tc, max_idx, max_value))