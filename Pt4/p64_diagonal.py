def sumOfDiagonal(a):
    n = len(a[0])
    sum1 = sum2 = 0
    for i in range(n):
        sum1 += a[i][i]
        sum2 += a[i][n-i-1]
    sum = sum1+sum2
    if n%2 == 1:
        sum -= a[n//2][n//2]
    return sum