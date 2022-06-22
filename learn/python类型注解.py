# 类型提示功能
# 1、增强代码的可读性
# 2、ide中代码提示
# 3、静态代码检查
# 用法一：为参数与返回数据指定类型
def greeting(name: str) -> str:  # 传递str，返回str
    return f"Hello,{name}"


# 用法二：为类型起别名
from typing import List

Vector = List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    print(scalar, vector)
    return [scalar * num for num in vector]

# 用法三：指定自定义类型
class Student:
    name: str
    age: str
    def get_money(self):
        print("1")

def get_stu(name:str)->Student:
    return Student()
get_stu("HARRY")

