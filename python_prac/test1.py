'''
# 消息:编写一个名为 display_message()的函数，它打印一个句子，指出你在本章学的是什么。调用这个函数，确认显示的消息正确无误。
def display_message():
    print('函数')
display_message()

#喜欢的图书：编写一个名为 favorite_book()的函数，其中包含一个名为 title的形参。这个函数打印一条消息，如 One of my favorite
# books is Alice in Wonderland-我最喜欢的书之一是《爱丽丝梦游仙境》。调用这个函数，并将一本图书的名称作为实参传递给它。
def favorite_book(title):
    print('One of my favorite books is '+title)
favorite_book('小王子')

#T恤：编写一个名为 make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。这个函数应打印一个句子，概要地说明T恤的尺码和字样。
#使用位置实参调用这个函数来制作一件T恤；再使用关键字实参来调用这个函数。
def make_shirt(aize,word):
    print('一件印有'+word+'的'+aize+'T恤')
make_shirt('大码','love')

#大号 T 恤：修改函数 make_shirt()，使其在默认情况下制作一件印有字样“I love Python”的大号T恤。调用这个函数来制作如下T恤：
# 一件印有默认字样的大号 T 恤、一件印有默认字样的中号 T 恤和一件印有其他字样的 T 恤（尺码无关紧要）。
def make_shirt(aize,word='I love Python'):
    print('一件印有'+word+'的'+aize+'T恤')
make_shirt('中码')
make_shirt('小码','love')

#城市：编写一个名为 describe_city()的函数，它接受一座城市的名字以及该城市所属的国家。这个函数应打印一个简单的句子，
#如 Reykjavik is in Iceland。给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
def describe_city(city,country='中国'):
    print(city+'在'+country)
describe_city('郑州')
describe_city('上海')
describe_city('杭州')
describe_city('Reykjavik','Iceland')

#城市名：编写一个名为 city_country()的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面这样的字符串：
#"Santiago, Chile"  至少使用三个城市-国家对调用这个函数，并打印它返回的值
def city_country(city,country):
    a = city+','+country
    return a
print(city_country('Reykjavik', 'Iceland'))
print(city_country('郑州', '中国'))
print(city_country('杭州', '中国'))

# 专辑：编写一个名为 make_album()的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
# 使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。给函数 make_album()添加一个可选形参，以便能
# 够存储专辑包含的歌曲数。如果调用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
def make_album(name,music,number = ''):
    a = {}
    a[name] = music
    if number != '':
        a[music] = number
    return a
print(make_album('白', '晚安'))
print(make_album('1', '晚'))
print(make_album('2', '安','1'))

#用户的专辑：在为完成练习 8-7 编写的程序中，编写一个 while 循环，让用户输入一个专辑的歌手和名称。获取这些信息后，使用它们来调用
# 函数 make_album()，并将创建的字典打印出来。在这个 while 循环中，务必要提供退出途径。
def make_album(name='',music=''):
    while True:
            name_1 = input('请输入歌手名:')
            music_1 = input('请输入专辑名称:')
            if name_1 != '':
                break
    a = {}
    a[name_1] = music_1
    return a
print(make_album())

#魔术师：创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians()的函数，这个函数打印列表中每个魔术师的名字。
def show_magicians():
    a = [1,2,3,4,5]
    for i in a:
        print(i)

show_magicians()

def make_great():
    n = 0
    a = [1,2,3,4,5]

    show_magicians()
    while len(a):
        n += 1
        c = a[n]
        str(c) + ' the Great'
make_great()



#了不起的魔术师：在你为完成练习 8-9 而编写的程序中，编写一个名为make_great()的函数，对魔术师列表进行修改，在每个魔术师的名字中都加入字样
# “the Great”。调用函数 show_magicians()，确认魔术师列表确实变了。
def make_great():
    a = [1,2,3,4,5]
    b = []
    for i in a:
        j = str(i)+' the Great'
        b.append(j)
    print(b)
make_great()
'''







