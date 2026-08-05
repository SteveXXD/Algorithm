from p34_sqstack import SqStack

def infix_to_postfix(expr):
    stack1 = SqStack(999)
    output = str()
    in_stack = False
    for ch in expr:
        if not ch in  "(*/+-)":
            output += ch
        else:
            if ch == "(":
                stack1.push("(")
                in_stack = True






'''
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