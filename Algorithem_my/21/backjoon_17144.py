import sys
sys.stdin = open('17144_input.txt')

R, C, T = map(int, sys.stdin.readline().strip().split())
d = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(R)]

a = []
for i in range(R):
    if d[i][0] == -1:
        a += [i]
a1 = a[0]
a2 = a[1]

rc = [(-1, 0), (0, 1), (1, 0), (-1, 0)]
up = [0,1,2,3]
down = [2,1,3,0]
result = 0
while T:
    T -= 1
    temp = list([0] * C for _ in range(R))
    for i in range(R):
        for j in range(C):
            if d[i][j] > 4:
                v = d[i][j]//5
                for r, c in rc:
                    if 0 <= i+r < R and 0 <= j+c < C and d[i+r][j+c] >= 0:
                        temp[i+r][j+c] += v
                        d[i][j] -= v
    for i in range(R):
        for j in range(C):
            d[i][j] += temp[i][j]
    y = a1-1
    x = 0
    for i in up:
        while 1:
            ry = y + rc[i][0]
            rx = x + rc[i][1]
            if ry == a1 and rx == 0:
                break
            if not(0<=ry<R and 0 <= rx < C):
                break
            d[y][x]= d[ry][rx]
            y = ry
            x = rx
    d[a1][1] = 0
    y = a2+1
    x = 0

    for i in down:
        while 1:
            ry = y + rc[i][0]
            rx = x + rc[i][1]
            if ry == a2 and rx == 0:
                break
            if not (0 <= ry < R and 0 <= rx < C):
                break
            d[y][x] = d[ry][rx]
            y = ry
            x = rx
    d[a2][1] = 0
    for i in range(R):
        print(d[i])
    for i in range(R):
        for j in range(C):
            if d[i][j] > 0:
                result += d[i][j]

print(result)





