from Pt3.p36_linkStack import LinkStack

#满二叉树的先序遍历
def preOrder(root):
    p = root
    s = LinkStack()
    while p is not None:
        print(p)
        if p.lchild is None:
            p = s.pop()
        else:
            s.push(p.rchild)
            p = p.lchild