import sys

sys.stdin = open('input_8706.txt')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    d = list(map(int, input().split()))
    d.insert(0,0)
    cnt = 0
    for i in range(1, N+1):
        while d[i]> M:
            d[i] -=M
            cnt +=i
        if d[i] < M and i!=N:
            d[i+1] +=d[i]
            d[i]=0
        elif d[i] < M and i ==N:
            cnt +=i
    print(cnt)




