n = int(input())
a = [list(input().split()) for _ in range(n)]#矩阵里的是字符串
total = 0
drc = {"S":(1,0),"W":(0,-1),"E":(0,1),"N":(-1,0)}

"""
0 0 0 0
0 0 0 1
0 0 0 0
1 0 1 0
"""

def slide(x,y,d):
    cell = list()
    dx,dy = drc[d]
    nx = x
    ny = y
    if not (0 <= x + dx < n and 0 <= y + dy< n):
        return -1,-1
    while not (nx >= n or ny >= n or nx < 0 or ny < 0 or a[nx][ny] != "0"):
        nx += dx
        ny += dy
        cell.append((nx,ny))
    cell.pop()
    nx -= dx
    ny -= dy
    return nx,ny,cell

print(slide(2,0,"E"))