d = list([0]*100 for _ in range(100))
cnt = 0
for _ in range(4):
    r1, c1, r2, c2 = map(int, input().split())
    for i in range(r1,r2):
        for j in range(c1,c2):
            if d[i][j]==0:
                d[i][j]=1
                cnt +=1

print(cnt)






