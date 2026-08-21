import math

from Pt6.p95_igraph import IGraph


class MGraph(IGraph):

    GRAPHKIND_UDG = 'UDG'
    GRAPHKIND_DG = 'DG'
    GRAPHKIND_DN = 'DN'
    GRAPHKIND_UDN = 'UDN'

    def __init__(self,kind = None,vNum = 0,eNum = 0,v = None,e = None):
        self.kind = kind
        self.vNum = vNum
        self.eNum = eNum
        self.v = v
        self.e = e


    def createUDG(self,vNum,eNum,v,e):
        """
        g = MGraph()
        g.createUDG(3, 2, ['A','B','C'], [('A','B'), ('B','C')])
        """
        self.vNum = vNum
        self.eNum = eNum
        self.v = [None] * vNum
        for i in range(vNum):
            self.v[i] = v[i]
        self.e = [[0 for _ in range(vNum)]for _ in range(vNum)]
        for i in range(eNum):
            a,b = e[i]
            m,n = self.locateVex(a),self.locateVex(b)
            self.e[m][n] = self.e[n][m] = 1

    def createDG(self,vNum,eNum,v,e):
        self.vNum = vNum
        self.eNum = eNum
        self.v = [None] * vNum
        for i in range(vNum):
            self.v[i] = v[i]
        self.e = [[0 for _ in range(vNum)]for _ in range(vNum)]
        for i in range(eNum):
            a,b = e[i]
            m,n = self.locateVex(a),self.locateVex(b)
            self.e[m][n] = 1

    def createUDN(self,vNum,eNum,v,e):
        self.vNum = vNum
        self.eNum = eNum
        self.v = [None] * vNum
        for i in range(vNum):
            self.v[i] = v[i]
        self.e = [[math.inf for _ in range(vNum)] for _ in range(vNum)]
        for i in range(eNum):
            a,b,w = e[i]
            m,n = self.locateVex(a),self.locateVex(b)
            self.e[m][n] = self.e[n][m] = w

    def createDN(self,vNum,eNum,v,e):
        self.vNum = vNum
        self.eNum = eNum
        self.v = [None] * vNum
        for i in range(vNum):
            self.v[i] = v[i]
        self.e = [[math.inf for _ in range(vNum)] for _ in range(vNum)]
        for i in range(eNum):
            a,b,w = e[i]
            m,n = self.locateVex(a),self.locateVex(b)
            self.e[m][n] = w

    def createGraph(self):
        pass

    def getVNum(self):
        pass

    def getENum(self):
        pass

    def getVex(self, i):
        pass

    def locateVex(self, x):
        for i in range(self.vNum):
            if self.v[i] == x:
                return i
        return -1

    def firstAdj(self,i):
        if i < 0 or i >= self.vNum:
            raise Exception("不存在该顶点")
        for j in range(self.vNum):
            if self.e[i][j] != 0 and self.e[i][j] < math.inf:
                return j
        return -1


    def nextAdj(self,i,j):
        if j == self.vNum -1:
            return -1
        for k in range(j+1,self.vNum):
            if self.e[i][k] != 0 and self.e[i][k] < math.inf:
                return k
        return -1
