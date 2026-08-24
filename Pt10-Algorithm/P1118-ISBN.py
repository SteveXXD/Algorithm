n = int(input())

for _ in range(n):
    a = input()
    l = []
    res = 0

    for k in a:
        if k != "-":
            l.append(int(k))

    for p in range(1, 10):  # 乘数p，1-9
        res += l[p - 1] * p
        res %= 11

    if l[len(l) - 1] == res:
        print("Right")
    else:
        print(a[:12] + str(res))