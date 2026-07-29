#写一个算法计算n的阶乘,并计算空间复杂度

def plus(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def main(n):
    result = 0
    for i in range(1,n+1):
        result += plus(i)
    return result

print(main(4))
#时间复杂度:O(n**2)
#空间复杂度:O(1)
#一般情况下，空间复杂度只需看变量的个数即可
