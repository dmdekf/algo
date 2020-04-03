for t in range(int(input())):
    V, E = map(int, input().split())
    d = []
    for e in range(E):
        d.append(list(map(int, input().split())))
    S, E = map(int, input().split())

    visit = []
    inno = [[] for _ in range(V + 1)]

    for i in range(E):
        inno[d[i][0]].append(d[i][1])
        inno[d[i][1]].append(d[i][0])

    cnt = 0
    queue = [S, -1]
    while queue:
        node = queue.pop(0)
        if node == E:
            break
        if node not in visit and node != -1:
            visit.append(node)
            queue.extend(inno[node])
        elif node == -1:
            queue.append(node)
            cnt += 1
            if queue[0] == -1:
                cnt = 0
                break

    print('#{} {}'.format(t + 1, cnt))
