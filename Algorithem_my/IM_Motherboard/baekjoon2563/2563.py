import sys
sys.stdin = open('input.txt')

N = int(input())
d = list([0]*100 for _ in range(100))
cnt = 0
for x in range(N):
    r, c = map(int,input().split())
    # print(r,c)
    for i in range(r, r+10):
        for j in range(c, c+10):
            if d[i][j] != 0:
                cnt +=1
            else:
                d[i][j] = 1
N*100 - cnt
print(N*100 - cnt)







