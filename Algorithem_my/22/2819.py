
import sys

sys.stdin = open('2819_input.txt')


def f(i, j, n, s):
    if n == 7:
        result.add(s)
        return
    else:
        for r, c in rc:
            if 0 <= i+r < 4 and 0 <= j+c < 4:
                f(i+r, j+c, n+1, s+d[i][j])


T = int(input())
for tc in range(1, T+1):
    d = [list(map(str, input().split())) for _ in range(4)]
    rc = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    result = set()
    for i in range(4):
        for j in range(4):
            temp = ''
            f(i, j, 0, temp)
    print(len(result))
