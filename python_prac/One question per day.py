# 0609
# 已知一个由数字组成的列表，请将列表中的所有0移到右侧。
# 例如 move_zeros([1, 0, 1, 2, 0, 1, 3]) ，预期返回结果： [1, 1, 2, 1, 3, 0, 0]
move_zeros = [1, 0, 1, 2, 0, 1, 3]
"""冒泡排序"""
"""
for i in range(len(move_zeros)):
    for j in range(len(move_zeros)-1):
        if move_zeros[j] == 0:
            move_zeros[j],move_zeros[j+1] = move_zeros[j+1],move_zeros[j]
print(move_zeros)

print(sorted(move_zeros,reverse=True,key = bool))
"""
# 0610
# 实现一个trim()函数，去除字符串首尾的空格（不能使用strip()方法）
# 例：1.字符串为空的情况，输入trim(’ ‘) 预期返回结果 ‘’
# 2.字符串首尾空格数大于1的情况，输入trim(’ a bc ') 预期返回结果 ‘a bc’
def trim(string):
    """去除字符串首尾的空格"""
    a=''
    for i in string:
        if i != '':
            a += i
    print("'"+a+"'")

trim('a bc ')



