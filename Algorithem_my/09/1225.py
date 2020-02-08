for _ in range(10):
    tc = int(input())
    d = list(map(int, input().split()))
    cnt = 1
    while d[-1] !=0:
        x=d.pop(0)-cnt
        if x < 0:
            x = 0
        d.append(x)
        cnt +=1
        if cnt == 6:
            cnt = 1
    print('#{}'.format(tc), end=' ')
    print(*d)