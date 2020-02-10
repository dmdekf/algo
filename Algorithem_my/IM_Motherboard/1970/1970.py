import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = [0] * 8
    dd = [
        50000,
        10000,
        5000,
        1000,
        500,
        100,
        50,
        10]
    for i in range(len(dd)):
        result[i] = N // dd[i]
        N = N % dd[i]
    print('#{}'.format(tc))
    print(*result)

