import sys
sys.stdin = open('input.txt')
T = 10
for tc in range(1, T+1):
    tc = int(input())
    d = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if d[99][i] == 2:
            x = i
    result = 0
    r = 99
    if d[r][x]:
        while r !=0:
            if x !=99 and d[r][x+1]:
                while x <99 and d[r][x+1]:
                    x +=1
            elif x !=0 and d[r][x-1]:
                while x >0 and d[r][x-1]:
                    x -=1
            r -= 1
        result = x

    print('#{} {}'.format(tc,result))
