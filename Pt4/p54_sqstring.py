from p53_string import IString

class SqString(IString):
    def __init__(self,obj=None):
        if obj is None:
            self.strValue = []
            self.curlen = 0

        elif isinstance(obj,str):
            self.curlen = len(obj)
            self.strValue = [None] * self.curlen
            for i in range(self.curlen):
                self.strValue[i] = obj[i]

        elif isinstance(obj, list):
            self.curlen = len(obj)
            self.strValue = [None] * self.curlen
            for i in range(self.curlen):
                self.strValue[i] = obj[i]

    def clear(self):
        self.curlen = 0

    def isEmpty(self):
        return self.curlen == 0

    def length(self):
        return self.curlen

    def charAt(self, i):
        if i < 0 or i > self.curlen:
            raise Exception("检索序号不在范围内")
        return self.strValue[i]

    def allocate(self,new_capacity):
        tmp = self.strValue
        self.strValue = [None] * new_capacity
        for i in range(self.curlen):
            self.strValue[i] = tmp[i]

    def subString(self, begin, end):
        if begin < 0 or begin >=end or end > self.curlen:
            raise Exception("参数不合法")
        tmp = [None] * (end-begin)
        for i in range(begin,end):
            tmp[i-begin] = self.strValue[i]
        return SqString(tmp)

    def insert(self, i, string):
        if i < 0 or i > self.curlen:
            raise Exception("插入位置不合法")
        new_capacity = self.curlen + string.length()
        self.allocate(new_capacity)
        for j in range(self.curlen-1,i,-1):
            self.strValue[j+string.length()] = self.strValue[j]
        for j in range(i,i+string.length()):
            self.strValue[j] = string.charAt(j - i)#j-i就是0,1,2,3,4,5,...
        self.curlen = new_capacity

    def delete(self, begin, end):
        if begin < 0 or end > self.curlen or begin >= end:
            raise Exception("参数不合法")
        self.strValue = self.strValue[0:begin] + self.strValue[end:self.curlen]#注意书上的写错了，这里不是self.strValue[i]
        self.curlen -= (end-begin)

    def concat(self, string):
        self.insert(self.curlen,string)

    def compareTo(self, string):
        length = string.length()
        n = self.curlen if self.curlen > length else length
        for i in range(n):
            if self.strValue[i] > string.charAt(i):
                return 1
            elif self.strValue[i] < string.charAt(i):
                return -1
        if self.curlen>length:
            return 1
        elif self.curlen < length:
            return -1
        else:
            return 0

    def indexOf(self, string, begin):#相关代码在串的模式匹配中

        pass

    def display(self):
        for i in range(self.curlen):
            print(self.strValue[i],end=" ")


'''

标准的删除做法应该是这样的
def delete(self, begin, end):
    if begin < 0 or end > self.curlen or begin >= end:
        raise Exception("参数不合法")
    # 把 end 后面的元素整体往前挪 begin 位
    for j in range(end, self.curlen):
        self.strValue[j - (end - begin)] = self.strValue[j]
    self.curlen -= (end - begin)
    
'''
