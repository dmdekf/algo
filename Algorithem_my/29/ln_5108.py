import sys

sys.stdin = open('input_5108.txt')


class Node():

    def __init__(self, data):

        self.data = data
        self.next = None

    def __del__(self):
        self.data


class LinkedList():

    def __init__(self, head=None):
        self.head = head
        self.tail = None

        self.size = 0

    def append(self, data):
        cur = self.head
        if self.head:
            while cur.next != None:
                cur = cur.next
            cur.next = data
            data.head = cur

        else:
            self.head = data
            self.tail = data

        self.size += 1

    def show(self, index):
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.data

    def insert(self, data, index):
        cur = self.head
        for i in range(index-1):
            cur = cur.next
        temp = cur.next
        cur.next = data
        data.head = cur
        data.next = temp
        self.size += 1

    def print(self):
        cur = self.head
        result = ''
        while cur:
            result += str(cur.data)+' '
            cur = cur.next
        return print(result)


T = int(input())
for tc in range(1, T+1):
    N, M, LI = map(int, input().split())
    d = list(map(int, input().split()))
    L = LinkedList()
    for i in range(N):
        L.append(Node(d[i]))

    for _ in range(M):
        index, data = map(int, input().split())
        L.insert(Node(data), index)

    print(f'#{tc} {L.show(LI)}')
