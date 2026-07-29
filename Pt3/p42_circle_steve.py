#我自己写的circleQueue

from p40_queue import IQueue

class CircleQueue(IQueue):
    def __init__(self,maxsize):
        self.maxSize = maxsize
        self.item = [None] * self.maxSize
        self.front = 0
        self.rear = 0

    def clear(self):
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def length(self):
        return (self.rear - self.front + self.maxSize) % self.maxSize

    def peek(self):
        if self.isEmpty():
            return None
        return self.item[self.front]

    def offer(self, x):
        if (self.rear + 1) % self.maxSize == self.front:
            raise Exception("队列已满")
        self.item[self.rear] = x
        self.rear = (self.rear+1)%self.maxSize

    def poll(self):
        if self.isEmpty():
            return None
        p = self.item[self.front]
        self.front = (self.front+1)%self.maxSize
        return p

    def display(self):
        i = self.front
        while i != self.rear:
            print(self.item[i],end = " ")
            i = (i+1) % self.maxSize

queue = CircleQueue(10)

for i in range(9):
    queue.offer("hello")

queue.display()
print(queue.length())