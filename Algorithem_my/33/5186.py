import sys

sys.stdin = open('input_5186.txt')


def f(num):
    result = []
    while num:
        if len(result) > 12:
            return 'overflow'
        temp = num*2
        print(temp)
        if temp - 1 >= 0:
            result.append(1)
            num = num*2 - 1
        else:
            result.append(0)
            num = num*2

    return ''.join(list(map(str, result)))


T = int(input())

for tc in range(1, T+1):
    N = float(input())
    print(f'#{tc} {f(N)}')
