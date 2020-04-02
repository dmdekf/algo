
import sys

sys.stdin = open('input_5099.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    d = list(map(int, input().split()))
    q = []
    for i in range(M):
        d[i] = [i+1, d[i]]
    for i in range(N):
        q.append(d.pop(0))

    while len(q) > 1:
        temp = q.pop(0)
        temp[1] = temp[1]//2
        if temp[1] != 0:
            q.append(temp)
        else:
            if d:
                q.append(d.pop(0))

    print(f'{tc} {q[0][0]}')
