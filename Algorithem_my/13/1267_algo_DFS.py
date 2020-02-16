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
