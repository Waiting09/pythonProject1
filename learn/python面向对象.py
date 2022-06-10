"""封装"""


# 创建一个人类
# 类（Class）：抽象的概念，一类事物
class People:
    # 类变量：类变量在整个实例化的对象中是公用的
    name = "L"
    sex = "女"
    weight = 0

    # 构造方法，在类实例化的时候被调用
    def __init__(self, name, age):
        # 实例变量：以“self.变量名”的方式定义的变量，可修改
        self.name = name
        self.age = age

    # 方法：类中定义的函数，对外提供的服务
    def eat(self):
        print("eat")

    @classmethod  # 类方法
    def sleep(cls):
        """
        类方法，使用@classmethod装饰器，第一个参数需改为cls（非强制）
        :return:
        """
        print("sleep")

    def play(self):
        print("play")


# 类变量：类变量在整个实例化的对象中是公用的,可修改
print(People.name)
# 实例引用：实例化一个对象
T = People("T", 20)
print(T.name)
print(T.age)
print(T.sex)
T.eat()

"""继承"""


# 继承父类
class Person(People):

    def jump(self):
        print("jump")


print(Person.name)
Q = Person("Q", 21)
Q.eat()
Q.jump()

"""多态"""


# 继承父类的方法，修改父类的方法
class Persom_1(People):

    @classmethod
    def play(self):
        print("修改父类的方法")


Persom_1.play()
