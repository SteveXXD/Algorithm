from p34_sqstack import SqStack
import copy

class MyQueue:
    def __init__(self):
        self.stack1 = SqStack(50)
        self.stack2 = SqStack(50)
        self.stack0 = SqStack(50)

    def move(self):
        self.stack2.clear()
        self.stack0 = copy.deepcopy(self.stack1)
        while not self.stack1.isEmpty():
            self.stack2.push(self.stack1.pop())
        self.stack1 = copy.deepcopy(self.stack0)

    def pop(self):
        pass

#原本想用自己的逻辑用栈构建一个队列，但是发现难以实现，遂放弃