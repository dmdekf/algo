T = int(input())
for tc in range(1, T+1):
    N = int(input())

    cnt = [0] * 201  # 1~200까지. 0은 제외하고

    for _ in range(N):
        a, b = map(int, input().split())
        a = (a+1)//2
        b = (b+1)//2
        if a > b:
            a, b = b, a
        for i in range(a, b+1):
            cnt[i] += 1
    ans = max(cnt)

    print('#{} {}'.format(tc, ans))
