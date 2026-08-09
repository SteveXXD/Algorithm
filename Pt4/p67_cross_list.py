#稀疏矩阵的十字链表存储
from os import close


class OLNode(object):
    def __init__(self,row = 0,col = 0,value = 0):
        self.row = row
        self.col = col
        self.value = value
        self.right = None
        self.left = None

class CrossList(object):
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.nums = 0

        self.r_head = [None] * rows
        self.c_head = [None] *cols