from _collections import deque


def node(s):
    q.append(s)
    v[s] = 1
    while q:
        f = q.popleft()
        for i in d[f]:
            if v[i] == 0:
                v[i] = v[f]+1
                if E in d[f]:
                    return v[f]
                q.append(i)

    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    d = [[] for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, input().split())
        d[i].append(j)
        d[j].append(i)
    S, E = map(int, input().split())
    q = deque()
    v = [0 for _ in range(V+1)]
    print(f'#{tc} {node(S)}')
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
