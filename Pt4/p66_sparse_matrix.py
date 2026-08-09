class TripleNode(object):
    def __init__(self,row = 0,column = 0,value = 0):
        self.row = row
        self.column = column
        self.value = value

class SparseMatrix(object):
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.data = [None] * self.maxSize
        for i in range(self.maxSize):
            self.data[i] = TripleNode()
        self.rows = 0
        self.cols = 0
        self.nums = 0

    def create(self,mat):
        count = 0
        self.rows = len(mat)
        self.cols = len(mat[0])
        for i in range(self.rows):
            for j in range(self.cols):
                if mat[i][j] != 0:
                    count += 1
        self.nums = count
        self.data = [None] * self.nums
        k = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if mat[i][j] != 0:
                    self.data[k] = TripleNode(i,j,mat[i][j])
                    k += 1


#将原大小为90的稀疏矩阵压缩为10

matrixColumn = [0,1,0,0,0,0,0,0,0,0]
matrix1 = [0] * 10

for j in range(10):
    matrix1[j] = matrixColumn

sparse_matrix1 = SparseMatrix(91)
sparse_matrix1.create(matrix1)
print(sparse_matrix1.nums)
