import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    d = [list(input()) for _ in range(5)]
    # print(d)
    default = [['!']*15 for _ in range(5)]
    # print(d)
    # print(default)
    for i in range(len(d)):
        for j in range(len(d[i])):
            default[i][j] = d[i][j]
    result = ''
    for j in range(15):
        for i in range(5):
            result += default[i][j]
    print('#{} {}'.format(tc, result.replace('!','')))
