import sys
sys.stdin = open('input.txt')

N = int(input())

d = list(map(int,input().split()))
result = 1

for i in range(N):
    cnt = 1
    if i!=N-1 and d[i] <= d[i+1]:
        while i<N-1 and d[i] <= d[i+1]:
            cnt+=1
            i +=1
    if cnt > result:
        result = cnt


for i in range(N):
    cnt = 1
    if i!=N-1 and d[i] >= d[i+1]:
        while i<N-1 and d[i] >= d[i+1]:
            cnt+=1
            i +=1
    if cnt > result:
        result = cnt

print(result)






