n = int(input())
for _ in range(n):
    l = list(map(int,input().split()))
    s = sum(l[:3])
    b = l[3:]
    b.sort()
    c = b[::-1]
    s += sum(c[:3])
    print(s)