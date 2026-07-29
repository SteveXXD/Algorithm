#P22例2.4 建立一个顺序表，实现对学生成绩的相关查询功能

from p18_python_list import SqList
q = SqList(5)
for i,x in zip(range(5),[89,93,92,90,100]):
    q.insert(i,x)
res = q.indexOf(90)
if res == -1:
    print("顺序表中不存在成绩为90的数据元素")
else:
    print(f"数据表中成绩为90的数据元素的位置为{q.indexOf(90)}")