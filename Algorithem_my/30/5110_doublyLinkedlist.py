import sys

sys.stdin = open('input_5110.txt')


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList():
    def __init__(self, head=None):
        self.head = head
        self.tail = None
        self.size = 0

    def append(self, data):
        cur = self.tail
        if self.head:
            while cur.next != None:
                cur = cur.next
            data.prev = L.tail
            L.tail.next = data
            L.tail = data
        else:
            self.head = data
            self.tail = data

        self.size += 1

    def insert(self, data, index):
        cur = self.head
        for i in range(index-1):
            cur = cur.next
        data.prev = cur.tail
        data.tail = cur.next.tail
        cur.next.head = data
        cur.tail.next = data
        cur.tail = data

        self.size += 1

    def datainsert(self, data):
        first = last = data[0]
        for i in range(1, len(data)):
            last.next = data[i]
            data[i].prev = last
            data[i].head = last
            last = data[i]

        if self.head is None:
            self.head, self.tail = first, last
        else:
            cur = self.head
            while cur is not None:
                if cur.data > first.data:
                    break
                cur = cur.next
            if cur is None:
                first.prev = L.tail
                L.tail.next = first
                L.tail = last
            elif cur.prev is None:
                last.next = L.head
                L.head.prev = last
                L.head = first
            else:
                prev = cur.prev
                first.prev = prev
                last.next = cur
                prev.next = first
                cur.prev = last
        self.size += len(data)

    def alltail(self):
        cur = self.tail
        result = []
        for i in range(10):
            result.append(cur.data)
            cur = cur.prev
        return result


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(M)]
    L = LinkedList()
    for i in range(N):
        for j in range(N):
            d[i][j] = Node(d[i][j])
    for i in range(N):
        L.append(d[0][i])
    for i in range(1, M):
        L.datainsert(d[i])
    print(f'#{tc} ', end='')
    print(*L.alltail())
