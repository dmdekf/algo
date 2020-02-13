# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import sys
sys.stdin = open('input.txt')

class Stack:
    def __init__(self):
        self.data = []

    def push(self,X):
        return self.data.append(X)

    def pop(self):
        if self.data:
            return print(self.data.pop())
        else:
            return print(-1)

    def size(self):
        return print(len(self.data))

    def empty(self):
        if self.data:
            return print(0)
        else:
            return print(1)

    def top(self):
        if self.data:
            return print(self.data[-1])
        else:
            return print(-1)



# for x in sys.stdin.readline():
N = int(sys.stdin.readline())
s = Stack()
for _ in range(N):
    x = list(sys.stdin.readline().split())
    # print(x)

    if 'push' in x:
        s.push(x[1])
    elif 'top' in x:
        s.top()
    elif 'size' in x:
        s.size()
    elif 'empty' in x:
        s.empty()
    elif 'pop' in x:
        s.pop()

