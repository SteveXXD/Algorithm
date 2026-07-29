from p40_queue import IQueue

class PriorityNode:
    def __init__(self,data = None,priority = None,next = None):
        self.data = data
        self.priority = priority
        self.next = next

class PriorityQueue(IQueue):
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

    def offer(self,x,priority=0):
        s = PriorityNode(x,priority,None)
        if not self.isEmpty():
            p = self.front
            q = self.front
            while p is not None and p.priority <= s.priority:#额这里就是找插入的位置。这个p跟q就跟猫猫虫差不多，想象一下就行了
                q = p
                p = p.next
            if p is None:
                self.rear.next = s
                self.rear = s
            elif p == self.front:
                s.next = self.front
                self.front = s
            else:
                q.next = s
                s.next = p
        else:
            self.front = s
            self.rear = s

    def poll(self):
        if self.isEmpty():
            return None
        p = self.front
        self.front = self.front.next
        if p == self.rear:
            self.rear = None
        return p.data


    def display(self):
        p = self.front
        while p is not None:
            print(p.data,end = " ")
            p = p.next

queue = PriorityQueue()
queue.offer("关闭Idle",13)
queue.offer("卸载Idle",78)
queue.offer("打开手机",91)
queue.offer("下载原神",100)

#优先级值越小，优先级越高。
while not queue.isEmpty():
    print(queue.poll())