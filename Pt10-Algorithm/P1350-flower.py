import sys
data = sys.stdin.buffer.read().split()
idx = 0
while idx < len(data):
    n = int(data[idx]);idx += 1
    m = int(data[idx]);idx += 1
    q = [0] * (n + 2)
    count = 0
    for i in range(m):
        l = int(data[idx]);idx += 1
        r = int(data[idx]);idx += 1
        q[l] = q[l] + 1
        q[r + 1] = q[r + 1] - 1

    res = [0] * (n + 2)

    c = 0

    for j in range(len(q)):
        res[j - 1] = c
        if q[j] != 0:
            c += q[j]

    a = int(data[idx]);idx += 1
    b = int(data[idx]);idx += 1

    for i in range(1, len(res)):
        res[i] = res[i - 1] + res[i]

    print(res[b] - res[a - 1])