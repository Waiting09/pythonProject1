#if 语句
import pickle

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car.title())
#是否是够投票的年龄
ages = [14,22,44,2]

for age in ages:
    if age >=18:
        print(age,'能够投票')
    else:
        print(age,'不能投票')
#4岁以下免费；
#4~18岁收费5美元；
#18岁（含）以上收费10美元
for age in ages:
    if age<4:
        print(age,'免费')
    elif age<18:
        print(age,'5美元')
    else:
        print(age,'10美元')
#65岁（含）以上的老人，可以半价（即5美元）购买门票
ages = [14,22,44,2,65,90]
for age in ages:
    if age<4:
        print(age,'免费')
    elif age<18:
        print(age,'5美元')
    elif age>=65:
        print(age,'5美元')
    else:
        print(age,'10美元')
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")
#列表为空时
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
a1= ['葡萄','香蕉','苹果','西瓜','芒果','凤梨','草莓']
a2 = ['葡萄','草莓','西瓜','樱桃']

for a in a2:
    if a in a1:
        print(a)

    else:
        print('不好意思，我们没有'+a)
