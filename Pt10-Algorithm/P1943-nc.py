n,m = map(int,input().split())
res = []

for _ in range(n):
    i,s = input().split()
    res.append(s)
for _ in range(m):
    k = int(input())
    print(res[k-1])