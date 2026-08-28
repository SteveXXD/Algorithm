K = int(input())
for _ in range(K):
    ia = False
    N,M = map(int,input().split())
    for a in range(1,M):
        if N % a == 0 and N % (M-a) == 0:
            ia = True
            print(a)
            break
    if not ia:
        print(-1)