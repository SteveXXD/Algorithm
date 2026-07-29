#P19给出的插入算法

def insert(self,i,x):
    """插入x作为第i个元素"""
    if i < 0 or i >self.curlen: #判断参数的值是否满足
        raise Exception("插入位置非法")
    if self.curlen == self.maxSize:
        raise Exception("顺序表已满") #判断顺序表的存储空间是否已满
    for j in range(self.curlen,i-1,-1):
        self.listItem[j] = self.listItem[j-1] #将插入位置及之后的元素后移一个存储位置
    self.curlen += 1 #在位置处插入新的元素
    self.listItem[i] = x #表长加1

#注意:这段代码跑不起来
#与书上文件中的内容可能略有出入，因为我重新写了一遍。
#↑下同
#由概率分析得出该算法的时间复杂度为O(n)
