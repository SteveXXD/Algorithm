from abc import ABCMeta,abstractmethod,abstractproperty

class IGraph(metaclass = ABCMeta):
    @abstractmethod
    def createGraph(self):
        pass
    @abstractmethod
    def getVNum(self):
        pass
    @abstractmethod
    def getENum(self):
        pass
    @abstractmethod
    def getVex(self,i):
        pass
    @abstractmethod
    def locateVex(self,x):
        pass
    @abstractmethod
    def firstAdj(self,i):
        pass
    @abstractmethod
    def nextAdj(self,i,j):
        pass
