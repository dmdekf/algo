import sys
from _collections import deque


def node(s):
    q.append(s)
    v[s] = 1
    while q:
        f = q.popleft()
        if E in d[f]:
            return v[f]
        for i in d[f]:
            if v[i] == 0:
                v[i] = v[f] + 1
                q.append(i)

    return 0


sys.stdin = open('input_5102.txt')


T = int(input())
# T = 1
for tc in range(1, T+1):
    V, E = map(int, input().split())
    d = [[] for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, input().split())
        d[i].append(j)
        d[j].append(i)
    S, E = map(int, input().split())
    q = deque()
    v = [0 for _ in range(V+1)]
    print(f'#{tc} {node(S)}')
