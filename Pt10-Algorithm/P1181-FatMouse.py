while True:
    M,N = map(int,input().split())#有M猫粮，N个房间
    if M == -1 and N == -1:
        break
    else:
        sell = []
        #J[i]代表第i个房间总共有的bean
        #F[i]代表第i个房间的bean的单价
        #第一个数字:总共储量 第二个数字:总价
        for i in range(N):
            sell.append(tuple(map(int,input().split())))
        res = sorted(sell, key=lambda x: -(x[0] / x[1]))
        jb = 0
        for ch in res:
            if M >= ch[1]:
                M -= ch[1]
                jb += ch[0]
            else:
                jb += M/(ch[1]/ch[0]) #付出的金额/单价
                M = 0
                break
        print(f"{jb:.3f}")