import sys

sys.stdin = open('input_5174.txt')


def f(N):
    global cnt
    cnt += 1
    if not tree[N]:
        return
    else:
        for i in tree[N]:
            f(i)


T = int(input())
# T = 1
for tc in range(1, T+1):
    E, N = map(int, input().split())
    tree = [[] for _ in range(E+2)]
    d = list(map(int, input().split()))
    for i in range(0, len(d), 2):
        tree[d[i]].append(d[i+1])
    cnt = 0
    f(N)
    print(f'#{tc} {cnt}')
