a,b = map(int,input().split())
s = 0

for i in range(1,a+1):
    s += i**b

print(s%10000)

#不是暴力怎么算得这么快