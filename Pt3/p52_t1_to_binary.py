#进制转换，栈的作用主要是存储
#这个算法的底层原理可以查一下

from p34_sqstack import SqStack

def transform(num,x):
    stack1 = SqStack(99)
    while num != 0:
        t = num % x
        stack1.push(t)
        num //= x
    stack1.display()

transform(114514,2) #x是进制,x=2就转换成二进制