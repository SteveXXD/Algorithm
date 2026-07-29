#P32第五题 差集的实现

from p16_linear_list import IList

class SequenceSet(IList): #继承linear_list里面的IList

    def __init__(self,a):
        self.newList = None
        self.curlen = 0
        self.maxSize = int(len(a) * 1.5)
        self.listItem = [None] * self.maxSize
        i = 0
        for items in a:
            if self.isItem(items):
                pass
            else:
                self.listItem[i] = items
                i += 1
                self.curlen += 1

    def isItem(self,x):#什么，这不是一个普通的函数，这是一个判断函数
        for i in range(0,self.curlen):#那么就有人要问了为什么不用in关键字
            if x == self.listItem[i]:#因为in关键字要遍历整个数组，会遍历到None，造成一些糟糕的后果
                return True
        return False

    def minus(self,x):#差集
        self.newList = []
        for i in range(0,self.curlen):
            self.newList.append(self.listItem[i])
        for item in x:
            if self.isItem(item):
                self.newList.remove(item)
        return SequenceSet(self.newList)


    def clear(self):
        pass

    def isEmpty(self):
        pass

    def length(self):
        pass

    def get(self,i):
        pass

    def insert(self,i,x):
        pass

    def copy(self,a):
        for items in a:
            if self.isItem(items):
                pass
            else:
                self.listItem[self.curlen] = items
                self.curlen += 1

    def remove(self,i):
        pass

    def indexOf(self,x):
        pass

    def display(self):
        for i in range(0,self.curlen):
            if self.listItem[i] is not None:
                print(self.listItem[i],end = " ")

ll = SequenceSet([1,5,3,100,4])
ll.minus([1,5]).display()