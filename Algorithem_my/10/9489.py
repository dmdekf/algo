# 3
# 3 3
# 0 1 0
# 0 1 0
# 0 1 0
import sys
sys.stdin = open('input_9489.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    d = [list(map(int,input().split())) for _ in range(N)]

    maxd = 0
    for i in range(N):
        temp = 0
        for j in range(M):
            if d[i][j] == 1:
                temp +=1
            else:
                if temp > maxd:
                    maxd = temp
                temp = 0

    for j in range(M):
        tempt = 0
        for i in range(N):
            if d[i][j] == 1:
                temp +=1
            else:
                if temp > maxd:
                    maxd = temp
                temp = 0
    if maxd < 2:
        maxd = 0

    print('#{} {}'.format(tc,maxd))
