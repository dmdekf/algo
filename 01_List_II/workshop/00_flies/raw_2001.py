import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T +1):
    N, M = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(N)]
    # d = [[map(int, input().split()] for _ in range(N))]
    max_kill = 0
    for i in range(N - M +1):
        for j in range(N - M + 1):
            s = 0
            
            for k in range(M):
                for l in range(M):
                    s+= d[i+k][j+l]
                
            if s > max_kill:
                max_kill = s

    print('#{} {}'.format(tc, max_kill))