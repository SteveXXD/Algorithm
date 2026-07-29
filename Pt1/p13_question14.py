A = [x for x in range(100,0,-1)]
n = 50
x = 0
for i in range(n-1,0,-1):
    for j in range(0,i):
        if A[j] > A[j+1]:
            A[j],A[j+1] = A[j+1],A[j]
            x += 1
            print(x)

#推测最坏频度为O(n**2),猜的
#具体推导过程建议手写
#D老师说确实是O(n**2)