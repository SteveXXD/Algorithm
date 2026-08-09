from p61_kmp_minus_1 import SqString

class SeqString(SqString):
    def test(self):#测试所有函数
        test_string = SqString("helloworld")
        self.insert(0,test_string)
        if_all_passed = False


