# 斐波那契矩阵快速幂版  O(log n)

def mat_mul(A, B):
    """2x2矩阵乘法: A × B
    就是四个数字按规则算, 记住公式就行:
    [a b]   [e f]   [a*e+b*g  a*f+b*h]
    [c d] × [g h] = [c*e+d*g  c*f+d*h]
    """
    return [
        [A[0][0]*B[0][0] + A[0][1]*B[1][0],
         A[0][0]*B[0][1] + A[0][1]*B[1][1]],
        [A[1][0]*B[0][0] + A[1][1]*B[1][0],
         A[1][0]*B[0][1] + A[1][1]*B[1][1]]
    ]

def mat_pow(M, k):
    """矩阵快速幂: 算 M^k
    核心: 指数二分, k是奇数就乘一下, M自己平方
    例子: k=10 → M^10 = (M^5)^2, 只需算M^5再平方
    """
    result = [[1, 0], [0, 1]]   # 单位矩阵(相当于数字里的1)
    while k > 0:
        if k % 2 == 1:          # k是奇数: 多乘一个M
            result = mat_mul(result, M)
        M = mat_mul(M, M)       # M自乘平方
        k //= 2                 # 指数减半
    return result

def fib_fast(n):
    """算F(n), 教材定义 F(1)=0, F(2)=1"""
    if n <= 1:
        return 0
    if n == 2:
        return 1
    # 核心魔法: F(n)  = M^(n-2) 的第一行第一列
    # 其中 M = [[1,1],[1,0]]   ← 斐波那契递推打包成的矩阵
    M = [[1, 1], [1, 0]]
    return mat_pow(M, n - 2)[0][0]

# 测试
print([fib_fast(i) for i in range(1, 10)])   # [0,1,1,2,3,5,8,13,21]
print(fib_fast(100))                          # 大数秒出