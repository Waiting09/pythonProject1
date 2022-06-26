"""集合创建"""
# 通过使用{}填充元素
set1 = {1, 2, 3}
print(set1, type(set1))
# 通过构造方法set(iterable)
set2 = set("hogwarts")  # 字符串
print(set2, type(set2))
set3 = set([1, 2, 3])  # 列表
print(set3, type(set3))
set4 = set()
print(set4, type(set4))
# 通过集合推导式
set5 = {i for i in range(1, 11) if i % 2 == 0}
print(set5, type(set5))
"""集合使用：成员检测"""
# in
# not in
set6 = {1, 2, 3, 4, 5, 6}
print(1 in set6)
print(1 not in set6)
"""集合方法"""
set7 = set()
'''add(item)'''
set7.add(1)
set7.add(2)
print(set7)
'''update(iterable)'''
set7.update("hogwarts")
set7.update([3, 4, 5])
print(set7)
'''remove(item)'''
# 1、元素存在，移除
set7.remove(1)
print(set7)
# 2、元素不存在，报错
# set7.remove(12)
print(set7)
'''discard(item)'''
# 1、元素存在，移除
set7.discard(2)
print(set7)
# 2、元素不存在，无影响
set7.discard(12)
'''pop()随机删除'''
a = set7.pop()
print(set7, a)
# 集合本身为空会报错
set8 = set()
# set8.pop()
'''clear() 清空集合'''
set9 = {1, 2, 3}
set9.clear()
print(set9)
"""集合运算"""
m = {1, 3, 2}
n = {5, 1, 4}
'''交集运算 intersection'''
print(m.intersection(n))
print(m & n)
'''并集运算 union'''
print(m.union(n))
print(m | n)
'''差集运算 difference'''
print(m.difference(n))
print(m - n)
"""集合推导式"""
# 寻找hogwarts与hello world的共相同字母
a = set("hogwarts")
b = set("hello world")
print(a & b)
# 集合推导式
st = {x for x in "hogwarts" if x in "hello world"}
print(st)
