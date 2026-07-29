from p40_queue import IQueue

class CircleQueue(IQueue):

    def __init__(self,maxsize):
        self.maxSize = maxsize
        self.queueElem = [None] * self.maxSize
        self.front = 0
        self.rear = 0

    def clear(self):
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def length(self):
        return (self.rear - self.front + self.maxSize)%self.maxSize

    def peek(self):
        if self.isEmpty():
            return None
        return self.queueElem[self.front]

    def offer(self, x):
        if (self.rear + 1) % self.maxSize == self.front:
            raise Exception("队列已满")
        self.queueElem[self.rear] = x
        self.rear = (self.rear + 1) % self.maxSize

    def poll(self):
        if self.isEmpty():
            return None
        p = self.queueElem[self.front]
        self.front = (self.front + 1) % self.maxSize
        return p

    def display(self):
        i = self.front
        while i != self.rear:
            print(self.queueElem[i],end = " ")
            i = (i+1) % self.maxSize


queue = CircleQueue(10)

for i in range(9):
    queue.offer("hello")

queue.display()

#简单来说就是让front和rear两个指针绕圈子就行，用取模