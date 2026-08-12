from Pt3.p45_LinkQueue import LinkQueue


def order(root):
    q = LinkQueue()
    q.offer(root)
    while not q.isEmpty():
        p = q.poll()
        print(p.data,end="")
        if p.lchild is not None:
            q.offer(p.lchild)
        if p.rchild is not None:
            q.offer(p.rchild)

