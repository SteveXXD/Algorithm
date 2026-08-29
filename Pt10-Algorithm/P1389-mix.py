import sys

sq = [i*i for i in range(1,21)]
dp = [0] * 1000
dp[0] = 1
for s in sq:
    for j in range(s,500):
        dp[j] += dp[j-s]

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    print(dp[int(line)])