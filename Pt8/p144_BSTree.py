import math


class BiTreeNode(object):
    def __init__(self,key,data,lchild=None,rchild=None):
        self.key = key
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

class BSTree(object):
    def __init__(self,root = None):
        self.root = root

    def searchBST(self,key,p):
        if p is None:
            return None
        if key == p.key:
            return p.data
        elif key < p.key:
            return self.searchBST(key,p.lchild)
        else:
            return self.searchBST(key,p.rchild)

    def insert(self,key,data):
        p = BiTreeNode(key,data)
        if self.root is None:
            self.root = p
        else:
            self.insertBST(self.root,p)

    def insertBST(self,r,p):
        if r.key < p.key:
            if r.rchild is None:
                r.rchild = p
            else:
                self.insertBST(r.rchild,p)
        else:
            if r.lchild is None:
                r.lchild = p
            else:
                self.insertBST(r.lchild,p)

    def remove(self,key):
        self.removeBST(key,self.root,None)

    def removeBST(self,key,p,parent):
        if p is None:
            return
        if p.key > key:
            self.removeBST(key,p.lchild,p)
        elif p.key < key:
            self.removeBST(key,p.rchild,p)
        elif p.lchild is not None and p.rchild is not None:
            in_next = p.rchild
            while in_next.lchild is not None:
                in_next = in_next.lchild
            p.data = in_next.data
            p.key = in_next.key
            self.removeBST(p.key,p.rchild,p)
        else:
            if parent is None:
                if p.lchild is not None:
                    self.root = p.lchild
                else:
                    self.root = p.rchild
                return
            if p == parent.lchild:
                if p is not None:
                    parent.lchild = p.lchild
                else:
                    parent.rchild = p.rchild

            elif p == parent.rchild:
                if p.lchild is not None:
                    parent.lchild = p.lchild
                else:
                    parent.rchild = p.rchild


l = map(int,input().split())
tree1 = BSTree()

for ch in l:
    tree1.insert(ch,ch)

res = []
p = tree1.root
mn = math.inf

def inOrder(root):
    if root is not None:
        inOrder(root.lchild)
        res.append(root.data)
        inOrder(root.rchild)

inOrder(tree1.root)

for i in range(1,len(res)):
    if res[i] - res[i-1] < mn:
        mn = res[i] - res[i-1]

print(mn)