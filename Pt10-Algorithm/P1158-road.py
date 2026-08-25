N = int(input())

def dfs(x,y,step):
    global count
    if x == n-1 and y == m-1:
        count += 1
        return
    for d in [(0,1),(1,0)]:
        dx,dy = d
        nx,ny = x+dx,y+dy
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        else:
            dfs(nx,ny,step+1)

for _ in range(N):
    n,m = map(int,input().split())
    n += 1
    m += 1
    count = 0
    dfs(0,0,0)
    print(count)