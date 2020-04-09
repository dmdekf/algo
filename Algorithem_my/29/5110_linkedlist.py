import sys

sys.stdin = open('input_5110.txt')


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
        for i in range(index-1):
            cur = cur.next
        print(cur.data)

    def insert(self, data, index):
        cur = self.head
        for i in range(index-1):
            cur = cur.next
        data.head = cur.next
        cur.next = data
        self.size += 1

    def datainsert(self, data):
        cur = self.head
        if self.head:
            while cur.data < data[0].data:
                cur = cur.next
            print(cur.data)
            temp = cur.next
            cur.next = data[0].data
            data[0].head = cur.data

            for i in range(1, len(data)):
                data[i-1].tail = cur.data
                cur = data[i-1]
            data[len(data)-1].tail = temp.data
            if temp:
                temp.head = data[i]
        self.size += len(data)

    def print(self):
        cur = self.head
        result = ''
        while cur:
            result += str(cur.data)+' '
            cur = cur.next
        return print(result)


T = int(input())
T = 1
for tc in range(1, T+1):
    N, M = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(M)]
    L = LinkedList()

    for i in range(N):
        for j in range(N):
            d[i][j] = Node(d[i][j])
            # print(d[i][j].data)
    for i in range(N):
        L.append(d[0][i])
    L.print()
    L.datainsert(d[1])
    L.print()

    # print(f'#{tc} {d[L]}')
