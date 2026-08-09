from p66_sparse_matrix import SparseMatrix,TripleNode

def unfold(m):
    matrix = m
    u_matrix = list()
    for i in range(matrix.rows):
        u_matrix.append([None] * matrix.cols)

    print(u_matrix)

matrix1 = SparseMatrix(100000)
matrix1.create([[1,2,3,4,5],
                [2,3,4,5,5],
                [3,4,5,6,6],
                [4,5,6,7,7]])
unfold(matrix1)

#没写完