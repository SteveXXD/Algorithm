#实现抽象数据类型

from  abc import ABCMeta,abstractproperty,abstractmethod

class Set(metaclass=ABCMeta):
    """
    集合抽象类，metaclass = ABCMeta表示将Set类作为ABCMeta的子类
    继承于abc.Meta的类可以使用abstractproperty，abstractmethod修饰器声明虚属性与虚方法
    """
    @abstractproperty
    def size(self):
        """
        返回集合中的元素个数
        """
        pass
    @abstractmethod
    def isEmpty(self):
        """
        判断集合是否为空
        """
        pass
    @abstractmethod
    def search(self,key):
        """
        在集合中查找关键字为key的元素并返回
        """
        pass
    @abstractmethod
    def contains(self,x):
        """
        判断集合中是否含有元素x
        """
        pass
    @abstractmethod
    def add(self,x):
        """
        向集合中添加元素x
        """
        pass
    @abstractmethod
    def remove(self,key):
        """
        删除集合中关键字值为key的元素
        """
        pass
    @abstractmethod
    def clear(self):
        """
        删除集合中的所有元素
        """
        pass

#声明实现抽象类的类

class HashSet(Set):
    @property
    def size(self):
        pass
    def isEmpty(self):
        pass
    def search(self,key):
        pass
    def contains(self,x):
        pass
    def add(self,x):
        pass
    def remove(self,key):
        pass
    def clear(self):
        pass
    def __init__(self):
        pass

