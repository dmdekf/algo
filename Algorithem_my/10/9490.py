#1 10
#2 26
#3 40
import sys
sys.stdin = open('input_9490.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    d = [list(map(int, input().split())) for _ in range(N)]
    cold = [[0]*N for _ in range(M)]
    for i in range(N):
        for j in range(M):
            cold[j][i] =d[i][j]

    result = 0
    for i in range(N):
        temp = 0
        for j in range(M):
            dnum=d[i][j]
            x = j-dnum
            y = j+dnum+1
            ix = i - dnum
            iy = i + dnum + 1
            if j-dnum < 0 :
                x =0
            if j+dnum+1 > M:
                y = M
            if i-dnum < 0 :
                ix =0
            if i+dnum+1 > N:
                iy = N
            temp = sum(d[i][x:y]) + sum(cold[j][ix:iy])-dnum
            if temp > result:
                result = temp
            else:
                result
    print('#{} {}'.format(tc, result))
