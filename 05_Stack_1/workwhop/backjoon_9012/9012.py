
import sys

sys.stdin = open('input.txt')
from collections import deque

N = int(input())
for _ in range(N):
    s = deque()
    d = list(input())
    a = True
    for i in d:
        if i == '(':
            s.append(i)
        else:
            if len(s) ==0:
                a = False
            else:
                s.pop()
    if len(s) == 0 and a:
        print('YES')
    else:
        print('NO')
