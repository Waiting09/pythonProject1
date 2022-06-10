"""字典使用：创建"""
# 1、使用大括号填充键值对
dc = {"name": "hogwarts", "age": 18}
print("dc", dc, type(dc))
# 2、使用字典构造方法
dc1 = dict()  # 空字典
print("dc1", dc1, type(dc1))
dc2 = dict(name="hogwarts", age=18)  # 关键字参数赋值
print("dc2", dc2, type(dc2))
dc3 = dict([("name", "hogwarts"), ("age", 18)])
print("dc3", dc3, type(dc3))
# 3、使用字典推导式
dc4 = {x: y for x, y in [("name", "hogwarts"), ("age", 18)]}
print("dc4", dc4, type(dc4))
"""字典使用：访问元素"""
# 1、访问存在的key
print(dc["age"])
# 2、访问不存在的key，会报KeyError错误
# print(dc["sex"])
"""字典使用：操作元素"""
# dict[key] = value 键不存在，添加元素  键已经存在，修改元素
# 1、修改年龄，改为20
dc["age"] = 20
print("dc", dc)
# 2、新增hobby字段
dc["hobby"] = "magic"
print("dc", dc)
"""字典使用：嵌套字典"""
dc5 = {"name": "hogwarts", "age": 18, "course": {"magic": 90, "python": 80}}
# 1、获取课程 magic的值
print(dc5["course"]["magic"])
# 2、把 python分数改成100分
dc5["course"]["python"] = 100
print("dc5", dc5)
"""字典方法"""
'''keys() 返回由字典键组成的一个新视图对象'''
'''values() 返回由字典值组成的一个新视图对象'''
'''items() 返回由字典项（（键，值）对）组成的一个新视图对象'''
# 1、遍历查看所有的键
for x in dc.keys():
    print(x)
# 2、将视图对象转成列表
print(list(dc.keys()))
print(list(dc.values()))
print(list(dc.items()))
'''get(key) 获取指定key关联的value值'''
# 1、key存在，返回key关联的value值
print(dc.get("name"))
# 2、key不存在，则返回None
print(dc.get("sex"))
'''update(dict) 使用来自dict的键/值对更新字典，覆盖原有的键和值'''
dc6 = {'name': 'hogwarts', 'age': 18}
dc7 = {'age': 20, 'hobby': 'magic'}
dc6.update(dc7)
print("dc6", dc6)
'''pop(key) 删除指定key的键值对，并返回对应value值'''
# 1、key存在，将其移除并返回value值
print(dc6.pop("hobby"))
# 2、key不存在，会引发KeyError
# print(dc6.pop("sex"))
"""字典推导式"""
# 给定一个字典对象{'a': 1, 'b': 2, 'c': 3},找出其中所有大于1的键值对，同时value值进行平方运算
dc8 = {'a': 1, 'b': 2, 'c': 3}
dc9 = dict()
# 未使用字典推导式的写法
for x, y in dc8.items():
    if y > 1:
        dc9[x] = y ** 2
print(dc9)
# 使用字典推导式
dc10 = {x: y ** 2 for x, y in dc8.items() if y > 1}
print(dc10)
'''实例
给定一个字典对象，请使用字典推导式，将她的key和value分别进行交换。也就是key变成值，值变成key。
输入：{'a': 1, 'b': 2, 'c': 3}
输出：{1:'a', 2:'b', 3:'c'}
'''
data = {y: x for x, y in dc8.items()}
print(data)
