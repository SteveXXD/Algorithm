from Pt3.p36_linkStack import LinkStack

def traverse(root):
    if root is None:
        return
    p = root
    s = LinkStack()
    while p is not None and not s.isEmpty():
        while p is not None:
            print(p.data,end=" ")#先序print在这
            s.push(p)
            p = p.lchild
        p = s.pop()
        #print(p.data,end=" ") #中序在这里print
        p = p.rchild