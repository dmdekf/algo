def dfs(k, now, dis):
    global res
    if dis > res:
        return
    if k == N:
        dis += dist[now][N+1]
        res = dis if dis < res else res
        return
    for w in range(1, N+1):
        if not v[w]:
            v[w] = 1
            dfs(k+1, w, dis + dist[now][w])
            v[w] = 0


T = int(input())
# T = 1
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    p = [(arr[2*i], arr[2*i+1])for i in range(N+2)]  # position => 회사0 집1 고객
    p.append(p.pop(1))  # 회사0 고객1~N 집N+1
    dist = [[abs(p[i][0]-p[j][0])+abs(p[i][1]-p[j][1])
             for j in range(N+2)] for i in range(N+2)]
    INF = float('inf')
    res = INF
    v = [0] * (N+1)
    dfs(0, 0, 0)
    print(f'#{tc} {res}')
