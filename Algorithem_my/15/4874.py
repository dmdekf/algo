def f(d):
    s = []
    if d[0] == '.':
        return 'error'
    while d[0] != '.':
        x = d.pop(0)
        if x.isdigit():
            s.append(x)
        else:
            if len(s) > 1:
                if x == '+':
                    s.append(int(s.pop()) + int(s.pop()))
                elif x == '-':
                    a = int(s.pop())
                    b = int(s.pop())
                    s.append(b - a)
                elif x == '*':
                    s.append(int(s.pop()) * int(s.pop()))
                elif x == '/':
                    a = int(s.pop())
                    b = int(s.pop())
                    s.append(b / a)

            else:
                return 'error'
    if len(s) > 1:
        return 'error'
    return int(s[0])


import sys
sys.stdin = open(('4874_input.txt'))


T = int(sys.stdin.readline().strip())

for tc in range(1, T+1):
    di = list(sys.stdin.readline().strip().split())
    # print(di)
    print(f'#{tc} {f(di)}')

