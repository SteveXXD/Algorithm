V = int(input())
n = int(input())
item = []
dp = [0] * (V+1)

for _ in range(n):
    w,v = map(int,input().split())
    item.append((w,v))

for w,v in item:
    for j in range(V,w-1,-1):
        dp[j] = max(dp[j-w]+v,dp[j])

print(dp[V])