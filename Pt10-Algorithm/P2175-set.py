n = int(input())
s = set()

for _ in range(n):
    t = False
    op,x = map(int,input().split())
    if op == 1:
        s.add(x)
    if op == 2:
        s.discard(x)
    if op == 3:
        b = list(s)
        b.sort()
        for m in b:
            if m >= x:
                print(m)
                t = True
                break
        if not t:
            print(-1)