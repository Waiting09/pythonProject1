# 9-1 餐馆：创建一个名为 Restaurant 的类，其方法__init__()设置两个属性：restaurant_name 和 cuisine_type。
# 创建一个名为 describe_restaurant()的方法和一个名为 open_restaurant()的方法，其中前者打印前述两项信息，
# 而后者打印一条消息，指出餐馆正在营业。
class Restaurant:
    """餐馆"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性restaurant_name和cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('餐厅名字:'+self.restaurant_name)
        print('烹饪风格:'+self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name+'正在营业中')


restaurant = Restaurant('星巴克','咖啡')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-3 用户：创建一个名为 User 的类，其中包含属性 first_name 和 last_name，还有用户简介通常会存储的其他几个属性。
# 在类 User 中定义一个名为 describe_user()的方法，它打印用户信息摘要；再定义一个名为 greet_user()的方法，它向用户发出个性化的问候。
class User:

    def __init__(self, first_name, last_name):
        """初始化属性first_name和last_name"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """打印用户信息摘要"""
        print('姓名：'+self.first_name+self.last_name)

    def greet_user(self):
        """个性化的问候"""
        print(self.first_name + self.last_name+',你好!')


xiaobai = User('小','白')
xiaobai.describe_user()
xiaobai.greet_user()

s = [1,2,3,4,5,6]
print(s[1:4:2])








