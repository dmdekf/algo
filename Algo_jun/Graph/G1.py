def dfs1(n, V):
    visited[n] = 1
    print(n, end = ' ')
    for i in range(1, V+1): #다른 노드 i에 대해
        if adj[n][i] and visited[i]==0:  #인접노드이고, 방문하지 않았다면
            dfs1(i, V)  #i노드로 이동

def dfs2(n,V):
    s = []
    s.append(n) #시작점
    visited[n] = 1
    while s: #인접노드가 남아있을때까지 갈 수 있는 목록을 저장하는 방식.
        n = s.pop()
        print(n, end = ' ')
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited[i] == 0:
                s.append(i)
                visited[i] = 1

V, E = 5, 6 #map(int, input().split())
edge = [1,2,1,3,2,5,5,4,3,2,3,4] #list(map(int,input().split()))
adj = [[0]*(V+1) for _ in range(V+1)]
visited = [0]*(V+1)

for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2+1]
    adj[n1][n2] = 1
    # adj[n2][n1] = 1 #무방향그래프일 경우에만 추가하기. ex)친구관계... 화살표가 없는경우


# dfs1(1, V)

dfs2(1,V)