
import sys

sys.stdin = open('3752_input.txt')


def f(d):
    r = {0}
    for i in d:
        for j in list(r):
            r.add(i+j)
    return len(r)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    d = list(map(int, input().split()))
    print(f'#{tc} {f(d)}')

    # dp = {0}
    # for s in d:
    #     temp = set()
    #     for n in dp:
    #         temp.add(s+n)
    #     dp.update(temp)
    # print(len(dp))
