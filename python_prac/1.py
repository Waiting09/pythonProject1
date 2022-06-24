"""
#定义一个变量
a = 'hello python world'
print(a)
#重新给这个变量赋值
a = 'hello python crash course world'
print(a)
#在字符串中加入引号和撇号
print('I told my friend, "Python is my favorite language!"')
print("The language 'Python' is named after Monty Python, not the snake.")
#将每个单词的首字母都改为大写
b = 'i miss you'
print(b.title())
b1 = 'i MiSs yOu'
print(b1.title())
#将字符串改为全部大写
print(b1.upper())
#将字符串改为全部小写
print(b1.lower())
#拼接字符串：使用加号（+）
print('ada'+'lovelace')
print('ada' + " " + 'lovelace')
#使用拼接，并将姓名设置合适的格式
print('Hello,' + 'ada lovelace'.title()+'!')
#制表符：\t 相当于tab的作用
print('‘'+'\tpython'+'’')
print('‘'+'python\tpytest'+'’')
print('‘'+'python\t'+'’')
#换行符：\n
print('Languages:\nPython\nC\nJavaScript')
#使用\n将Python换到下一行，并在下一行开头添加一个制表符\t
print("Languages:\n\tPython\n\tC\n\tJavaScript")
#剔除字符串末尾的空白：rstrip()
print('‘'+'  python  '.rstrip()+'’')
#剔除字符串开头的空白：lstrip()
print('‘'+'  python  '.lstrip()+'’')
#剔除字符串末两端的空白：strip()
print('‘'+'  python  '.strip()+'’')
#永久删除字符串两端的空白
c = '  python  '
c = '  python  '.strip()
print('‘'+c+'’')
#将整数转换成字符串：str（）
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
"""









