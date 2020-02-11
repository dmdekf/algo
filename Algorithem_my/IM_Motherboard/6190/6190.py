import sys
sys.stdin = open('input.txt')
def p(num):
    while num:
        r = num % 10
        num = num // 10
        if r < num%10:
            return False
    return True

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    d = list(map(int, input().split()))
    d = sorted(d)
    for i in range(N-1,0,-1):
        x=d[i]*d[i-1]
        if p(x):
            print('#{} {}'.format(tc,x))
            break





