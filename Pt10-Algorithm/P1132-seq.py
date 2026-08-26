#f(n) = f(n-1)*9 + 10**(n-1)
#f(1) = 1

import sys
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    dp = [-1] * n
    dp[0] = 1

    for i in range(1, n):
        dp[i] = dp[i - 1] * 9 + 10 ** i

    print(dp[n - 1])