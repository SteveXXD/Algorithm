def getDepth(t):
    if t is None:
        return 0
    l_depth = getDepth(t.lchild)
    r_depth = getDepth(t.rchild)
    if l_depth < r_depth:
        return r_depth + 1
    else:
        return l_depth + 1
#Wh1t3Zz