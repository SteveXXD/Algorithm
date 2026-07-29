#写一个算法计算n的阶乘
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