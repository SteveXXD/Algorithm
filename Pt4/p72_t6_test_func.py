from p61_kmp_minus_1 import SqString

class SeqString(SqString):
    def test(self):#测试所有函数
        s = SqString("hello world")
        # clear / isEmpty
        s2 = SqString()
        assert s2.isEmpty()
        # length / charAt
        assert s.length() == 11
        assert s.charAt(0) == 'h'
        assert s.charAt(10) == 'd'
        # subString
        sub = s.subString(6, 11)
        assert "".join(sub.strValue) == "world"
        # insert / delete
        s.insert(5, SqString(","))
        assert "".join(s.strValue) == "hello, world"
        s.delete(5, 6)
        assert "".join(s.strValue) == "hello world"
        # concat
        s.concat(SqString("!"))
        assert "".join(s.strValue) == "hello world!"
        # compareTo
        assert s.compareTo(SqString("hello world!")) == 0
        assert s.compareTo(SqString("aaa")) == 1
        # kmp / BF
        assert s.kmp(SqString("world"), 0) == 6
        assert s.BF(SqString("world"), 0) == 6
        # allocate 间接被 insert 触发
        print("全部测试通过 ✔")


string1 = SeqString()
string1.test()

#clear  isEmpty  length  charAt  allocate  subString  insert  delete
#concat  compareTo  kmp  BF

