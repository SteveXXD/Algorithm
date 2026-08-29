#D_n = n! * Σ(0-k) (-1)**k/k!

def pls(n0):
    s = 1
    for i in range(1, n0 + 1):
        s *= i
    return s

def D(n0):
    rig = 0
    for i in range(n0+1):
        rig += (-1)**i/pls(i)
    rig *= pls(n0)
    return rig

import sys
data = sys.stdin.buffer.read().split()
idx = 0

while idx < len(data):
    n = int(data[idx]);idx += 1
    m = int(data[idx]);idx += 1
    P = D(n - m) / (pls(m) * pls(n - m))
    print(f"{P:.8f}")