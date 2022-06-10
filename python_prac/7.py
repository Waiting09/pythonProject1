'''
#定义一个函数
def greet_user():
    """显示简单的问候语"""
    print("Hello!")
#调用
greet_user()
#向函数传递信息
def greet_user(name):
    """显示简单的问候语"""
    print('Hello,'+name+'!')
greet_user('小红')
#位置实参
def describe_pet(animal_type, name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + name.title() + ".")
describe_pet('cat', 'baby')
#关键字实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='cat', pet_name='harry')
#默认值
def describe_pet(pet_name,animal_type = 'dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='cat', pet_name='harry')
#等效的函数调用
def describe_pet(pet_name, animal_type='dog'):
    print(pet_name,animal_type)
#一条名为Willie的小狗
describe_pet('willie')
describe_pet(pet_name='willie')
# 一只名为Harry的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
#返回值
def get_formatted_name(first_name,last_name ):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
#让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('john', 'hooker')
print(musician)

#返回字典
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

#结合使用函数和 while 循环
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

#传递列表
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg= "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
'''
#创建一个列表，并将其传递给一个名为show_magicians()的函数，这个函数打印列表中每个元素

def show_magicians(names):
    for name in names:
        print(name.title())
'''

def print_models(unprinted_designs, completed_models):
    """
     模拟打印每个设计，直到没有未打印的设计为止
     打印每个设计后，都将其移到列表completed_models中
     """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        completed_models.append(current_design)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_magicians(completed_models)
print(unprinted_designs)

#传递任意数量的实参
def make_pizza(*toppings):
    """概述要制作的比萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#如果前面的函数还需要一个表示比萨尺寸的实参，必须将该形参放在形参*toppings的前面：
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

#编写一个名为make_great()的函数，对魔术师列表进行修改，在每个魔术师的名字中都加入字样“the Great”。
#调用函数 make_great()，确认魔术师列表确实变了。

def make_great(a):
    c = []
    while a:
        b = a.pop()
        c.append(b+'the Great')
    return c
a1 = ['red1','green','yellow']
print(make_great(a1))


#解包
print(list(range(1, 5)))
list_a=(1,3)
print(list(range(*list_a)))
def test(a,b,c):
    print(a)
    print(b)
    print(c)
test = {'a':'1','b':'2','c':'3'}
test(**test)
'''

