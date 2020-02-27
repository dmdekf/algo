def dfs(n, V, y):
    s = []
    s.append(n)
    visited[n] = 1
    while s:
        n = s.pop()
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited[i] == 0:
                s.append(i)
                visited[i] = 1

    if visited[y] == 1:
        return 1
    else:
        return 0


T = int(input())

for tc in range(1, T+1):

    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        f, e = map(int, input().split())
        adj[f][e] = 1

    x, y = map(int, input().split())

    print('#{} {}'.format(tc, dfs(x, V, y)))
