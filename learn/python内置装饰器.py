"""classmethod	类方法"""


# 1. 类的定义
class MethodsDemo:
    param_a = 0

    def normal_demo(self):  # 定义一个类方法，第一个参数必须为self
        """
        普通方法
        :return:
        """
        print("这是一个普通方法1", self.param_a)

    def normal_demo1(self):  # 定义一个类方法，第一个参数必须为self
        """
        实例方法内，可以直接调用实例方法，实例变量
        """
        self.normal_demo()

        print("这是一个普通方法2", self.param_a)

    # 定义类方法必须加 classmethod装饰器
    @classmethod
    def classmethod_demo(cls):
        """
        类方法，第一个参数需要改为cls
        :return:
        """
        # cls.normal_demo()       #类方法内，不可以直接调用实例方法，实例变量
        cls.classmethod_demo2()  # 类方法内，可以直接调用类方法，类变量
        print("类方法2", cls.param_a)

    @classmethod
    def classmethod_demo2(cls):
        """
        类方法，第一个参数需要改为cls
        :return:
        """

        # cls.normal_demo()   #类方法内，不可以直接调用实例方法，实例变量
        print("类方法", cls.param_a)


# 2. 类的调用
MethodsDemo.classmethod_demo()  # 无需实例化，直接调用
md = MethodsDemo()
md.normal_demo1()

"""staticmethod	静态方法"""


class MethodsDemo:
    @classmethod
    def classmethod_demo2(cls):
        print("类方法")

    @staticmethod  #没有self、或者cls
    # 无法直接使用任何类变量、类方法或者实例方法、实例变量
    def static_demo(s):
        print(f"静态方法{s}")

    def normal_demo(self):  # 定义一个类方法，第一个参数必须为self
        print("这是一个普通方法1")

# 调用
# 类.方法名调用
MethodsDemo.static_demo(1)
# 实例.方法名调用
demo=MethodsDemo
demo.static_demo(2)

