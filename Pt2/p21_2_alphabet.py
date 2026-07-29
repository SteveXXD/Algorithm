#p21例2.3 建立一个a-z的由26个字母组成的字母顺序表，求每个字母的直接前驱和直接后继，编程实现

from p18_python_list import SqList

L = SqList(26)

for i in range(26):
    L.insert(i,chr(ord("a")+i))

while True:
    i = input("请输入要查询元素的位序号")
    i = int(i)
    # noinspection PyChainedComparisons
    if i>0 and i<25:
        print(f"第{i}个元素的直接前驱为:{L.get(i - 1)}")
        print(f"第{i}个元素的直接后继为:{L.get(i + 1)}")
    elif i == 0:
        print(f"第{i}个元素的直接前驱不存在")
        print(f"第{i}个元素的直接后继为:{L.get(i + 1)}")
    elif i == 25:
        print(f"第{i}个元素的直接前驱为:{L.get(i - 1)}")
        print(f"第{i}个元素的直接后继不存在")
    else:
        print("查询位置非法")
