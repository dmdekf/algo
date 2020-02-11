import sys
sys.stdin = open('input.txt')

d = list([1000]*100 for _ in range(100))
n = int(input())
cnt = 0
for _ in range(n):
    r,c,r1,c1 = map(int,input().split())
    for i in range(r, r+r1):
        for j in range(c, c+c1):
            d[i][j]=cnt
    cnt +=1
x = 0
result = []
for k in range(n):
    y = 0
    for i in range(100):
        for j in range(100):
            if d[i][j] == k:
                y +=1
    result.append(y)
for i in result:
    print(i)














