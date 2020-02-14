import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    stack = []
    D = input()
    # print(D)
    for i in D:
        if stack:
            if i ==stack[-1
            ]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    print(f'#{tc} {len(stack)}')
    
