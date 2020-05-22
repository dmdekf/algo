import heapq
import sys

sys.stdin = open('input_5249.txt')


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = {i: [] for i in range(V+1)}
    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1].append([n2, w])
        adj[n2].append([n1, w])
    mst = [0]*(V+1)
    cost = [float('inf')] * (V + 1)
    # 시작노드
    mst[0] = 1
    q = []
    heapq.heappush(q, (0, 0))
    while q:
        temp, node = heapq.heappop(q)
        mst[node] = 1
        for i, val in adj[node]:
            if not mst[i] and cost[i] > val:
                cost[i] = val
                heapq.heappush(q, (val, i))
    print(f'#{tc} {sum(cost[1::])}')
