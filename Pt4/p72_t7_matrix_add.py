from p66_sparse_matrix import SparseMatrix,TripleNode

def merge(A,B):
    i = 0
    j = 0
    res = []
    while i < A.nums and j < B.nums:
        if (A.data[i].row,A.data[i].column) == (B.data[j].row,B.data[j].column):
            if A.data[i].value + B.data[j].value != 0:
                res.append(TripleNode(A.data[i].row,A.data[i].column,A.data[i].value + B.data[j].value))
            i += 1
            j += 1
        elif (A.data[i].row,A.data[i].column) <= (B.data[j].row,B.data[j].column):
            res.append(A.data[i])
            i += 1
        else:
            res.append(B.data[j])
            j += 1
    while i < A.nums:
        res.append(A.data[i])
        i += 1
    while j < B.nums:
        res.append(B.data[j])
        j += 1
    matrix_new = SparseMatrix(A.maxSize)
    matrix_new.data = res
    matrix_new.rows = A.rows
    matrix_new.cols = A.cols
    matrix_new.nums = len(res)
    return matrix_new

matA = [[0, 0, 3],
        [1, 0, 0],
        [0, 2, 0]]
matB = [[0, 4, 0],
        [0, 0, 0],
        [0, 2, 5]]
A = SparseMatrix(10); A.create(matA)
B = SparseMatrix(10); B.create(matB)
merge(A,B).display()