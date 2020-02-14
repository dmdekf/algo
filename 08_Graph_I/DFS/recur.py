def DFS(v):
    visited[v] = 1
    print(v, end=' ')

    for w in G[v]:
        if not visited[w]:
            DFS(w)


import sys
sys.stdin = open('input.txt')

V , E = map(int, input().split())

G = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
print('G', G)
print('visited', visited)
print(DFS(1))