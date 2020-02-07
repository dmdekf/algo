t = int(input())


def cala(num):
    x = 1
    while ((x-1)*(x-2)/2 != num:
        x += 1
    i=int(num - ((x-1)*(x-2)/2))
    return 1+i, x-1-i


def calresult(x, y):
    num=x + y
    i=(x-1)*(x-2)/2
    return int(i + x - 1)

T=int(input())
for tc in range(1, T+1):
    p, q=map(int, input().split())

    p=cala(p)
    q=cala(q)

    print(f'#{tc} {calresult(p[0]+q[0],p[1]+q[1])}')
