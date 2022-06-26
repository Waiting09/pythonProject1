food = input("请输入水果：")
color = "red"
if food == "apple" and color == "red":
    print("这是一个红色的苹果")
    if color == "green":  # 嵌套
        print("绿色")
    else:
        print("红色")
elif food == "banana":
    print("香蕉")
else:
    print("橙子")
# 三目运算符
a = 1
b = 1
if a > b:
    h = "变量1"
else:
    h = "变量2"
print(h)
"""三目运算符--赋值语句放在最前面 if 判断条件 else需要赋值的内容"""
h = "变量1" if a > b else "变量2"
print(h)

