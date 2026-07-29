#p41队列的实现

from p40_queue import IQueue

class SqQueue(IQueue):

    def __init__(self,maxsize):
        self.maxSize = maxsize
        self.queueElem = [None] * self.maxSize
        self.rear = 0
        self.front = 0

    def clear(self):
        self.rear = 0
        self.front = 0

    def isEmpty(self):
        return self.rear == self.front

    def length(self):
        return self.rear - self.front

    def peek(self):
        if self.isEmpty():
            return None
        return self.queueElem[self.front]

    def offer(self, x):
        """将数据元素x插入作为队尾元素"""
        if self.length() == self.maxSize:
            raise Exception("队列已满")
        self.queueElem[self.rear] = x
        self.rear += 1

    def poll(self):
        """将队首元素删除并返回其值"""
        if self.isEmpty():
            return None
        p = self.queueElem[self.front]
        self.front += 1
        return p

    def display(self):
        for i in range(self.front,self.rear):
            print(self.queueElem[i],end=" ")


queue1 = SqQueue(10)
queue1.offer("hello")
queue1.offer("world")
queue1.offer("123")
print(f"删除了{queue1.poll()}")
queue1.display()



