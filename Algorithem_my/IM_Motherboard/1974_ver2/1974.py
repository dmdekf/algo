import sys
sys.stdin = open('input.txt')

def c(num):
    for i in range(9):
        d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if num[i][j] in d:
                d.remove(num[i][j])
        if d:
            return 0
    for j in range(9):
        d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(9):
            if num[i][j] in d:
                d.remove(num[i][j])
        if d:
            return 0
    for i in range(0,9,3):
        for j in range(0, 9, 3):
            d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for k in range(3):
                for l in range(3):
                    if num[i+k][j+l] in d:
                        d.remove(num[i+k][j+l])
            if d:
                return 0
    return 1


T = int(input())

for tc in range(1, T+1):
    d = [list(map(int,input().split())) for _ in range(9)]
    print('#{} {}'.format(tc, c(d)))





