#前缀转后缀，详细的可以自己查。

from p34_sqstack import SqStack

prior = {"+":1,"-":1,"*":2,"/":2}

def infix_to_postfix(expr):
    stack1 = SqStack(999)
    output = str()

    for ch in expr:
        print(output)
        if not ch in  "(*/+-)":#如果是字母，直接推
            output += ch
        else:#运算符号的进一步判断
            if ch == "(":#前括号
                stack1.push("(")
            elif ch == ")":#后括号
                temp = stack1.pop()
                while temp != "(":
                    output += temp
                    temp = stack1.pop()
            else:#是加减乘除符号
                if stack1.isEmpty():#栈为空的情况
                    stack1.push(ch)#推送
                elif stack1.peek() in "*/+-":#栈不为空且栈顶为运算符
                    while (not stack1.isEmpty()
                           and stack1.peek() != "("
                           and prior[stack1.peek()] >= prior[ch]):
                        output += stack1.pop()
                    stack1.push(ch)
                else:#栈顶为前括号"("
                    stack1.push(ch)
    while not stack1.isEmpty():
        output += stack1.pop()
    return output

print(infix_to_postfix("a+b+c*e/f+a-d"))


'''

((a * (b+c)) - (d/e))

a*(b+c) - d/e
abc+*de/-

assert infix_to_postfix("a+b*c")     == "abc*+"
assert infix_to_postfix("(a+b)*c")   == "ab+c*"
assert infix_to_postfix("a+b*(c-d)/e") == "abcd-*e/+"
assert infix_to_postfix("a+b-c")     == "ab+c-"   # 同级从左到右!



从左到右扫：
  操作数(a,b,c...) → 直接输出
  ( → 压栈
  ) → 弹栈输出直到遇到(
  运算符 → 栈顶优先级 >= 它？弹栈输出；然后自己压栈
优先级: */ = 2, +- = 1
扫完 → 栈里全弹出

这规则的意思是：遇到右括号 )，说明括号里的内容结束了，要把括号里"攒着"的运算符全部倒出来。
用 (a+b)*c走一遍（关键在 )那一步）：


扫 (  → 压栈          栈: [(]        输出: 
扫 a  → 输出          栈: [(]        输出: a
扫 +  → 压栈          栈: [(, +]     输出: a
扫 b  → 输出          栈: [(, +]     输出: ab

扫 )  ← 关键一步:
       弹栈, 弹出+ → 输出           输出: ab+
       继续弹, 弹出( → 丢弃(不输出)  栈清空
       # 弹到(为止, (本身扔掉

扫 *  → 压栈          栈: [*]        输出: ab+
扫 c  → 输出                         输出: ab+c
结束  → 弹出*                        输出: ab+c*
结果: ab+c*

拆开理解规则c：
弹栈输出, 直到弹出"(" 
= ① 弹出栈顶元素加入输出（这些是括号里的运算符 +）
  ② 一直弹，直到弹出"(" 
  ③ "(" 本身不输出，直接丢弃
'''