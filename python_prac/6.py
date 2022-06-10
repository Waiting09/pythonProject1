'''#函数 input()
message = input("今天周几:")
print(message)
#提示超过一行
message = "hi"
message += "\n今天周几:"
name = input(message)
print(name)
#使用 int()来获取数值输入
age = input('how old are you:')
age = int(age)
if age <= 12:
    print('儿童')
#用%判断奇数还是偶数
number = input('请输入整数:')
if int(number) % 2 == 0:
    print(number+'是偶数')
else:
    print(number+'是奇数')
#餐馆订位：编写一个程序，询问用户有多少人用餐。如果超过 8 人，就打印一条消息，指出没有空桌；否则指出有空桌
number = input('请问有多少人用餐:')
if int(number) > 8:
    print('不好意思，没有空桌了')
else:
    print('有空桌')
current_number = 1
while current_number <= 5:
 print(current_number)v
 current_number += 1
#让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
#使用标志
a = True
while a:
    message = input('输入：')
    if message == 'quit':
        a = False
    else:
        print(message)
#使用 break 退出循环
message = ""
while True:
    message = input('输入：')
    if message == 'quit':
        break
#在循环中使用 continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
#创建一个待验证列表a和一个存储已验证的空列表b
a = ['1','2','3','4']
b = []
#将经过验证的转移到b
while a:
    c = a.pop()
    print(c)
    b.append(c)
print(b)
#删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)'''
#使用用户输入填充字典
responses = {}
# 设置一个标志，指出调查是否继续
active = True
while active:
    # 提示输入被调查者的名字和年龄
    name = input('what is your name:')
    age = input('how old are you:')
    # 将答卷存储在字典中
    responses[name] = age
    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        active = False
print(responses)






