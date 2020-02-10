import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    d = list(map(int,input().split()))

    for _ in range(N):
        d= sorted(d)
        d[-1] -=1
        d[0] +=1
    print(tc, max(d)-min(d))
