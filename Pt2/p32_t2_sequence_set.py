#P32 第二题 实现顺序集合以及内存分配策略

from p16_linear_list import IList

class SequenceSet(IList): #继承linear_list里面的IList

    def __init__(self,a):
        self.maxSize = int(len(a) * 1.5)
        self.listItem = [None] * self.maxSize
        index = 0
        for items in a:
            if self.isItem(items):
                pass
            else:
                self.listItem[index] = items
                index += 1

    def isItem(self,x):
        for i in self.listItem:
            if x == i:
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

    def remove(self,i):
        pass

    def indexOf(self,x):
        pass

    def display(self):
        pass


ll = SequenceSet([1,5,3,100,4])

'''
for i in ll.listItem:
    if i is not None:
        print(i)
'''