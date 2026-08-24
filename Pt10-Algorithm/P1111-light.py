n,g = map(int,input().split())

l = [True] * (n+1)
l[0] = False

for ch in range(2,g+1):
    i = ch
    k = 1
    while ch * k < len(l):
        if l[ch * k]:
            l[ch * k] = False
        else:
            l[ch * k] = True
        k += 1

a = l[1:]

for t in range(len(a)):
    if a[t]:
        print(t+1)