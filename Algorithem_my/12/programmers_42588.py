# 송신 탑(높이)	수신 탑(높이)
# 5(4)	4(7)
# 4(7)	2(9)
# 3(5)	2(9)
# 2(9)	-
# 1(6)	-
from collections import deque


def solution(d):
    t = deque()
    answer = []
    while d:
        start = d.pop()
        while d and d[-1] <= start:
            t.append(d.pop())
        answer.append(len(d))
        while t:
            d.append(t.pop())

    return list(reversed(answer))
