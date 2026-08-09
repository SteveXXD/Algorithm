from p61_kmp_minus_1 import SqString

class SeqString(SqString):
    def string_count(self,string):#我第一次写的拼凑版本
        count = 0
        i = 0
        if self.kmp(string,0) == 0:
            count += 1#因为不知道为什么会跳过第一个导致count少一个所以写了这个神秘判断
        while i < self.curlen - string.length():
            i = self.kmp(string, i + 1)
            if i == -1:
                return count
            else:
                count += 1
        return count

    def string_count_fixed(self,string):#精简版本
        count = 0
        i = 0
        while True:
            i = self.kmp(string,i)
            if i == -1:
                break
            count += 1
            i += 1#跳过本次匹配位置
        return count

string2 = SeqString("abc")
string1 = SeqString("abcabcabc")
print(string1.string_count(string2))
print(string1.string_count_fixed(string2))