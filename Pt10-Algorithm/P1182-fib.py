def f(n):
    a,b = 7,11
    for i in range(n):
        a,b = b,a+b
    return a

n = int(input())
if f(n)%3 == 0:
    print("yes")
else:
    print("no")