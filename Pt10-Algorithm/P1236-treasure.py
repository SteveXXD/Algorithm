m,n = map(int,input().split())
maze = []
dp = [[0] * n for _ in range(m)]
#dp[0][0] = 0

for _ in range(m):
    maze.append(list(map(int,input().split())))

for x in range(m):
    for y in range(n):
        if y-1 < 0 or x-1 < 0:
            if y == 0 and x == 0:
                continue
            if x-1 < 0:
                dp[x][y] = dp[x][y-1] + maze[x][y]
            if y-1 < 0:
                dp[x][y] = dp[x-1][y] + maze[x][y]
        else:dp[x][y] = max(dp[x-1][y],dp[x][y-1]) + maze[x][y]

res = []

for c in dp:
    res.append(max(c))

print(max(res))