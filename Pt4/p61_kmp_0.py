#这是0派的kmp，常见于严蔚敏的教材中

from p53_string import IString


class SqString(IString):
    def __init__(self, obj=None):
        if obj is None:
            self.strValue = []
            self.curlen = 0

        elif isinstance(obj, str):
            self.curlen = len(obj)
            self.strValue = [None] * self.curlen
            for i in range(self.curlen):
                self.strValue[i] = obj[i]

        elif isinstance(obj, list):
            self.curlen = len(obj)
            self.strValue = [None] * self.curlen
            for i in range(self.curlen):
                self.strValue[i] = obj[i]

    def clear(self):
        self.curlen = 0

    def isEmpty(self):
        return self.curlen == 0

    def length(self):
        return self.curlen

    def charAt(self, i):
        if i < 0 or i > self.curlen:
            raise Exception("检索序号不在范围内")
        return self.strValue[i]

    def allocate(self, new_capacity):
        tmp = self.strValue
        self.strValue = [None] * new_capacity
        for i in range(self.curlen):
            self.strValue[i] = tmp[i]

    def subString(self, begin, end):
        if begin < 0 or begin >= end or end > self.curlen:
            raise Exception("参数不合法")
        tmp = [None] * (end - begin)
        for i in range(begin, end):
            tmp[i - begin] = self.strValue[i]
        return SqString(tmp)

    def insert(self, i, string):
        if i < 0 or i > self.curlen:
            raise Exception("插入位置不合法")
        new_capacity = self.curlen + string.length()
        self.allocate(new_capacity)
        for j in range(self.curlen - 1, i, -1):
            self.strValue[j + string.length()] = self.strValue[j]
        for j in range(i, i + string.length()):
            self.strValue[j] = string.charAt(j - i)  # j-i就是0,1,2,3,4,5,...
        self.curlen = new_capacity

    def delete(self, begin, end):
        if begin < 0 or end > self.curlen or begin >= end:
            raise Exception("参数不合法")
        self.strValue = self.strValue[0:begin] + self.strValue[end:self.curlen]
        self.curlen -= (end - begin)

    def concat(self, string):
        self.insert(self.curlen, string)

    def compareTo(self, string):
        length = string.length()
        n = self.curlen if self.curlen > length else length
        for i in range(n):
            if self.strValue[i] > string.charAt(i):
                return 1
            elif self.strValue[i] < string.charAt(i):
                return -1
        if self.curlen > length:
            return 1
        elif self.curlen < length:
            return -1
        else:
            return 0

    def indexOf(self, string, begin):  # 相关代码在串的模式匹配
        # 见kmp0
        pass

    # ================= 0派KMP =================
    # 0派：用占位符把模式串变成1-based（pp = " " + p）
    # next下标从1开始，next[1]=0（哨兵），next[i] = 前i-1个字符最长相等前后缀长度 + 1
    @staticmethod
    def get_next0(p):
        m = p.length()
        nxt = [0] * (m + 1)              # nxt[1..m] 有效，nxt[0] 弃用
        pp = " " + "".join(p.strValue)   # 占位符模拟1-based
        nxt[1] = 0
        i = 1
        j = 0
        while i < m:
            if j == 0 or pp[i] == pp[j]: # j==0 是哨兵：退无可退，直接进1
                i += 1
                j += 1
                nxt[i] = j
            else:
                j = nxt[j]               # 失配回退，和-1派同款
        return nxt

    def kmp0(self, p, begin):
        # 主串保持0-based，模式串占位符1-based；哨兵 j==0
        nxt = SqString.get_next0(p)
        m = p.length()
        pp = " " + "".join(p.strValue)
        i = begin
        j = 1
        while i < self.curlen and j <= m:
            if j == 0 or self.strValue[i] == pp[j]:
                j += 1
                i += 1
            else:
                j = nxt[j]
        if j > m:
            return i - m                 # 0-based 起始位置
        return -1

    def display(self):
        for i in range(self.curlen):
            print(self.strValue[i], end=" ")


string1 = SqString("ababaab")
string2 = SqString("abaab")
string1.display()
print("")
string2.display()
print("")
print("0派 kmp0 :", string1.kmp0(string2, 0))
print("0派 next :", SqString.get_next0(string2)[1:])
