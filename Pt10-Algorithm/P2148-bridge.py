T = int(input())
num = []

for _ in range(T):
    num.append(int(input()))

mx = max(num)
f = [0]*(mx+1)
f[0] = 2
f[1] = 3

for i in range(2,mx+1):
    f[i] = (f[i-1]+f[i-2]) % 998244353

for c in num:
    print(f[c-1])
