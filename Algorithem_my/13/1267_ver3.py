T = int(10)
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge_list = list(map(int, input().split()))
    d = [[edge_list[2*idx], edge_list[2*idx+1]] for idx in range(E)]
    pre = [[] for _ in range(V+1)]

    for edge in d:
        pre[edge[1]] += [edge[0]]

    vertice = list(set(edge_list))
    vertice = list(range(1, V+1))
    del_list = []
    while vertice != []:
        for v in vertice:
            if len(pre[v]) == 0:
                for x in pre:
                    if v in x:
                        x.remove(v)
                del_list.append(v)
                vertice.remove(v)
    print('#{} '.format(tc), end="")
    print(*del_list)
