# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import sys
sys.stdin = open('input.txt')
from collections import deque


T = int(input())
for tc in range(1, T+1):
    a = deque()
    result = 1
    d = list(input())
    for i in range(len(d)-1,-1,-1):
        if d[i] ==')':
            a.append(d[i])
        elif d[i] == '}':
            a.append(d[i])
        else:
            if d[i]=='(':
                if len(a) == 0 or a[-1] != ')' :
                    result = 0
                    break
                else:
                    a.pop()
            elif d[i] =='{' :
                if len(a) == 0 or a[-1] != '}':
                    result = 0
                    break
                else:
                    a.pop()
    if len(a):
        result =0

    if result == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')




