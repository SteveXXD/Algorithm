import sys
from abc import ABCMeta

sys.path.insert(0, r"C:\Users\ALIENWARE\PycharmProjects\Algorithm")
sys.path.insert(0, r"C:\Users\ALIENWARE\PycharmProjects\Algorithm\Pt3")
from Pt3.p36_linkStack import LinkStack


class BiTreeNode(metaclass=ABCMeta):
    def __init__(self,data = None,lchild = None,rchild = None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class BiTree(object):
    def __init__(self,root=None):
        self.root = root

    @staticmethod
    def preOrder(root):
        if root is not None:
            print(root.data,end = " ")
            BiTree.preOrder(root.lchild)
            BiTree.preOrder(root.rchild)

    @staticmethod
    def inOrder(root):
        if root is not None:
            BiTree.inOrder(root.lchild)
            print(root.data,end=" ")
            BiTree.inOrder(root.rchild)

    @staticmethod
    def postOrder(root):
        if root is not None:
            BiTree.postOrder(root.lchild)
            BiTree.postOrder(root.rchild)
            print(root.data,end = " ")

    @staticmethod
    def preOrder2(root):
        p = root
        s = LinkStack()
        s.push(p)
        while not s.isEmpty():
            p = s.pop()
            print(p.data,end = " ")
            while p is not None:
                if p.lchild is not None:
                    print(p.lchild.data,end= " ")
                if p.rchild is not None:
                    s.push(p.rchild)
                p = p.lchild




