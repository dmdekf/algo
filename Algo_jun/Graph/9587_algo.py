
def dfs2(n, V, t):
    if n == t: #목적지에 방문한 경우
        return 1
    else:
        visited[n] = 1
         # 인접노드가 남아있을때까지 갈 수 있는 목록을 저장하는 방식.
        for i in range(1, V + 1):
            if adj[n][i] == 1 and visited[i] == 0:
                if dfs2(i, V, t) == 1:
                    return 1
        return 0
import sys
sys.stdin = open('9587_input.txt')

T = int(input())

for tc in range(1,T+1):

    V, E = map(int,input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        f,e = map(int,input().split())
        adj[f][e] = 1

    x, y = map(int, input().split())

    print('#{} {}'.format(tc, dfs2(x, V, y)))
