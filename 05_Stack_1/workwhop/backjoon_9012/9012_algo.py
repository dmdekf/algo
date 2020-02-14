'''
1.'('가 나오면 스텍에 '('를 넣어줌.
2. ')'가 나오면 스텍에서 '('를 빼줌
- 스텍이 비어있는지 
-비어있다면  false
-아니면pop()
3. 스텍이 비어있다면 True
아니면 False
'''

import sys

T = int(sys.stdin.readline())


for _ in range(T):
    D = sys.stdin.readline().strip()
    stack = []
    for p in D:
        if p == '(':
            stack.append(p)
        else:
            if len(stack):
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')


                
