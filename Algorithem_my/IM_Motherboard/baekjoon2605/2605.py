import sys
sys.stdin = open('input.txt')

N = int(input())

d = list(map(int,input().split()))
result = []
for i in range(N):
    result.insert(i-d[i],i+1)
print(*result)






