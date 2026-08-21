import math

from Pt6.p95_igraph import IGraph


class VNode(object):
    def __init__(self,data = None,firstNode = None):
        self.data = data
        self.firstArc = firstNode

class ArcNode(object):
    def __init__(self,adjVex,value,nextArc = None):
        self.adjVex = adjVex
        self.value = value
        self.nextArc = nextArc

class ALGraph(IGraph):

    GRAPHKIND_UDG = 'UDG'
    GRAPHKIND_DG = 'DG'
    GRAPHKIND_DN = 'DN'
    GRAPHKIND_UDN = 'UDN'

    def __init__(self,kind = None,vNum = 0,eNum = 0,v = None,e = None):
        self.kind = kind
        self.v = v
        self.e = e
        self.vNum = vNum
        self.eNum = eNum

    def createUDG(self):
        v = self.v
        self.v = [None] * self.vNum
        for i in range(self.vNum):
            self.v[i] = VNode(v[i])
        for i in range(self.eNum):
            a,b = self.e[i]
            u,v = self.locateVex(a),self.locateVex(b)
            self.addArc(u,v,1)
            self.addArc(v,u,1)

    def createDG(self):
        v = self.v
        self.v = [None] * self.vNum
        for i in range(self.vNum):
            self.v[i] = VNode(v[i])
        for i in range(self.eNum):
            a,b = self.e[i]
            u,v = self.locateVex(a),self.locateVex(b)
            self.addArc(u,v,1)

    def createUDN(self):
        v = self.v
        self.v = [None] * self.vNum
        for i in range(self.eNum):
            a,b,w = self.e[i]
            u,v = self.locateVex(a),self.locateVex(b)
            self.addArc(u,v,w)
            self.addArc(u,v,w)

    def createDN(self):
        v = self.v
        self.v = [None] * self.vNum
        for i in range(self.eNum):
            a,b,w = self.e[i]
            u,v = self.locateVex(a),self.locateVex(b)
            self.addArc(u,v,w)

    def addArc(self,i,j,value):
        arc = ArcNode(j,value)
        arc.nextArc = self.v[i].firstArc
        self.v[i].firstArc = arc

    def createGraph(self):
        pass

    def getVNum(self):
        return self.vNum

    def getENum(self):
        return self.eNum

    def getVex(self, i):
        if i < 0 or i >= self.vNum:
            raise Exception("不存在该顶点")
        return self.v[i].data


    def locateVex(self, x):
        for i in range(self.vNum):
            if self.v[i].data == x:
                return i
        return -1

    def getArcs(self,u,v):
        """返回顶点距离"""
        if u < 0 or u >= self.vNum:
            raise Exception("节点不存在")
        if v < 0 or v >= self.vNum:
            raise Exception("节点不存在")
        p = self.v[u].firstArc
        while p is not None:
            if p.adjVex == v:
                return p.value
            p = p.nextArc
        return math.inf


    def firstAdj(self, i):
        if i < 0 or i >= self.vNum:
            raise Exception("节点不存在")
        p = self.v[i].firstArc
        if p is not None:
            return p.adjVex
        return -1

    def nextAdj(self, i, j):
        if i < 0 or i >= self.vNum:
            raise Exception("节点不存在")
        p = self.v[i].firstArc
        while p is not None:
            if p.adjVex == j:
                break
            p = p.nextArc
        if p is not None and p.nextArc is not None:
            return p.nextArc.adjVex
        return -1