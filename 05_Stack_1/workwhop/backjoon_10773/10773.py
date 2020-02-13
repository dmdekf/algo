# [1]
# [1,3]
# [1,3,5]
# [1,3,5,4]
# [1,3,5] (0을 불렀기 때문에 최근의 수를 지운다)
# [1,3] (0을 불렀기 때문에 그 다음 최근의 수를 지운다)
# [1,3,7]
# [1,3] (0을 불렀기 때문에 최근의 수를 지운다)
# [1] (0을 불렀기 때문에 그 다음 최근의 수를 지운다)
# [1,6]
# 합은 7이다.
# 4
# 3
# 0
# 4
# 0
import sys
sys.stdin = open('input.txt')
class Stack:
    def __init__(self):
        self.data = []

    def pop(self,X):
        if X == '0\n':
            return self.data.pop()
        else:
            return self.data.append(int(X))
s = Stack()
N = int(sys.stdin.readline())
# print(N)
for _ in range(N):
    s.pop(sys.stdin.readline())
    # print(s.data)

print(sum(s.data))

