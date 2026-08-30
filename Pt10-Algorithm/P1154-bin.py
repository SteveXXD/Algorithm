def plus(n):
    r = 1
    for i in range(1,n+1):
        r *= i
    return r

import sys
data = sys.stdin.buffer.read().split()
idx = 0
while idx < len(data):
    n = int(data[idx]);idx += 1
    k = int(data[idx]);idx += 1
    if n == 0 and k == 0:
        break
    print(int(plus(n)/(plus(k)*plus(n-k))))