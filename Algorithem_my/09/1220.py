import sys

sys.stdin = open('input_1220.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    d = [list(map(int, input().split())) for _ in range(100)]
    # print(len(d))
    cnt = 0
    for j in range(100):
        for i in range(100):
            if i != 99 and d[i][j] == 1:
                while i != 99 and d[i+1][j] == 0:
                    d[i+1][j] = d[i][j]
                    d[i][j] = 0
                    i += 1
                if i != 99  and d[i+1][j] + d[i][j] == 3:
                    cnt += 1
                    d[i+1][j], d[i][j] = 4, 4
    print('#{} {}'.format(tc, cnt))