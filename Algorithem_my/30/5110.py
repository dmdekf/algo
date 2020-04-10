import sys

sys.stdin = open('input_5110.txt')


T = int(input())
# T = 1
for tc in range(1, T+1):
    N, M = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(M)]
    newd = d[0]
    print(newd[0], d[1][0])
    for i in range(1, M):
        print(newd)
        print(newd[0], d[i][0])
        if newd[0] > d[i][0]:
            newd.insert(0, d[i])
        else:
            j = 1
            while newd[j] < d[i][0] and j < len(newd):
                j += 1
            j += 1
            for k in range(M):
                newd.insert(j, d[i][k])
                j += 1

    print(f'#{tc} {newd[::-1][10]}')
