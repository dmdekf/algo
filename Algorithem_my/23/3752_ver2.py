
import sys

sys.stdin = open('3752_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    d = [0] + list(map(int, input().split()))
    res = [0 for _ in range(sum(d)+1)]
    v = [0]
    for n in d:
        temp = v[:]
        for i in temp:
            if not res[i+n]:
                res[i+n] = 1
                v.append(i+n)
    print(f'#{tc} {sum(res)}')
