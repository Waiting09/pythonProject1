"""函数定义
def function_name([parameter_list]):
    ['''comments''']
    [function_body]
def：函数定义关键词
function_name：函数名称
()：参数列表放置的位置，可以为空
parameter_list：可选，指定向函数中传递的参数
形式参数:定义函数时,函数名称后面括号中的参数
实际参数:调用函数时,函数名称后面括号中的参数
comments：可选，为函数指定注释
function_body：可选，指定函数体
"""
"""定义函数"""


def func_with_params(a, b, c):
    """
    这是一个携带参数和注释的函数
    """
    print(f"传入的参数为：a={a},b={b},c={c}")


# 打印函数comments的内容
print(func_with_params.__doc__)
# 函数名与comments
help(func_with_params)

"""定义空函数"""


# 1、使用 pass 语句占位
def filter_char(t):
    pass


# 2、写函数注释 comments
def filter_sensitive_words(f):
    """
    过滤敏感词
    """


"""调用函数"""
# 位置参数：数量必须与定义时一致，位置必须与定义时一致
func_with_params(1, 2, 3)
# 关键字参数：使用形式参数的名字确定输入的参数值，不需要与形式参数的位置完全一致
func_with_params(a=1, c=3, b=2)


# 默认值：定义函数时可以指定形式参数的默认值，指定默认值的形式参数必须放在所有参数的最后，否则会产生语法错误
# 默认值一定要用不可变对象，否则的话默认值可能会随着调用发生变化
def person(name, age, sex="男"):
    print(f"姓名为{name}，性别{sex}，今年{age}")


# 1、不传sex，使用默认值
person("Tom", 20)
# 2、传sex，使用传递的实参
person("Tom", 20, "女")

"""return 指定返回值"""


def s(a, b):
    result = a + b
    return result


print(s(1, 2))

"""*args 接收任意多个实际参数，并将其放到一个元组中"""


def print_language(*args):
    print(args, type(args))


print_language("python", "java", "php", "go")

# 使用已经存在的列表或元组作为函数的可变参数，可以在列表的名称前加*
params = ["python", "java", "php", "go"]
print_language(params)
print_language(*params)

"""**kwargs 接收任意多个类似关键字参数一样显式赋值的实际参数，并将其放到一个字典中"""


def print_info(**kwargs):
    print(kwargs)


print_info(Tom=18, Jim=20, Lily=12)
# 使用已经存在字典作为函数的可变参数，可以在字典的名称前加**
params = {'Tom': 18, 'Jim': 20, 'Lily': 12}
print_info(**params)

"""lambda 表达式
result = lambda [arg1 [, arg2, .... , argn]]: expression
result：调用 lambda 表达式
[arg1 [, arg2, …. , argn]]：可选，指定要传递的参数列表
expression：必选，指定一个实现具体功能的表达式
"""
import math


# 常规写法
def circle_area(r):
    '''
    计算圆的面积
    r:半径
    '''
    result = math.pi * r ** 2
    return result


# print(circle_area(10))

# lambda 表达式

result = lambda r: math.pi * r ** 2

print(result(10))

# 书籍信息
book_info = [
    ('python', 22.6),
    ('java', 20),
    ('测试', 21)
]
print(book_info)
book_info.sort(key=lambda x: x[1])
print(book_info)
