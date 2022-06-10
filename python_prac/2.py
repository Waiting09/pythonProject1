#列表：[]表示，用逗号来分隔其中的元素。
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#从列表bicycles中访问第一个列表元素
print(bicycles[0])
#使用方法title()让元素'trek'的格式更整洁,首字母大写
print(bicycles[0].title())
#从列表bicycles中访问第四个列表元素
print(bicycles[3])
#访问倒数第二个列表元素
print(bicycles[-2])
#使用bicycles[0]的值生成一个句子
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
#修改第一个元素为ducati
bicycles[0] = '1'
print(bicycles)
#在列表末尾添加元素'1'：append()
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.append('1')
print(bicycles)
#在列表中插入元素:insert()
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.insert(1,'1')
print(bicycles)
#使用del语句删除元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
del bicycles[0]
print(bicycles)
# 使用方法pop()删除列表最末尾的元素，并打印出删除的元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
popped = bicycles.pop()
print(bicycles)
print(popped)
#使用pop()删除列表中任何位置处的元素，并打印出删除的元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
popped = bicycles.pop(0)
print(bicycles)
print(popped)
#使用方法remove()根据值删除元素,并接着使用他的值
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
v = 'trek'
bicycles.remove('cannondale')
bicycles.remove(v)
print(bicycles)
print(v)
#使用方法 sort()对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()    #升序
print(cars)
cars.sort(reverse=True) #倒序
print(cars)
#使用函数 sorted()对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(sorted(cars,reverse=True))
print(cars)
#使用方法reverse()倒着打印列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
#使用函数len()确定列表的长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))






