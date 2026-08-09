from p61_kmp_minus_1 import SqString

#检测是否有空格到非空格的过程
class SeqString(SqString):
    def count(self):
        in_word = False
        word = 0
        for ch in self.strValue:
            if ch != " " and not in_word:
                word += 1
                in_word = True
            elif ch == " ":
                in_word = False
        return word+1

string1 = SeqString("hello i am steve,i like playing minecraft")
print(string1.count())