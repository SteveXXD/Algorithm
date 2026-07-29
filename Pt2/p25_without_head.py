#不带头节点的插入
def insert(self,i,x):
    p = self.head
    j = 0
    while p is not None and j < i - 1:
        p = p.next
        j += 1
    if j > i - 1 or p is None:
        raise Exception("插入位置不合法")
    s = Node(data = x)
    if i == 0:
        s.next = self.head
    else:
        s.next = p.next
        p.next = s


class Node(object):
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next