#p45的链队列

from p40_queue import IQueue

class Node(object):
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class LinkQueue(IQueue):
    def __init__(self):
        self.front = None
        self.rear = None

    def clear(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def length(self):
        p = self.front
        i = 0
        while p is not None:
            p = p.next
            i += 1
        return i

    def peek(self):
        if self.isEmpty():
            return None
        return self.front.data

    def offer(self, x):
        s = Node(x,None)
        if not self.isEmpty():
            self.rear.next = s
        else:
            self.front = s
        self.rear = s

    def poll(self):
        if self.isEmpty():
            return None
        p = self.front
        self.front = self.front.next
        if p == self.rear:#这一步判断是因为,如果队列中只有一个元素,self.front和self.rear指向同一个Node（节点），但是前面只删掉了self.front，self.rear没删
            self.rear = None#删掉self.rear
        return p.data

    def display(self):
        p = self.front
        while p is not None:
            print(p.data,end=" ")
            p = p.next


queue = LinkQueue()
for i in range(10):
    queue.offer(i)
queue.display()