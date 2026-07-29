#设计一个算法，打印出一个具有 n 行的乘法表，
# 第 i 行(1 ≤ i ≤ n)中有 n-i+1 个乘法项，
# 每个乘法项为 i 与 j(i ≤ j ≤ n)的乘积，
# 并计算算法的时间复杂度。

def multi(n):
    i = 1
    j = 1
    for i in range(1,n+1):
        for j in range(i,n+1):
            print(f"{i}x{j}",end = "\t")
        print()
multi(15)

#时间复杂度:O(n**2)



