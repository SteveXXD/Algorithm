class BiTreeNode(object):
    def __init__(self,data = None,used = None,lchild = None,rchild = None):
        self.data = data
        self.used = used
        self.lchild = lchild
        self.rchild = rchild


def createBiTree(preOrder):
    c = preOrder[0]
    if len(preOrder) == 0:
        return BiTreeNode(None,0)
    if c == "#":
        return BiTreeNode(None,1)

    lchild = createBiTree(preOrder[1:len(preOrder)])
    rchild = createBiTree(preOrder[1+lchild.used:len(preOrder)])
    root = BiTreeNode(c,lchild.used+rchild.used+1)
    root.rchild = rchild
    root.lchild = lchild
    return root