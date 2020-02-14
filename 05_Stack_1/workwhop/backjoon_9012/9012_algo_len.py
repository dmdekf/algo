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
    stack = 0
    for p in D:
        if p == '(':
            stack +=`1`
        else:
            if stack:
                stack -=1
            else:
                print('NO')
                break
            # if  stack < 0:
            #     print('NO')
    else:
        if stack:
            print('NO')
        else:
            print('YES')


                
