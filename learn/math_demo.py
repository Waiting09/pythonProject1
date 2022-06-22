import math
'''数字常量'''
# π 圆周率
print(math.pi)
# e 自然对数
print(math.e)
# ∞ 正无穷大
print(math.inf)
# 负无穷大
print(-math.inf)
# NAN 非数字
print(math.nan)
'''数论与表示函数'''
#向上取整  大于4.3最小的整数 5
print(math.ceil(4.3))
#向上取整  大于-4.3最小的整数 -4
print(math.ceil(-4.3))
#向下取整 小于4.3的最大的整数 4
print(math.floor(4.3))
#向下取整 小于-4.3的最大的整数 -5
print(math.floor(-4.3))
#获取2的3次幂
print(math.pow(2, 3))
#4的根次方
print(math.sqrt(4))

# 实例：天天向上的力量
# 一年365天,以第1天的能力值为基数,记为1.0，当努力学习时,能力值相比前一天提高1%,
# 当没有学习时能力值相比前一天下降1%。每天努力和每天放任,一年下来的能力值相差多少呢?)
print(math.pow((1.0 + 0.01), 365))
print(math.pow((1.0 - 0.01), 365))