def l_s(limit):
    is_prime = [True] *(limit+1)
    primes = []
    for i in range(2,limit+1):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if i*p > limit:
                break
            is_prime[i*p] = False
            if i%p == 0:
                break
    return primes

pr = l_s(1000)

import sys
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    m,a,b = map(int,line.split())
    if m == 0 and a == 0 and b == 0:
        break
    mx = 0
    res = {}
    for p in pr:
        for h in pr:
            if p / h < a / b or p / h > 1:
                continue
            if p * h > m:
                break
            if p * h > mx:
                mx = p * h
                res[p * h] = (p, h)

    print(res[mx][0], res[mx][1])