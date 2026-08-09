#-1派的kmp

from p53_string import IString

class SqString(IString):
    def __init__(self, obj=None):
        if obj is None:
            self.strValue = []
            self.curlen = 0

        elif isinstance(obj, str):
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

    def allocate(self, new_capacity):
        tmp = self.strValue
        self.strValue = [None] * new_capacity
        for i in range(self.curlen):
            self.strValue[i] = tmp[i]

    def subString(self, begin, end):
        if begin < 0 or begin >= end or end > self.curlen:
            raise Exception("参数不合法")
        tmp = [None] * (end - begin)
        for i in range(begin, end):
            tmp[i - begin] = self.strValue[i]
        return SqString(tmp)

    def insert(self, i, string):
        if i < 0 or i > self.curlen:
            raise Exception("插入位置不合法")
        new_capacity = self.curlen + string.length()
        self.allocate(new_capacity)
        for j in range(self.curlen - 1, i - 1, -1):
            self.strValue[j + string.length()] = self.strValue[j]
        for j in range(i, i + string.length()):
            self.strValue[j] = string.charAt(j - i)  # j-i就是0,1,2,3,4,5,...
        self.curlen = new_capacity

    def delete(self, begin, end):
        if begin < 0 or end > self.curlen or begin >= end:
            raise Exception("参数不合法")
        self.strValue = self.strValue[0:begin] + self.strValue[end:self.curlen]  # 注意书上的写错了，这里不是self.strValue[i]
        self.curlen -= (end - begin)

    def concat(self, string):
        self.insert(self.curlen, string)

    def compareTo(self, string):
        length = string.length()
        n = self.curlen if self.curlen > length else length
        for i in range(n):
            if self.strValue[i] > string.charAt(i):
                return 1
            elif self.strValue[i] < string.charAt(i):
                return -1
        if self.curlen > length:
            return 1
        elif self.curlen < length:
            return -1
        else:
            return 0

    def indexOf(self, string, begin):  # 相关代码在串的模式匹配
        #见kmp
        pass

    @staticmethod
    def next(self,p):
        next = [0] * p.length()
        k = 0
        j = 1
        next[0] = -1
        next[1] = 0
        while j < p.length() - 1:
            if p.charAt(j) == p.charAt(k):
                next[j + 1] = k + 1
                k += 1
                j += 1
            elif k == 0:
                next[j + 1] = 0
                j += 1
            else:
                k = next[k]
        return next

    def kmp(self,p,begin):
        next = SqString.next(self,p)
        i = begin
        j = 0
        while i < self.curlen and j < p.length():
            if j == -1 or self.strValue[i] == p.charAt(j):
                j += 1
                i += 1
            else:
                j = next[j]
        if j == p.length():
            return i-j
        else:
            return -1

    def BF(self,string,begin):
        length = string.length()
        if string is not None and self.curlen > 0 and string.length() <= self.curlen:
            i = begin
            length = string.length()
            while i <= self.curlen - length:
                for j in range(length):
                    if string.charAt(j) != self.strValue[j+i]:
                        i+=1
                        break
                    elif j == length - 1:
                        return i
        return -1


    def display(self):
        for i in range(self.curlen):
            print(self.strValue[i], end=" ")


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

