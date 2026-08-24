N,M,Q = map(int,input().split())
#N个空间站，M个航道，Q次询问

g = [[] for _ in range(N + 1)]

for _ in range(M):
    u,v = map(int,input().split())
    g[u].append(v)

for _ in range(Q):
    u,k = map(int,input().split())
    if len(g[u]) == 0 or k > len(g[u]):
        print(-1)
    else:
        g[u].sort()
        print(g[u][k-1])