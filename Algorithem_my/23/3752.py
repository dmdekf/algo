
import sys

sys.stdin = open('3752_input.txt')


def f(i, score):
    if i == N+1:
        r.add(score)
    else:
        f(i+1, score+d[i])
        f(i+1, score)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    d = [0] + list(map(int, input().split()))
    r = set()
    f(0, 0)
    print(f'#{tc} {len(r)}')
