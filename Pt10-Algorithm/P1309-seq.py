n = int(input())


for _ in range(n):
    l = list(input())
    dp = [1] * len(l)
    dp[0] = 1

    for i in range(len(l)):
        for j in range(i):
            if l[j] < l[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))