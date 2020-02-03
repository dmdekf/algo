import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    n = int(input())
    d = list(map(int,input().split())) 
    #data
    for c in range(n):
        '''  매 반복 시 sorted가 필요하다. => import hipq(log(n)으로 bigO를 해결.)를 이용하면 간단히 해결.'''
        d.sort()
        d[-1] -= 1
        d[0] += 1

    print('#{} {}'.format(tc, max(d)-min(d)))

