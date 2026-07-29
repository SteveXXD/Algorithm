#使用顺序栈判断括号是否匹配
from p34_sqstack import SqStack

def isMatched(s):
    stack = SqStack(100)
    for c in s:
        if c == "(":
            stack.push("(")
        elif c == ")" and not stack.isEmpty():
            stack.pop()
        elif c == ")" and stack.isEmpty():
            print("括号不匹配")
            return False
    if stack.isEmpty():
        print("括号匹配")
        return True
    else:
        print("括号不匹配")
        return False

isMatched("(((114514)))")