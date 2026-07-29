#P20的顺序表删除操作的算法

def remove(self,i):
    """删除第i个元素"""
    if i < 0 or i > self.curlen - 1:
        raise Exception("删除位置不合法")
    for j in range(i,self.curlen):
        self.listItem[j] = self.listItem[j+1]
    self.curlen -= 1

#时间复杂度:O(n)