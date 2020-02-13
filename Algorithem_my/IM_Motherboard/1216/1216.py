import sys
sys.stdin = open('input.txt')
def palin(x):
    if x == x[::-1]:
        return True
    else:
        return False


T = 10
for tc in range(1, T+1):
    c = 100
    n = int(input())
    d = [list(input()) for _ in range(c)]

    cold = []
    for i in range(100):
        col = ''
        for j in range(100):
            col += d[j][i]
        cold.append(col)
    result = 1
    num = 101
    while num >= 1 and result == 1:
        num -= 1
        for i in range(100):
            for j in range(100-num+1):
                if palin(d[i][j:j+num]):
                    result = 0
                if palin(cold[i][j:j+num]):
                    result = 0
        

    print('#{} {}'.format(tc, num))




