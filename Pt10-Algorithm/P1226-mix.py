"""
from functools import cmp_to_key

n = int(input())
num = []

def cmp(x, y):
    if x + y > y + x: return -1
    if x + y < y + x: return 1
    return 0

for _ in range(n):
    num.append(input())

num.sort(key = cmp_to_key(cmp))
print("".join(num))

"""

import sys
from functools import cmp_to_key

data = sys.stdin.read().split()
n = int(data[0])
nums = data[1:1+n]

def cmp(x, y):
    if x + y > y + x: return -1
    if x + y < y + x: return 1
    return 0

nums.sort(key=cmp_to_key(cmp))
ans = "".join(nums)
print(ans if ans[0] != '0' else '0')
