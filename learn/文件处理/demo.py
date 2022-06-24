"""文件操作步骤"""
# # 第一步：（以只读模式）打开文件
# f = open('data.txt', 'r', encoding='utf-8')
#
# # 第二步：读取文件内容
# #读取过一次，再次去读，光标位置会改变
# # 换行符会占一个字符
# '''read()一次读取文件的所有内容，返回一个str'''
# print(f.read(14), type(f.read(14)))
# f.seek(0)  # 光标位置设置成0
# '''readlines()一次读取文件的所有内容，返回一个str'''
# print(f.readlines(12), type(f.readlines()))
# f.seek(0)  # 光标位置设置成0
# '''readline()每次只读取一行内容'''
# print(f.readline(), type(f.readline(14)))
# # 第三步：关闭文件
# f.close()
# print(f.closed)  # 查看关闭状态

# # with open的方式打开文件进行读写后会自行关闭文件
# w+ 会清空，再写入，如果没有文件，会创建新文件
# a+ 会在最末尾的位置，追加数据，不清空原来的内容，如果没有文件，会创建新文件
data = "写入文"
with open('data.txt', 'w+', encoding='utf-8') as j:
    print(j.write(data))
print(j.closed)  # 查看关闭状态
