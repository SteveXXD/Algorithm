from collections import deque
q = deque()
res = deque()

t = 0

N,Q = map(int,input().split()) #Q:时间片长度

for _ in range(N):
    Name,Time = input().split()
    Time = int(Time)
    q.append((Name,Time))

while q:
    w = q.popleft()
    if w[1] <= Q:
        t += w[1]
        res.append((w[0],t))
    else:
        t += Q
        q.append((w[0],w[1]-Q))

for ch in res:
    print(ch[0],ch[1])