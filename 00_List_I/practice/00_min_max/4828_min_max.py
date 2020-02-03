import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    d = list(map(int,input().split())) 

    # max_num = max(d)
    # min_num = min(d)

    print('#{} {}'.format(tc,max(d) - min(d)))

