n,m = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(n)]
mem = [[-1]*m for _ in range(n)]
res = []

def dfs(x,y):
    if mem[x][y] != -1:
        return mem[x][y]
    best = 1
    for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        nx,ny = x+dx,y+dy
        if nx > n-1 or ny > m-1 or nx < 0 or ny < 0:
            continue
        if maze[nx][ny] >= maze[x][y]:
            continue
        best = max(best,dfs(nx,ny) + 1)
    mem[x][y] = best
    return best

for i in range(n):
    for j in range(m):
        res.append(dfs(i,j))

print(max(res))
