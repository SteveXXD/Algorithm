#优化后的检查匹配

from p34_sqstack import SqStack

def check(code):
    stack = SqStack(999)
    pairs = {")":"(","]":"[","}":"{"}
    for ch in code:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if stack.peek() != pairs[ch] or stack.isEmpty():
                return False
            else:
                stack.pop()
    if stack.isEmpty():
        return True
    else:
        return False

print(check("{{}}{{}}125()()[11213]"))