import sys
data = sys.stdin.buffer.read().split()
idx = 0
while idx < len(data):
    a = int(data[idx]);idx += 1
    b = int(data[idx]);idx += 1
    print(pow(a,b,1337))
