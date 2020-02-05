import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range( 1, T+1):
    n = int(input())
    d = list(map(int, input().split()))
    # print(d)
    sort_d = []
    for i in range(n):
        sort_d.append([d[i*2],d[i*2+1]])

    result = sort_d[0]
    # print(result)
    start = sort_d[0][0]
    end = sort_d[0][1]
    # print(len(sort_d))
    while len(result)/2 !=len(sort_d):
        
        for i in range(len(d)//2):
            if end == sort_d[i][0]:
                end = sort_d[i][1]
                result.append(sort_d[i][0])
                result.append(sort_d[i][1])
            elif start == sort_d[i][1]:
                start = sort_d[i][0]
                result.insert(0,sort_d[i][1])
                result.insert(0,sort_d[i][0])
    print('#{}'.format(tc),end = ' ')
    print(*result)

