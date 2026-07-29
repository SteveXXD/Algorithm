#顺序栈的实现
from p33_stack import IStack

class SqStack(IStack):
    def __init__(self,maxSize):
        self.maxSize = maxSize#栈的最大存储个数
        self.stackItem = [None] * self.maxSize#顺序栈存储空间
        self.top = 0#指向栈顶元素的下一存储单元位置(?)(就是栈的元素个数)

    def clear(self):
        """将栈置空"""
        self.top = 0

    def isEmpty(self):
        """判断栈是否为空"""
        return self.top == 0

    def length(self):
        """返回栈的数据元素个数"""
        return self.top

    def peek(self):
        """返回栈顶元素"""
        if not self.isEmpty():
            return self.stackItem[self.top-1]
        else:
            return None

    def push(self,x):
        """数据元素x入栈"""
        if self.top == self.maxSize:
            raise Exception("栈已满")
        self.stackItem[self.top] = x
        self.top += 1

    def pop(self):
        """将栈顶元素出栈并返回"""
        if self.isEmpty():
            return None
        self.top -= 1
        return self.stackItem[self.top]

    def display(self):
        """输出栈中所有元素"""
        for i in range(self.top-1,-1,-1):
            print(self.stackItem[i],end = "")
