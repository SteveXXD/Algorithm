#P32 第7题 约瑟夫问题 顺序表解决方式
from p18_python_list import SqList

mainList = SqList(999)
n = int(input("请输入n的值"))
m = int(input("请输入m的值"))

class Pointer(object):
    def __init__(self):
        self.p = 1
    def next(self):
        if self.p < mainList.length():
            self.p += 1
        else:
            self.p = 1
    def say(self):
        print(mainList.get(p.p - 1))
        pass

for i in range(1,n+1):
    mainList.insert(mainList.curlen,i)

p = Pointer()

while not mainList.isEmpty():
    for i in range(m - 1):
        p.next()
    if p.p != mainList.curlen:
        p.say()
        mainList.remove(p.p - 1)
    else:
        p.say()
        mainList.remove(p.p - 1)
        p.p = 1

#这是我第一次解这个题目时的方法。不是标准解法，但是勉强能用