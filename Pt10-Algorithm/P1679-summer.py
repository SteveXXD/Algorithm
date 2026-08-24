from collections import deque

n,m = map(int,input().split())

vis = [[False] * m for _ in range(n)]
a = [list(map(int,input().split())) for _ in range(n)]
sx,sy,ex,ey = map(int,input().split())
sx -= 1
sy -= 1
ex -= 1
ey -= 1
acc = False
q = deque([(sx,sy,[(sx,sy)])])
vis[sx][sy] = True

while q:
    x,y,path = q.popleft()
    if (x,y) == (ex,ey):
        acc = True
        print(len(path) - 1)
        break
    for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        nx,ny = x+dx,y+dy
        if not (0<=nx<n and 0 <=ny < m):
            continue
        if a[nx][ny] == 1 or vis[nx][ny]:
            continue
        vis[nx][ny] = True
        q.append((nx,ny,path+[(nx,ny)]))

if not acc:
    print(-1)
