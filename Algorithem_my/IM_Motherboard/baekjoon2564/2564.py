import sys
sys.stdin = open('input.txt')

R,C = map(int(input()))
N = int(input())
d = [list(map(int,input().split()))for _ in range(N)]
default, dong = map(int, input().split())
dr, dc = 0, 0
if default ==1 :
    dr = 0, dc = dong
if default ==2 :
    dr = R, dc = dong
if default ==3 :
    dr = dong, dc = 0
if default ==4 :
    dr = dong, dc = C

total = (R+C)*2
result = 0
nr, nc = 0,0
for i in range(N):
    if d[i][0]==1:
        nr = 0, nc = d[i][1]
        if nr == dr:
            result +=abs(nc-dc)
        else:
            if C - (nc + dc)>0:
                result +=nc + dc +R
            else:
                result +=C*2-(nc+dc) +R
    if d[i][0] == 2:
        nr = R, nc = d[i][1]
        if nr == dr:
            result += abs(nc - dc)
        else:
            if C - (nc + dc) > 0:
                result += nc + dc + (R-dr)
            else:
                result += C * 2 - (nc + dc) + (R-dr)
    if d[i][0] == 3:
        nc = 0, nr = d[i][1]
        if nc == dc:
            result += abs(nr - dr)
        else:
            if R - (nr + dr) > 0:
                result += nr + dr + C
            else:
                result += R * 2 - nr + dr + C
    if d[i][0] == 4:
        nc = 0, nr = d[i][1]
        if nc == dc:
            result += abs(nr - dr)
        else:
            if R - (nr + dr) > 0:
                result += nr + dr + C
            else:
                result += R * 2 - nr + dr + C
        abs(nr - dr)
    print(result)






