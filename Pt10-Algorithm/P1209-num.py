#使用埃氏筛加快了速度

def sieve(limit):
    is_prime = [True] * (limit+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2,int(limit**0.5)+1):
        if is_prime[i]:
            for j in range(i*i,limit+1,i):
                is_prime[j] = False
    return is_prime

m = int(input())

s = sieve(m)

for p in range(m,1,-1):
    if s[p] and s[p-2]:
        print(p-2,p)
        break