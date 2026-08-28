#666依旧杀鸡用牛刀这一块


class Node(object):
    def __init__(self,val=None,left = None,next = None):
        self.val = val
        self.left = left
        self.next = next

class LinkList(object):
    def __init__(self):
        self.length = 0
        self.head = Node()
        self.pos = {}

    def create(self,ls):
        idx = 0
        p = self.head
        while idx < len(ls):
            s = Node(ls[idx])
            s.left = p
            p.next = s
            self.pos[ls[idx]] = s
            p = p.next
            idx += 1
            self.length += 1

    def display(self):
        p = self.head.next
        while p is not None:
            res.append(p.val)
            p = p.next

    def mvr(self, x, y):
        xp = self.pos.get(x)
        yp = self.pos.get(y)
        if xp is None or yp is None or xp == yp:
            return
        xp.left.next = xp.next
        if xp.next is not None:
            xp.next.left = xp.left
        r = yp.next
        xp.left = yp
        xp.next = r
        yp.next = xp
        if r is not None:
            r.left = xp

    def mvl(self, x, y):
        xp = self.pos.get(x)
        yp = self.pos.get(y)
        if xp is None or yp is None or xp == yp:
            return
        xp.left.next = xp.next
        if xp.next is not None:
            xp.next.left = xp.left
        L = yp.left
        xp.left = L
        xp.next = yp
        L.next = xp
        yp.left = xp

import sys
data = sys.stdin.buffer.read().split()
idx = 0
while idx < len(data):
    n = int(data[idx]);idx += 1
    m = int(data[idx]);idx += 1
    l = [x for x in range(1, n + 1)]
    res = []
    lst = LinkList()
    lst.create(l)
    x = 0
    c = 0
    for _ in range(m):
        c = data[idx];idx += 1
        x = int(data[idx]);idx += 1
        y = int(data[idx]);idx += 1

        if c == b"A":
            lst.mvl(x,y)
        else:
            lst.mvr(x,y)
    lst.display()
    print(" ".join(map(str, res)))

