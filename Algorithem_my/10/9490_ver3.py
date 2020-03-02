import sys
sys.stdin = open('input_9490.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(N)]
    m = 0
    for i in range(N):
        for j in range(M):
            ssum = -d[i][j]
            for k in range(-d[i][j], d[i][j]+1):
                if i+k in range(N):
                    ssum += d[i+k][j]
                if j+k in range(M):
                    ssum += d[i][j+k]
            if m < ssum:
                m = ssum
    print(m)
