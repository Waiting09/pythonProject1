# 字符串string
var = "0123456"
# 前闭后开原则，1<=x<5
# start:stop:step
print(var[1:5:1])
# \n 换行符
Hogwarts = "hogwarts \n school"
print(Hogwarts)
# \ 转义符
Hogwarts = "hogwarts \\n school"
print(Hogwarts)
# %s 格式化字符串
print("hogwarts teacher is %s" % "思寒")
# %d 格式化整型
print("hogwarts teacher is %d" % 100)
# %f 格式化浮点型,可指定小数点后的精度
print("hogwarts teacher is %f" % 3.16)
# "str".format() 格式化
# 位置
demo = "{} teacher is {}"
print(demo.format("hogwarts", "思寒"))
# 下标
demo = "{1} teacher is {0}"
print(demo.format("思寒", "hogwarts"))
# key
demo = "{school} teacher is {name}"
print(demo.format(name="思寒", school="hogwarts"))
# f"{变量}" 格式化
name = "飞飞"
print(f"hogwarts teacher is {name}")
# join 将列表根据想要的格式拼接成字符串
a = ["a", "a", "p", "l", "e"]
print("".join(a))
print("|".join(a))


def join_(array, splitor):
    return splitor.join(array)


print(join_(['a', 'b', 'c'], '-'))
# split 将字符串根据规定的内容进行切分
a = "a,b-c-d"
print(a.split('-'))
print('+'.join(a.split('-')))
# replace 替换
a = "hogwarts teacher is 飞飞"
print(a.replace("飞飞", "ad"))
# strip 剔除字符串末两端的空白
a = " abc "
print(len(a)) #len() 函数返回字符串中的字符数
print(a.strip())
