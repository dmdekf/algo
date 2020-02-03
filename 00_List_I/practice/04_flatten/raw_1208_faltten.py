import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1,T+1):
    n = int(input())
    d = list(map(int,input().split())) 
    max_idx = 0
    min_idx = 0
    # 첫번째 값은 이미 담겨 있으므로  range(1,100)으로 시작.
    # dumping과정
    for _ in range(n):
        for i in range(1, 100):

            if d[max_idx] < d[i]:
                max_idx = i
            if d[min_idx] > d[i]:
                min_idx = i

        d[max_idx] -=1
        d[min_idx] +=1
    # 비교해보기.
    # print('#{} {}'.format(tc, d[max_idx] - d[min_idx]))

    #dump가 끝난 과정.
    max_value = d[0]
    min_value = d[0]

    for j in range(1,100):
        if max_value < d[j]:
            max_value = j
        if min_value > d[j]:
            min_value =
    print('#{} {}'.format(tc, max_value - min_value))
            
