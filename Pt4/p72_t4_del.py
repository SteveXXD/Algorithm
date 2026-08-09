
from p61_kmp_minus_1 import SqString

class SeqString(SqString):
    def delete_all_char(self,ch):#没有用列表推导式的比较绕的方法
        tmp = list()
        for c in self.strValue:
            tmp.append(c)#先赋值一份
        self.strValue = list()
        self.curlen = 0
        for c in tmp:
            if c != ch:
                self.curlen += 1
                self.strValue.append(c)

    def delete_all_char_revised(self, ch):#使用列表推导式的简单方法
        self.strValue = [c for c in self.strValue if c != ch]
        self.curlen = len(self.strValue)

    def delete_all_char_pointer(self, ch):#快慢指针,更省空间
        k = 0
        for c in self.strValue:#c跑得一直比k快
            if c != ch:
                self.strValue[k] = c
                k += 1
        self.curlen = k
        # 收尾：把尾巴上残留的旧值抹掉
        for i in range(k, len(self.strValue)):
            self.strValue[i] = None

string1 = SeqString("helloworld")
string1.delete_all_char("l")
string1.display()