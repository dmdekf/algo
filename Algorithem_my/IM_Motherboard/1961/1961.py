import sys
sys.stdin = open('input.txt')

def rec(num):
    newnum = [[0]*len(num[0]) for _ in range(len(num))]
    for i in range(len(num)):
        for j in range(len(num[0])):
            newnum[j][i] = num[len(num)-i-1][j]
    return newnum



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        print(rec(d)[i])
