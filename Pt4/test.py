#在这里测试各种小东西
from Pt4.p61_kmp_minus_1 import SqString

a = "abcdefg"
string1 = SqString(a)
string1.subString(0,4).display() #subString 左闭右开

b = "ab abcdefg"
c = b.split(" ")#返回一个list
print(c[1])