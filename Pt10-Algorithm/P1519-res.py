l = list(map(int,input().split()))
l.pop()
res = []
rs = len(l)
total = sum(l)
aver = total/rs
mx = max(l)
lo = min(l)

res.append(str(rs))
res.append(f"{aver:.2f}")
res.append(str(mx))
res.append(str(lo))
print(",".join(res))