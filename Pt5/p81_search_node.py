def searchNode(t,x):
    if t is None:
        return None
    if t.data == x:
        return t
    else:
        l_result = searchNode(t.lchild,x)
    if l_result is None:
        return searchNode(t.rchild,x)
    else:
        return l_result