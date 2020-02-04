import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    l = 1
    r = P
    # c = P//2

    result =True
    cnta = 0
    while result == True:
        c = (l+r)// 2
        cnta +=1
        if c > A:
            r=c
        elif c < A:
            l=c
        else:
            result = False

    l = 1
    r = P        
    result =True
    cntb = 0
    while result == True:
        c = (l+r)// 2
        cntb +=1
        if c > B:
            r=c
        elif c < B:
            l=c
        else:
            result = False
    r = ''
    if cnta > cntb:
        r = 'B'
    elif cnta < cntb:
        r = 'A'
    else:
        r = '0'
        
    print('#{} {}'.format(tc, r))
    

