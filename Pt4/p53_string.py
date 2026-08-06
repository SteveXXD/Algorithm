from abc import ABCMeta,abstractmethod,abstractproperty

class IString(metaclass=ABCMeta):
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
    def charAt(self,i):
        """读取并返回第i个元素"""
        pass
    @abstractmethod
    def subString(self,begin,end):
        """返回位序号从begin到end-1的子串"""
        pass
    @abstractmethod
    def insert(self,i,string):
        """在第i个字符之前插入string"""
        pass
    @abstractmethod
    def delete(self,begin,end):
        pass
    @abstractmethod
    def concat(self,string):
        """将string连接到字符串最后"""
        pass
    @abstractmethod
    def compareTo(self,string):
        """比较string和当前字符串的大小"""
        pass
    @abstractmethod
    def indexOf(self,string,begin):
        """从序号为begin的字符开始搜索与str相同的子串"""
        pass


