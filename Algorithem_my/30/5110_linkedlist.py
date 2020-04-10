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
            if self.head.data > data[0].data:
                temp = cur
                self.head = data[0]
                cur = data[0]
                for i in range(1, len(data)):
                    cur.next = data[i]
                    data[i].head = cur
                    cur = data[i]
                if temp:
                    cur.next = temp
                    temp.head = data[i]
            else:
                while cur.next and cur.next.data <= data[0].data:
                    cur = cur.next
                temp = cur.next
                cur.next = data[0]
                data[0].head = cur
                cur = cur.next
                for i in range(1, len(data)):
                    cur.next = data[i]
                    data[i].head = cur
                    cur = data[i]
                if temp:
                    cur.next = temp
                    temp.head = data[i]

        self.size += len(data)

    def print(self):
        cur = self.head
        result = ''
        while cur:
            result += str(cur.data)+' '
            cur = cur.next
        return print(result)

    def all(self):
        cur = self.head
        result = []
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result

    def alltail(self):
        cur = self.tail
        result = []
        while cur:
            result.append(cur.data)
            cur = cur.head
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
    print(*L.all()[::-1][:10])
    # print(*L.alltail())
