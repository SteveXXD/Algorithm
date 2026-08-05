#检查代码圆括号，方括号，花括号是否匹配（第一版）

from p34_sqstack import SqStack

def check(code):
    stack = SqStack(999)
    for ch in code:
        if ch == "(":
            stack.push("(")
        elif ch == "[":
            stack.push("[")
        elif ch == "{":
            stack.push("{")
        if ch == ")":
            if not stack.peek() == "(":
                return False
            else:
                stack.pop()
        elif ch == "]":
            if not stack.peek() == "[":
                return False
            else:
                stack.pop()
        elif ch == "}":
            if not stack.peek() == "{":
                return False
            else:
                stack.pop()
    if stack.isEmpty():
        return True
    else:
        return False

print(check("{{}}(())[][]"))

