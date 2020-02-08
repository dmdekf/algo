T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(N)]
    check = True
    for i in range(N):
        if d[i] != d[i + 1] and d != N:
            pd = d[i + 1]
            break
        else:
            print('#{} 0'.format(tc))
            check = False
            break
    if check == False:
        continue

    pd.split(pd[0])
    pw = []
    for i in range(56):
        for j in pd[i:56]:
            cnt = 1
            while pd[j] != pd[j + 1] and j != 55:
                i += 1
                cnt += 1
            pw.append(cnt)
    for i in pw[0:7:2]:
        even = sum(i)
    for i in pw[1:7:2]:
        odd = sum(i)
    if odd * 3 + even + pw[7] % 10 == 0:
        print(sum(even + odd))
    else:
        print('#{} 0'.format(tc))