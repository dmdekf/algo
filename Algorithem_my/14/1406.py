import sys
sys.stdin = open('1406_input.txt')

d = list(input())
s = []
for _ in range(int(input())):
    o = input().split()
    # print(o)
    if o[0] == 'L':
        if d:
            s.append(d.pop())
        else:
            continue
    elif o[0] == 'D':
        if s:
            d.append(s.pop())
        else:
            continue
    elif o[0] == 'B':
        if d:
            d.pop()
        else:
            continue
    elif len(o) > 1 and o[0] == 'P':
        d.append(o[1])
    # print(d)
while s:
    d.append(s.pop())
print(''.join(d))
