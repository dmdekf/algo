# ()()	true
# (())()	true
# )()(	false
# (()(	false

from collections import deque


def solution(s):
    stack = deque()
    for i in range(len(s)-1, -1, -1):
        if s[i] == ')':
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False
