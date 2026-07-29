#P32 约瑟夫问题 顺序表解法（官方解法）
from p18_python_list import SqList

def Jos(m,n):
    index = 0
    sq = SqList(999)

    for i in range(1,n+1):
        sq.insert(sq.curlen,i)

    while not sq.isEmpty():
        index = (index + m - 1) % sq.curlen
        print(sq.get(index))
        sq.remove(index)

Jos(4,8)