import sys

sys.stdin = open('input.txt')
N = int(input())

d = list(map(int,input().split()))
result = 1

cnt = 1
for i in range(N):
    if i!=N-1 and d[i] <= d[i+1]:
        cnt+=1
        if cnt > result:
            result = cnt
    else:
        cnt = 1



for i in range(N):
    if i!=N-1 and d[i] >= d[i+1]:
        cnt+=1
        if cnt > result:
            result = cnt
    else:
        cnt = 1

print(result)