#自动找周期

def find_period(m, a0, b0):
    a, b = a0 % m, b0 % m
    seen = {}
    seq = []
    i = 0
    while True:
        key = (a, b)            # 状态对
        if key in seen:
            return seen[key], i - seen[key], seq   # 起点, 周期, 序列
        seen[key] = i
        seq.append(a)
        a, b = b, (a + b) % m   # 模 m 递推
        i += 1

# 用法：找模3的周期
start, period, seq = find_period(3, 7, 11)
print(period, seq)