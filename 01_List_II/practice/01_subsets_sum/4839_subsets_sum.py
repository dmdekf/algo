import sys
sys.stdin = open("input.txt")
def sub(n, subset):
    if n < 1:
        return subset
    else:
        subsets.append(sub(n-1, subset+[n]))
        subsets.append(sub(n-1, subset))
T = int(input())
for case in range(1,T+1):
    N, K = map(int,input().split())
    n = 12
    count = 0
    subsets = []
    s = []
    sub(n,s)
    for i in subsets:
        if i:
            if len(i) == N:
                if sum(i) == K:
                    count += 1
    print('#{} {}'.format(case, count))