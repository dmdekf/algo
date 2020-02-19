import sys


def DFS(v):
    visited[v] = 1
    print(v, end=' ')

    for w in G[v]: #다른 노드 w에 대해 인접하고
        if not visited[w]:  # 방문하지 않았으면
            DFS(w)


sys.stdin = open('input.txt')

V, E = map(int, input().split())

G = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
print('G', G)
print('visited', visited)
print(DFS(1))
