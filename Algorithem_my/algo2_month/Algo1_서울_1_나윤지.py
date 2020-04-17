T = int(input())

for tc in range(1, T+1):
    N = int(input())
    d = list(map(int, input().split()))

    while N !=0:
        temp = [0] * 10
        for i in range(0,10):
            if d[i]:
                if i==0:
                    if 0<d[i]<10:
                        temp[i+1]+=d[i]
                    elif 0>d[i]>-10:
                        temp[i]=-d[i]
                    else:
                        b = -(abs(d[i]) // 2)
                        a = abs(d[i]) // 2
                        temp[i + 1] += a
                        temp[i] = -b
                elif i==9:
                    if 0<d[i]<10:
                        temp[i]=-d[i]
                    elif 0>d[i]>-10:
                        temp[i-1]+=d[i]
                    else:
                        b = -(abs(d[i]) // 2)
                        a = abs(d[i]) // 2
                        temp[i] = -a
                        temp[i - 1] += b
                else:
                    if abs(d[i]) >=10:
                        b=-(abs(d[i])//2)
                        a=abs(d[i])//2
                        temp[i+1]+=a
                        temp[i-1]+=b
                    elif d[i] > 0:
                        temp[i+1]+=d[i]
                    elif d[i] < 0:
                        temp[i-1]+=d[i]
        N-=1
        d=temp
    print('#{} '.format(tc),end='')
    print(*d)
