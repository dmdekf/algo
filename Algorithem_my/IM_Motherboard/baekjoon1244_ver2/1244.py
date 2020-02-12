import sys
sys.stdin = open('input.txt')
# 8
# 0 1 0 1 0 0 0 1
# 2
# 1 3
# 2 3
N = int(input())
d = list(map(int,input().split()))
# print(d)
M = int(input())
for _ in range(M):
    s, n = map(int,input().split())
    if s == 1:
        for i in range(n-1,N,n):
            if d[i]:
                d[i]=0
            else:
                d[i]=1
        # print(d)

    else:
        n=n-1
        for i in range(N):
            if n-i>=0 and n+i<=N and d[n-i] == d[n+i]:
                if d[n-i]:
                    d[n - i], d[n+i] = 0,0
                else:
                    d[n - i], d[n + i] = 1,1
            else:
                break
x = 0
while x < N:
    print(*d[x:x+20])
    x +=20








