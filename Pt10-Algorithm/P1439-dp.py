import sys

data = sys.stdin.read().split()
idx = 0

V = int(data[idx]); idx += 1
w = [0]
v = [0]

n = int(data[idx]); idx += 1

for _ in range(n):
    vi = int(data[idx]); wi = int(data[idx + 1]); idx += 2
    w.append(wi)
    v.append(vi)

f = [[0] * (V + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, V + 1):
        if j - v[i] < 0:
            f[i][j] = f[i - 1][j]
        else:
            f[i][j] = max(f[i - 1][j], f[i - 1][j - v[i]] + w[i])

print(max(f[n]))