import sys
sys.stdin = open('input.txt')
def c(num):
    nd = list([0]*len(num) for _ in range(len(num)))
    for i in range(len(num)):
        for j in range(len(num[0])):
            nd[j][len(num)-i-1] = num[i][j]
    return nd
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # print(N)
    d = [list(map(int,input().split())) for _ in range(N)]
    # print(d)
    d1 = c(d)

    d2 = c(d1)
    d3 = c(d2)
    print('#{}'.format(tc))
    for i in range(N):
        print('{}'.format(''.join(map(str,d1[i]))),end=' ')
        print('{}'.format(''.join(map(str, d2[i]))),end=' ')
        print('{}'.format(''.join(map(str, d3[i]))))


