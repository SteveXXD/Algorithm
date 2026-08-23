#DFS全参型

def main(n,a):
    global total, drc, slide, dfs
    total = 0
    drc = {"S": (1, 0), "W": (0, -1), "E": (0, 1), "N": (-1, 0)}

    for r in range(n):
        for c in range(n):
            if a[r][c] == "0":
                total += 1  # 确认总共有几个空位

    def slide(x, y, d, path):
        dx, dy = drc[d]
        nx, ny = x, y
        cell = []
        while True:
            tx, ty = nx + dx, ny + dy
            if tx < 0 or tx >= n or ty < 0 or ty >= n:
                break
            if a[tx][ty] == '1':
                break
            if (tx, ty) in path:
                break
            nx, ny = tx, ty
            cell.append((nx, ny))
        if not cell:
            return -1, -1, []
        return nx, ny, cell

    def dfs(x, y, cnt, seq, path, sx, sy):
        if cnt == total:
            print(sx + 1, sy + 1)
            print(seq)
            return True
        for d in "ESWN":
            nsq = seq + d
            nx, ny, cell = slide(x, y, d, path)
            if nx == -1 or ny == -1:
                continue
            if dfs(nx, ny, cnt + len(cell), nsq, path + cell, sx, sy): return True

    for i in range(n):
        for j in range(n):
            if a[i][j] == '0':
                if dfs(i, j, 1, "", [(i, j)], i, j):
                    break


import sys

tokens = sys.stdin.read().split()
idx = 0
while idx < len(tokens):
    n = int(tokens[idx]); idx += 1
    a = []
    for _ in range(n):
        a.append(tokens[idx:idx + n])   # 一行 n 个
        idx += n
    main(n, a)
