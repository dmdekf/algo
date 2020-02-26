
import sys
sys.stdin = open('6485_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    line = list(list(map(int, input().split())) for _ in range(N))

    P = int(input())
    stop = [0]*P
    dic = {}
    for i in range(P):
        stop[i] = int(input())
        dic[stop[i]] = 0
    print(f'stop:{stop}, Ai,Bi:{line}')
    print(dic)

    for i in range(N):
        for j in range(line[i][1] - line[i][0]+1):
            dic[line[i][0]+j] += 1

    print(f'#{tc}', end='')
    for i in range(P):
        print(f' {dic[stop[i]]}', end='')
