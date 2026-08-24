Q = int(input())
bcp = {}

for _ in range(Q):
    a = input().split()
    if len(a) == 3:
        C,S,x = a
        C = int(C)
        x = int(x)
    else:
        C,S = a
        C = int(C)
    if C == 1:
        bcp[S] = bcp.get(S, 0) + x
    if C == 2:
        if not S in bcp:
            print(-1)
        elif bcp[S] < x:
            print(-1)
        else:
            bcp[S] = bcp.get(S, 0) - x
            print(bcp[S])
    if C == 3:
        if not S in bcp:
            print(0)
        else:
            print(bcp[S])
