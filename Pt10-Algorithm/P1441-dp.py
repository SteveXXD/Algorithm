T = int(input())

for _ in range(T):
    items = []
    N,V = map(int,input().split())
    for _ in range(N):
        c,w = map(int,input().split())
        items.append((c,w))
    dp = [0]*(V+1)
    for w,v in items:
        for j in range(w,V+1):
            dp[j] = max(dp[j],dp[j-w]+v)
    print(dp[V])