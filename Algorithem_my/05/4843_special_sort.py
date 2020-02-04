import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = list(map(int, input().split()))
    for i in range(N-1):
        for j in range(i, N):
            if d[i]>d[j]:
                d[i] , d[j] = d[j] ,d[i]
    result = []
    for i in range(N//2):
        result.append(d[-1-i])
        result.append(d[i])

    # result = print(*result)
    
    print('#{}'.format(tc),end=' ')
    print(*result[:10])