#Steve的简化解法

def plusOne(x):
    n = len(x)
    for i in range(len(x)-1,-1,-1):
        if x[i] != 9:
            x[i] += 1
            return x
        x[i] = 0
    return [1] + [0] * n

print(plusOne([9,9,9,9,9]))
