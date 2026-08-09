from p61_kmp_minus_1 import SqString

class SeqString(SqString):
    def reverse(self):
        rev = list()
        for i in range(self.curlen-1,-1,-1):
            rev.append(self.strValue[i])
        j = 0
        for ch in rev:
            self.strValue[j] = ch
            j += 1

string1 = SeqString("helloworld")
string1.reverse()
string1.display()
