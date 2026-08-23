n = int(input())
A = list(map(int,input().split()))
pre = [0]
for c in range(len(A)):
    pre.append(A[c]+pre[c])

m = int(input())
for _ in range(m):
    l,r = map(int,input().split())
    print(pre[r] - pre[l-1])