from abc import ABCMeta,abstractmethod,abstractproperty

class IStack(metaclass = ABCMeta):
    @abstractmethod
    def clear(self):
        """将栈置空"""
        pass
    @abstractmethod
    def isEmpty(self):
        """判断栈是否为空"""
        pass
    @abstractmethod
    def length(self):
        """返回栈的元素个数"""
        pass
    @abstractmethod
    def peek(self):
        """返回栈顶元素"""
        pass
    @abstractmethod
    def push(self,x):
        """数据元素x入栈"""
        pass
    @abstractmethod
    def pop(self):
        """将栈顶元素出栈并返回"""
        pass
    @abstractmethod
    def display(self):
        """输出栈中的全部元素"""
        pass
