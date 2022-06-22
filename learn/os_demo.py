import os

# 查看os模块说明文档
# help(os)
# 查看os模块的属性和方法
# print(dir(os))

"""os操作系统相关"""
# os.name：获取系统名称 nt代表window，posix代表linux
# print(os.name)
# os.environ：获取系统环境变量信息
# print(os.environ)
# os.getenv('PATH')：获取指定名称的环境变量信息
# print(os.getenv('PATH'))
# os.system()：执行系统指令
# os.system('pwd')  # linux系统
# print(os.system('dir')) # windows系统

"""目录相关"""
# 获取当前所在目录 get current directory
# print(os.getcwd())
# # 切换目录 change directory
# os.chdir('..') #切换到上一级目录
# # 列出当前目录下的所有文件
# print(os.listdir())
# # 创建空目录
# os.mkdir('a')
# #递归创建多级空目录
# os.makedirs('a/b/c')
# 删除空目录
# os.rmdir('a1')
# # 重命名目录
# os.rename('a', 'a1')
# 删除文件
# os.remove('demo.txt')

"""os 路径相关"""
# # 返回绝对路径
# print(os.path.abspath("./os_demo.py"))
# # 返回文件名
# print(os.path.basename("D:\pythonProject\learn\os_demo.py"))
# # 返回文件路径
# print(os.path.dirname("D:\pythonProject\learn\os_demo.py"))
# # 分割路径
# print(os.path.split("D:\pythonProject\learn\os_demo.py"))
# # 拼接路径
# print(os.path.join('D:\\pythonProject\\learn', 'os_demo.py'))
# # 判断路径是否存在
# print(os.path.exists("/Users/xiaofo/coding/pythonProject/course/os_demo.py"))
# print(os.path.exists("./os_demo.py"))
# # 判断是否是目录
# print(os.path.isdir("../demos"))
# print(os.path.isdir("../learn"))
# # 判断是否是文件
# print(os.path.isfile("./os_demo.py"))
# # 获取文件大小
# print(os.path.getsize("D:\pythonProject\learn\os_demo.py"))

