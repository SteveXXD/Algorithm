#斐波那契迭代版

def fib(n):
    a = 0
    b = 1
    for i in range(n-1):
        a,b = b,a+b
    return a

for i in range(1,10):
    print(fib(i))