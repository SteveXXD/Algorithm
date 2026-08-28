#一坨屎。
"""
n,T = map(int,input().split())
mc = []

for _ in range(n):
    ti,bi,hi = map(int,input().split())
    mc.append((ti,bi,hi))

mc.sort(key = lambda x:x[1])

ans = 0
acc = 0; ok_all = True
for t, b, h in mc:
    acc += t
    if acc > b: ok_all = False
if ok_all and acc <= T:
    ans = sum(h for t, b, h in mc)

for mk in mc:
    tm = 0;H = 0;ok = True
    res = []
    for t, b, h in mc:
        if b < mk[1]:
            tm += t;H += h
            if tm > b: ok = False
        elif b > mk[1]:
            res.append((t, b, h))
    if not ok or tm >= mk[1] or tm > T:
        continue
    dp = [0] * (mk[1] - tm)
    for t, b, h in res:
        for j in range(mk[1] - tm-1, t - 1, -1):
            dp[j] = max(dp[j - t] + h, dp[j])
    ans = max(ans, H + max(dp))

print(ans)
"""

#不知道为什么最后一个数据点总是tle。所以抄了一个
n, T = map(int, input().split())
mc = [tuple(map(int, input().split())) for _ in range(n)]
mc.sort(key=lambda x: x[1])

ts = [x[0] for x in mc]
bs = [x[1] for x in mc]
hs = [x[2] for x in mc]


acc = 0; ok_all = True
for i in range(n):
    acc += ts[i]
    if acc > bs[i]: ok_all = False
ans = sum(hs) if (ok_all and acc <= T) else 0


pt = [0]*(n+1); ph = [0]*(n+1); pok = [True]*(n+1)
for i in range(1, n+1):
    pt[i] = pt[i-1] + ts[i-1]
    ph[i] = ph[i-1] + hs[i-1]
    pok[i] = pok[i-1] and pt[i] <= bs[i-1]

M = max(bs) - 1
dp = [0]*(M+1)
for p in range(n, 0, -1):
    b = bs[p-1]
    if pok[p-1] and pt[p-1] < b:
        cap = b - 1 - pt[p-1]
        v = ph[p-1] + dp[cap]
        if v > ans: ans = v
    t = ts[p-1]; h = hs[p-1]
    d = dp
    for j in range(M, t-1, -1):
        v = d[j-t] + h
        if v > d[j]: d[j] = v

print(ans)