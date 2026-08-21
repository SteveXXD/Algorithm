#P17与P18给出的顺序表类的python语言实现

from utils_p16_linear_list import IList

class ListNode(object):
    def __init__(self,data,key):
        self.data = data
        self.key = key


class SqList(IList): #继承linear_list里面的IList

    def __init__(self,maxsize):
        self.curlen = 0 #顺序表的当前长度
        self.maxSize = maxsize  #顺序表的最大长度
        self.listItem = [None] * self.maxSize   #顺序表的存储空间

    def clear(self):
        """将线性表置为空表"""
        self.curlen = 0

    def isEmpty(self):
        return self.curlen == 0

    def length(self):
        """返回线性表的长度"""
        return self.curlen

    def get(self,i):
        """读取并返回线性表的第i个数据元素"""
        if i < 0 or i>self.curlen:
            raise Exception(f"第{i}个元素不存在")
        return self.listItem[i]

    def insert(self,i,x):
        """插入x作为第i个元素"""
        if self.curlen == self.maxSize:
            raise Exception("顺序表已满")
        if i < 0 or i > self.maxSize:
            raise Exception("插入位置不合法")
        for j in range(self.curlen,i-1,-1):
            self.listItem[j] = self.listItem[j-1]
        self.listItem[i] = x
        self.curlen += 1

    def remove(self,i):
        """删除第i个元素"""
        if i < 0 or i > self.curlen - 1:
            raise Exception("删除位置不合法")
        for j in range(i,self.curlen):
            self.listItem[j] = self.listItem[j+1]
        self.curlen -= 1


    def indexOf(self,x):
        """返回x首次出现时的序号"""
        for i in range(self.curlen):
            if self.listItem[i].data == x:
                return i
        return -1

    def display(self):
        for i in range(self.curlen):
            print(self.listItem[i],end = "")


    def binarySearch(self,key):
        if self.curlen > 0:
            low = 0
            high = self.curlen - 1
            while low <= high:
                mid = (low+high)//2
                if self.listItem[mid].key == key:
                    return mid
                elif self.listItem[mid].key < key:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
    #O(lbn)



