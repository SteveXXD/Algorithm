#设计一个算法，求出满足不等式1+2+....+i>=n的最小i值，并计算时间复杂度
def judge(n):
    sum = 0
    i = 1
    while sum < n:
        sum += i
        i += 1
    return i - 1

print(judge(10))
#时间复杂度:O(n**0.5)