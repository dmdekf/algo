import sys

sys.stdin = open('input.txt')

n = int(input())
default = list(map(int,input().split()))
pn = int(input())
d = [list(map(int, input().split())) for _ in range(pn)]
# print(d)
# print(pn)
for i in range(pn):
    # print(default)
    #남자일때
    if d[i][0] == 1:
        for j in range(d[i][1]-1,n,d[i][1]):
            if default[j]:
                default[j] = 0
            else:
                default[j] = 1
        # print(default)
    #여자일때
    else:
        result = True
        x = 0
        while result:
            # print(default)
        # while True:
            if -1< d[i][1]-1-x < n and -1< d[i][1]-1+x < n:
                if default[d[i][1]-1-x] == default[d[i][1]-1+x]:
                    if default [d[i][1]-1-x]:
                        default[d[i][1]-1+x] = 0
                        default[d[i][1]-1-x] = 0
                    else:
                        default[d[i][1]-1+x] = 1
                        default [d[i][1]-1-x] = 1
                else:
                    result = False
            else:
                result = False
            x+=1
x = 0       
while x < len(default):
    print(*default[x:x+20])
    x += 20

    # 0 1 2 3 4 5
    # 6 7 8 9 10 11

        

            
