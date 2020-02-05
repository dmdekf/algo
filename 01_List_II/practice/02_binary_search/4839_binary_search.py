import sys

sys.stdin = open('input.txt')

def find(total, target):
    cnt = 1
    start = 1
    end = total
    # middle = int(end + start / 2) == end + start // 2
    middle = (end + start) // 2
    # 1~9까지의 숫자 중 target이 3일 경우
    # m :5
    #target = 3
    while middle != target:
        if target > middle:
            start = middle
        else:
            end = middle
        middle = (end + start) // 2
        cnt +=1
        # print(cnt)

    return cnt

T = int(input())
for tc in range(1, T+1):
    #P: 전체페이지  A, B : 찾아야 할 페이지
    P, A, B = map(int, input().split())
    a = find(P, A)
    b = find(P, B)
    result = '0'
    if a > b:
        result = 'B'
    elif a < b:
        result = 'A'    
        
    print('#{} {}'.format(tc, result))
    

