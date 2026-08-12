from Pt3.p36_linkStack import LinkStack


def postOrder2(root):
    p = root()
    s1 = LinkStack()
    s2 = LinkStack()
    while (not s1.isEmpty()) or (p is not None):
        while p is not None:
            s1.push(p)
            s2.push(p)
            p = p.rchild
        p = s1.pop()
        p = p.lchild
    while not s2.isEmpty():
        print(s2.pop().data,end=" ")
