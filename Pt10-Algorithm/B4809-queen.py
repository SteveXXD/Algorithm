qp = [list(input().split()) for _ in range(8)]

cols = [False] * 8
l1 = [False] * 15
l2 = [False] * 15
count = 0

fixed_row = set()

for row in range(8):
    for c in range(8):
        if qp[row][c] == '1':
            cols[c] = True
            l1[row - c + 7] = True
            l2[row + c] = True
            fixed_row.add(row)

def dfs(row):
    global count
    if row == 8:
        count+= 1
        return

    if row in fixed_row:
        dfs(row + 1)
        return

    for c in range(8):
        if cols[c] or l1[row-c+7] or l2[row+c]:
            continue
        cols[c] =True
        l1[row-c+7] = True
        l2[row+c] = True
        dfs(row+1)
        cols[c] = False
        l1[row - c + 7] = False
        l2[row + c] = False

dfs(0)

print(count)