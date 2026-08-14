n = 15
for i in range(n):
    l, r = 2*i+1, 2*i+2
    print(i, "的孩子:", l if l < n else "-", r if r < n else "-")