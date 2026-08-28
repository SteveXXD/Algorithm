import sys
data = sys.stdin.buffer.read().split()
idx = 0

while idx < len(data):
    b = []
    N = int(data[idx]);idx += 1
    for _ in range(N):
        b.append(int(data[idx]));idx += 1
    if max(b) > sum(b) - max(b):
        print(f"{(sum(b) - max(b)):.1f}")
    else:
        print(f"{sum(b)/2:.1f}")