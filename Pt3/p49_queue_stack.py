from p34_sqstack import SqStack

class MyQueue:
    def __init__(self):
        self.stack1 = SqStack(50)
        self.stack2 = SqStack(50)

    def move(self):
        while not self.stack1.isEmpty():
            self.stack2.push(self.stack1.pop())#将stack1的成员推送至stack2(反向)

    def push(self,x):
        self.stack1.push(x)

    def pop(self):
        if self.stack2.isEmpty():
            self.move()
        return self.stack2.pop()

    def peek(self):
        if self.stack2.isEmpty():
            self.move()
        return self.stack2.peek()

    def empty(self):
        return self.stack1.isEmpty() and self.stack2.isEmpty()


#那么有人就要问了，主播主播，这个move方法是什么玩意
#可以把stack1看成缓存，每次需要peek或者pop（就是poll）的时候就把stack1的东西倒进stack2再peek或者pop
#push的时候先进入缓存（stack1）
#这样实现的队列就和普通的队列一样了。（pop方法就是poll方法）