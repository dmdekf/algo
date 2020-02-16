import sys

sys.stdin = open('input.txt')


for tc in range(1, 4):
    V, E = map(int, input().split())
    G = list([] for _ in range(V+1))
    d = list(map(int, input().split()))
    dfs = [0 for _ in range(V+1)]
    visited = []
    s = set()
    # print(G)
    # print(d)
    for i in range(0, len(d), 2):
        G[d[i]].append(d[i+1])
        dfs[d[i+1]-1] += 1

        s.update({d[i+1]})
        stack = {i for i in range(1, V+1)}.difference(s)
    print(dfs)
    stack = list(stack)
    print(G, s, stack)
    # for i in range(0, len(e), 2):
    #     graph[e[i]-1].append(e[i+1]) # [[2, 5], [3, 7], [], [1], [6], [], [6], [5, 9], []]
    #     dfs[e[i+1]-1] += 1
    #     s.update({e[i+1]})
    #     stack = {i for i in range(1, V+1)}.difference(s)
    # stack = list(stack)
    # while stack:
    #     node = stack.pop()
    #     if dfs[node-1]:
    #         dfs[node-1] -= 1
    #     if dfs[node-1] == 0:
    #         visited.append(node)
    #         stack.extend(graph[node-1])
    # print('#{} {}'.format(t+1, ' '.join(list(map(str, visited)))))
