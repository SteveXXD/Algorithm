from functools import reduce

def singleNumber(nums):
    return reduce(lambda x,y:x^y,nums)

if __name__ == "__main__":
    tmp_input = input()
    tmp_input = tmp_input[1:len(tmp_input) - 1]
    input_arr = tmp_input.split(',')
    input_arr = [int(item) for item in input_arr]
print(singleNumber(input_arr))

#原理:reduce()函数符合结合率与交换律，代码中的reduce函数会依次取出数组中的元素，反复应用同一个函数，最终得到一个结果。
#DeepSeek给出的解释:
#reduce(函数, 数组)
# 相当于：
# 第1步：用 函数(第1个, 第2个)
# 第2步：用 函数(上一步结果, 第3个)
# 第3步：用 函数(上一步结果, 第4个)
# ...直到处理完所有元素