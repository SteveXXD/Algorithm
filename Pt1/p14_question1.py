#写一个算法判断n是否为素数

def judgeNum(n):
    if n == 1:#1不是素数
        return False
    if n ==2:
        return True
    if n%2 == 0:#所有除了2以外所有的偶数都不是素数
        return False
    else:
        i = 3
        while i*i <= n:#之所以是i*i，是因为i大于根号n时的遍历没有意义
            if n % i == 0:
                return False
            i += 2
        return True

print(judgeNum(4))

#时间复杂度:O(n**0.5)