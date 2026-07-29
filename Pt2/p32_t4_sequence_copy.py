#P32第四题 copy的实现

from p16_linear_list import IList

class SequenceSet(IList): #继承linear_list里面的IList

    def __init__(self,a):
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

    def isItem(self,x):
        for i in range(0,self.curlen):
            if x == self.listItem[i]:
                return True
        return False

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
ll.copy([6,6,7])
ll.display()