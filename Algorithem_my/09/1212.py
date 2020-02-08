import sys

sys.stdin = open('input_1212.txt')

T = int(input())
for tc in range(1,T+1):
    dlen = int(input())
    correct = input()
    answer = input()
    cnt = 0
    for i in range(dlen):
        if correct[i] == answer[i]:
            cnt +=1
    print('#{} {}'.format(tc, cnt))