import sys
sys.setrecursionlimit(10000000)

mem = {}

def dfs(rest,last):
    if rest == last:
        return 1
    if rest - last < last:
        return 0
    if (rest,last) in mem:
        return mem[(rest,last)]
    cnt = 0
    for i in range(last,rest):
        cnt += dfs(rest-last,i)
        mem[(rest,last)] = cnt
    return cnt


for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    total = 0
    for i in range(1,n//2+1):
        total += dfs(n,i)
    print(total)