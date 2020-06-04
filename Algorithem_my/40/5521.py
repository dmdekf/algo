import sys
from collections import deque
sys.stdin = open('input_5521.txt')


def dfs(v):
    visited[v] = 1
    print(v, end=" ")
    for w in range(1, N+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)


def bfs(v):
    global cnt
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1
                if visited[w] == 2 or visited[w] == 3:
                    cnt += 1
    return cnt


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    visited = [0] * (N+1)
    # dfs(1)
    cnt = 0

    print(f'#{tc} {bfs(1)}')
