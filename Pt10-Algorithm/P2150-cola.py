t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = []
    b = []

    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)  # 价格list
        b.append(bi)  # 好喝程度list
    # ab[0]:价格,ab[1]:好喝程度
    ab = list(zip(a, b))
    # [(100, 1), (101, 2)]
    # [(1, 5), (3, 2), (5, 3)]

    sp = [0] * (n + 1)
    sb = [0] * (n + 1)
    for i in range(1, n + 1):
        sp[i] = sp[i - 1] + a[i - 1]
        sb[i] = sb[i - 1] + b[i - 1]

    # pre[sp]返回买掉第k瓶需要的总价。从1开始计数

    i = 0
    while i < len(sp):
        if sp[i] > m:
            break
        i += 1

    i -= 1  # i 代表最大可购买的饮料瓶

    i += k  # 代表最大可达序号
    # print(min(i,n),sp[min(i,n)])
    print(sb[min(i, n)])