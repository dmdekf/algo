
import sys

sys.stdin = open('input_1248.txt')


def preorder(node):
    global cnt
    if node !=0:
        cnt +=1
        preorder(tree[node][0])
        preorder(tree[node][1])


T = int(input())

for tc in range(1, T+1):
    V, E, v1, v2 = map(int,input().split())
    d = list(map(int,input().split()))
    t = [[] for _ in range(V+1)]
    for i in range(1,E+1):
        t[d[i]].append(d[i+1])
        t[d[i+1]].append(d[i])
    # 인접 노드 l, r, p로 행렬로 저장하기.
    tree = [[0 for _ in range(3)] for _ in range(V+1)]
    for i in range(E):
        n1 = d[i*2]
        n2 = d[i*2+1]
        if not tree[n1][0]:
            #left
            tree[n1][0] = n2
        else:
            #right
            tree[n1][1] = n2
        #parent
        # 자기 부모가 0 인 요소가 root다.
        tree[n2][2] = n1
    cnt = 0
    visited = [0]+[0]*V

    p = 1
    # print(tree)
    while 1:
        if v1 != 1:
            p1 = tree[v1][2]
            if visited[p1]:
                p = p1
                break
            visited[p1] = 1
            v1 = p1
        if v2 !=1:
            p2 = tree[v2][2]
            if visited[p2]:
                p = p2
                break
            visited[p2] = 1
            v2 = p2
    # print(p)
    preorder(p)

    print(f'#{tc} {p} {cnt}')
