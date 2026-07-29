from abc import ABCMeta,abstractmethod,abstractproperty

class IQueue(metaclass=ABCMeta):
    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def length(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def offer(self,x):
        """将数据元素x插入作为队尾元素"""
        pass

    @abstractmethod
    def poll(self):
        """将队首元素删除并返回其值"""
        pass

    @abstractmethod
    def display(self):
        pass