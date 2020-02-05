def inc(num):
    if num < 10:
        return True
    else:
        while num:
            y = num % 10
            num = num//10
            if y < num %10:
                return False
        return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = list(map(int, input().split()))
    
    mymax = -987654321
    chk = False
    for i in range(N):
        for j in range(i+1,N):
            temp = d[i]*d[j]
            if inc(temp):
                chk = True
                if mymax < temp:
                    mymax = temp
    if chk:
        print('#{} {}'.format(tc, mymax))
    else:
        print('#{} -1'.format(tc))
            
            

        