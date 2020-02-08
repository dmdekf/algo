import sys

sys.stdin = open('input_9386.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = input()
    cnt = 0
    result = 0
    for i in d:
        if i == '1':
            cnt +=1
            if result <cnt:
                result=cnt
        else:
            if result <cnt:
                result=cnt
            cnt = 0
    print('#{} {}'.format(tc, result))
