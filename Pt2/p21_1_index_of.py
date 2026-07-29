#P21查找操作的算法

def indexOf(self,x):
    """返回元素x首次出现的序号"""
    for i in range(self.curlen):
        if x == self.listItem[i]:
            return i
    return -1

#时间复杂度：O(n)