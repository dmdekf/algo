
import sys
sys.stdin = open('6485_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    line = list(list(map(int, input().split())) for _ in range(N))

    P = int(input())
    stop = []

    for _ in range(P):
        stop += [[int(input()), 0]]
    print(stop)
    for a, b in line:
        for i in stop:
            if a <= i[0] <= b:
                i[1] += 1

    print(f'#{tc}', end='')
    for i in range(P):
        print(f' {stop[i][1]}', end='')
