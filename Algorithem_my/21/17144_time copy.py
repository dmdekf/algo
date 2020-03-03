import sys
sys.stdin = open('17144_input.txt')
R, C, T = map(int, sys.stdin.readline().strip().split())
d = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(R)]

rc = [(0, 1), (-1, 0), (0, -1), (1, 0)]

a = []
for i in range(R):
    if d[i][0] == -1:
        a += [i]
a1 = a[0]
a2 = a[1]

def mixa():
    global d
    temp = list([0] * C for _ in range(R))
    for i in range(R):
        for j in range(C):
            if d[i][j] > 4:
                v = d[i][j] // 5
                for r, c in rc:
                    if 0 <= i + r < R and 0 <= j + c < C and d[i + r][j + c] >= 0:
                        temp[i + r][j + c] += v
                        d[i][j] -= v
    for i in range(R):
        for j in range(C):
            d[i][j] += temp[i][j]
def air():
    for i in range(a1-2, -1, -1):
        d[i+1][0] = d[i][0]
    for i in range(C-1):
        d[0][i] = d[0][i+1]
    for i in range(a1):
        d[i][C-1] = d[i+1][C-1]
    for i in range(C-2, -1, -1):
        d[a1][i+1] = d[a1][i]
    d[a1][1] = 0
    for i in range(a2+1, R-1):
        d[i][0] = d[i+1][0]
    for i in range(C-1):
        d[R-1][i] = d[R-1][i+1]
    for i in range(R-2, a2-1, -1):
        d[i+1][C-1] = d[i][C-1]
    for i in range(C-2, -1, -1):
        d[a2][i+1] = d[a2][i]
    d[a2][1] = 0
def result():
    for _ in range(T):
        mixa()
        air()
    print(sum(map(sum,d))+2)

result()




