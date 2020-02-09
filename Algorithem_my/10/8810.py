import sys

sys.stdin = open('input_8810.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    d = list(map(int, input().split()))
    d.append(0)
    longd = []
    cnt = 0
    sumd = 0
    for i in range(N):
        if d[i] < d[i + 1]:
            sumd += d[i]
            cnt += 1
            i += 1
        else:
            sumd += d[i]
            cnt += 1
            if sumd != d[i]:
                longd.append((cnt, sumd))
            cnt = 0
            sumd = 0
    result = (0, 0)
    for i in range(len(longd)):
        if result < longd[i]:
            result = longd[i]

    print('#{} {} {}'.format(tc, len(longd), result[1]))
