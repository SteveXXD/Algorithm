C = int(input())

for _ in range(C):
    M,N = map(int,input().split())
    a = max(M,N)
    b = min(M,N)
    while a != 0 and b != 0:
        print(a,b)
        if a>b:
            a %= b
        else:
            b %= a
    print(a,b)
    if a == 0:
        print("Ollie wins")
    if b == 0:
        print("Stan wins")