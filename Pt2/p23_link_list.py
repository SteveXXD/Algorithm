#P21单链表的类描述
from p16_linear_list import IList

class Node(object):
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class LinkList(IList):
    def __init__(self):
        self.head = Node()

    def create(self,l,order):
        if order:
            self.create_tail(l)
        else:
            self.create_head(l)

    def create_tail(self,l): #尾插法
        for item in l:
            self.insert(self.length(),item)

    def create_head(self,l): #头插法
        for item in l:
            self.insert(0,item)

    def clear(self):
        """将线性表置为空表"""
        self.head.data = None
        self.head.next = None

    def isEmpty(self):
        """判断线性表是否为空表"""
        return self.head.next == None

    def length(self):
        """返回线性表的长度"""
        p = self.head.next
        length = 0
        while p is not None:
            p = p.next
            length += 1
        return length

    def get(self,i):
        """读取并返回线性表中的第i个数据元素"""
        p = self.head.next #p指向单链表的头节点
        j = 0
        #从头节点开始向后查找，直到p指向第i个节点或者p为None
        while j < i and p is not None:
            p = p.next
            j += 1
        if j > i or p is None:
            raise Exception(f"第{i}个数据元素不存在")
        return p.data

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

data = [i for i in range(10)]
ll = LinkList()
ll.create(data,True)
ll.insert(1,"hello")
ll.remove(1)
ll.display()