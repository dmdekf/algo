import sys

sys.stdin = open('input.txt')

T = 10
for _ in range(T):
    c = 100
    tc = input()
    d = [list(map(int, input().split())) for _ in range(c)]
    # print(d)
    #max_sum
    m = 0

    for i in range(c):
        #sum
        s = 0
        for j in range(c):
            s+= d[i][j]
        if s > m:
            m = s

    for i in range(c):
        s = 0
        for j in range(c):
            s +=d[j][i]
        if s > m:
            m = s
    s = 0
    for i in range(c):
        s += d[i][i]
    if s > m:
            m = s
    s = 0
    for i in range(c):
        s += d[i][c-(1+i)]
    if s > m:
            m = s
    print(m)
