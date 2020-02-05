import sys
sys.stdin = open("input.txt")
from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 12까지의 원소 중  N개가 포함된 부분집합 
    subsets = combinations(range(1,13), N)
    
    # cnt = 0

    # for i in subsets:
    #     if sum(i) == K:
    #         cnt +=1 

    cnt = sum(1 for i in subsets if sum(i) == K)
    print('#{} {}'.format(tc, cnt))