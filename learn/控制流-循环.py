"""
# 使用for循环遍历列表中的元素
a = [1, 2, 3, 4, 5, ]
for i in a:
    print(i)
# 当range只传入一个参数的时候，传入的是结束数值，遵循前闭后开原则
for i in range(11):
    print(i)
# 当range传入两个个参数的时候，(开始数值，结束数值）2<=i<12
for i in range(2, 12):
    print(i)
# 当range传入两个个参数的时候，(开始数值，结束数值,步长）2<=i<12
for i in range(2, 12, 3):
    print(i)

# while循环条件，满足条件执行循环体内代码
count = 0
while count < 5:
    count += 1
    print(count)
# break 跳出整个循环体
count = 0
while True:
    count += 1
    print(count)
    if count == 5:
        break

list_demo = [1, 2, 3, 4, 5, 6]
for i in list_demo:
    print(i)
    if i == 3:
        break
# continue 跳出当前轮次循环
count = 0
while count < 10:
    print(count)
    if count == 3:
        count += 1.5
        continue
    count += 1
# if语句结果为True，就执行continue语句，让Python忽略余下的代码，并返回到循环的开头。如果为False，就执行循环中余下的代码，Python将这个数字打印出来
list_demo = [1, 2, 3, 4, 5, 6]
for i in list_demo:
    if i == 3:
        continue
    print(i)
# 1-100之间的偶数求和
# 方法1：
sum = 0
for i in range(1, 101):
    if i % 2 != 0:
        continue
    sum += i
    print(i)
print(sum)
# 方法2：
sum = 0
for i in range(0, 101, 2):
    sum += i
print(sum)
"""
# while循环实例
# 计算机出一个1~100之间的随机数由人来猜
# 计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
import random

number1 = random.randint(1,100)
print(number1)
number2 = int(input("请输入数字："))

if number1 == number2:
    print("猜对了")
elif number1 > number2:
    print("大一点")
else:
    print("小一点")

