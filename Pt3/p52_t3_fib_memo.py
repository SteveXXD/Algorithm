#用一个缓存字典保存已经算过的，时间复杂度O(n)

memo = {1:0,2:1}

def fib(n):
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib(100))