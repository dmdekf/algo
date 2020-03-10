n = int(input())

for tc in range(1, n+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if A > B:
        A, B = B, A
        N, M = M, N
    Max = float('-inf')
    for i in range(M - N + 1):
        s = 0
        for j in range(N):
            s += A[j] * B[i+j]
        Max = max(Max, s)

    print(f'#{tc} {Max}')
