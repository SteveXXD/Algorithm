from Pt5.p77_BiTree import BiTreeNode, BiTree

#说实话,书上这个写得很恶心
#有一个接近人类一点的切片版，在p84_createBiTree_steve.py

def createBiTree(preorder,inorder):
    pre_len = len(preorder)
    in_len = len(inorder)
    if pre_len != in_len:
        raise Exception("数据输入错误")
    root = __create_bi_tree(preorder,0,pre_len - 1,inorder,0,in_len - 1)
    return BiTree(root)

def __create_bi_tree(preorder,pre_left,pre_right,inorder,in_left,in_right):
    if pre_left > pre_right or in_left > in_right:
        return None
    pivot = preorder[pre_left]
    pivot_index = in_left
    while inorder[pivot_index] != pivot:
        pivot_index += 1
    root = BiTreeNode(pivot)
    root.lchild = __create_bi_tree(preorder,pre_left+1,pre_left+pivot_index - in_left,inorder,in_left,pivot_index -1)
    root.rchild = __create_bi_tree(preorder,pre_left+pivot_index-in_left+1,pre_right,inorder,pivot_index+1,in_right)

    return root