def gcd(a,b):#辗转相除法求公约数
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a

print(gcd(17,34))
