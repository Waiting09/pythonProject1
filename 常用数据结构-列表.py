# 通过构造函数创建列表
li1 = list()  # 空列表
print(li1, type(li1))
li2 = list("apple")  # 字符串
print(li2, type(li2))
li3 = list((1, 2, 3, 4, 5, 6))  # 元组
print(li3, type(li3))
li4 = list({4, 5, 6, 7})  # 集合
print(li4, type(li4))
li5 = list({"color": "red", "food": "apple"})
print(li5, type(li5))
# 中括号创建
li6 = []  # 空列表
li7 = [1, 2, 3, 4, "red", [6, 7, 8]]  # 直接填充对象
print(li7[5][2])  # 正向索引
print(li7[-2])  # 反向索引
# 列表推导式
li8 = [i for i in range(1, 11) if i % 2 == 0]
print(li8)
# 特殊的切片写法：逆向打印
print(li8[::-1])
# 运算符
print(li8 * 5)
print(li7 + li8)
# 成员检测
print(2 in li8)
print(2 not in li8)
'''append(item) 将一个对象item添加到列表的末尾'''
li8.append(99)
print(li8, len(li8))  # len()返回列表中的项目数
print(type(li8[-1]))
'''extend(iterable):将一个可迭代对象的所有元素，添加到列表末尾'''
li8.extend("apple")
print(li8)
li8.extend(li7)
print(li8)
'''insert(index,item)将一个对象插入到指定索引的位置'''
li8.insert(0, 20)
li8.insert(1, 68)
print(li8)
'''pop(index)或者pop()弹出并返回所指定索引的元素'''
n = li8.pop()  # 未指定索引则返回末尾元素
n1 = li8.pop(0)  # 指定索引的元素
print(n, n1)
print(li8)
'''remove(item)#移除列表中第一个等于item的元素'''
li8.remove(68)
print(li8)
'''sort(key=None,reverse=False)'''
# key:指定带有一个参数的函数，用于从每一个列表元素中提取比较键。 reverse：默认值为False表示升序，为True表示降序
num = [2, 3, 5, 1, 4]
num.sort()  # 不传参数默认升序
print(num)
num.sort(reverse=False)  # 升序
print(num)
num.sort(reverse=True)  # 降序
print(num)
num1 = ["a", "11", "apple", "b"]
num1.sort(key=len, reverse=True)  # 按元素的长度降序
print(num1)
num1.sort(key=len)  # 按元素的长度升序
print(num1)
'''reverse()将列表中的元素顺序反转  参数：无'''
num2 = [2, "a", "参数"]
num2.reverse()
print(num2)
# 列表嵌套
li9 = [[2, 3, 4], ["a", "b"]]
print(li9[1][1])
li9[1].append(1)
print(li9)
"""列表推导式"""
# for循环
li10 = []
for i in range(1, 11):
    if i % 2 == 0:
        li10.append(i ** 2)
print(li10)
# 列表推导式
li11 = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(li11)


