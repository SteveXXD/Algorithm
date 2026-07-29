#链栈的实现
from p33_stack import IStack

class Node(object):
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class LinkStack(IStack):
    def __init__(self):
        self.top = None

    def clear(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def length(self):
        i = 0
        p = self.top
        while p is not None:
            i += 1
            p = p.next
        return i

    def push(self,x):
        s = Node(x,self.top)
        self.top = s

    def peek(self):
        return self.top.data

    def pop(self):
        if self.isEmpty():
            return None
        p = self.top
        self.top = self.top.next
        return p.data

    def display(self):
        p = self.top
        while p is not None:
            print(p)
            p = p.next

stack1 = LinkStack()
stack1.push("a")
stack1.push("b")
stack1.push("c")
stack1.push("d")
print(str(stack1.peek()))