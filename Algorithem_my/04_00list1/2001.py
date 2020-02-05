T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            temp = 0
            for r in range(M):
                for c in range(M):
                    temp += d[i+r][j+c]
            if temp > max_sum:
                max_sum = temp
    print('#{} {}'.format(tc, max_sum))
