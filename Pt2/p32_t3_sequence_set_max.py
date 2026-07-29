#P32 第三题 最大项

from p16_linear_list import IList

class SequenceSet(IList): #继承linear_list里面的IList

    def __init__(self,a):
        self.maxSize = int(len(a) * 1.5)
        self.listItem = [None] * self.maxSize
        i = 0
        for items in a:
            if self.isItem(items):
                pass
            else:
                self.listItem[i] = items
                i += 1

    def isItem(self,x):
        for i in self.listItem:
            if x == i:
                return True
        return False

    def maxItem(self):
        m = self.listItem[0]
        for i in self.listItem:
            if i is not None:
                if i > m:
                    m = i
            else:
                pass
        return m

#1,2,3,4,5,6,7
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

    def remove(self,i):
        pass

    def indexOf(self,x):
        pass

    def display(self):
        pass


ll = SequenceSet([1000,5,3,100,4])
print(ll.maxItem())