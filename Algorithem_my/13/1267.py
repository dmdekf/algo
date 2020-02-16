import sys


def dfs(graph, v):
    visit = list()
    needvisit = list()
    needvisit.append(v)
    while needvisit:
        node = needvisit.pop(0)
        if node not in visit:
            visit.append(node)
            needvisit.extend(graph[node])
    return visit


sys.stdin = open('input.txt')

for tc in range(1, 4):
    N, M = map(int, input().split())
    d = list(map(int, input().split()))
    G = list([] for _ in range(max(d)+1))
    for i in range(0, M*2, 2):
        G[i].append(d[i+1])
    print(G)
