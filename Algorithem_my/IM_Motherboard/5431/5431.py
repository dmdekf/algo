import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    d = list(map(int, input().split()))
    result = []
    for i in range(1, N+1):
        if i not in d:
            result.append(i)
    print('#{} '.format(tc), end = '')
    print(*result)

#
#
# 2
# 5 3
# 2 5 3