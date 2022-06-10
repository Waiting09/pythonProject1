#使用for循环来打印colours中的颜色
colours = ['红','橙','黄','绿','青','蓝','紫']
for colour in colours:
    print(colour)
#使用函数 range()生成一系列的数字,要打印数字1~5，需要使用range(1,6)
for value in range(1,6):
    print(value)
#使用 range()创建数字列表:使用函数list()将range()的结果直接转换为列表
numbers = list(range(1,6))
print(numbers)
#使用函数range(),打印1~10内的偶数.函数range()从2开始数，然后不断地加2，直到达到或超过终值（11）
numbers = list(range(2,11,2))
print(numbers)
#何创建一个列表，其中包含前10个整数（即1~10）的平方
a = []
for j in range(1,11):
    a.append(j**2)
print(a)
#列表解析
a = [j**2 for j in range(1,11)]
print(a)
#对数字列表执行简单的统计计算: min() max() sum()
b = [1,2,3,4,5]
print(min(b))
print(max(b))
print(sum(b))
#切片
colours = ['红','橙','黄','绿','青','蓝','紫']
#打印列表前三个颜色
print(colours[0:3])
#提取列表的第2~4个元素
print(colours[1:4])
#打印列表前4个颜色
print(colours[:4])
print(colours[:-3])
#打印列表后4个颜色
print(colours[-5:])
#遍历切片
#遍历前三个颜色
for colour in colours[:3]:
    print(colour)
#元组不可修改，可重新定义
n = (1,2,3)
print(n)
n = (1,2)
print(n)





