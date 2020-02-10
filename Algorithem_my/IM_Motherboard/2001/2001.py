import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(N)]
    maxsum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(M):
                for l in range(M):
                    temp += d[i+k][j+l]
            if maxsum < temp:
                maxsum = temp
    print('#{} {}'.format(tc,maxsum))

