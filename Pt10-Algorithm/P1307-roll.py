import sys

data = sys.stdin.buffer.read().split()
idx = 0

while idx < len(data):
    R = int(data[idx]);idx += 1
    prev = [0] * R
    prev[0] = int(data[idx]);idx += 1
    for i in range(1,R):
        cur = [0]*R
        for j in range(i+1):
            v = int(data[idx]);idx += 1
            cur[j] = max(prev[j],prev[j-1] if j > 0 else 0) + v
        prev = cur
    print(max(prev))

#8.25 学习dp+空间优化