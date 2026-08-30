import sys
sys.setrecursionlimit(100000)

data = sys.stdin.buffer.read().split()
idx = 0
outs = []
while idx < len(data):
    n = int(data[idx]);idx += 1
    m = int(data[idx]);idx += 1
    g = [[]for _ in range(n+1)]
    for _ in range(m):
        a = int(data[idx]);idx += 1
        b = int(data[idx]);idx += 1
        g[a].append(b)

    memo = [0] * (n+1)
    def dfs(u):
        if memo[u]:
            return memo[u]
        best = 0
        for v in g[u]:
            best = max(best,dfs(v))
        memo[u] = best + 1
        return memo[u]

    ans = 0
    for i in range(1,n+1):
        ans = max(ans,dfs(i))
    outs.append(str(ans))
print("\n".join(outs))