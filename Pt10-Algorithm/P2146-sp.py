T = int(input())
score = [0] * 4

for _ in range(T):
    l = list(map(int,input().split()))
    idx = [1,2,3,4]
    ch = list(zip(l,idx))
    res = sorted(ch,key=lambda x:(-x[0],x[1]))
    score[res[0][1]-1] = 15
    score[res[1][1]-1] = 5
    score[res[2][1]-1] = -5
    score[res[3][1]-1] = -15
    js = [0] * 4
    js[0] = (l[0] - 25000)/1000 + score[0]
    js[1] = (l[1] - 25000) / 1000 + score[1]
    js[2] = (l[2] - 25000) / 1000 + score[2]
    js[3] = (l[3] - 25000) / 1000 + score[3]
    for h in js:
        if h == -0:
            print(0,end=" ")
        else:
            print(int(h),end=" ")
    print()