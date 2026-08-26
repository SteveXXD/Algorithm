N = int(input())

class Stack:
    def __init__(self):
        self.l = []
        self.len = 0
    def push(self,x):
        self.l.append(x)
        self.len += 1
    def pop(self):
        tmp = []
        while self.len > 0:
            tmp = [self.l.pop()]
            self.len -= 1
        return tmp
    def peek(self):
        if self.len == 0:
            return -1
        else:
            return self.l[0]

def zp(c):
    res = []#存储结果的列表
    s = Stack()#新建栈
    i = 0#初始化指针
    while i < len(c):
        if c[i] != s.peek():
            if s.len != 1:
                res.append(str(s.len))
            res += s.pop()
        s.push(c[i])
        i+=1
    if s.len > 1:
        res.append(str(s.len))
        res += s.pop()
    else:
        res+=s.pop()
    return res


for _ in range(N):
    l = input()
    print("".join(zp(l)[1:]))
