import sys
  result = ''
   for i in range(1, v+1):
        stack = []
        stack.append(i)
        while stack:
            node = stack.pop()
            if visit[node] > 0:
                visit[node] -= 1
            elif visit[node] == 0:
                visit[node] = 'X'
                result += str(node) + ' '
                stack.extend(adj[node])
    print('#{} {}'.format(t+1, result))


def DFS(s):
    p = 1
    for i in rev[s]:
        if visited[i] == 0:
            p = 0
    if p == 1:
        if visited[s] == 0:
            visited[s] = 1
            print('', s, end='')
        for i in D[s]:
            DFS(i)


def f(n):
    if not V[n]:
        print(n, end=' ')
        return
    else:
        if V[n]:
            V[n] -= 1
        for i in G[n]:
            f(i)


sys.stdin = open('input.txt')
for tc in range(1, 4):
    N, M = map(int, input().split())
    d = list(map(int, input().split()))
    G = [[] for _ in range(N+1)]
    V = [0]*(N+1)
    r = [i for i in range(1, N+1)]
    # list(range(1, V+1))
    print(d)
    print(G, V)
    for i in range(0, len(d), 2):
        G[d[i]].append(d[i+1])
        V[d[i+1]] += 1
        r.remove(d[i+1])
    print(G, V, r)
    for i in r:
        f(i)
