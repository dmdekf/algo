import sys


def f(d):
    for i in d:
        if i == '(':
            s.append(i)
        elif i == ')':
            while s and s[-1] != '(':
                num.append(s.pop())
            s.pop()
        elif i == '*':
            s.append(i)
        elif i == '+':
            if s and s[-1] == '*':
                while s and s[-1] == '*':
                    num.append(s.pop())
            s.append(i)
        else:
            num.append(i)
    while s:
        num.append(s.pop())
    return s, num


sys.stdin = open(('1224_input.txt'))

T = 10

for tc in range(1, T+1):
    N = int(input())
    d = list(input())
    s = []
    num = []
    s, num = f(d)
    # print(num)
    result = []
    # print(f's:{s}, num:{num}')
    for i in num:
        # print(result)
        if i.isdigit():
            result.append(int(i))
        elif i == '+':
            a = result.pop()
            b = result.pop()
            result.append(a+b)
        elif i == '*':
            a = result.pop()
            b = result.pop()
            result.append(b*a)

    print(f'#{tc} ', end='')
    print(*result)
