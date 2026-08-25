import sys

data = sys.stdin.buffer.read().split()
idx = 0

while idx < len(data):
    tri = []
    R = int(data[idx]);idx += 1
    for i0 in range(R):
        row = []
        for j0 in range(i0+1):
            row.append(int(data[idx]));idx += 1
        tri.append(row)
    mem = [[-1] * R for _ in range(R)]
    mem[0][0] = tri[0][0]

    def dp(i, j):
        if j < 0 or j > i:
            return 0
        if mem[i][j] != -1:
            return mem[i][j]
        else:
            if i == 0 and j == 0:
                return tri[0][0]
            mem[i][j] = max(dp(i - 1, j), dp(i - 1, j - 1)) + tri[i][j]
            return mem[i][j]


    res = []
    for i in range(R):
        res.append(dp(R - 1, i))

    print(max(res))