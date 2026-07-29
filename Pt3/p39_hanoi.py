#p39的汉诺塔

def move(s,t):
    print(f"将{s}塔座上最顶端的圆盘移动到{t}塔座上")

def hanoi(n,x,y,z):
    if n == 1:
        move(x,z)
    else:
        hanoi(n-1,x,z,y)
        hanoi(n-1,y,x,z)

hanoi(5,"x","y","z")

#这个思维很巧妙