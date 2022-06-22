# 导入sys模块
import sys

# 查看sys模块帮助文档
# help(sys)

# 查看sys模块的属性和方法
# print(dir(sys))

"""sys模块常用属性"""
# # 返回Python 解释器版本
# print(sys.version)
# # 返回操作系统平台名称
# print(sys.platform)
# # 返回外部向程序传递的参数
# print(sys.argv)
# # 返回已导入的模块信息
# print(sys.modules)
# # 返回已导入的模块名称
# print(sys.modules.keys())
# # 返回导包的搜索路径列表
# print(sys.path)

"""sys模块常用方法"""
# 获取系统当前编码
# print(sys.getdefaultencoding())

# # 运行时退出
# sys.exit()

#第六秒时退出
import time
for i in range(1,10):
    if i == 6:
        print("exit...")
        sys.exit("结束")
    print(f"running{i}...")
    time.sleep(1)