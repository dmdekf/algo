import sys
sys.stdin = open('input_9490.txt')

dr = [-1,1,0,0]
dc = [0,0,-1,1]

T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(n)]
    maxsum = 0
    for i in range(n):
        for j in range(m):
            ssum = d[i][j]
            for c in range(1, ssum+1):
                for k in range(4):
                    nr = dr[k]*c
                    nc = dc[k]*c
                    if nr < 0 or nc < 0 or nr >= n or nc >= m :          continue
                    ssum +=d[nr][nc]
            if maxsum < ssum:
                maxsum = ssum
    print(maxsum)
