import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    d = [list(map(int,input())) for _ in range(N)]
    # print(d)
    result = 0
    x = N//2
    k = 1
    for i in range(N//2):
        result += sum(d[i][x:x+k])
        result +=sum(d[-i-1][x:x+k])
        k+=2
        x -=1
    result += sum(d[N//2])
    print('#{} {}'.format(tc, result))

# 50
# 5
# 14054
# 44250
# 02032
# 51204
# 52212





