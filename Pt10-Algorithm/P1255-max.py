T = int(input())

for _ in range(T):
    l = list(map(int,input().split()))
    n = l[0]
    ls = l[1:]
    ans = ls[0]
    dp = [0] * n
    dp[0] = ls[0]
    start=end=0
    s = 0
    for i in range(1, n):
        if dp[i-1] + ls[i] >= ls[i]:
            dp[i] = dp[i-1] + ls[i]
        else:
            dp[i] = ls[i]
            s = i
        if dp[i] > ans:
            ans = dp[i]
            start = s
            end = i
        ans = max(dp[i],ans)

    print(ans,start+1,end+1)
