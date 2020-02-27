import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    V, E = map(int, input().split())
    G = list([] for _ in range(V+1))
    d = list(map(int, input().split()))
    visited = [None] + [0]*V
    # print(G)
    # print(d)
    for i in range(0, len(d), 2):
        G[d[i]].append(d[i+1])
        visited[d[i+1]] += 1
    print(visited)
    result = ''
    for i in range(1, V+1):
        stack = []
        stack.append(i)
        while stack:
            node = stack.pop()
            if visited[node] > 0:
                visited[node] -= 1
            elif visited[node] == 0:
                visited[node] = 'X'
                result += str(node) + ' '
                stack.extend(G[node])
    print(f'#{tc} {result}')

# for t in range(10):
#     v, e = map(int, input().split())
#     data = list(map(int, input().split()))
#     adj = [[] for i in range(v + 1)]
#     visit = [None] + [0] * v

#     for k in range(0, len(data), 2):
#         adj[data[k]].append(data[k + 1])
#         visit[data[k + 1]] += 1
#     # print(adj)    # [[], [2, 5], [3], [], [1], []]
#     # print(visit)  # [None, 1, 1, 1, 0, 1]

#     result = ''
#     for i in range(1, v+1):
#         stack = []
#         stack.append(i)
#         while stack:
#             node = stack.pop()
#             if visit[node] > 0:
#                 visit[node] -= 1
#             elif visit[node] == 0:
#                 visit[node] = 'X'
#                 result += str(node) + ' '
#                 stack.extend(adj[node])
#     print('#{} {}'.format(t+1, result))

# for t in range(10):
#     V, E = map(int, input().split())
#     e = list(map(int, input().split()))
#     dfs = [0 for i in range(1, V+1)]
#     visited = []
#     graph = [[] for i in range(V)]
#     s = set()
#     for i in range(0, len(e), 2):
#         graph[e[i]-1].append(e[i+1]) # [[2, 5], [3, 7], [], [1], [6], [], [6], [5, 9], []]
#         dfs[e[i+1]-1] += 1
#         s.update({e[i+1]})
#         stack = {i for i in range(1, V+1)}.difference(s)
#     stack = list(stack)
#     while stack:
#         node = stack.pop()
#         if dfs[node-1]:
#             dfs[node-1] -= 1
#         if dfs[node-1] == 0:
#             visited.append(node)
#             stack.extend(graph[node-1])
#     print('#{} {}'.format(t+1, ' '.join(list(map(str, visited)))))
