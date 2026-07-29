class DulNode(object):
    def __init__(self,data = None,prior = None,next = None):
        self.data = data
        self.prior = prior
        self.next = next

    def insert(self,i,x):
        p = self.head
        j = -1
        #寻找插入位置i
        while p is not None and j < i:
            p = p.next
            j += 1
        if j > i or p is None:
            raise Exception("插入位置不合法")
        s = DulNode(data = x)
        p.prior.next = s
        s.next = p
        s.prior = p.prior
        p.prior = s

    def remove(self,i):
        p = self.head
        j = -1
        while p is not None and j < i:
            p = p.next
            j += 1
            if j > i or p is None:
                raise Exception("删除位置不合法")
            p.prior.next = p.next
            p.next.prior = p.prior

