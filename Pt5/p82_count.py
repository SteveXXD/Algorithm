def nodeCount(t):
    count = 0
    if t is not None:
        count += 1
        count += nodeCount(t.lchild)
        count += nodeCount(t.rchild)
    return count