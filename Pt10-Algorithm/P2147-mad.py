n = int(input())

for _ in range(n):
    t = int(input())
    a = list(input())
    a.sort()
    i = 0
    while "acg" in "".join(a):
        if a[i] == "a" and a[i+1] == "c":
            a[i],a[i+1] = a[i+1],a[i]
            i += 1
        if i >= t - 2:
            i = 0
    print("".join(a))


