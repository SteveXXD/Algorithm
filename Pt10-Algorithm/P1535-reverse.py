n = int(input())
for _ in range(n):
    l = 0
    r = 0
    c = list(input())
    a, b = input().split()

    for i in range(len(c)):
        if c[i] == a:
            l = i
        if c[i] == b:
            r = i

    cet = c[l:r + 1]
    cet.reverse()
    q = c[:l]
    p = c[r + 1:]
    res = []
    res += q
    res += cet
    res += p
    print("".join(res))