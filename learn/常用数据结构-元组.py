"""创建元组"""
# 通过使用逗号分隔直接创建元组
t1 = 1, 2, 3
print(type(t1))
# 通过小括号填充元素
t2 = (1, 2, 3, 4, 5)
print(type(t2))
# 通过构造函数tuple()
t3 = tuple()
print(t3)
t4 = tuple("apple")  # 字符串
print(t4)
t5 = tuple([1, 2, 3, 4, 5])  # 列表
print(t5)
t6 = tuple({1, 2, 3})  # 集合
print(t6, type(t6))
# 注意：单元素元组，逗号不可或缺
t7 = (1)
print(type(t7), t7)
"""元组使用：索引"""
print(t4[0])
print(t4[-5])
"""元组使用：切片"""
# 切片[start:stop:step]
print(t4[:3])
'''index(item) 返回与目标元素相匹配的首个元素的索引， 目标必须在元组中存在的，否则会报错'''
print(t4.index("a"))
# count(item):返回某个元素出现的次数
print(t4.count("a"))
print(t4.count("p"))
"""元组解包"""
# 传统逐个赋值的方式
t5 = 1, 2, 3
a = t5[0]
b = t5[1]
c = t5[2]
# 解包平行赋值
# a, b, c = t5
print(a, b, c)
d, e, f = [4, 5, 6]
print(d, e, f)
