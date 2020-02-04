import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    default = [[0]*10 for _ in range(10)]
    N = int(input())
    d = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        if d[i][4] == 1:
            for x in range(d[i][2]-d[i][0]+1): # 0,2 -0, 0
                for y in range(d[i][3]-d[i][1]+1): # 0,3 - 0,1
                    default[d[i][0]+x][d[i][1]+y] +=1 # 0,0 + 0 0,1 + 0
                # 01 01
                # 2 2

        else:
            for x in range(d[i][2]-d[i][0]+1):
                for y in range(d[i][3]-d[i][1]+1):
                    default[d[i][0]+x][d[i][1]+y] +=2
    s = 0
    for i in range(10):
        for j in range(10):
            if default[i][j] == 3:
                s +=1
            
    # print(default)
    print('#{} {}'.format(tc, s))
