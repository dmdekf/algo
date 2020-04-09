import sys

sys.stdin = open('input_5122.txt')


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


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

    def change(self, index, data):
        cur = self.head
        for i in range(index-1):
            cur = cur.next
        temp = cur.next
        cur.next.data = data

    def insert(self, index, data):
        cur = self.head
        for i in range(index-1):
            cur = cur.next
        temp = cur.next
        cur.next = data
        data.head = cur
        data.next = temp
        self.size += 1

    def delete(self, index):
        cnt = 0
        cur = self.head

        if index == 0:
            self.head = cur.next
        else:
            while cur.next:
                if cnt == index-1:
                    cur.next = cur.next.next
                cur = cur.next
                cnt += 1
        self.size -= 1


T = int(input())
for tc in range(1, T+1):
    N, M, ANSERINDEX = map(int, input().split())
    d = list(map(int, input().split()))

    L = LinkedList()

    for i in range(N):
        L.append(Node(d[i]))

    for i in range(M):

        m = list(input().split())
        if m[0] == 'I':
            L.insert(int(m[1]), Node(int(m[2])))
        if m[0] == 'D':
            L.delete(int(m[1]))
        if m[0] == 'C':
            L.change(int(m[1]), int(m[2]))

    if L.size < ANSERINDEX:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {L.show(ANSERINDEX)}')
