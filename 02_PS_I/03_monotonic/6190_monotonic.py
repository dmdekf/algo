import sys

sys.stdin = open('input.txt')

def check(n):
    flag = True
    while n:
        n, r = n // 10, n % 10
        if n % 10 > r:
            return False
        
    return flag

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    result = -1
    for i in range(N):
        for j in range(i+1,N):
            num = numbers[i]*numbers[j]
            if result < num:
                if check(num):
                    result = num
    print('#{} {}'.format(tc, result))
