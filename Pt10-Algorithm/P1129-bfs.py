from collections import deque
n,m = map(int,input().split())

q = deque([(0,0,[(0,0)])])
vis = [[False] * m for _ in range(n)]
vis[0][0] = True
a = [list(map(int, input().split())) for _ in range(n)]

while q:
    x,y,path = q.popleft()
    if (x,y) == (n-1,m-1):
        print(">".join(f"({x+1},{y+1})" for x,y in path))
        break
    for dx,dy in [(0,1),(1,0)]:
        nx,ny = x+dx,y+dy
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if a[nx][ny] == 0 or vis[nx][ny]:
            continue
        vis[nx][ny] = True
        q.append((nx,ny,path+[(nx,ny)]))
