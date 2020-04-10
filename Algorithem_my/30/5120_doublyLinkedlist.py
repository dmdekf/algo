import sys

sys.stdin = open('input_5120.txt')


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList():
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def append(self, data):
        if self.head:
            tail = L.head.prev
            data.prev = tail
            data.next = L.head
            tail.next = data
            L.head.prev = data
        else:
            self.head = data
            data.prev = data.next = data

        self.size += 1

    def insert(self, index):
        cur = self.head
        for _ in range(index-1):
            cur = cur.next
        data = Node(cur.data+cur.next.data)
        data.next = cur.next
        data.prev = cur
        data.head = cur.next
        cur.next.head = data
        cur.next = data
        tail = L.head.prev
        self.size += 1

    def print(self):
        if self.head is None:
            return
        cur = self.head
        tail = L.head.prev
        result = []
        while cur != tail:
            result.append(cur.data)
            cur = cur.next
        result.append(tail.data)
        return result

    def alltail(self):
        cur = L.head.prev
        result = []
        for i in range(10):
            result.append(cur.data)
            cur = cur.prev
        return result


T = int(input())
# T = 1
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    d = list(map(int, input().split()))
    L = LinkedList()
    for i in range(N):
        d[i] = Node(d[i])
    m = M
    for i in range(N):
        L.append(d[i])
    for _ in range(K):
        print(M, L.size)
        L.insert(M)
        M += m
        if M > L.size:
            # print(M)
            M -= (L.size)
            # print(M)

    print(f'#{tc} ', end='')
    print(*L.print()[::-1][:10])
    print(*L.print())
