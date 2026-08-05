#递归算斐波那契数列
#效率非常低!建议使用缓存递归

def fib(n):
    if n >= 3:
        return fib(n-1) + fib(n-2)
    elif n == 2:
        return 1
    else:
        return 0

for i in range(1,10):
    print(fib(i))