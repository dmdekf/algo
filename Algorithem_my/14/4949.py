import sys
sys.stdin = open('input.txt')


def chk(data):
    s = []
    for i in data:
        if i == '(':
            s.append(i)
        elif i == '[':
            s.append(i)
        elif i == ')':
            if s and s[-1] == '(':
                s.pop()
            else:
                return print('no')
        elif i == ']':
            if s and s[-1] == '[':
                s.pop()
            else:
                return print('no')
    else:
        if s:
            return print('no')
        else:
            return print('yes')


while True:
    data = input()
    if data == ".":
        break
    chk(data)
# len(data) != 1 and
