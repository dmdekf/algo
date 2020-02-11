def p(num):
    while num:
        r = num % 10
        num = num // 10
        if r < num % 10:
            return False
    return True


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    d = list(map(int, input().split()))
    d = sorted(d)
    result = -1
    for i in range(N):
        for j in range(i + 1, N):
            x = d[i] * d[j]
            if result < x:
                if p(x):
                    result = x

    print('#{} {}'.format(tc, result))

