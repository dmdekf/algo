import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = sorted(list(map(int, input().split())))
    
    # print(r)
    # r = reversed(d[:5]) == d[-5:][::-1]
    r = d[-5:][::-1]
    print(r)
    
    print('#{}'.format(tc),end=' ')
    for i, j in zip(r, d[:6]):
        print(i, end = ' ')
        print(j, end = ' ')
    print()
