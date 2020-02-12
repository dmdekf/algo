import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            d[i][j]= int(d[i][j])
    sumd = 0
    x = N//2
    y = 1
    for i in range(N//2):
        sumd +=sum(d[i][x:x+y])
        sumd += sum(d[-i-1][x:x + y])
        x-=1
        y+=2
    sumd += sum(d[N//2])
    print('#{} {}'.format(tc,sumd))
# 50
# 5
# 14054
# 44250
# 02032
# 51204
# 52212



