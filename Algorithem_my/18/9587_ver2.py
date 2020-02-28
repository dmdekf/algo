def dfs(S, G):
    visited[S] = 1
    for i in range(1, V + 1):
        if adj[S][i] == 1 and visited[i] == 0:
            visited[i] == 1
            if visited[G] == 1:
                break
            dfs(i, G)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        u, v = map(int, input().split())
        adj[u][v] = 1

    S, G = map(int, input().split())
    dfs(S, G)
    print('#{} {}'.format(tc, visited[G]))