tc = int(input())
for t in range(1, tc+1):
    n, m = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    Min = Max = s
    s = 0
    for i in range(m, n):
        s += (arr[i] - arr[i-m])
        Min = min(Min, s)
        Max = max(Max, s)

    print('#{} {}'.format(t, Max - Min))
