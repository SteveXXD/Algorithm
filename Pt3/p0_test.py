from p34_sqstack import SqStack

stack1 = SqStack(999)
stack1.push("a")
stack1.push("b")
stack1.push("c")
stack1.push("(")
stack1.push("b")
stack1.push(")")

temp = stack1.pop()

while temp != "(":
    temp = stack1.pop()

stack1.display()