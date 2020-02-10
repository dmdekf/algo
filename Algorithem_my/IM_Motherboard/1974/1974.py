import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    d = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    for i in range(9):
        if sum(d[i]) != 45:
            result = 0
    for j in range(9):
        temp = 0
        for i in range(9):
            temp += d[i][j]
        if temp != 45:
            result = 0
    if result == 0:
        print('#{} {}'.format(tc,result))
        continue
    else:
        for i in range(0,9,3):
            for j in range(0,9,3):
                temp = 0
                for k in range(3):
                    for l in range(3):
                        temp+=d[i+k][j+l]
                if temp != 45:
                    result = 0

    print('#{} {}'.format(tc, result))



