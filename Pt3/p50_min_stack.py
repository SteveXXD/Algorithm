#最小栈

from p34_sqstack import SqStack
import math

class MinStack:
    def __init__(self):
        self.stack1 = SqStack(50)
        self.min_stack = SqStack(50)
        self.min_stack.push(math.inf)

    def push(self,x):
        self.stack1.push(x)
        self.min_stack.push(min(x,self.min_stack.peek()))

    def pop(self):
        self.min_stack.pop()
        return self.stack1.pop()

    def top(self):
        return self.stack1.peek()

    def min(self):
        return self.min_stack.peek()