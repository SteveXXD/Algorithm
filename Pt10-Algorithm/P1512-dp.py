from cmath import inf
import sys

data = sys.stdin.buffer.read().split()
idx = 0
while idx < len(data):
    n = int(data[idx]);idx += 1
    prices = []
    for _ in range(n):
        prices.append(int(data[idx]));idx += 1
    fee = int(data[idx]);idx += 1
    cash, hold = 0, -inf

    for p in prices:
        cash = max(cash, hold + p)
        hold = max(hold, cash - p - fee)

    print(cash)