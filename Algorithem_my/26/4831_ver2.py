
# k = 최대이동횟수
# m 충전기 설치 개수
# n : 도달지점.
tc = int(input())
for t in range(1, tc+1):
    K, N, m = list(map(int, input().split()))
    pos = list(map(int, input().split()))
    # ver 1
    station = [0] * (N+1)
    for p in pos:
        station[p] = 1

    bus = ans = 0
    while bus + K < N:
        for p in range(bus+K, bus, -1):
            if station[p]:
                bus = p
                ans += 1
                break
        else:
            ans = 0
            break

    # ver 2
    k, n, m = list(map(int, input().split()))
    pos = [0] + list(map(int, input().split())) + [n]

    bus = ans = 0

    for i in range(1, m+2):
        if pos[i] - pos[i-1] > k:
            ans = 0
            break
        if bus + k < pos[i]:
            bus = pos[i-1]
            ans += 1
    print('#{} {}'.format(t, ans))
