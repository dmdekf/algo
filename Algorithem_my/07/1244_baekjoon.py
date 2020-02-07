import sys

sys.stdin = open('input.txt')

n = int(input())
default = list(map(int,input().split()))
pn = int(input())
for i in range(pn):
    sex, start= map(int,input().split())
    if sex == 1:
        for i in range(start-1,n,start):
            if default[i]:
                default[i] = 0
            else:
                default[i] = 1
    elif sex == 2:
        start = start -1
        for i in range(n):
            
            if default[start + i] == default[start - i] and (start + i < n) and (start - i > -1):
                # print(start + i, start - i)
                if default[start + i]:
                    default[start + i] = 0
                    default[start - i] = 0
                else:
                    default[start + i] = 1
                    default[start - i] = 1
            else:
                break
    x= 0
while x < len(default):
        print(*default[x:x+20])
        x +=20

                
