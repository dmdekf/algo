def f(n, s, d, m, m3):
    global minV
    if n > 12:
        if minV > s:
            minV = s
        return
    elif s >= minV:
        return
    else:
        f(n+1, s+min(data[n]*d, m), d, m, m3)
        f(n+3, s+m3, d, m, m3)


T = int(input())
# T = 1
for tc in range(1, T+1):
    d, m, m3, y = map(int, input().split())
    data = [0] + list(map(int, input().split()))
    # print(d)
    minV = y
    f(1, 0, d, m, m3)
    print(f'#{tc} {minV}')