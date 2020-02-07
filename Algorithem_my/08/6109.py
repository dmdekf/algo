
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M :
        short = M
        large = N
    else:
        short = N
        large = M

    for i in range(large - short +1):
        for j in 
