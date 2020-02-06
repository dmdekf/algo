import sys

sys.stdin = open('input copy.txt')


T = 10
for _ in range(T):
    tx = int(input())
    d = [list(map(int, input().split())) for _ in range(100)]

    result = 1000
    cnt = 1000000
    # 각 사다리 점검하기.
    for i in range(99, -1, -1):
        c = i
        r = 0
        temp = 0

        if d[r][c]:
            while r != 99:
                if c != 99 and d[r][c+1]:
                    while c < 99 and d[r][c+1]:
                        temp += 1
                        c += 1
                elif c != 0 and d[r][c-1]:
                    while c > 0 and d[r][c-1]:
                        temp += 1
                        c -= 1
                r = r+1
                temp += 1
            if cnt > temp:
                cnt = temp
                result = i

    print('#{} {} {}'.format(tx, result, cnt))
