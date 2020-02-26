T = int(input())

for tc in range(1, T+1):
    N = int(input())

    line = list(list(map(int, input().split())) for _ in range(N))

    P = int(input())
    stop = []

    for i in range(P):
        stop += [[int(input()), 0]]

    for a, b in line:
        for i in stop:
            if a <= i[0] <= b:
                i[1] += 1

    result = [i[1] for i in stop]
    print(f'#{tc} ', end='')
    print(*result)
