import sys

sys.stdin = open('input_5178.txt')


def f(node):
    global N
    if node > N:
        return 0
    else:
        if tree[node]:
            return tree[node]
        else:
            a = f(2*node)
            b = f(2*node + 1)
            tree[node] = a + b
        return tree[node]


T = int(input())
# T = 1
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]
    for _ in range(M):
        i, j = map(int, input().split())
        tree[i] = j
    cnt = 0
    f(1)
    print(f'#{tc} {tree[L]}')
