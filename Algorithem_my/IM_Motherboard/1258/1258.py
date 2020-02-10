import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(i,N):
                for l in range(j,N):
                    while d[i][j] != 0:

