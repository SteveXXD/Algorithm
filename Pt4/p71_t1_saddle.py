from utils import PriorityQueue
from p69_1_transpose import transpose

#貌似行和列命名是错的，不过无所谓了
#排序实际上不是必要的，只是我想尝试优先队列（堆排序）
#直接取最大/最小值的代码见p71_t1_saddle_pro.py
#时间复杂度O(mn),没有什么最坏情况
'''
class MatrixNode(object):
    def __init__(self,value,row,col):
        self.value = value
        self.row = row
        self.col = col

class Matrix(object):#是一个list，存储元素是MatrixNode
    def __init__(self,m):
        self.data = list()
        for i in m:
            for j in m[i]:
                tmp = list()
                tmp.append(MatrixNode(m[i][j],i,j))
            self.data[i] = tmp
'''


def col_m(m):#matrix:PythonList
    col_max = list()
    for l in m:
        col_max.append(sort(l)[0])
    return col_max #列出列最大值表

def row_m(m):#matrix:PythonList
    reversed_max = transpose(m)
    row_max = list()
    for l in reversed_max:
        row_max.append(sort(l)[len(l) - 1])
    return row_max #列出列最大值表

def sort(l):#输入:PythonList
    temp = PriorityQueue()
    new_list = []
    for ch in l:
        temp.offer(ch,ch)
    for i in range(temp.length()):
        new_list.append(temp.poll())
    return new_list#输出:排序后的PythonList

def saddle_point(matrix):
    c = col_m(matrix)
    r = row_m(matrix)
    rw = 0
    cw = 0
    for row in c:
        rw += 1
        cw = 0
        for col in r:
            cw += 1
            if row == col:
                print(f"马鞍点:({rw},{cw})")

A = [
    [6, 3, 8, 9],
    [2, 7, 5, 4],
    [10, 11, 12, 13],
    [1, 14, 15, 16],
]
test_matrix = ([[1,2,4,5],[2,3,5,1],[4,5,6,6,],[5,6,2,9],[7,8,7,8],[8,1,1,3],[7,3,3,2]])
saddle_point(A)