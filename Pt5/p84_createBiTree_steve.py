from Pt5.p77_BiTree import BiTreeNode


def build(preorder, inorder):
    if not preorder:
        return None
    pivot = preorder[0]                    # 先序第一个 = 根
    idx = inorder.index(pivot)             # 在中序里找到根的位置
    root = BiTreeNode(pivot)
    root.lchild = build(preorder[1:idx+1], inorder[:idx])      # 左子树
    root.rchild = build(preorder[idx+1:], inorder[idx+1:])     # 右子树
    return root