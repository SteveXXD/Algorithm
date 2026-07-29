#P32 链表集合类的差集操作
from p16_linear_list import IList

class Node(object):
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class LinkList(IList):
    def __init__(self):
        self.newList = None
        self.head = Node()

    def inList(self,x):
        #print("hooked contains")
        p = self.head
        j = -1
        while p is not None:
            if p.data == x:
                return True
            j += 1
            p = p.next
        return False

    def create(self,l,order):
        if order:
            self.create_tail(l)
        else:
            self.create_head(l)

    def create_tail(self,l): #尾插法
        for item in l:
            if not self.inList(item):
                self.insert(self.length(),item)
            else:
                pass


    def create_head(self,l): #头插法
        pass

    def clear(self):
        pass

    def isEmpty(self):
        pass

    def length(self):
        """返回线性表的长度"""
        p = self.head.next
        length = 0
        while p is not None:
            p = p.next
            length += 1
        return length

    def get(self,i):
        pass

    def insert(self,i,x): #带头节点的插入
        """插入x作为第i个元素"""
        p = self.head
        j = -1
        while p is not None and j < i - 1:
            p = p.next
            j += 1
        if j > i -1 or p is None:
            raise Exception("插入位置不合法")
        s = Node(x,p.next)
        p.next = s#几乎完成

    def delete(self,item):
        idx = self.indexOf(item)
        if idx != -1:
            self.remove(idx)

    def minus(self,linklist):
        self.newList = LinkList()
        k = self.head.next
        while k is not None:
            self.newList.insert(self.newList.length(),k.data)
            k = k.next
        p = linklist.head.next
        while p is not None:
            self.newList.delete(p.data)
            p = p.next
        return self.newList

    def remove(self,i):
        """删除第i个元素"""
        p = self.head
        j = -1
        #寻找第i个节点的前驱节点
        while p is not None and j < i - 1:
            p = p.next
            j += 1
        if j > i - 1 or p.next is None:
            raise Exception("删除位置不合法")
        p.next = p.next.next

    def indexOf(self,x):
        """返回元素x首次出现的位序号"""
        p = self.head.next
        j = 0
        while p is not None and not (p.data == x):
            p = p.next
            j += 1
        if p is not None:
            return j
        else:
            return -1

    def display(self):
        """输出线性表中各个元素的值"""
        p = self.head.next
        while p is not None:
            print(p.data,end = " ")
            p = p.next

data = [1,1,2,3,4,5,5,6,7,7,8]
ll = LinkList()
ll.create(data,True)
data2 = [1,2,2,9]
ll2 = LinkList()
ll2.create(data2,True)
ll.minus(ll2).display()