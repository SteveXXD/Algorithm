n = int(input())
items = []

for _ in range(n):
    t,v = map(int,input().split())
    items.append((t,v))

items.sort(key = lambda x:-x[1])
ddl = max(k for k,kk in items)

vis = [False] * (ddl+1)
s = 0
dp = [0] * (ddl + 1)

for t,v in items:
    for T in range(t,0,-1):
        if not vis[T]:
            u=vis[T] = True
            s += v
            break

print(s)

